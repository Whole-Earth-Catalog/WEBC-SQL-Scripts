from write_create_table import write_create_table
from write_load_data import write_load_data

file_path = "../../../../data/wc_data/fsplit/"
tags = ["245", "100", "260"]

for tag in tags:
    filename = tag + '.tsv'
    delim_char = '\t'
    delim_name = "\'\\t\'"
    tablename = 'tag' + tag
    write_create_table(file_path + filename, delim_char, tablename, col_prefix='col_')
    write_load_data(filename, delim_name, tablename)

