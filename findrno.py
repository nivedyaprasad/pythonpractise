import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Prasad@123", database = "kichudb")
mycurs = mydb.cursor()

rno = int(input("enter a roll no: "))
ct = input("eneter city: ")
age


query = "SELECT * FROM kichu1 WHERE CITY = '{city}' AND ROLLNO= {rollno}".format(city=ct,rollno=rno)

mycurs.execute(query)
myrec = mycurs.fetchone()

if myrec!= None:
    print(myrec)
else:
    print("student not found")
