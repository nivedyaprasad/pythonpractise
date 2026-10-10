Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

== RESTART: C:\Users\krish\AppData\Local\Programs\Python\Python312\record18.py =

===== EMPLOYEE MENU =====
1. Create Table and Insert Records
2. Update Salary of Managers
3. Display All Employees
4. Exit
Enter your choice (1-4): 3

All Employee Records:
(200, 'hazel', 'manager', 25000.0)
(201, 'nidhi', 'assistant', 10000.0)
(202, 'nivedya', 'manager', 25000.0)
(203, 'joanne', 'manager', 25000.0)
(204, 'prisha', 'assistant', 10000.0)

===== EMPLOYEE MENU =====
1. Create Table and Insert Records
2. Update Salary of Managers
3. Display All Employees
4. Exit
Enter your choice (1-4): 4
Exiting program...

== RESTART: C:\Users\krish\AppData\Local\Programs\Python\Python312\record18.py =

===== EMPLOYEE MENU =====
1. Create Table and Insert Records
2. Update Salary of Managers
3. Display All Employees
4. Exit
Enter your choice (1-4): 3

All Employee Records:
(200, 'hazel', 'manager', 25000.0)
(201, 'nidhi', 'assistant', 10000.0)
(202, 'nivedya', 'manager', 25000.0)
(203, 'joanne', 'manager', 25000.0)
(204, 'prisha', 'assistant', 10000.0)

===== EMPLOYEE MENU =====
1. Create Table and Insert Records
2. Update Salary of Managers
3. Display All Employees
4. Exit
Enter your choice (1-4): 4
Exiting program...

== RESTART: C:\Users\krish\AppData\Local\Programs\Python\Python312\record19.py =

=== CLIENT MANAGEMENT MENU ===
1. Create Database, Table & Insert Records
2. Display Clients from Delhi
3. Delete Client by ID
4. Display All Clients
5. Exit
Enter your choice (1-5): 4

All Client Records:
(100, 'ramesh', 'bangalore')
(101, 'ram', 'delhi')
(103, 'anurag', 'delhi')
(104, 'anita', 'delhi')

=== CLIENT MANAGEMENT MENU ===
1. Create Database, Table & Insert Records
2. Display Clients from Delhi
3. Delete Client by ID
4. Display All Clients
5. Exit
Enter your choice (1-5): 
== RESTART: C:\Users\krish\AppData\Local\Programs\Python\Python312\rceord16.py =
>>> 
== RESTART: C:\Users\krish\AppData\Local\Programs\Python\Python312\rceord16.py =

===== PRODUCT MENU =====
1. Create Table and Insert Records
2. Display All Products
3. Display Specific Product
4. Exit
Enter choice (1-4): 2
Traceback (most recent call last):
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\Lib\site-packages\mysql\connector\connection_cext.py", line 772, in cmd_query
    self._cmysql.query(
_mysql_connector.MySQLInterfaceError: Table 'company.product' doesn't exist

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\rceord16.py", line 65, in <module>
    display_products()
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\rceord16.py", line 32, in display_products
    mycurs.execute("SELECT * FROM product")
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\Lib\site-packages\mysql\connector\cursor_cext.py", line 353, in execute
    self._connection.cmd_query(
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\Lib\site-packages\mysql\connector\opentelemetry\context_propagation.py", line 97, in wrapper
    return method(cnx, *args, **kwargs)
  File "C:\Users\krish\AppData\Local\Programs\Python\Python312\Lib\site-packages\mysql\connector\connection_cext.py", line 781, in cmd_query
    raise get_mysql_exception(
mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'company.product' doesn't exist
