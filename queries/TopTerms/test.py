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

print("executing sql....")
db_cursor.execute("select * from tag008 limit 10;")
result  = db_cursor.fetchall()
for line in result:
    print(line)
print("Done.\n")
