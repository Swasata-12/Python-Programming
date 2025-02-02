# Write a program to find the greatest of four numbers entered by the user.

greatest=0
for i in range(4):
    num=int(input(f"Enter {i+1} number: "))         # we can also apply if...else here
    if (num>greatest):
        greatest=num
print(f"The greatest number is {greatest}")

# Another approach

a1=int(input("Enter 1 number: "))
a2=int(input("Enter 2 number: "))
a3=int(input("Enter 3 number: "))
a4=int(input("Enter 4 number: "))
if (a1>a2 and a1>a3 and a1>a4):
    print(f"Greatest number is {a1}")
elif (a2>a1 and a2>a3 and a2>a4):
    print(f"Greatest number is {a2}")
elif (a3>a1 and a3>a2 and a3>a4):
    print(f"Greatest number is {a3}")
elif (a4>a1 and a4>a2 and a4>a3):
    print(f"Greatest number is {a4}")
else:
    print("Something went wrong!")