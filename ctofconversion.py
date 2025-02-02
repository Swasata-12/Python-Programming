# Write a python program using function to convert Celsius to Fahrenheit.

def conversion(c):
    f=(9*c+160)/5
    return f

c=int(input("Enter temperature in Celcius: "))
print(f"The temperature in Fahrenheit is: {conversion(c)}")