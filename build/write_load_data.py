""" Written by Vasco Madrid
Date created: 6/25/2020
Description: Contains definition to print an sql load data command to standard output. The output should be inserted into an .sql file and run using MySQL using the source command
"""
def write_load_data(file_name, delim, table_name):
    """Print sql create table command to standard output. 
    
    Arguments:
    file_name -- the name of the tsv file to be created into a table
    delim -- the name of the delimiter of the tsv/csv file. Should not be the delimiter character itself as it will not properly print. 
             For example a tab delimited file will have delim = "\'\\t\'" since that will print to standard output as '\t'.
    table_name -- the name of the table to load data into
    """
    print("LOAD DATA LOCAL INFILE \"" + file_name + "\"")
    print("INTO TABLE " + table_name)
    print("FIELDS TERMINATED BY " + delim)
    print("LINES TERMINATED BY \'\\n\';")

