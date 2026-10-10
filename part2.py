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

        

