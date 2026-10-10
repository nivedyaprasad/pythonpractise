s=0
k=""
Total = 0
while k != 'n':
    s = int(input("input any number:"))
    Total = Total + s
    k = input("would you like to enter more numbers (y/n):")
    
print(Total)
