'''nput: "Hello World" ● Output: "olleH dlroW'''
s = input('enter a string: ')
s2=s.split()
s3 =''

for i in s2:
    w=''
    for j in i:
        w = j+w
    s3+=w+' '
     
    
print(s3)
