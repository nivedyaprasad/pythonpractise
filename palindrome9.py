
s = input('Enter a string: ')
s1=''
for i in s[::-1]:
    s1+=i
if s1==s:
    print('true')
else:
    print('false')
