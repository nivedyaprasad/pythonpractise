import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prasad@123"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS student_management")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prasad@123",
    database="student_management"
)
mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
)
""")

login_data = [
    ('admin1', 'admin123', 'admin'),
    ('teacher1', 'teach123', 'teacher'),
    ('student1', 'stud123', 'student')
]

for record in login_data:
    mycursor.execute("SELECT * FROM login WHERE username=%s", (record[0],))
    if not mycursor.fetchone():
        mycursor.execute("INSERT INTO login VALUES (%s,%s,%s)", record)
        mydb.commit()

def login_user():
    uname = input("Please enter username: ").strip()
    pword = input("Please enter password: ").strip()
    mycursor.execute("SELECT username, password, role FROM login WHERE username = %s", (uname,))
    result = mycursor.fetchone()
    if result and result[1] == pword:
        print(f"\nLogin successful. Welcome, {result[0]} ({result[2]})\n")
        return result[2]
    else:
        print("\nInvalid username or password.\n")
        return None


def student_management():
    print("\n=== STUDENT MANAGEMENT ===")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            roll_no VARCHAR(20),
            gender VARCHAR(10),
            class_name VARCHAR(20),
            section VARCHAR(10)
        )
    """)
    mydb.commit()
    while True:
        print("\n1. Insert student record")
        print("2. Display all students")
        print("3. Display specific student")
        print("4. Back to main menu")
        choice = input("Enter choice: ")
        if choice == '1':
            sid = int(input("Student ID: "))
            name = input("Name: ")
            roll = input("Roll no: ")
            gender = input("Gender: ")
            class_name = input("Class: ")
            section = input("Section: ")
            mycursor.execute("""
                INSERT INTO students (student_id, name, roll_no, gender, class_name, section)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (sid, name, roll, gender, class_name, section))
            mydb.commit()
            print("Student added successfully.")
        elif choice == '2':
            mycursor.execute("SELECT * FROM students")
            for x in mycursor.fetchall():
                print(x)
        elif choice == '3':
            sid = int(input("Enter student ID: "))
            mycursor.execute("SELECT * FROM students WHERE student_id=%s", (sid,))
            record = mycursor.fetchone()
            print(record if record else "No record found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


def academic_management():
    print("\n=== ACADEMIC MANAGEMENT ===")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS academics (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            physics INT,
            chemistry INT,
            math INT,
            percentage FLOAT
        )
    """)
    mydb.commit()
    while True:
        print("\n1. Insert record")
        print("2. Display all")
        print("3. Display specific")
        print("4. Back to main menu")
        ch = input("Enter choice: ")
        if ch == '1':
            sid = int(input("Student ID: "))
            name = input("Name: ")
            phy = int(input("Physics: "))
            chem = int(input("Chemistry: "))
            math = int(input("Math: "))
            pc = (phy + chem + math) / 3
            mycursor.execute("""
                INSERT INTO academics (student_id, name, physics, chemistry, math, percentage)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (sid, name, phy, chem, math, pc))
            mydb.commit()
            print("Academic record added.")
        elif ch == '2':
            mycursor.execute("SELECT * FROM academics")
            for x in mycursor.fetchall():
                print(x)
        elif ch == '3':
            sid = int(input("Enter student ID: "))
            mycursor.execute("SELECT * FROM academics WHERE student_id=%s", (sid,))
            rec = mycursor.fetchone()
            print(rec if rec else "Not found.")
        elif ch == '4':
            break
        else:
            print("Invalid choice.")


def attendance_management():
    print("\n=== ATTENDANCE MANAGEMENT ===")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            student_id INT PRIMARY KEY,
            doa DATE,
            name VARCHAR(100),
            status CHAR(1)
        )
    """)
    mydb.commit()
    while True:
        print("\n1. Insert attendance")
        print("2. Display all")
        print("3. Back to main menu")
        c = input("Enter choice: ")
        if c == '1':
            sid = int(input("Student ID: "))
            name = input("Name: ")
            doa = input("Enter attendance date (YYYY-MM-DD): ")
            status = input("Present or Absent (P/A): ").upper()
            mycursor.execute("""
                INSERT INTO attendance (student_id, name,doa , status)
                VALUES (%s,%s,%s,%s)
            """, (sid, name,doa, status))
            mydb.commit()
            print("Attendance added.")
        elif c == '2':
            mycursor.execute("SELECT * FROM attendance")
            for x in mycursor.fetchall():
                print(x)
        elif c == '3':
            break
        else:
            print("Invalid choice.")


