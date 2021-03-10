#Chetan Velonde 3019155
#Python program to find the factors of the number given by the user
import array
s1 = array.factors = []
def factor(num):
    print("The factors of " + str(num) + " are: \n")
    if num > 0:
        for i in range (1, num+1):
            if num % i == 0:
                s1.append(i)
        print(s1)

num = int(input("Enter the value of the Number whose factors are needed: "))
factor(num)
