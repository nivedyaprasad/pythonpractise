s = input('enter a string: ')
s2=''
for i in s:
    if not i.isspace():
        s2+=i
print(s2)