def fee_management():
    print("\n==== FEE MANAGEMENT SYSTEM ====")
    while True:
        print("\n1. View Fee Structure")
        print("2. Track Fee Payment")
        print("3. Generate Fee Receipt")
        print("4. Back to main menu")

        ch = input("Enter choice: ")

        if ch == '1':
            # Fee Structure
           mycursor.execute("SELECT * FROM FEESTRUCT")
           result = mycursor.fetchall()
           for x in result:
                print(x)

        elif ch == '2':
            # Track fee payments
            mycursor.execute('CREATE TABLE IF NOT EXISTS FEE(Name varchar(20) Primary key, Class integer, Amountpaid integer)')
            while True:
                ch2 = input("Do you want to insert fee payment?(y/n): ")
                if ch2 == 'y':
                    name = input("Enter name of student: ")
                    class1 = int(input("Enter class: "))
                    amt = int(input("Enter amount paid: "))
                    query = "INSERT INTO FEE (Name, Class, Amountpaid) VALUES (%s, %s, %s)"
                    values = (name, class1, amt)
                    mycursor.execute(query, values)
                    mydb.commit()
                    print("Payment recorded successfully")
                elif ch2 == 'n':
                    break
                else:
                    print("Wrong choice")

        elif ch == '3':
            # Generate fee receipt
            nm = input("Enter name of student whose payment receipt is required: ")
            mycursor.execute("SELECT * FROM FEE WHERE Name=%s" ,(nm,))
            receipt = mycursor.fetchall()
            mydb.commit()
            if receipt:
                print("\n--- PAYMENT RECEIPT DETAILS ---")
                for z in receipt:
                    print(z)
                print("THANK YOU!")
            else:
                print("Not found")

        elif ch == '4':
            break

        else:
            print("Invalid choice, try again.")



def club_management():
    print("\n=== CLUB MANAGEMENT ===")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            Club VARCHAR(30) PRIMARY KEY,
            Date DATE
        )
    """)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS register (
            Clubname VARCHAR(30),
            Studentname VARCHAR(30)
        )
    """)
    mydb.commit()
    while True:
        print("\n1. Add Club")
        print("2. View Clubs")
        print("3. Register Student")
        print("4. Back to main menu")
        c = input("Enter choice: ")
        if c == '1':
            club = input("Club name: ")
            date = input("Date (YYYY-MM-DD): ")
            mycursor.execute("INSERT INTO schedule VALUES (%s,%s)", (club, date))
            mydb.commit()
            print("Club added.")
        elif c == '2':
            mycursor.execute("SELECT * FROM schedule")
            for x in mycursor.fetchall():
                print(x)
        elif c == '3':
            club = input("Club name: ")
            name = input("Student name: ")
            mycursor.execute("INSERT INTO register (Clubname, Studentname) VALUES (%s, %s)", (club, name))
            mydb.commit()
            print("Registered successfully.")
        elif c == '4':
            break
        else:
            print("Invalid choice.")


def main_menu():
    role = login_user()
    if not role:
        return
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Student Management")
        print("2. Academic Management")
        print("3. Attendance Management")
        print("4. Fee Management")
        print("5. Club Management")
        print("6. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            student_management()
        elif ch == '2':
            academic_management()
        elif ch == '3':
            attendance_management()
        elif ch == '4':
            fee_management()
        elif ch == '5':
            club_management()
        elif ch == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


main_menu()
