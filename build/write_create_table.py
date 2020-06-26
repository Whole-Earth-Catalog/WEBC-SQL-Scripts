import csv

def write_create_table(
	file_name, delim, table_name, col_prefix="", 
	default_type="varchar(100)"):
    print("CREATE TABLE " + table_name + " {")
    with open(file_name) as csv_file:
	reader = csv.reader(csv_file, delimiter=delim)
	header = next(reader)
	for col in header:
	    name = col_prefix + col
	    print("\t" + name + " " + default_type + ",")
    print("};")

