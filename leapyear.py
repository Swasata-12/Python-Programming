# Python program to check if year is a leap year or not

year=int(input("Enter year: "))
if (year%400==0) and (year%100==0):
    print(f"{year} is a Leap year")
elif (year%4==0) and (year%100!=0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")