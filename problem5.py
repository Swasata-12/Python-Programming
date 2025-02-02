# Write a program to store seven fruits in a list entered by the user.

fruits=[]
for i in range(7):
    name=input(f"Enter the name of {i+1} fruit: ")
    fruits.append(name)
print(fruits)