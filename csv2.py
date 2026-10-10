import csv
def create():
    f= open("address.csv", 'w', newline='')
    wr = csv.writer(f)
    l2=[]
    while True:
        name=input("eneter name- ")
        mobno = int(input("enter mobileno: "))
        email = input("eneter email: ")

        lst = [name,mobno,email]
        l2.append(lst)

        ch = input("do u wanna continue: ")
        if ch not in 'yY':
            break
    wr.writerows(l2)
    print("records added!")
create()

def read():
    f= open("address.csv", 'r', newline='')
    r = csv.reader(f)
    for i in r:
        print(i)
read()

def search():
    f= open("address.csv", 'r', newline='')
    r = csv.reader(f)
    l2=[]
    srch = int(input("enter mobileno to be searched: "))
    found=0
    for i in r:
        if i[1]==srch:
            found=1
            l2.append(i)
            print("record found!")
            
    if found==0:
        print("record not found")
    else:
        f= open("newaddress.csv", 'w', newline='')
        wr = csv.writer(f)
        wr.writerows(l2)
        
search()


















        
            
    
