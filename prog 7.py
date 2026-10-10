x = int(input("no of days taken by A to finish work: "))
y = int(input("no of days taken by B to finish work: "))
z = int(input("no of days taken by C to finish work: "))

total = x*y*z*(x*y + y*z + z*x)

print ("no of days to finish work if they work together = ", total)
