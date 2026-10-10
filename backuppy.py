
mycurs.execute("""CREATE TABLE students(
               student_id INT NOT NULL PRIMARY KEY,
               roll_no VARCHAR(20) ,
               name VARCHAR(100),
               gender VARCHAR(7),
               dob DATE,
               class_name VARCHAR(20),
               section VARCHAR(10),
               admission_year YEAR,
               contact VARCHAR(15),
               email VARCHAR(100),
               address VARCHAR(255),
               guardian_name VARCHAR(100),
               guardian_contact VARCHAR(15))""")


    mycurs.execute("CREATE TABLE academics (student_id INT NOT NULL PRIMARY KEY, name VARCHAR(50), class_name VARCHAR(20), physics INT, chemistry INT, math INT, english INT, computer INT, PERCENTAGE FLOAT)")
