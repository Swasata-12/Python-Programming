# Create a calculator capable of performing addition, substraction, multiplication and division operations
# on two numbers. Your program should format the output in a readable manner.

def calculator(option):
    match option:
        case 1:
            return print(f"The summation of {a} and {b} is {a+b}")
        case 2:
            return print(f"The substraction of {a} and {b} is {a-b}")
        case 3:
            return print(f"The multiplication of {a} and {b} is {a*b}")
        case 4:
            return print(f"The division of {a} and {b} is {a/b}")
        case _:
            return "Wrong choice"
            
while(True):
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    print("""
Choose the option which you want to perform: 
1. Addition 2. Substraction 3. Multiplication 4. Division""")
    option=int(input("Enter your option: "))
    calculator(option)
    
