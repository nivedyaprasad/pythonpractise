'''Menu-driven program to create user defined functions to perform the following Text file
(Story.txt) operations:
a) To write data to a text file (Any Sample text data)
b) To read the entire contents of the file and display it
c) To print the statistics of the file. Read the text file and display the total no. of characters,
Total no of words and total no of digits'''

def wr():
    f = open('story.txt', 'w')
    l = input("enter text- ")
    f.write(l)
    print('written!')
wr()

def readtxt():
    f = open('story.txt', 'r')
    l = f.readlines()
    for i in l:
        print(i)
readtxt()

def stats():
    f = open('story.txt', 'r')
    l = f.read() #string full
    
    char = len(l)
    print("total characters are- ",char)
    l2= l.split() #list of strings
    length = len(l2)
    print("total words are- ", length)
    count=0
    for i in l:
        if i.isdigit():
            count+=1
    print("total digits- ",count)
stats()            
            
    


    
