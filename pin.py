'''Priya has stored all her passwords in one binary file named ‘PASSWD.DAT’.
The passwords were stored in following format:
[app_name, username, password]
i. Write a function that accepts app name as a parameter and displays the
username and password for that particular app.
ii. Write a function to read the data and display all the app names which start
with ‘A’.
iii. Write a function to add a new app detail to the binary file'''

def disp():
    f = open('PASSWD.DAT','rb')
    l = pickle.load(f)
    found=0
    try:
        for i in l:
            if i[0]=='':
                found=1
                print(i[1],i[2])
    except EOFError:
        pass

    if found==0:
        print('not found')
    else:
        print('yayy')
