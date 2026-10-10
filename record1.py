#Menu driven program to integrate MySQL with Python and perform the following operations:
#a) Create a database school, create a table student with fields as Rollno, Stu_Name, Stream and Percentage. Then insert 5
#records into it.
#b) Display all the records from the table

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Prasad@123")
mycurs = mydb.cursor()

def create_table():
    mycurs.execute("CREATE DATABASE IF NOT EXISTS school")
    mycurs.execute("USE school")
    mycurs.execute("CREATE TABLE IF NOT EXISTS student(Rollno int NOT NULL PRIMARY KEY, Stu_Name varchar(50), Stream varchar(20), Percentage float)")
    print("table created!")
    for i in range(5):
        # Input student details
        roll_no = input("enter roll number: ")
        name = input("enter name: ")
        stream = input("enter stream: ")
        percentage = input("enter percentage: ")

        # Insert student into database
        query = """INSERT INTO student 
                   (Rollno, Stu_Name, Stream, Percentage)
                   VALUES (%s, %s, %s, %s)"""
        
        values = (roll_no, name, stream, percentage)
        mycurs.execute(query, values)
        mydb.commit()

        print("\nStudent added successfully!\n")
    mydb.commit()

def display_records():
    mycurs.execute("select * from student")
    myrec = mycurs.fetchall()
    for i in myrec:
        print(i)

    
while True:
    print("1. Create Database, Table & Insert Records")
    print("2. Display All Records")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        create_table()
    elif choice == '2':
        display_records()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-3.\n")
