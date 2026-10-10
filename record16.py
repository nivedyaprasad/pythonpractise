# Menu-driven program to integrate MySQL with Python
# a) Create a database school, create a table student with fields as Rollno, Stu_Name, Stream, and Percentage, then insert 5 records.
# b) Display all the records from the table.

import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Prasad@123")
mycurs = mydb.cursor()

# Create database, table, and insert records
def create_table():
    mycurs.execute("CREATE DATABASE IF NOT EXISTS school")
    mycurs.execute("USE school")
    mycurs.execute("""
        CREATE TABLE IF NOT EXISTS student(
            Rollno INT PRIMARY KEY,
            Stu_Name VARCHAR(50),
            Stream VARCHAR(20),
            Percentage FLOAT
        )
    """)
    print("Table created!\n")

    for i in range(5):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        stream = input("Enter Stream: ")
        percentage = input("Enter Percentage: ")

        query = "INSERT INTO student (Rollno, Stu_Name, Stream, Percentage) VALUES (%s, %s, %s, %s)"
        values = (roll_no, name, stream, percentage)
        mycurs.execute(query, values)
        mydb.commit()
        print("Student added!\n")

# Display all student records
def display_records():
    mycurs.execute("USE school")
    mycurs.execute("SELECT * FROM student")
    for rec in mycurs.fetchall():
        print(rec)

# Menu
while True:
    print("\n1. Create Database, Table & Insert Records")
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
