'''● Input: "Hello World" ● Output: "hELLO wORLD"'''
s = input('enter a string: ')
s2=''
for i in s:
    if i.isupper():
        n = i.lower()
        s2+=n
    elif i.islower():
        n = i.upper()
        s2+=n
    else:
        n=' '
        s2+=n

print(s2)
