# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode


p=Programmmer("Harry","90k",700006)
print(p.company,p.name,p.salary,p.pincode)
r=Programmmer("Rohan","60k",700091)
print(r.company,r.name,r.salary,r.pincode)