# Write a python program to remove the duplicates in a list using list methods.

numbers=[5, 10, 25, 40, 10, 5]                  # There is an another approach to solve this (see copy)
uniques=[]
# for i in numbers:
#     if numbers.count(i) > 1:
#         numbers.remove(i)
#numbers.sort()
#print(numbers)


for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)