# Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name=input("Enter the name of the student: ")
marks=int(input("Enter the marks of the student: "))
phNo=int(input("Enter Phone No.: "))
print("The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,marks,phNo))