# Language Matrix Build
Use matrix of search terms to perform SQL queries
- lm2sql.py: writes create table sql command for the language matrix using the Google Sheets API to read spreadsheet. The language matrix does not have many terms and I could have created the table by reorganizing the spreadsheet. But if spreadsheet gets updated over time, python script can write a new sql script for the updated matrix. 
- create_term_table.sql: script to create a term table in MySQL 
