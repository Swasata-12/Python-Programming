# Write a pythone code to define a type called Person which contain a method talk() and an attribute name

class Person:
    def __init__(self,name):
        self.name=name


    def talk(self):
        print(f"{self.name} Start talking...")


swasata=Person("Swasata")
bob=Person("Bob Smith")
swasata.talk()
bob.talk()
print(swasata.name)
# swasata.name="Marry"
# print(swasata.name)

