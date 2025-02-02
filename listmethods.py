# Lists are mutable i.e list methods changes the original list.

numbers=[5,2,1,7,4]

list_1 = [1, 'a']
list_2 = [1, 2, 3]

numbers.append(20)              # add item 20 in the list
print(numbers)
numbers.insert(0,10)            # insert item 10 at 0th index 
print(numbers)
numbers.remove(5)               # remove the item 5 from the list
print(numbers)
# numbers.clear()               # remove all the items from the list
numbers.pop()                   # remove the last item from the list
print(numbers)
numbers.pop(2)                  # remove the item at index 2
print(numbers)
print(numbers.index(7))         # return the index of item 7 from the list
print(50 in numbers)            # returns a boolean value if 50 present in the list
print(numbers.count(1))         # count how many times 1 occures in the list
numbers.sort()                  # sort the list
print(numbers)
numbers.reverse()               # reverse the list
print(numbers)
numbers2=numbers.copy()         # copy the original list
print(numbers2)

print(list_1+list_2)            # Concatenates two lists
list_2.extend(list_1)
print(list_2)
print(list(set(list_1+list_2))) # Concatenate two lists with only unique values

# Python Program to Iterate Through Two Lists in Parallel
for i,j in zip(list_1,list_2):
    print(i,j)
