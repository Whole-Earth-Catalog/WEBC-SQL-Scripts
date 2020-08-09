import gspread 
import mysql.connector

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

gc = gspread.service_account()

# Open language matrix sheet
lm = gc.open_by_key('1X9Ifq6mgzT0G-yjJPBoi1MVWh4KCc4qAQUfatY8rekE')
# select worksheet
lm_sheet = lm.get_worksheet(0)

# connect to webc database
print("Connecting to database ...")
webc_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "webc"
)
print("Done.\n")
# create database cursor
db_cursor = webc_db.cursor()

# Get a map of keys
keys = lm_sheet.col_values(1)
key_rows = fill_keys(keys)
#print("Map of key col")
#print(key_rows)

# get all values as list of lists
all_values = lm_sheet.get_all_values()
num_row = len(all_values)
# print("number of rows: " + str(num_row))
columns = all_values[0]
num_col = len(all_values[0])
# print("number of columns: " + str(num_col))
# print("columns: " + str(columns))

# remove terms table if it exists
db_cursor.execute("drop table if exists terms")

# write create table command for full term table
create_statement = ("CREATE TABLE terms (" + 
      "term_lc varchar(40), " 
      "term_key varchar(20), " 
      "term_type varchar(20), " 
      "language varchar(20));")

# create term table
db_cursor.execute(create_statement)

for row in range(1,num_row):
    for col in range(1,num_col-1):
	term = clean_item(all_values[row][col])
	if term != "":
	    term_lc = term.lower()
	    term_type = "search_term"
	    language = columns[col]
	    term_key = key_rows[row]
	    # insert row into database
	    db_cursor.execute("INSERT INTO terms " + 
                   "VALUES (\"" + term_lc +
                   "\", \"" + term_key + 
                   "\", \"" + term_type +
                   "\", \"" + language + "\");")

