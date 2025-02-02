# Write a python program to find the largest number in a list.

numbers=[5, 10, 45, 2, 11]
maximum=numbers[0]
minimum=numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print(f"The largest number is {maximum}")
print(f"The smallest number is {minimum}")
# print("The largest number is "+str(maximum))