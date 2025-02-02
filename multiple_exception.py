# Python Program to Catch Multiple Exceptions in One Line

string=input("Enter a String: ")

try:
    num=int(input("Enter a number: "))
    print(string+num)
except (TypeError,ValueError) as e:
    print(e)