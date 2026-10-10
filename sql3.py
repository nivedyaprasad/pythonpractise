import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Prasad@123", database = "kichudb")
mycurs = mydb.cursor()
mycurs.execute("INSERT INTO kichu1 VALUES(11, 'avni', 'f', '2004-01-02', 49, 'kolkata', 'science')")
mycurs.execute("INSERT INTO kichu1 VALUES(12, 'anirudh', 'm', '2005-01-02', 90, 'kochi', 'commerce')")
mycurs.execute("INSERT INTO kichu1 VALUES(13, 'ivan', 'm', '2006-01-02', 89, 'ahmedabad', 'humanities')")

mydb.commit()
print(mycurs.rowcount,("record inserted"))
