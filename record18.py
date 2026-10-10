import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Prasad@123")
mycurs = mydb.cursor()

# --- Function to create database, table, and insert records ---
def create_table():
    mycurs.execute("CREATE DATABASE IF NOT EXISTS company")
    mycurs.execute("USE company")
    mycurs.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            Empid INT NOT NULL PRIMARY KEY,
            Empname VARCHAR(50),
            Designation VARCHAR(30),
            Salary FLOAT
        )
    """)
    print("Table created successfully!\n")

    for i in range(5):
        empid = int(input("Enter Employee ID: "))
        empname = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))

        query = "INSERT INTO employee (Empid, Empname, Designation, Salary) VALUES (%s, %s, %s, %s)"
        values = (empid, empname, designation, salary)
        mycurs.execute(query, values)
        mydb.commit()
        print("\nEmployee added successfully!\n")

# --- Function to update salary of all Managers ---
def update_salary():
    mycurs.execute("USE company")
    mycurs.execute("UPDATE employee SET Salary = Salary + 5000 WHERE Designation = 'Manager'")
    mydb.commit()
    print("\nSalary of all Managers increased by 5000!\n")

# --- Function to display all employees ---
def display_employees():
    mycurs.execute("USE company")
    mycurs.execute("SELECT * FROM employee")
    records = mycurs.fetchall()

    print("\nAll Employee Records:")
    for row in records:
        print(row)
# --- Menu-driven section ---
while True:
    print("\n===== EMPLOYEE MENU =====")
    print("1. Create Table and Insert Records")
    print("2. Update Salary of Managers")
    print("3. Display All Employees")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        create_table()
    elif choice == '2':
        update_salary()
    elif choice == '3':
        display_employees()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
