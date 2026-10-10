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


        



