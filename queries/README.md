# Queries

- *basicqs_on_terms_and_titles.sql*: basic queries to understand the terms and titles table       
RESULTS
  - Q1) Returns total number of rows: 502,571, this means there are 502,571 matches between the terms and the titles
  - Q2) The second query returns a list of the found terms and the number of titles that have the term
  - Q3) Number of unique search terms (no duplicates due to language difference): 172
  - Q4) Number of terms matched with titles: 148, this means that 24 terms were not found in any title
  - Q5) This query returns the 24 terms that were not in any titles
  - Q6) Returns number of titles per language (some titles are associated with more than one language due to cognates)
  - Q7) Returns number of titles associated with more than one language: 66,548. This is about 13% of the titles with terms. This is due to there being a few exact strings associated with different languages (there are 200 total terms and 172 unique terms indicating 28 exact duplicates). 
  - Q8) Returns number of unique ids where terms were found: 408,370. This is about 80% of the entire data set meaning that most titles are only associated with one language and term. 
- *grouping.sql*: uses group by command to create republication groups
- *hamlet_variations*: select all publications of hamlet and study output for an idea of title variation in dataset
- *terms_by_decade.sql*: gets terms and key term frequency counts per decade, exported as json files 

## Language Matrix
To search the database I'm given a matrix in google sheets of terms organized by languages and keys. I use the google sheets API in python (import gspread) to turn
the language matrix into an sql table to help me run queries. The python script can be rerun to provide a new create table statement everytime the language matrix is updated.

