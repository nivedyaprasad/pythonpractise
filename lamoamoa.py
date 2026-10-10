l = []
def push():

    while True:
        ele = input('enter element: ')
        l.append(ele)
        ch = input('want more?: ')
        if ch not in 'Yy':
            break
    print('records added')
push()
def pop():
    if l==[]:
        print('stack empty')
    else:
        print(l.pop(),'popped')
pop()
        
def disp():
    ln = len(l)
    for i in range(ln-1,-1,-1):
        print(l[i])
disp()    
