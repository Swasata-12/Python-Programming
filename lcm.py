# Python Program to find the L.C.M. of two input number

def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0 and greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm


x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
print(f"The L.C.M of this two numbers is: {lcm(x,y)}")