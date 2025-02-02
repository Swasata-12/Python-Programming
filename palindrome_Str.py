# Program to check if a string is palindrome or not

string=input("Enter your string or number: ")
if(string == string[::-1]):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
