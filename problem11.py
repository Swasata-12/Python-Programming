# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]
for item in l:
    if(item[0]=="S"):                       # if(item.startswith("S")):
        print(f"Hi {item}")