names=["Swasata","Subham","Bob","Mosh","Harry"]  # list of strings
numbers=[1,2,5,56,25]                            # list of integers
friends=["Apple","Orange",5,345.06,False,"Aakash","Rohan"] 
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]                                               # 2D list
print(names)                                    # print the list of names
print(numbers)                                  # print the  list of inntegers
print(names[2])                                 # print the 3rd item of the list
print(names[4])
print(names[2:4])                               # print  the items of the list from index 2 to 3
print(numbers[2])
print(numbers[3])
names[0]="John"                                 # we can modify the list elements using index
print(names)
print(matrix[0][2])                             # print the item on 1st row and 3rd column
print(matrix[2][2])

for i in matrix:                               # we can iterates the items of a matrix and print them using 
    for j in i:                                # nested for loop. Here i represents the each row and j 
        print(j)                               # represents the each item on a particular

friends.append(45)
friends.pop(5)
# print(friends.pop(5))
# friends.pop()
print(friends)
friends[0]="harry"                             # Unlike strings lists are mutable
print(friends)
print(names[len(names)-1])                     # Get the Last Element of the List
print(names[-1])