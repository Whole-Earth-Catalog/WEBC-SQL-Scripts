# Queries

- create_terms_and titles.sql: creates a table with all titles that have a term from the language matrix in it with the associated term, term key, and language. 
- basicqs_on_terms_and_titles.sql: basic queries to understand the terms and titles table
- grouping.sql: uses grouping command to create republication groups, Results:
-- Q1) Returns total number of rows: 775,731, this means there are 775,731 matches between the terms and the titles
-- Q2) The second query returns a list of the found terms and the number of titles that have the term
-- Q3) Number of unique search terms (no duplicates due to language difference): 147
-- Q4) Number of terms matched with titles: 128, this means that 19 terms were not found in any title
-- Q5) This query returns the 19 terms that were not in any titles
-- Q6) Returns number of titles per language (some titles are associated with more than one language due to cognates)
-- Q7) Returns number of titles associated with more than one language: 205,275. This is about half of the titles with terms. This is due to there being a few exact strings associated with different languages (there are 178 total terms and 147 unique terms indicating 31 exact duplicates). 
-- Q8) Returns number of unique ids where terms were found: 506,302. This is about 0.1% of the entire data set. 

## Language Matrix
To search the database I'm given a matrix in google sheets of terms organized by languages and keys. I use the google sheets API in python (import gspread) to turn
the language matrix into an sql table to help me run queries. The python script can be rerun to provide a new create table statement everytime the language matrix is updated.

