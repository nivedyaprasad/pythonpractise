import mysql.connector

# Connect to MySQL server
root_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
root_cursor = root_conn.cursor()
root_cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
print("Database 'student_management' ready.")

# Connect to the created database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management"
)
mycursor = mydb.cursor()

# Create login table if not exists
mycursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
)
""")

# Insert login records safely
login_data = [
    ('admin1', 'admin123', 'admin'),
    ('principal', 'headadmin', 'admin'),
    ('system_admin', 'sys@2025', 'admin'),
    ('management', 'mgmt2025', 'admin'),
    ('director', 'dir2025', 'admin'),
    ('teacher1', 'teach123', 'teacher'),
    ('teacher2', 'teach456', 'teacher'),
    ('math_teacher', 'math2025', 'teacher'),
    ('science_teacher', 'sci2025', 'teacher'),
    ('english_teacher', 'eng2025', 'teacher'),
    ('student1', 'stud123', 'student'),
    ('student2', 'stud456', 'student'),
    ('nidhi', 'pass2025', 'student'),
    ('rohan', 'rohan2025', 'student'),
    ('aisha', 'aisha2025', 'student')
]

# Prevent duplicate insertions
for record in login_data:
    mycursor.execute("SELECT * FROM login WHERE username = %s", (record[0],))
    if not mycursor.fetchone():
        mycursor.execute("INSERT INTO login (username, password, role) VALUES (%s, %s, %s)", record)
        mydb.commit()

print("Table 'login' ready with default records.\n")

# Login method
def login_user():
    uname = input("Please enter username: ").strip()
    pword = input("Please enter password: ").strip()
    
    mycursor.execute("SELECT username, password, role FROM login WHERE username = %s", (uname,))
    result = mycursor.fetchone()
    
    if result and result[1] == pword:
        print(f"\nLogin successful. Welcome\n")
    else:
        print("\nLogin unsuccessful. Invalid username or password.\n")

# Run login
login_user()



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Prasad@123",
    database="srgs"
)
mycurs = mydb.cursor()


def add_student():
    while True:
        # Input student details
        student_id = int(input("enter student ID: "))
        roll_no = input("enter roll number: ")
        name = input("enter name: ")
        gender = input("enter gender: ")
        dob = input("enter date of birth (YYYY-MM-DD): ")
        class_name = input("enter class: ")
        section = input("enter section: ")
        adm_yr = input("enter admission year (YYYY): ")
        email = input("enter email: ")
        guardian_name = input("enter guardian name: ")
        contact_no = input("enter contact number: ")

        # Insert student into database
        query = """INSERT INTO students 
                   (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        values = (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
        mycurs.execute(query, values)
        mydb.commit()

        print("\nStudent added successfully!\n")

        # Ask if the user wants to add another student
        choice = input("do you want to add another student? (y/n): ").lower()
        if choice != 'y':
            break

def display_all():
    print("\n--- All Students in Database ---")
    mycurs.execute("SELECT * FROM students")
    records = mycurs.fetchall()
    for row in records:
        print(row)

def display_specific_student():
    # Ask for specific student ID
    while True:
        choice2 = input("\nDo you want to view a specific record? (y/n): ").lower()
        if choice2 != 'y':
            break
        else:
            student_id = int(input("\nEnter Student ID to view details: "))

            mycurs.execute("SELECT * FROM students")
            records = mycurs.fetchall()

            found = False
            for row in records:
                if row[0] == student_id:
                    found=True
                    print(row)
                    break
            if found==False:
                    print("\nNo student found with that ID.")

while True:
    print("\n=== Student Management Menu ===")
    print("1. insert a students record")
    print("2. display all student records")
    print("3. display a specific student record")
    print("4. exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
                add_student()

    elif choice == '2':
                display_all()

    elif choice == '3':
                display_specific_student()
                
    elif choice == '4':
        print("closing academic management system!")
        break
    else:
        print("\nInvalid choice! Please try again.")


        

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Prasad@123",
    database="srgs"
)
mycurs = mydb.cursor()

def insertrec():
    while True:
        student_id = int(input("Enter Student ID (integer): "))
        name = input("enter name: ")
        class_name = input("enter class: ")
        exam_name = input("enter exam name: ")
        phy = int(input("enter physics marks: "))
        chem = int(input("enter chemistry marks: "))
        math = int(input("enter math marks: "))
        comp = int(input("enter computer marks: "))
        eng = int(input("enter english marks: "))
        pc = float(input("enter percentage: "))

        query = """INSERT INTO academics 
                   (student_id, name, class_name, exam_name, physics, chemistry, math, computer, english, percentage)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = (student_id, name, class_name, exam_name, phy, chem, math, comp, eng, pc)
        mycurs.execute(query, values)
        mydb.commit()
        print("Record added successfully!")

        choice1 = input("Do you want to add another record? (y/n): ").lower()
        if choice1 != 'y':
            break


def display_all():
    print("\n--- All Records in Database ---")
    mycurs.execute("SELECT * FROM academics")
    records = mycurs.fetchall()
    for row in records:
        print(row)


def display_specific():
    while True:
        choice2 = input("\nDo you want to view a specific record? (y/n): ").lower()
        if choice2 != 'y':
            break
        else:
            student_id = int(input("\nEnter Student ID to view details: "))

            mycurs.execute("SELECT * FROM academics WHERE student_id = %s", (student_id,))
            record = mycurs.fetchall()

            found = 0  

            for row in record:
                if row[0] == student_id:
                    found = 1
                    print("\n--- Student Record ---")
                    print(row)
            if found==0:
                    print("\nNo student found with that ID.")


while True:
    print("\n=== Academic Management Menu ===")
    print("1. insert a student record")
    print("2. display all student records")
    print("3. display a specific student record")
    print("4. exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
                insertrec()

    elif choice == '2':
                display_all()

    elif choice == '3':
                display_specific()
                
    elif choice == '4':
        print("closing academic management system!")
        break
    else:
        print("\nInvalid choice! Please try again.")


  import mysql.connector

# Connect to MySQL server 
root_conn = mysql.connector.connect(host="localhost",user="root",password="root")
root_cursor = root_conn.cursor()

# Create database if not exists
root_cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
print("Database 'attendance_management' verified/created successfully.")

# Connect to the created database
mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="attendance_students")
mycurs = mydb.cursor()

# Create attendance table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS attendance (
    student_id INT PRIMARY KEY,
    roll_no VARCHAR(20),
    name VARCHAR(100),
    doa DATE,
    class_name VARCHAR(20),
    section VARCHAR(10),
    status CHAR(1)
)
"""
mycurs.execute(create_table_query)
mydb.commit()
print("Table 'attendance' verified/created successfully.")


def insert_attendance():
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            doa = input("Enter attendance date (YYYY-MM-DD): ")
            class_name = input("Enter class: ")
            section = input("Enter section: ")
            status = input("Enter whether present or absent (P/A): ").upper()

            query = """INSERT INTO attendance 
                       (student_id, roll_no, name, doa, class_name, section, status)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (student_id, roll_no, name, doa, class_name, section, status)
            mycurs.execute(query, values)
            mydb.commit()
            print("\nAttendance record added successfully!\n")

        except mysql.connector.IntegrityError:
            print(" Student ID already exists! Please use a unique ID.")
        except Exception as e:
            print(" Error:", e)

        choice = input("Do you want to add another record? (y/n): ").lower()
        if choice != 'y':
            break


def display_all():
    print("\n--- All Attendance Records ---")
    mycurs.execute("SELECT * FROM attendance")
    records = mycurs.fetchall()
    if not records:
        print("No records found.")
    for row in records:
        print(row)


def display_specific_student():
    student_id = int(input("Enter Student ID to view: "))
    mycurs.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    records = mycurs.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print(" No student found with that ID.")


def update_attendance():
    student_id = int(input("Enter Student ID to update: "))
    mycurs.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    record = mycurs.fetchone()

    if record:
        print("Existing Record:", record)
        status = input("Enter new status (P/A): ").upper()
        mycurs.execute("UPDATE attendance SET status = %s WHERE student_id = %s", (status, student_id))
        mydb.commit()
        print(" Attendance updated successfully!")
    else:
        print(" No student found with that ID.")


def delete_attendance():
    student_id = int(input("Enter Student ID to delete: "))
    mycurs.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    record = mycurs.fetchone()

    if record:
        confirm = input("Are you sure you want to delete this record? (y/n): ").lower()
        if confirm == 'y':
            mycurs.execute("DELETE FROM attendance WHERE student_id = %s", (student_id,))
            mydb.commit()
            print(" Record deleted successfully!")
        else:
            print(" Deletion cancelled.")
    else:
        print(" No student found with that ID.")


#Menu for pragram
while True:
    print("\n=== Attendance Management System ===")
    print("1. Insert attendance record")
    print("2. Display all records")
    print("3. Display specific student record")
    print("4. Update attendance")
    print("5. Delete attendance record")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        insert_attendance()
    elif choice == '2':
        display_all()
    elif choice == '3':
        display_specific_student()
    elif choice == '4':
        update_attendance()
    elif choice == '5':
        delete_attendance()
    elif choice == '6':
        print("Exiting Attendance Management System." )
        break
    else:
        print("Invalid choice! Please try again.")

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Hazel@123", database="student")
curs=mydb.cursor()


#fee management system
def fee_management():
    #Fee structure
    curs.execute('CREATE TABLE FEESTRUCT(Course varchar(30) Primary key, PT1 integer, MIDTERM integer, PT2 integer, FINAL integer)')
    curs.execute('INSERT INTO FEESTRUCT VALUES("class 1 to 2",6000, 7000, 6000, 7000)')
    curs.execute('INSERT INTO FEESTRUCT VALUES("Class 3 to 4", 6500, 7500, 6500, 7500)')
    curs.execute('INSERT INTO FEESTRUCT VALUES("Class 5 to 6", 7000, 8000, 7000, 8000)')
    curs.execute('INSERT INTO FEESTRUCT VALUES("Class 7 to 8", 7500, 8500, 7500, 8500)')
    curs.execute('INSERT INTO FEESTRUCT VALUES("Class 9 to 10", 8000, 9000, 8000, 9000)')
    curs.execute("select * from FEESTRUCT")
    result=curs.fetchall()
    mydb.commit()
    for x in result:
        print(x)

    #Track fee payments
    curs.execute('CREATE TABLE FEE(Name varchar(20) Primary key, Class integer, Amountpaid integer)') 
    while True:
        ch=input("Do you want to insert fee payment?(y/n)")
        if ch=='y':
           name=input("Enter name of student: ")
           class1=int(input("Enter class: "))
           amt=int(input("Enter amount paid: "))
           query = "INSERT INTO FEE (Name, Class, Amountpaid) VALUES (%s, %s, %s)"
           values = (name, class1, amt)
           curs.execute(query, values)
           mydb.commit()
           print("Payment recorded successfully")
           
        elif ch=='n':
            break
        else:
            print("wrong choice")
        mydb.commit()

    #Generate fee receipt
    nm=input("Enter name of student whose payment receipt required: ")
    curs.execute("SELECT * FROM FEE WHERE Name='%s'"%(nm,))
    receipt=curs.fetchall()
    mydb.commit()
    if receipt:
        print("PAYMENT RECEIPT DETAILS: ")
        for z in receipt:
            print(z)
        print("THANK YOU!")
    else:
        print("Not found")
fee_management()

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Hazel@123", database="student")
curs=mydb.cursor()

#club managament system
def club_management():
    #Scheduling clubs
    curs.execute("CREATE TABLE SCHEDULE(Club varchar(30) Primary key, Date DATE)")
    while True:
        ch=input("Any new clubs?(y/n): ")
        if ch=='y':
            club=input("Enter club name: ")
            date=input("Enter event date(yyyy-mm-dd): ")
            data1=(club,date)
            query1="INSERT INTO SCHEDULE(Club, Date) VALUES (%s,%s)"
            curs.execute(query1,data1)
            mydb.commit()
            print("NEW CLUB INSERTED")
        elif ch=='n':
            break;
        else:
            print("wrong choice")
   
   

    #Display schedule
    print("CLUBS SCHEDULED: ")
    curs.execute("SELECT * FROM SCHEDULE")
    sched=curs.fetchall()
    for a in sched:
        print(a)
    

    
    #Registration
    curs.execute("CREATE TABLE REGISTER(Clubname varchar(20), Studentname varchar(20), Class integer)")
    while True:
        ch=input("Do you want to register for a club?(y/n): ")
        if ch=='y':
            club1=input("Enter club name: ")
            stu=input("Enter student name: ")
            class1=int(input("Enter class: "))
            data2=(club1,stu,class1)
            query2="INSERT INTO REGISTER(Clubname,Studentname, Class) VALUES (%s,%s,%s)"
            curs.execute(query2,data2)
            curs.execute("SELECT * FROM REGISTER")
            result=curs.fetchall()
            mydb.commit()
            for x in result:
                print(x)
            mydb.commit()
            print("YOU HAVE REGISTERED!")
                
        elif ch=='n':
             break;
        else:
            print("wrong choice: ")
    
    print("THANK YOU!")

club_management()
     

