import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Prasad@123")
mycurs = mydb.cursor()

def create_table():
    mycurs.execute("CREATE DATABASE IF NOT EXISTS company")
    mycurs.execute("USE company")
    mycurs.execute("""
        CREATE TABLE IF NOT EXISTS product(
            Pid INT NOT NULL PRIMARY KEY,
            Pname VARCHAR(50),
            Qty FLOAT,
            Price FLOAT
        )
    """)
    print("Table created!")

    for i in range(5):
        p_id = input("Enter product ID: ")
        pname = input("Enter product name: ")
        qty = input("Enter quantity: ")
        price = input("Enter price: ")

        query = "INSERT INTO product (Pid, Pname, Qty, Price) VALUES (%s, %s, %s, %s)"
        values = (p_id, pname, qty, price)
        mycurs.execute(query, values)
        mydb.commit()
        print("\nProduct added successfully!\n")

def display_products():
    mycurs.execute("USE company")
    mycurs.execute("SELECT * FROM product")
    myrec = mycurs.fetchall()
    print("\nAll Products:")
    for i in myrec:
        print(i)

def display_specific():
    mycurs.execute("USE company")
    while True:
        choice2 = input("\nDo you want to view a specific product? (y/n): ").lower()
        if choice2 != 'y':
            break
        else:
            prod_id = int(input("Enter product ID to view details: "))
            mycurs.execute("SELECT * FROM product WHERE Pid = %s", (prod_id,))
            record = mycurs.fetchone()
            if record:
                print(record)
            else:
                print("No product found with that ID.")

# --- Example usage ---
while True:
    print("\n===== PRODUCT MENU =====")
    print("1. Create Table and Insert Records")
    print("2. Display All Products")
    print("3. Display Specific Product")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        create_table()
    elif choice == '2':
        display_products()
    elif choice == '3':
        display_specific()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")



