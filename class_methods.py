class Employee:
    a = 1           # class attribute
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45            # instance attribute

e.show()
Employee.show()