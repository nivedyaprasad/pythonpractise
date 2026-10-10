def insert():
    f = open('story.txt', 'w')
    l=[]

    while True:
        name = input("enter name: ")
        rno = int(input("enter roll no: "))
        rec = [name,rno]
        l.append(rec)
        ch = input('do u wanna add more: ')
        if ch not in 'Yy':
            break
    f.writelines(l)
    print('added successfully')
    f.close()
insert()   


