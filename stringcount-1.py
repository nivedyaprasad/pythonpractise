'''Input: "aaabbc" ● Output: "a3b2c1" '''

s = input('enter a string: ')
s1=''
for i in s:
    c=0
    if i in s1:
        continue
    for j in s:
        
        if j==i:
            c+=1
    s1+=i
    s1+=str(c)
print(s1)
