#Chetan Velonde 3019155
#Python Program to Find LCM

#Using GCD method
def lcm(i,j):
    num1 = i
    num2 = j
    while(j):
        i, j = j, i%j
    print(i)
    gcd = abs(num1*num2)/i
    print("The value of LCM is " + str(gcd))

print("To find the value of the LCM:")
i = int(input("Enter the first value: "))
j = int(input("Enter the second value: "))
lcm(i,j)