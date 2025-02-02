# Write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce
l=[14,25,7,13,54,78,16]
def greater(a,b):
    if(a>b):
        return a
    return b
print(f"The greatest no in the list is: {reduce(greater,l)}")