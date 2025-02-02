# Python Program to Flatten a Nested List

import itertools

my_list = [[1], 
           [2, 3], 
           [4, 5, 6, 7]]
flat_list=[]
for rows in my_list:
    for column in rows:
        flat_list.append(column)
print(flat_list)

# Another approach by using itertools 
flat_list1=list(itertools.chain(*my_list))
print(flat_list1)

# Another approach by using sum() function
flat_list2=sum(my_list,[])
print(flat_list2)