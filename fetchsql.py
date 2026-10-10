import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Prasad@123", database = "kichudb")
mycurs = mydb.cursor()
query = "SELECT * FROM kichu1"
mycurs.execute(query)
rd = mycurs.fetchmany(3)
norow = mycurs.rowcount
print("no of rows are: ", norow)

for i in rd:
    print(i)
