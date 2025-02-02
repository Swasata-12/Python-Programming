# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    @staticmethod
    def greet_user():
        print("Hi Swasata. After Calculating we get: ")
    
    
    def __init__(self,n):
        self.n=n


    def get_square(self):
        print(f"Square is: {self.n*self.n}")


    def get_cube(self):
        print(f"Cube is: {self.n**3}")


    def get_squareroot(self):
        print(f"Squareroot is: {self.n**(1/2)}")


n=int(input("Enter a number: "))
a=Calculator(n)
# a.greet_user()
Calculator.greet_user() # calling static method using class 
a.get_square()
a.get_cube()
a.get_squareroot()