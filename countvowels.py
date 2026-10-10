'''Input: "Hello World" ● Output: Vowels: 3, Consonants: 7 '''

s = input('enter a string: ')
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in 'AEIOUaeious':
            vc+=1
        else:
            cc+=1
    else:
        continue
print("vowels: ",vc)
print("consonants: ",cc)
        
