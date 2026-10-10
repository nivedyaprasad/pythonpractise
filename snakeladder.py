c=110

for j in range(1,11):
    if j%2!=0:
        c=c-10
        for i in range(10):
            print(c, end=" ")
            c-=1
        print("\n")
    else:
        c=c-10
        for i in range(10):
            print(c+1, end=" ")
            c+=1
        print("\n")
        
