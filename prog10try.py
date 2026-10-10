"""a) Read the contents of the text file line by line and display it.(File should be created before)
b) Display all the lines starting with a letter‘s’.
c) Display each word separated by a # symbol."""

"""def line():
    f= open("story.txt", "r")
    p = f.readlines()
    for i in p:
        print(i)
    f.close()"""

"""def letter_s():
    f= open("story.txt", "r")
    p = f.readlines()
    for line in p:
        words=line.split()
        if words[0][0] in 'Ss':
            print(line, end='')


letter_s()"""


f= open("story.txt", "r")
p = f.read()
words = p.split()

for i in words:
    print (i, end="#")
        
    
    

