# Queries

- create_terms_and titles.sql: creates a table with all titles that have a term from the language matrix in it with the associated term, term key, and language. 
- grouping.sql: uses grouping command to create republication groups

## Language Matrix
To search the database I'm given a matrix in google sheets of terms organized by languages and keys. I use the google sheets API in python (import gspread) to turn
the language matrix into an sql table to help me run queries. The python script can be rerun to provide a new create table statement everytime the language matrix is updated.

