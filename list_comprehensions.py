# List Comprehension is an elegant way to create lists based on existing lists.

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)

list1 = [1,7,12,11,22]
list2 = [item for item in list1 if item > 8]
list3=[item for item in list1 if (item%2==0)]
print(list1)
print(list2)
print(list3)