# Python program to find H.C.F of two numbers

def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0 and y%i==0):
            hcf=i
    return hcf


x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
print(f"The H.C.F of this two numbers is: {hcf(x,y)}")