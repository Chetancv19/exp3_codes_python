#Chetan Velonde 3019155
#Python Program to Find HCF or GCD

#defining the euclid's algorithm for the purpose

def hcf(i,j):
    while(j):
        i, j = j, i%j
    print("The value of HCF is " + str(i))

print("To find the value of the HCF:")
i = int(input("Enter the first value: "))
j = int(input("Enter the second value: "))
hcf(i,j)