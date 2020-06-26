""" Written by Vasco Madrid
Date created: 6/25/2020
Description: Contains definition to print an sql create table command to standard output. The output should be inserted into an .sql file and run using MySQL using the source command
"""
import csv
def write_create_table(
	file_name, delim, table_name, col_prefix="", 
	default_type="varchar(100)"):
    """Print sql create table command to standard output. 

    Arguments:
    file_name -- the name of the tsv file to be created into a table
    delim -- the delimiter of the tsv/csv file
    table_name -- the name of the table to create
    col_prefix -- prefix for the columns incase names in tsv are improper
    """
    print("CREATE TABLE " + table_name + " {")
    with open(file_name) as csv_file:
	reader = csv.reader(csv_file, delimiter=delim)
	header = next(reader)
	for col in header:
	    name = col_prefix + col
	    print("\t" + name + " " + default_type + ",")
    print("};")

