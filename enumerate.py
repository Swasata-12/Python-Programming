l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function
# The ‘enumerate’ function adds counter to an iterable and returns it

# my_list = [21, 44, 35, 11]

# for index, val in enumerate(my_list, start=1):
#     print(index, val)

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")        # Prints the items of list 1 with index