import xml.etree.ElementTree as ET

file_path = "../../../../../backup/data/wc_data/"
file_name = "dr59.xml"

tsv_file = open("008.tsv", 'w')
tsv_file.write("id\tdata\n")
with open(file_path + file_name, 'r') as f :
    for line in f:
	tree = ET.fromstring(line)
	id = ""
	tag008 = ""
	for child in tree:
	    if str(child.attrib) == "{\'tag\': \'001\'}":
	        id = child.text
	    elif str(child.attrib) == "{\'tag\': \'008\'}":
		tag008 = child.text
	tsv_file.write(id + "\t" + tag008 + "\n")
 
