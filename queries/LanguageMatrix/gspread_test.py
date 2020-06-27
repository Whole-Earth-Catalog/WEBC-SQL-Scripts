import gspread 

def clean_list(a_list):
    b_list = []
    # strip words of extra characters
    for item in a_list:
	b_list.append(item.strip("\n").strip("*"))
    b_set = set(b_list)
    c_list = list(b_set)
    c_list.remove("")
    return c_list

gc = gspread.service_account()

# Open language matrix sheet
lm = gc.open_by_key('1X9Ifq6mgzT0G-yjJPBoi1MVWh4KCc4qAQUfatY8rekE')
# select worksheet
lm_sheet = lm.get_worksheet(0)
# Get columns as lists
keys = clean_list(lm_sheet.col_values(1))
english_terms = clean_list(lm_sheet.col_values(2))
dutch_terms = clean_list(lm_sheet.col_values(3))
french_terms = clean_list(lm_sheet.col_values(4))
german_terms = clean_list(lm_sheet.col_values(5))
italian_terms = clean_list(lm_sheet.col_values(6))
latin_terms = clean_list(lm_sheet.col_values(7))
spanish_terms = clean_list(lm_sheet.col_values(8))
# create dictionary for all key lists
lm_dict = {"English" : english_terms, "Dutch" : dutch_terms,
	   "French" : french_terms, "German" : german_terms, "Italian" : italian_terms,
	   "Latin" : latin_terms, "Spanish" : spanish_terms}
'''
# print all terms
for elem in lm_dict:
    for term in lm_dict[elem]:
	print(elem + ": " + term)
'''
# create table for terms
print("CREATE TABLE terms (" + 
      "term_cap1 varchar(30), " + 
      "term_lc varchar(30), " +
      "language varchar(30))")
for language in lm_dict:
    for term in lm_dict[language]:
	term_cap1 = term[0].upper() + term[1:].lower()
	term_lc = term.lower()
        print("INSERT INTO terms " +
	      "VALUES (\"" + term_cap1 + 
              "\", \"" + term_lc + 
              "\", \"" + language + "\");")

