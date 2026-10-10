"""Menu-driven program to perform the following operations on a binary file ‘Player.dat’, which has the following structure:
Player_id, Player_name, Player_game].
a) Create a function File_Create () to add records into the file.
b) Create a function File_Read () to read the records
c) Create a function Search_Data () to search for a particular Player using his Player_id. If found, print the Player details.
Otherwise print appropriate message."""
import pickle

"""def create():
    

    list2 = []
    while True:
        pid = int(input("enter id: "))
        name = input("enter name: ")
        game = input("enter game: ")
        list1 = [pid, name, game]
        list2.append(list1)

        choice = input("wish to enter more recs (y/n)?: ").lower()
        if choice == 'n':
            break

    f=open('Player.dat', 'wb')
    
    pickle.dump(list2,f)
    print("record added")
create()

def read():
    f=open('Player.dat', 'rb')
    rd = pickle.load(f)
    for i in rd:
        pid = i[0] 
        name = i[1] 
        game = i[2]
        list1 = [pid, name, game]
        print(list1)
read()"""

def search():
    f=open('Player.dat', 'rb')
    rd = pickle.load(f)
    found=0
    rno = int(input("enter a rollno: "))

    for i in rd:
    
        if i[0]==rno:
            found=1
            print("current roll no is: ", i[0])
            new = input("enter new roll no: ")
            i[0] = new
            print("update successful! new roll no is: ",i[0])
            break
    if found==0:
        print("player not found!")

search()

        
    
        

    


    
    
    

    
    
