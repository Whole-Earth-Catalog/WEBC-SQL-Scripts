def write_load_data(file_name, delim, table_name):
    print("LOAD DATA LOCAL INFILE \"" + file_name + "\"")
    print("INTO TABLE " + table_name)
    print("FIELDS TERMINATED BY " + delim)
    print("LINES TERMINATED BY \'\\n\';")

