from functools import reduce
# map function 

l=[1,2,3,4,5]

square=lambda x:x*x
sqList=map(square,l)
print(f"The output of map function is: {list(sqList)}")

# filter function 

def even(n):
    if(n%2==0):
        return True
    return False
onlyEven=filter(even,l)
print(f"The output of the filter function is: {list(onlyEven)}")

# reduce function 

def sum(a,b):
    return a+b
mul=lambda a,b:a*b
print(f"The output of the reduce function is: {reduce(sum,l)}")
print(f"The output of the reduce function is for mul: {reduce(mul,l)}")