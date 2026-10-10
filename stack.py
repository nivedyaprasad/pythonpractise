'''a) To push an object containing Doc_ID and Doc_name of doctors who specialize in "ENT"
to the stack.
b) To Pop the objects from the stack and display them.
c) To display the elements of the stack (after performing PUSH or POP)'''


stack = []

def push():
    while True:    
        docid = int(input('enter doc is: '))
        docname = input('enter doc name: ')
        spl = input('enter specialization: ')
        l = [docid, docname, spl]
        if spl.upper()== 'ENT':
            stack.append(l)
        

        ch = input('do u wanna insert another record? (y/Y): ')
        if ch not in 'yY':
            break
push()

def pop():
    if stack==[]:
        print('stack empty!')
    else:
        print("popped object: ", stack.pop())
pop()
        
def disp():
    for i in stack:
        print(i)
disp()    
            
        
