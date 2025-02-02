# In python lists are actually referential arrays. Dynamic array is implemented using this concept.

import sys
list=[]
for i in range(100):
    print(i,sys.getsizeof(list))
    list.append(i)