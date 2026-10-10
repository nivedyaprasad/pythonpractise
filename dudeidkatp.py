import pickle


def add_candidate():
    
    f = open("candidate.dat", "ab")   # append binary
    while True:
        name = input("Enter name: ")
        cid = int(input("Enter ID: "))
        marks = int(input("Enter marks: "))
        
        rec = [name, cid, marks]   # one record
        
        pickle.dump(rec, f)
    
    f.close()
add_candidate()
'''
(ii) ) Write a function to increase the percentage of student to 95% whose admission number
is input by the user.'''

def app():
    
    f = open("candidate.dat", "rb")
    
    records=[]
    found=0
    try:
        while True:
            l = pickle.load(f)
            if l[0]=='niv':
                l[2]=95
                found=1
            records.append(l)
    except EOFError:
        pass
    if found==0:
        print('no such record')
    else:
        print('success!')
    
    f.close()
#################################    
    f = open("candidate.dat", "wb")
    for i in records:
        pickle.dump(i,f)
    
################################3333

    f = open("candidate.dat", "rb")

    try:
        while True:
            l = pickle.load(f)
            print(l)
    except EOFError:
        pass

    f.close()
app()

