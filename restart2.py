## Count the number of factors of a given number, and the sum of those factors.
## Display the squares of all numbers, and the square roots of all numbers, from 1 to n.

'''n = int(input("enter a number: "))
c=0
s=0
for i in range(1,n):
    if n%i==0:
        print(i)
        c+=1
        s+=i
print("number of factors is", c)
print("sum of those factors is",s)


n = int(input("enter a number: "))
for i in range(1,n):
    if i*i==n:
        print(i)

 Program to display the first Fibonacci number that is strictly greater than n.

n = int(input("enter a number: "))
n1=0
n2=1

n3=0

while not(n3>n):
    n3=n1+n2
    
    n1=n2
    n2=n3
print(n3)'''

n = int(input("enter a number: "))
for i in range(1,n+1):
    
    
