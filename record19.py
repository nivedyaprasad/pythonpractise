import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Prasad@123")
mycurs = mydb.cursor()

# Function to create database, table, and insert records
def create_table():
    mycurs.execute("CREATE DATABASE IF NOT EXISTS company")
    mycurs.execute("USE company")
    mycurs.execute("""
        CREATE TABLE IF NOT EXISTS client(
            C_ID INT PRIMARY KEY,
            ClientName VARCHAR(50),
            City VARCHAR(30)
        )
    """)
    print("Table created successfully!\n")

    # Insert 5 records
    for i in range(5):
        cid = input("Enter Client ID: ")
        cname = input("Enter Client Name: ")
        city = input("Enter City: ")

        query = "INSERT INTO client (C_ID, ClientName, City) VALUES (%s, %s, %s)"
        values = (cid, cname, city)
        mycurs.execute(query, values)
        mydb.commit()
        print("Client record added successfully!\n")

# Function to display clients from Delhi
def display_delhi_clients():
    mycurs.execute("USE company")
    mycurs.execute("SELECT * FROM client WHERE City = 'Delhi'")
    records = mycurs.fetchall()

    if records:
        print("\nClients from Delhi:")
        for row in records:
            print(row)
    else:
        print("\nNo clients found from Delhi.\n")

# Function to delete a record based on Client ID
def delete_client():
    mycurs.execute("USE company")
    cid = input("Enter Client ID to delete: ")
    mycurs.execute("DELETE FROM client WHERE C_ID = %s", (cid,))
    mydb.commit()
    print("Record deleted successfully (if it existed).\n")

# Function to display all records
def display_all():
    mycurs.execute("USE company")
    mycurs.execute("SELECT * FROM client")
    records = mycurs.fetchall()

    if records:
        print("\nAll Client Records:")
        for row in records:
            print(row)
    else:
        print("\nNo records found.\n")

# Main menu
while True:
    print("\n=== CLIENT MANAGEMENT MENU ===")
    print("1. Create Database, Table & Insert Records")
    print("2. Display Clients from Delhi")
    print("3. Delete Client by ID")
    print("4. Display All Clients")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_table()
    elif choice == '2':
        display_delhi_clients()
    elif choice == '3':
        delete_client()
    elif choice == '4':
        display_all()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-5.\n")
