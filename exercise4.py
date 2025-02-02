# write a python program to implement the following.
# If name is less than 3 character long then print name must be at  least 3 characters otherwise if it's more
# than 50 charecter long then print name can be maximum of 50 charecters, otherwise say name looks good.

name=input("Enter your name:\n")
char=len(name)
if char < 3:                                    # here we can also use if len(name)<3:
    print("Name must be at least 3 charecters")
elif char > 50:
    print("Name can be of maximum 50 charecters")
else:
    print("Name looks good")