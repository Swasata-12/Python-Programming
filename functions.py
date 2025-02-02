def greet_user(name):                           # function definition with parameters
    print(f"Hi {name}. Welcome aboard")


def square(number):
    return number*number                # return the square of the value given


def goodDay(first_name,ending="Thank You"):
    print(f"Have a good day {first_name}, {ending}")


print("Start")
greet_user("Swasata")                           # calling a function with argument. The arguments can be str
greet_user("Shubham")                           # or a integer value. we can also pass more than one arg
print("Finish")                                 # keyword arg always comes after positional arg

result=square(3)                # we can store the return value in a variable and print that variable 
print(result)
print(square(3))                # or we can directly call the func with args inside another func

for i in range(3):
    first_name=input("Enter your name: ").title()
    goodDay(first_name)

