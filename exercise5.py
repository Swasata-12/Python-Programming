# Write a python code to calculate the total cost of price in a given list using for loop.

price=[10, 20, 30, 60]
total=0
for i in price:
    total += i                                          # total = total + i   here i is looping variable
print(f"The total price of all the items are {total}")