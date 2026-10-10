'''Program to prompt the user to input a string (sentence). Write a menu-driven program to
create separate user defined functions to print the statistics related to the inputted string.
a) Print total number of characters (including spaces and punctuations)
b) Print total number of words.
c) Check whether any alphabet is present, and if present then print the total number of uppercase and lower-case letters. Otherwise print appropriate message.
d) Exit'''
inp = input("enter a sentence- ")
def char():
    l = len(inp)
    print("total characters are- ",l)
char()

def words():
    s=inp.split(' ')
    words = len(s)
    print("total words are- ",words)
words()

def alpha():
    c=0
    for i in inp:
        if i.isalpha:
            c+=1

    print(c)
alpha()           
