from write_create_table import write_create_table

file_path = "../../../../data/wc_data/fsplit/"
tags = ["245", "100", "260"]

for tag in tags:
    write_create_table(file_path+ tag+'.tsv', '\t', 'tag' + tag, col_prefix='col_')


