'''Program to print from 1 to n in separate lines.
2. Program to find the sum of all numbers from 1 to n.
3. Input a string from the user; print the Unicode value of every character in the string in a separate line.
4. Program to print all odd numbers from 1 to n in separate lines.
5. Program to print all numbers divisible by both 3 and 5 between 1 and n in separate lines.
6. Program to print all numbers between 1 and n which end with 9, in separate lines.
7. Program to print all numbers from 1 to 10 except 5.
8. Write a program to take first name, middle name, and last name as input in different lines, and print them on the terminal as a single name separated by spaces.
9. Classify the number entered by the user as an even or odd number; keep prompting the user for further numbers until the user says “stop.”
10. Generate n random integers between 1 and 1000.
11. Write a program to print all Armstrong numbers from 1 to n (display a suitable message if none exist). An Armstrong number is one whose digits, each raised to the
power equal to the number of digits, sum to the number itself — e.g. the three-digit Armstrong numbers include 0, 1, 153, 370, 371, 407; four-digit examples include
1634, 8208, 9474, and there are many more.
12. Given a number, determine whether it is an Armstrong number.
13. Display whether a given number is a perfect number (a positive integer equal to the sum of its positive divisors, excluding the number itself).
'''


'''n = int(input("enter a number: "))
i=0
for i in range(n+1):
    print (i)

n = int(input("enter a number: "))
i=0
sum=0

for i in range(n+1):
    sum+=i

print(sum)


n = input("enter a string: ")
for i in n:
    print(ord(i))

n = int(input("enter a number: "))
i=1
for i in range(1,n+1,2):
    print(i)

n = int(input("enter a number: "))
for i in range(n+1):
    if i%3==0 and i%5==0:
        print(i)

n = int(input("enter a number: "))
for i in range(n+1):
    if i%10==9:
        print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

f = input("enter first name: ")
m = input("enter middle name: ")
l = input("enter last name: ")

print(f,m,l,end="")

while True:
    print("1. enter a number\n2. stop")
    ch = int(input("enter choice: "))
    if ch==1:
        n = int(input("enter a number: "))
        
        if n%2==0:
            print("number is even")
        else:
            print("number is odd")
    if ch==2:
        break

import random
for i in range(5):
    print(random.randint(1,100))

##armstrong##
n = int(input("enter a number: "))
dupe = n
c = len(str(n))
print("count: ",c)
s=0
while n>0:
    d = n%10
    s += (d**c)
    n = n//10

if s==dupe:
    print("yes is armstrong")
else:
    print("is not armstrong")

n = int(input("enter a number: "))

for i in range(0,n+1):
    c = len(str(i))
    dupe = i
    s=0
    while i>0:
        d = i%10
        s += (d**c)
        i = i//10

    if s==dupe:
        print(dupe)

n = int(input("enter a number: "))
dupe = n
s=0
while n>0:
    d = n%10
    s=(s*10)+d
    n=n//10
if s==dupe:
    print("yes tis palindrome")
else:
    print("nope!")


n = int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"is a perfect number")
else:
    print("nahhh")

14. Program to swap the first and last digits of a given number and print the new number.

n = int(input("enter a number: "))
c = len(str(n))
s=0
d = n%10
s+=(d*10**(c-1))
n=n//10


d=n%(10**(c-2))
s+=(d*10)
n=n//10**(c-2)

s+=n

print(s)


n = int(input("enter a number: "))
s=0
dupe=n
while n>0:
    d=n%10
    
    f=1

    for i in range(1,d+1):
        
        f *= i
    print(f)
    n=n//10
    s+=f
print("sum: ",s)

if s==dupe:
    print("is a strong number")
else:
    print("is not a strong number")



n1=0
n2=1

n = int(input("enter a number: "))
print(n1,end=" ")
print(n2,end=" ")
for i in range(n-2):
    n3 = n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3

s1 = int(input("enter a number: "))
s2 = int(input("enter a number: "))  
s3 = int(input("enter a number: "))  
s4 = int(input("enter a number: "))  
d1 = int(input("enter a number: "))  
d2 = int(input("enter a number: "))

if s1==s2==s3==s4 and d1==d2:
    print("quadrilateral is a square")
elif s1==s3 and s2==s4 and d1==d2:
    print("quadrilateral is a rectangle")
elif s1==s2==s3==s4:
    print("quadrilateral is a rhombus")
elif s1==s3 and s2==s3:
    print("quadrilateral is a parallelogram")
elif (s1 == s2 and s3 == s4) or (s2 == s3 and s4 == s1):
    print("quadrilateral is a kite")
else:
    print("quadrilateral is a quad")'''
    



    


        




