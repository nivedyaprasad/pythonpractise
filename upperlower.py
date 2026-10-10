'''Menu-driven program to perform the following operations on a CSV file ‘Login.csv’, which
has the structure as [uid, passwd]:
a) Create a function Create_csv () to add records to the file.
b) Create a function Search_csv() to search whether a user exists or not with the uid which is
passed as an argument.'''

import csv

def create():
    f = open('login.csv', 'w', newline='')
    wr = csv.writer(f)
    l=[]

    while True:
        uid = int(input('enter uid- '))
        pswd = input('pswdd- ')
        rec = [uid,pswd]
        l.append(rec)
        ch = input('yY ')
        if ch not in 'yY':
            break
    wr.writerows(l)
    print('records added')
create()

def srch():
    f = open('login.csv', 'r', newline='')
    r = csv.reader(f)
    s = int(input('id- '))
    found=0
    l=[]
    for i in r:
        if int(i[0])==s:
            found=1
            l.append(i)
            print('record found')
            
            
    if found==0:
        print('record not found')

    f = open('newaddress.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerows(l)
    

    
        
srch()
        



















            

        
