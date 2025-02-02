# Tuples are immutable and can contain different types of data types like lists

tuple1=(1,2,3)
tuple2=(4,5,60)
concatenated=tuple1+tuple2
print(concatenated)
repeated=tuple1*3
print(repeated)
# there are two methods in tuple
print(tuple1.count(2))              # count how many times 2 occures in the tuple
print(tuple2.index(60))             # return the index of first occurence of item 60 
print(len(tuple1))
print(60 in tuple2)

# Unpacking
e=tuple1[0]*tuple1[1]*tuple1[2]     # this is very tidious to do
print(e)
x,y,z=tuple1
f=x*y*z
print(f)
print(x)
print(y)
print(z)