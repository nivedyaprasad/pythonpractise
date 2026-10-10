import statistics

s = input("enter nos with spaces- ")
l = s.split() #list of strings -l
l2=[]
for i in l:
    l2.append(int(i))#list of integers -l2
new = []


def oddeven():
    for i in l2:
        if i%2==0:
            l3 = i*2
            new.append(l3)
        else:
            l3=i/2
            new.append(l3)

    print("new modified list- ", new)
oddeven()

def search():
    find = int(input("enter no: "))
    found=0
    for i in l2:
        if i==find:
            print("no found at index", l2.index(find))
            found=1
    if found==0:
        print("not found")
search()

def mode():
    
    m = statistics.mode(l2)
    print(m)
mode()        
    
