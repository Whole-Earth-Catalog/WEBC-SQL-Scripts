# How to load large amount of data into table

Using the import function in mysql workbench is too slow but the 
load data command is significantly quicker:             

CREATE TABLE *table name* {          
    *column name* *datatype*,    
    *column name* *dataype,        
    ....                    
    *column name* *dataype                    
};               
                
To print a standard create table command based off of the header of the
tsv use the write_create_table.py script. You will probably want to adjust
the default data type for each column  but this helps save some typing.

LOAD DATA LOCAL INFILE *filename*
INTO TABLE *table name*
FIELDS TERMINATED BY *delimiter*
LINES TERMINATED BY '\n' 
