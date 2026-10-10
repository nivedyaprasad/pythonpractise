'''l = []
while True:
    s = int(input("enter a number: "))
    l.append(s)
    ch = input("do u wanna add more?: ")
    if ch not in 'yY':
        break
for i in l:
    print(i**2)'''

l = []
for i in range(1,21):
    l.append(i)
print (l)

for i in l:
    if i%4!=0:
        print(i)

