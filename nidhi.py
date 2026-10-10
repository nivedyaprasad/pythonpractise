import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prasad@123"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
print("Database 'student_management' ready.")

# Connect to the created database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prasad@123",
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

# ✅ Create students table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT NOT NULL PRIMARY KEY,
    roll_no VARCHAR(20),
    name VARCHAR(100),
    gender VARCHAR(7),
    dob DATE,
    class_name VARCHAR(20),
    section VARCHAR(10),
    adm_yr YEAR,
    email VARCHAR(100),
    guardian_name VARCHAR(100),
    contact_no VARCHAR(15)
)
""")

# ---------- Student Management Functions ----------

def add_student():
    while True:
        student_id = int(input("Enter student ID: "))
        roll_no = input("Enter roll number: ")
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        class_name = input("Enter class: ")
        section = input("Enter section: ")
        adm_yr = input("Enter admission year (YYYY): ")
        email = input("Enter email: ")
        guardian_name = input("Enter guardian name: ")
        contact_no = input("Enter contact number: ")

        query = """INSERT INTO students 
                   (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        values = (student_id, roll_no, name, gender, dob, class_name, section, adm_yr, email, guardian_name, contact_no)
        mycursor.execute(query, values)
        mydb.commit()

        print("\nStudent added successfully!\n")

        choice = input("Do you want to add another student? (y/n): ").lower()
        if choice != 'y':
            break

def display_all():
    print("\n--- All Students in Database ---")
    mycursor.execute("SELECT * FROM students")
    records = mycursor.fetchall()
    for row in records:
        print(row)

def display_specific_student():
    while True:
        choice2 = input("\nDo you want to view a specific record? (y/n): ").lower()
        if choice2 != 'y':
            break
        else:
            student_id = int(input("\nEnter Student ID to view details: "))
            mycursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            record = mycursor.fetchone()

            if record:
                print(record)
            else:
                print("\nNo student found with that ID.")

# ---------- Menu ----------

while True:
    print("\n=== Student Management Menu ===")
    print("1. Insert a student record")
    print("2. Display all student records")
    print("3. Display a specific student record")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_all()
    elif choice == '3':
        display_specific_student()
    elif choice == '4':
        print("Closing Student Management System!")
        break
    else:
        print("\nInvalid choice! Please try again.")




mycursor.execute("""
CREATE TABLE IF NOT EXISTS academics (
    student_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    class_name VARCHAR(20),
    exam_name VARCHAR(50),
    physics INT,
    chemistry INT,
    math INT,
    english INT,
    computer INT,
    percentage FLOAT
)
""")

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
        mycursor.execute(query, values)
        mydb.commit()
        print("Record added successfully!")

        choice1 = input("Do you want to add another record? (y/n): ").lower()
        if choice1 != 'y':
            break


def display_all():
    print("\n--- All Records in Database ---")
    mycursor.execute("SELECT * FROM academics")
    records = mycursor.fetchall()
    for row in records:
        print(row)


def display_specific():
    while True:
        choice2 = input("\nDo you want to view a specific record? (y/n): ").lower()
        if choice2 != 'y':
            break
        else:
            student_id = int(input("\nEnter Student ID to view details: "))

            mycursor.execute("SELECT * FROM academics WHERE student_id = %s", (student_id,))
            record = mycursor.fetchall()

            found = 0  

            for row in record:
                if row[0] == student_id:
                    found = 1
                    print("\n--- Student Record ---")
                    print(row)
            if found == 0:
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
mycursor.execute(create_table_query)
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
            mycursor.execute(query, values)
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
    mycursor.execute("SELECT * FROM attendance")
    records = mycursor.fetchall()
    if not records:
        print("No records found.")
    for row in records:
        print(row)


def display_specific_student():
    student_id = int(input("Enter Student ID to view: "))
    mycursor.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    records = mycursor.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print(" No student found with that ID.")


def update_attendance():
    student_id = int(input("Enter Student ID to update: "))
    mycursor.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    record = mycursor.fetchone()

    if record:
        print("Existing Record:", record)
        status = input("Enter new status (P/A): ").upper()
        mycursor.execute("UPDATE attendance SET status = %s WHERE student_id = %s", (status, student_id))
        mydb.commit()
        print(" Attendance updated successfully!")
    else:
        print(" No student found with that ID.")


def delete_attendance():
    student_id = int(input("Enter Student ID to delete: "))
    mycursor.execute("SELECT * FROM attendance WHERE student_id = %s", (student_id,))
    record = mycursor.fetchone()

    if record:
        confirm = input("Are you sure you want to delete this record? (y/n): ").lower()
        if confirm == 'y':
            mycursor.execute("DELETE FROM attendance WHERE student_id = %s", (student_id,))
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


def fee_management():
    print("\n====FEE MANAGEMENT====")
    # Ask user if they want to see fee structure
    show = input("Do you want to see the fee structure table? (y/n): ").lower()
    if show == 'y':
        mycursor.execute("SELECT * FROM FEESTRUCT")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    # Track fee payments
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS FEE(
            Name VARCHAR(20) PRIMARY KEY,
            Class INT,
            Amountpaid INT
        )
    ''')

    while True:
        ch = input("Do you want to insert fee payment?(y/n): ").lower()
        if ch == 'y':
            name = input("Enter name of student: ").strip()
            class1 = int(input("Enter class: "))
            amt = int(input("Enter amount paid: "))
            query = "INSERT INTO FEE (Name, Class, Amountpaid) VALUES (%s, %s, %s)"
            values = (name, class1, amt)
            mycursor.execute(query, values)
            mydb.commit()
            print("Payment recorded successfully")
        
        elif ch == 'n':
            break
        else:
            print("Wrong choice. Please enter 'y' or 'n'.")

    # Generate fee receipt
    nm = input("Enter name of student whose payment receipt required: ")
    mycursor.execute("SELECT * FROM FEE WHERE Name=%s", (nm,))
    receipt = mycursor.fetchall()
    if receipt:
        print("PAYMENT RECEIPT DETAILS: ")
        for z in receipt:
            print(z)
        print("THANK YOU!")
    else:
        print("Not found")

fee_management()


# Club management system
def club_management():
    # Scheduling clubs
    print("\n====CLUB MANAGEMENT====")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SCHEDULE(Club VARCHAR(30) PRIMARY KEY, Date DATE)")
    
    while True:
        ch = input("Any new clubs? (y/n): ").lower()
        if ch == 'y':
            club = input("Enter club name: ").strip()
            date = input("Enter event date (yyyy-mm-dd): ").strip()
            
            # Insert only if not exists
            mycursor.execute("SELECT * FROM SCHEDULE WHERE Club=%s", (club,))
            if not mycursor.fetchone():
                mycursor.execute("INSERT INTO SCHEDULE(Club, Date) VALUES (%s,%s)", (club, date))
                mydb.commit()
                print("NEW CLUB INSERTED")
            else:
                print("Club already scheduled.")
        
        elif ch == 'n':
            break
        else:
            print("Wrong choice. Please enter 'y' or 'n'.")

    # Display schedule
    print("\n--- CLUBS SCHEDULED ---")
    mycursor.execute("SELECT * FROM SCHEDULE")
    sched = mycursor.fetchall()
    for a in sched:
        print(a)

    # Registration
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS REGISTER(
            Clubname VARCHAR(20),
            Studentname VARCHAR(20),
            Class INT
        )
    """)

    while True:
        ch = input("\nDo you want to register for a club? (y/n): ").lower()
        if ch == 'y':
            club1 = input("Enter club name: ").strip()
            stu = input("Enter student name: ").strip()
            class1 = int(input("Enter class: "))
            
            # Optional: prevent duplicate registration
            mycursor.execute("""
                SELECT * FROM REGISTER WHERE Clubname=%s AND Studentname=%s
            """, (club1, stu))
            
            if not mycursor.fetchone():
                mycursor.execute(
                    "INSERT INTO REGISTER(Clubname, Studentname, Class) VALUES (%s,%s,%s)",
                    (club1, stu, class1)
                )
                mydb.commit()
                print("YOU HAVE REGISTERED!")
            else:
                print("Student already registered for this club.")
        
        elif ch == 'n':
            break
        else:
            print("Wrong choice. Please enter 'y' or 'n'.")

    print("\nTHANK YOU!")

# Run club management
club_management()
