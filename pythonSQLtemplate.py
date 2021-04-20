import mysql.connector

# connect to webc database
print("Connecting to database ...")
webc_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "webc"
)
print("Done.\n")

# create database cursor
db_cursor = webc_db.cursor()

query = "" # put query here
db_cursor.execute(query)
result = db_cursor.fetchall()

file_name = "" # put filename here
f = open(file_name, 'w')
for line in top_terms:
    f.write(line)
f.close()
