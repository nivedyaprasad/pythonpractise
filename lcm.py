a = int(input("enter a number: "))
b = int(input("enter a number: "))

if a>b:
    factor = b
else:
    factor = a

while not(a%factor==0 and b%factor==0):
    
    factor-=1

gcd = factor
lcm = (a*b)/gcd
print("gcd is",gcd)
print("lcm is", lcm)
