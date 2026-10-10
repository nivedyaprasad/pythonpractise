'''● Input: "The quick brown fox" ● Output: "quick"'''

s = input('enter a string: ')
s2=s.split()
ch=0
for i in s2:
    l = len(i)
    if l>ch:
        ch=l
        name=i
print(name)

