s = input('Enter a string: ')
s1=''
for i in s:
    if i not in s1:
        s1+=i
l=len(s1)
print(l)
