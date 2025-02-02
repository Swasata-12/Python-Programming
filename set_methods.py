s={1,8,2,3}
s.add(56)                   # add the item 56 in the set
print(s)
print(len(s))               # find the length of the set
s.remove(8)                 # remove the item 8 from the set
print(s)
s.pop()                     # pop an arbritary element from the set
print(s)
# s.clear()                 # clear all the elements of set

s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))         # union of two sets
print(s1.intersection(s2))  # intersection of two sets