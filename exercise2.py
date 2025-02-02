name=input("What is your name?\n")
print("Hi "+name)
fav_colour=input("What is your favourite colour?\n")
print(name+' likes '+fav_colour)
print(f"{name} likes {fav_colour}")
birth_year=input('Birth Year: \n')   # typecasting , the input func always return a string
age=2024-int(birth_year)
print(type(birth_year))
print(type(age))
print("The age of "+name+" is "+str(age))       # we only concatinate same type of variables