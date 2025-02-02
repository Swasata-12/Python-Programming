from array import *

a1=array("i",[23,56,11])
print(type(a1))
print(a1)
print(len(a1))

# Printing the array elements
for x in a1:
    print(x)
for i in range(3):
    print(a1[i],end=" ")
    # print("")

# Array methods
a1.append(100)          # Append the element to the last
print(a1)
print(a1.count(100))    # Count how many times the element occures
print(a1.index(56))     # Return the index of the element
print(a1.pop())         # Pop the last element from the array and return it
a1.pop(1)               # Pop the element from the mentioned index 
print(a1)
a1.remove(23)           # Remove the element 
print(a1)

# We can also use numpy here 