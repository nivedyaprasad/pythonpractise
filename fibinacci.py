"""n = int(input("enter no: "))
n1=0
n2=1
print(n1)
print(n2)

for i in range(n-2):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

fact=1
n = int(input("enter no: "))
for i in range(1,n+1):
    fact*=i
print(fact)"""

n = int(input("enter no: "))
if n<=1:
    print("not prime")
else:
    for i in range(2,int(n**0.5 +1)):
        if n%i==0:
            print("not prime")
            break
    else:
        print("is prime")
               

