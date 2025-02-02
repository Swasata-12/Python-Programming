# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint

class Train:
    @staticmethod
    def greet_user():
        print("Welcome to Indian Railways....")


    def __init__(self,trainNo):
        self.trainNo=trainNo
        self.noSeats=100


    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        self.noSeats-=1


    def get_Status(self):
        print(f"Train no: {self.trainNo} is running on time and {self.noSeats} seats are available")


    def get_Fare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(10, 550)}")


num=int(input("Enter Train No: "))
location=input("Enter Boarding station: ")
destination=input("Enter Destination station: ")
t=Train(num)
t.greet_user()
t.book(location,destination)
t.get_Status()
t.get_Fare(location,destination)
Train.greet_user() # We can call a static method without creating object rather directly call by class name