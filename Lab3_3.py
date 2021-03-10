#Chetan Velonde 3019155
#Python Program to Convert Decimal to Binary, Octal and Hexadecimal

def base_change(d):
    b = bin(d)
    o = oct(d)
    h = hex(d)
    print("The binary, Octal and Hexadecimal equivalent of the given number " + str(d) + " is " + str(b) + ", \n" + str(o) + ", and " + str(h) + " respectively")

d = int(input("Enter the value of the decimal number to be converted into binary, octal and Hexadecimal: "))
base_change(d)