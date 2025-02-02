is_hot=False
is_cold=True
statement1="""
It's a hot day.
Drink plenty of water."""
statement2="""
It's a cold day.
Wear warm clothes"""
if is_hot:
    print(statement1)
    #print("Drink plenty of water")
elif is_cold:
    print(statement2)
    #print("Wear warm clothes")
else:
    print("It's a lovely day")


# short hand if else statement 
a=330
b=3303
print("A") if a>b else print("=") if a==b else print("B") 

c=9 if a>b else 0
print(c)