#Chetan Velonde 3019155
#Python program to make a simple calculator

def calculate(a,b,i):
    if i == 1:
        c = a + b
        print(str(a) + " + " + str(b) + " = " + str(c))

    if i == 2:
        c = a - b
        print(str(a) + " - " + str(b) + " = " + str(c))

    if i == 3:
        c = a*b
        print(str(a) + " * " + str(b) + " = " + str(c))

    if i == 4:
        c = a/b
        print(str(a) + " / " + str(b) + " = " + str(c))

    if i == 5:
        print("The value of base and power is " + str(a) + " and " + str(b) + " respectively")
        c = a**b
        print(str(a) + "^" + str(b) + " = " + str(c))
print("The operations available for calculation are: ")
print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Power")
i = int(input("Enter the value corresponding to the operation: "))
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
calculate(a,b,i)
