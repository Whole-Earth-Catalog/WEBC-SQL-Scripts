import gspread 

def clean_list(a_list):
    b_list = []
    # strip words of extra characters
    for item in a_list:
        b_list.append(item.strip("\n").strip("*"))
    b_set = set(b_list)
    c_list = list(b_set)
    # remove empty strings
    if "" in c_list:
        c_list.remove("")
    return c_list

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
# list of column titles
col_title = lm_sheet.row_values(1)
# list of languages
languages = col_title
# dont include first column in language list (keys)
languages.pop(0)
# dont include last column in language list (definitions)
languages.pop(len(col_title)-1)
# print(languages)
# number of columns
num_col = len(col_title)
# Get a map of keys
keys = lm_sheet.col_values(1)
key_rows = fill_keys(keys)
key_set = set(key_rows)
unique_keys = list(key_set)
# print(key_rows)
# number of rows
num_row = len(keys)
# create dict of all terms
'''  
all_terms = {}
for language in languages:
    col_num = col_title.index(language) + 1
    term_list = lm_sheet.col_values(col_num)
    all_terms.update({language : term_list})
print(all_terms)
# create dict of keys with specific term dictionaries
keys = {}
for key in unique_keys:
    term_dict = {}
    row_nums = []
    # get list of rows associated with term
    for row_num in range(len(key_rows)):
	if key == key_rows[row_num]:
	    row_nums.append(row_num)
    # get terms for each language
    for language in all_terms:
	all_term_list = all_terms[language]
	key_term_list = []
	for num in row_nums:
            key_term_list.append(all_term_list[num])
	key_term_list = clean_list(key_term_list)
        term_dict.update({language : key_term_list})
    keys.update({key : term_dict})

sql_file = open('create_terms_table.sql', 'w')

# write create table command for full term table
sql_file.write("CREATE TABLE terms (" + 
               "term_lc varchar(20), " +
               "term_cap1 varchar(20), " +
               "term_key varchar(20), " + 
               "language varchar(20));")
# write input into commands for each term
for key in keys:
    key_term_dict = keys[key]
    for language in key_term_dict:
        for term in key_term_dict[language]:
	    term_lc = term.lower()
	    term_cap1 = term[0].upper() + term[1:].lower()
            sql_file.write("INSERT INTO terms " + 
		                   "VALUES (\"" + term_lc +
                           "\", \"" + term_cap1 + 
		                   "\", \"" + key +
		                   "\", \"" + language + "\");")
''' 