#Chetan Velonde 3019155
#Write a program in python to determine whether the name entered is in upper case, lower case or wrong format.
# Generate a function and use it in the code.
# for the above code, do conversion for the string. i.e upper case if found will be converted to lower case and vice a versa
# for the wrong statement, do not do any computation.
def case_check(s):
    str_1 = s.isupper()
    str_2 = s.islower()
    if (str_1 == True) & (str_2 == False):
        print("The string is in upper case.")
        print("The string in lower case is " + s.lower())
    elif (str_1 == False) & (str_2 == True):
        print("The string is in lower case.")
        print("The string in lower case is " + s.upper())
    else:
        print("The string does not belong to a single case.")

s = input("Please enter the string for check: ")
case_check(s)
