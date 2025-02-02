#weight=input("Enter your weight in Pounds: ")
#weight_after = 0.453592 * int(weight)               # typecast weight as integer
#print("Your weight in kg is "+str(weight_after))    # typecast weight_after as string

weight=int(input("Enter your weight: "))
unit=input("(L)bs or (K)g: ")
if unit.upper()=="L":
    converted = weight * 0.45
    print(f"You are {converted}Kgs")
else:
    converted = weight // 0.45
    print(f"You are {converted}Lbs")