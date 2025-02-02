# Python Program to Calculate the Area of a Triangle

def area(a,b,c):
    s=(a+b+c)/2
    areaoftri=(s*(s-a)*(s-b)*(s-c))**0.5
    print(f"The Area of the Triangle is {areaoftri}")


while(True):
    a=int(input("Enter 1st side: "))
    b=int(input("Enter 2nd side: "))
    c=int(input("Enter 3rd side: "))
    area(a,b,c)