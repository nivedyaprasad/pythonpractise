import mysql.connector
from tabulate import tabulate

# Connect to the database
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Prasad@123",database="srgs")
mycurs = mydb.cursor()

def add_multiple_students():
    try:
        # List of student records
        students = [
            (902, "16", "Aisha Sharma", "Female", "2010-07-20", "10", "A", "2020", "9876543211", "aisha.sharma@example.com", "MG Road, Bangalore", "Ramesh Sharma", "9876501235"),
            (903, "17", "Vikram Singh", "Male", "2009-12-05", "11", "B", "2019", "9876543212", "vikram.singh@example.com", "Brigade Road, Bangalore", "Sunita Singh", "9876501236"),
            (904, "18", "Neha Patel", "Female", "2010-03-15", "10", "C", "2020", "9876543213", "neha.patel@example.com", "Jayanagar, Bangalore", "Kiran Patel", "9876501237")
        ]

        query = """INSERT INTO students 
                   (student_id, roll_no, name, gender, dob, class_name, section, admission_year, contact, email, address, guardian_name, guardian_contact)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        # Insert each student using execute()
        for student in students:
            mycurs.execute(query, student)
        mydb.commit()
        print("students added successfully!")

        # Fetch and display the students table
        mycurs.execute("SELECT * FROM students")
        rows = mycurs.fetchall()
        if rows:
            columns = [desc[0] for desc in mycurs.description]
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        else:
            print("No students found in the table.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
add_multiple_students()

# Close resources
mycurs.close()
mydb.close()
