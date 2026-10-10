import csv

def create():
    f = open("login.csv", 'w', newline='')
    csvwr = csv.writer(f)

    l2=[]
    userid = input("enter user id: ")
    pswd = int(input("enetr pswd: "))
    l1 = [userid, pswd]
    l2.append(l1)

    csvwr.writerows(l2)
    print("records added")

def display():
     f = open("login.csv", 'r', newline='')
     rdr = csv.reader(f)
     for i in rdr:
         print(i)

def search():
    f = open("login.csv", 'r', newline='')
    rdr = csv.reader(f)
    inp= input("eneter id: ")
    found=0
    for i in rdr:
        if i[0]==inp:
            print("user exists")
            found=1
            break
    if found==0:
        print("user not found")

while True:
    ch=input('enter choice- ')
    if ch=='1':
        create()
    elif ch=='2':
        display()
    elif ch=='3':
        search()
    elif ch=='4':
        break
        
        













    
