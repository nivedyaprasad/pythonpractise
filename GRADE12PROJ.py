import mysql.connector
mydb = mysql.connector.connect(host="localhost", user = "root", passwd="Prasad@123", database="srgs")
mycurs = mydb.cursor()

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Prasad@123",
    database="srgs"
)
mycurs = mydb.cursor()


def add_student():
    # Input student details
    student_id = int(input("Enter Student ID (integer): "))
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    gender = input("Enter Gender (Male/Female/Other): ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    class_name = input("Enter Class: ")
    section = input("Enter Section: ")
    adm_yr = input("Enter Admission Year (YYYY): ")
    email = input("Enter Email: ")
    guardian_name = input("Enter Guardian Name: ")
    contact_no = input("Enter Guardian Contact Number: ")

    # Insert student into database
    query = """INSERT INTO students 
               (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    values = (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
    mycurs.execute(query, values)
    mydb.commit()

    # Display using a for loop
    print("Student added successfully!")

    mycurs.execute("SELECT * FROM students")
    records = mycurs.fetchall()
    for i in records:
        print(i)


# Call the function
add_student()


