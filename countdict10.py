'''Input: "hello world"
● Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}'''

s = input('Enter a string: ')
d={}
for i in s:
    c=0
    for j in s:
        if j==i:
            c+=1
    d[i]=c    

print(d)
