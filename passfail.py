# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1=int(input("Enter the marks of 1 subject: "))
marks2=int(input("Enter the marks of 2 subject: "))
marks3=int(input("Enter the marks of 3 subject: "))
total_percentage=(marks1+marks2+marks3)/3
if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed")
else:
    print("You Failed!")