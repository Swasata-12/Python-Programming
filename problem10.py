# Write a program which finds out whether a given name is present in a list or not.

list=["Rohan","Swasata","Harry","Rahul"]
name=input("Enter name: ").title()
if(name in list):
    print("Your name is present in the list")
else:
    print("Invalid name")