'''Write a program to find the frequency of all the characters
in a string and then remove all the duplicate characters.'''

s = input('enter a string: ')
s2=''
l = len(s)

for i in s:
    if i not in s2:
        c=0
        for j in s:
            if j==i:
                c+=1
                s2+=i

        print(i,'-',c, end=',')
print(s2)

            
    




