'''Input: "Hello World from Python" ● Output: "Python from World Hello" '''
s = input('enter a string: ')
s2=s.split()
s3=''
for i in range(len(s2)-1, -1, -1):
    s3+=s2[i]
    s3+=' '
print(s3)
    
