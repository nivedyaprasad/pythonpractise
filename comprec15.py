Stack = []

def PUSH():
    while True:
        Doc_ID = int(input("Enter Doctor ID: "))
        Doc_name = input("Enter Doctor Name: ")
        Doc_spec = input("Enter Specialisation: ")

        # Add all doctors, not just ENT
        L = [Doc_ID, Doc_name, Doc_spec]
        Stack.append(L)

        ch = input("Enter Y or y to create more entries: ")
        if ch not in 'Yy':
            break
    print("\nStack after PUSH:")
    for i in range(len(Stack)-1, -1, -1):
        print(Stack[i])


def POP():
    if not Stack:
        print("Stack is empty!")
    else:
        # Pop only ENT doctors
        temp_stack = []
        found = False
        while Stack:
            doc = Stack.pop()
            if doc[2].upper() == "ENT":
                print("Popped ENT doctor:", doc)
                found = True
                break
            else:
                temp_stack.append(doc)
        # Put back the non-ENT doctors
        while temp_stack:
            Stack.append(temp_stack.pop())
        if not found:
            print("No ENT doctor found in stack!")


def DISPLAY():
    if not Stack:
        print("Stack is empty!")
    else:
        print("\nCurrent Stack:")
        for i in range(len(Stack)-1, -1, -1):
            print(Stack[i])


while True:
    print("\n1. Push Doctor to Stack")
    print("2. Pop ENT Doctor from Stack")
    print("3. Display Stack")
    print("4. Exit")

    c = input("Enter choice: ")

    if c == '1':
        PUSH()
    elif c == '2':
        POP()
    elif c == '3':
        DISPLAY()
    elif c == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")



    
