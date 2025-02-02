class Mammals:
    def walk(self):
        print("Walk")

class Dog(Mammals):
    def bark(self):
        print("barking")
    # pass

class Cat(Mammals,Dog):
    def annoying(self):
        print("annoying")
    # pass

dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.walk()
cat1.annoying()
cat1.bark()
