#Menu-driven program to create user defined functions to perform the following Text file (Story.txt) operations:
#a) To write data to a text file (Any Sample text data)
#b) To read the entire contents of the file and display it
#c) To print the statistics of the file. Read the text file and display
#the total no. of characters, Total no of words and total no of
#digits.

def wrt():
    f= open("story.txt", "w")
    text = "hello world"
    f.write(text)
    print("data written successfully")
    f.close()

def read():
    f= open("story.txt", "r")
    p = f.read()
    print(p)
    f.close()

def stats():
    f= open("story.txt", "r")
    digcount=0
    q = f.read()
    char = len(q)
    words = len(q.split())
    for i in q:
        if i.isdigit():
            digcount+=1

    print("Characters:", char)
    print("Words:", words)
    print("Digits:", digcount)
            
        
    

    
