"""Gets top terms among titles for each language in webc database.

For each language and decade combination, we find the most common terms
among the titles in the language and from the decade.
Then, for each language we find the intersection of all the sets from the different
decades. This will give us a list of the most popular terms among titles that were
popular every decade to help us draw a continuous line.
I have not yet implemented a way to omit unwanted words like "the", "a", etc. from
english or any language since it is a bit different for each language. Right now,
to find the best words to graph a human must go through the words and think about them
and consider the linguistic, historical, and pragmatic uses of the term.

   To use:

   run: python topterms.py
   In the current directory there will a txt file for each
   language containing the topterms. 
"""
import mysql.connector
import re
from collections import Counter

def get_decade_list(start_decade, end_decade):
    """Creates list of decades

    Makes a list of all decades between the decades 
    given in the args. Includes the start_decade
    and excludes 

    Args:
        start_decade: integer of decade to start
           list from.
        end_decade: integer of decade to end list at.

    Returns:
        An integer array  list of all decades.
    """
    decade_list = []
    for decade in range(start_decade, end_decade, 10):
        decade_list.append(decade)
    return decade_list

def get_terms(lang, decade, count):
    # select all titles for the language and decade
    query = "select title from master_help where lang=\"" + lang + "\" and decade=\"" + str(decade/10) + "\";"
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    all_terms = []
    for row in result:
	title = row[0].lower()
	# remove unwanted characters from titles
	title = re.sub(r'[^\w\s]', '', title)
	#print(title)
	these_terms = title.split()
	all_terms += these_terms
    term_counts = Counter(all_terms)
    top = []
    for term in term_counts.most_common(count):
	top.append(term[0])
    return top

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

decades = get_decade_list(1500, 1800)


# get languages in database
print("Getting languages from tag008")
db_cursor.execute("select lang from master_help group by lang;")
result  = db_cursor.fetchall()
langs = []
for row  in result:
    if row[0] != '':
        langs.append(row[0])
	print(row[0])
print("Done.\n")


# iterate through each decade for each lang
for lang in langs:
    con_terms = set([])
    # print("Getting most common words that exist in each decade...")
    for decade in decades:
        # print(decade)
        terms = get_terms(lang, decade, 500)
        if decade == 1500:
            con_terms = set(terms)
        else:
            con_terms = con_terms.intersection(set(terms))
    final_terms = list(con_terms)
    f_name = lang + "_terms.txt"
    f = open(f_name, 'w')
    f.write(lang + "\n")
    for term in final_terms:
        f.write(term + "\n")
    f.close()

'''
# test english
con_terms = set([])
print("Getting most common words that exist in each decade...")
for decade in decades:
    print(decade)
    terms = get_terms('eng', decade, 500)
    if decade == 1500:
	con_terms = set(terms)
    else:
	con_terms = con_terms.intersection(set(terms))
print(con_terms)
'''
