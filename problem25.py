# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

a=int(input("Enter a: "))
b=int(input("Enter b: "))
if(b==0):
    raise ZeroDivisionError("Infinite")
else:
    print(f"The division a/b is {a/b}")