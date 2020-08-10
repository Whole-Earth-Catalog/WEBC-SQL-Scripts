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
          "term_type varchar(20), " 
          "language varchar(20));")
    cursor.execute(create_statement)
    db.commit()
    cursor.close()

def insert_terms(db, term_lc, term_key, term_type, language):
    cursor = db.cursor() # create database cursor
    cursor.execute("INSERT INTO terms " + 
                   "VALUES (\"" + term_lc +
                   "\", \"" + term_key + 
                   "\", \"" + term_type +
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
                insert_terms(db, term_lc, term_key, term_type, language)
		if term_key not in all_term_keys:
                    all_term_keys.append(term_key)
    return all_term_keys

def insert_common_terms(db):
    common_terms = []
    with open('common_terms.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count > 0:
                common_terms.append(row[0])
                insert_terms(db, row[0],row[1],row[2],row[3])
            count += 1
    return common_terms

def create_master_help(db):
    cursor = db.cursor() # create database cursor
    query =  """create table master_help as 
        select tag245.id as id, 
            concat(\' \', clean_title(tag245.$a), \' \') as title, 
            substring(tag008.data, 36, 3) as lang, substring(tag008.data, 8, 3) as decade
        from tag245, tag008
        where tag008.id=tag245.id;
        """
    cursor.execute(query)
    db.commit()
    cursor.close()

def create_terms_and_titles(db):
    cursor = db.cursor() # create database cursor
    query =  """CREATE table terms_and_titles AS
    SELECT master_help.id, master_help.title, terms.term, terms.term_key, 
        terms.language, master_help.decade, terms.term_type
    FROM master_help, terms
    WHERE master_help.title LIKE(CONCAT(\'% \',terms.term,\' %\'))AND master_help.lang=lower(substring(terms.language,1,3));  """
    cursor.execute(query)
    db.commit()
    cursor.close()

def get_final_tsv(db):
    cursor = db.cursor() # create database cursor
    select_query = """ select term_key, language, term_type, concat(decade, '0'), count(id)
                        from terms_and_titles
                        group by term_key, decade, language, term_type
                        having term_type=\"search_term\"
                        union
                        select term, language, term_type, concat(decade, '0'), count(id)
                        from terms_and_titles
                        group by term, language,decade, term_type
                        having term_type=\"common_term\"
                        order by 4;"""
    cursor.execute(select_query)
    result = cursor.fetchall()
    tsv_name = "data.tsv"
    results_to_tsv(result, tsv_name, "term,language,type,decade,count")
    cursor.close()

def results_to_tsv(results, tsv_name, column_title_row):
    tsv_file = open(tsv_name, 'w')
    tsv_file.write(column_title_row + "\n")
    for row in results:
        index = 0
        tsv_line = str(row[index])
        for item in row:
            if index > 0:
                tsv_line += "," + str(item)
            index += 1
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

print("Dropping terms table if it exists...")
drop_table(webc_db, "terms")
print("Done.\n")

print("Creating terms table...")
create_terms_table(webc_db) 
print("Done.\n")

print("Inserting search terms from spreadsheet...")
all_term_keys = lm_to_table(webc_db)
print("Done.\n")

print("Inserting common term values from csv into terms table...")
common_terms = insert_common_terms(webc_db)
print("Done.\n")

print("Creating term lines file...")
f = open('all_terms.tsv', 'w')
for term in all_term_keys:
    f.write(term + "\tsearch_term\n")
for term in common_terms:
    f.write(term + "\tcommon_term\n")
f.close()
print("Done")

'''
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
'''

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

print("Selecting term groups per decade...")
get_final_tsv(webc_db)
print("Done.\n")
