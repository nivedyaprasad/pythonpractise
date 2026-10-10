import csv

def Create_CSV():
    file = open("Login.csv", "w", newline = '')
    List = []
    wrb = csv.writer(file)
    wrb.writerow(["uid", "passwd"])
    while True:
        uid = input("Enter User Id : ")
        passwd = input("Enter password : ")
        L = [uid, passwd]
        List.append(L)
        ch = input("Enter Y or y to create more entries")
        if ch not in 'Yy':
            break
    wrb.writerows(List)
    file.close()
    


def Read_CSV():
    file = open("Login.csv", "r")
    data = csv.reader(file)
    for i in data:
        print(i)
    file.close()


def Search_CSV():
    file = open("Login.csv", "r")
    found = 0
    data = csv.reader(file)
    s = input("Enter user id to be searched: ").strip().lower()
    for i in data:
        if i[0] == s:
            print("USER EXISTS!")
            found = 1
            break

    if found == 0:
        print("NO SUCH ENTRY FOUND")
    file.close()

while True:
    print("Enter \n 1: Add records to Login.csv file \n 2: Read the records in the file \n 3: Search a user using uid \n 4: exit")
    c = int(input("Enter Choice : "))
    if c == 1:
        Create_CSV()
    elif c == 2:
        Read_CSV()
    elif c == 3:
        Search_CSV()
    elif c == 4:
        print("exiting program!")
        break
    else:
        print("ERROR")

