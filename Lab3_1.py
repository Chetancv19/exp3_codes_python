import string
#def palindrome(s):
#    if list(s) == list(s[::-1]):
#        print("The string is a palindrome.")
#    else:
#        print("The string is not a palindrome.")

#s = input("Enter the string to check for palindrome: ")
#print(type(s))
#palindrome(s)



#Chetan Velonde 3019155
def palindrome(s):
    s_1 = reversed(s)
    if s == s_1:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

s = input("Enter the string to check for palindrome: ")
palindrome(s)