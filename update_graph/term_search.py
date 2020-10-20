""" Runs search term queries on database.
"""
import gspread 
import mysql.connector
import csv
import time

def clean_item(item):
    clean_item = item.strip("\n").strip("*").strip()
    return clean_item

def fill_keys(key_list):
    row_list = []
    curr_key = ""
    for elem in key_list:
        if elem != "":
            curr_key = elem
        else:
            elem = curr_key
        row_list.append(elem)
    return row_list

def drop_table(db, table_name):
    cursor = db.cursor() # create database cursor
    cursor.execute("drop table if exists " + table_name + ";")
    db.commit()
    cursor.close()

def create_terms_table(db):
    cursor = db.cursor() # create database cursor
    # write create table command for full term table
    create_statement = ("CREATE TABLE terms (" + 
          "term varchar(40), " 
          "term_key varchar(20), "
          "language varchar(20));")
    cursor.execute(create_statement)
    db.commit()
    cursor.close()

def insert_terms(db, term_lc, term_key, language):
    cursor = db.cursor() # create database cursor
    cursor.execute("INSERT INTO terms " + 
                   "VALUES (\"" + term_lc +
                   "\", \"" + term_key + 
                   "\", \"" + language + "\");")
    db.commit()
    cursor.close()

def lm_to_table(db):
    gc = gspread.service_account()
    # Open language matrix sheet
    print("Opening spreadsheet...")
    lm = gc.open_by_key('1X9Ifq6mgzT0G-yjJPBoi1MVWh4KCc4qAQUfatY8rekE')
    # select worksheet
    lm_sheet = lm.get_worksheet(0)
    print("Getting values...")
    # Get a map of keys
    keys = lm_sheet.col_values(1)
    key_rows = fill_keys(keys)
    # get all values as list of lists
    all_values = lm_sheet.get_all_values()
    num_row = len(all_values)
    # print("number of rows: " + str(num_row))
    columns = all_values[0]
    num_col = len(all_values[0])
    print("Inserting search term values into table...")
    all_term_keys = []
    for row in range(1,num_row):
        for col in range(1,num_col-1):
            term = clean_item(all_values[row][col])
            if term != "":
                term_lc = term.lower()
                term_type = "search_term"
                language = columns[col]
                term_key = key_rows[row]
	        # insert row into database
                insert_terms(db, term_lc, term_key, language)
		if term_key not in all_term_keys:
                    all_term_keys.append(term_key)
    return all_term_keys

def create_master_help(db):
    cursor = db.cursor() # create database cursor
    query_create = """ create table master_help (
             id varchar(100),
             title varchar(7000),
             title_nopunct varchar(7000),
             lang varchar(3),
             decade varchar(4)
        );
        """
    query_insert =  """insert into master_help (id, title, title_nopunct, lang, decade) 
        select tag245.id as id,
            concat(tag245.$a, \' \', tag245.$b) as title, 
            concat(\' \', clean_title(concat(tag245.$a, \' \', tag245.$b)), \' \') as title_nopunct, 
            substring(tag008.data, 36, 3) as lang, substring(tag008.data, 8, 3) as decade
        from tag245, tag008
        where tag008.id=tag245.id;
        """
    cursor.execute(query_create)
    db.commit()
    cursor.execute(query_insert)
    db.commit()
    cursor.close()

def create_terms_and_titles(db):
    cursor = db.cursor() # create database cursor
    query =  """CREATE table terms_and_titles AS
    SELECT master_help.id, master_help.title_nopunct, terms.term, terms.term_key, 
        terms.language, master_help.decade
    FROM master_help, terms
    WHERE master_help.title_nopunct LIKE(CONCAT(\'% \',terms.term,\' %\'))
    AND master_help.lang=lower(substring(terms.language,1,3));  """
    cursor.execute(query)
    db.commit()
    cursor.close()

def get_total_titles(db):
    totals = {'eng':{}, 'spa':{}, 'lat':{}, 'fre':{}, 'ita':{}, 'ger':{}, 'dut':{}}
    cursor = db.cursor() # create datbase cursor
    query = """ select lang, concat(decade, '0'), count(id)
                from master_help
                group by lang, decade
                order by lang, decade
    """
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        lang = row[0]
        decade = row[1]
        count = row[2]
        totals[lang].update({decade:count})
    return totals

def get_final_tsv(db):
    cursor = db.cursor() # create database cursor
    select_query = """ select term_key, language, concat(decade, '0'), count(id)
                        from (
			   select term_key, decade, language, id
                           from terms_and_titles
                           group by term_key,decade, language, id
                        ) as clean_tt
                        group by term_key, decade, language
                        order by term_key, language, decade;
                   """
    cursor.execute(select_query)
    result = cursor.fetchall()
    tsv_name = "data.tsv"
    totals = get_total_titles(db)
    results_to_tsv(result, tsv_name, "term\tlanguage\ttype\tdecade\tproportion", totals)
    cursor.close()

def results_to_tsv(results, tsv_name, column_title_row, totals):
    tsv_file = open(tsv_name, 'w')
    tsv_file.write(column_title_row + "\n")
    for row in results:
        long_lang = row[1]
        short_lang = long_lang[0:3:1].lower()
        decade = row[2]
        count = float(row[3])
        total = float(totals[short_lang][decade])
        proportion = count/total * 100 * 1000
        tsv_line = str(row[0]) + "\t" + str(long_lang) + "\tsearch_term\t" + str(decade) + "\t" + str(proportion)
        tsv_file.write(tsv_line + "\n")
    tsv_file.close()


# connect to webc database
print("Connecting to database ...")
webc_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "webc"
)
print("Done.\n")

'''
print("Dropping terms table if it exists...")
drop_table(webc_db, "terms")
print("Done.\n")

print("Creating terms table...")
create_terms_table(webc_db) 
print("Done.\n")

print("Inserting search terms from spreadsheet...")
all_term_keys = lm_to_table(webc_db)
print("Done.\n")


print("Updating master_help table...")
print("Dropping master_help if it already exists...")
drop_table(webc_db, "master_help")

print("Creating master table...")
start_time = time.time()
create_master_help(webc_db)
end_time = time.time()
total_time = end_time - start_time
print("Time (in seconds) to create master table: " + str(total_time))
print("Done.\n")

print("Dropping terms and titles table if it exists...")
drop_table(webc_db, "terms_and_titles")
print("Done.")

print("Creating terms and titles table...")
start_time = time.time()
create_terms_and_titles(webc_db)
end_time = time.time()
total_time = end_time - start_time
print("Time (in seconds) to create terms_and_titles table: " + str(total_time))
print("Done.")
'''
print("Selecting term groups per decade...")
get_final_tsv(webc_db)
print("Done.\n")




