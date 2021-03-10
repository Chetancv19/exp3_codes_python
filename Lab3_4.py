#Chetan Velonde 3019155
#Python Program to Find ASCII Value of Character
def ascii(c):
    p = ord(c)
    print("The ASCII value of the character " + str(c) + " is given by " + str(p))

c = input("ENTER THE CHARACTER TO GET THE ASCII VALUE: ")
ascii(c)