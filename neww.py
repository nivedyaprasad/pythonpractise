import pickle
def create():
    with open('passengers.dat', 'wb') as f:
        while True:
            pnr = input("Enter Passenger Number (PNR): ")
            pname = input("Enter Passenger Name: ")
            brdstn = input("Enter Boarding Station: ")
            destn = input("Enter Destination Station: ")
            fare = float(input("Enter Fare: "))
                    
                    # Store as a list as per the structure: [PNR, PName, BRDSTN, DESTN, FARE]
            record = [pnr, pname, brdstn, destn, fare]
            pickle.dump(record, f)
                    
            choice = input("Do you want to add more records? (Y/N): ")
            if choice.lower() != 'y':
                    break
create()
def search(s):
    with open('passengers.dat', 'rb') as f:#READING
    
        try:
            while True:
                l = pickle.load(f)
                
                if l[3]==s:
                    print(l)
        except EOFError:
            pass
s = input("Enter destination: ")
search(s)

def update():
    with open('passengers.dat', 'rb') as f:
        rec=[]
        try:
            while True:#READING
                l = pickle.load(f)
                l[4] *= 1.05
                rec.append(l)
        except EOFError:
            pass
############################
    with open('passengers.dat', 'wb') as f:
        for i in rec:
            pickle.dump(i,f)

    with open('passengers.dat', 'rb') as f:
        try:
            while True:
                l = pickle.load(f)
                print(l)
        except EOFError:
            pass
            
update()


















            
