# Scripts for building tables from tsv files for MySQL database

- CodeToWriteScript/write_create_tables.py: has def write_create_table(file_name, delim, table_name, col_prefix="", default_type="varchar(100)") that prints to standard output the sql command to create a table based on given tsv file. Output example below.
- CodeToWritScript/write_load_data.py: has def write_load_data(file_name, delim, table_name)) that prints to standard output the sql command to load the data from the tsv file into the table created by the write_create_tables method.
- CodeToWriteScript/wct_tags.py: implements write_create_table and write_load_data methods to create build_tags.sql
- build_tags.sql : sql script to build tables out of important tags, needs to be in directory with data files
- CodeToWriteScript/XMLTagToTSV.py: iterates through XML file extracting the id and tag008 data and writing it to a tsv file.
- create_008_table.sql: sql script to create a table for tag 008 which has date information and was missing from the master build. Loads data from tsv created by XMLTagToTSV.py
- LanguageMatrix/create_terms_table.sql: script written by lm2sql.py to create table of terms from language table
- LanguageMatrix/create_terms_and_titles.sql: script that joins terms table and title table (tag245) where title has term
- LanguageMatrix/lm2sql.py: uses google sheets api to read language matrix and writes to standard output sql commands to create a term table out of matrix

# How to load large amount of data into table

Using the import function in mysql workbench is too slow but the 
load data command is significantly quicker:             

CREATE TABLE *table name* (          
    *column name* *datatype*,    
    *column name* *dataype,        
    ....                    
    *column name* *dataype                    
);               
                
To print a standard create table command based off of the header of the
tsv use the write_create_table.py script. You will probably want to adjust
the default data type for each column  but this helps save some typing if there are many columns.

LOAD DATA LOCAL INFILE *filename*                   
INTO TABLE *table name*                     
FIELDS TERMINATED BY *delimiter*                       
LINES TERMINATED BY '\n';    

# SQL Errors and fixes during build
- ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides                     
Fixed by using instructions from top answer here: https://stackoverflow.com/questions/59993844/error-loading-local-data-is-disabled-this-must-be-enabled-on-both-the-client                      
| set the global variables by using this command:                 
|| mysql> SET GLOBAL local_infile=1;              
||     Query OK, 0 rows affected (0.00 sec)            
| quit current server:           
|| mysql> quit              
|| Bye                            
| connect to the server with local-infile system variable :            
| mysql --local-infile=1 -u root -p1                
- ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)              
Fixed by using instructions from second top answer here: https://stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run              
| mysql -h 127.0.0.1 -P 3306 -u root -p <database>
- For both error 2002 and 42000 I combined the commands to be            
| mysql -h 127.0.0.1 -P 3306 -u root -p 'wc' --local-infile
