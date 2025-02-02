import findmaxno
# numbers=[10,3,6,2]
# maxno=findmaxno.find_max(numbers)
# print(maxno)

n=int(input("Enter no of items you want to take: "))
numbers=[]
for i in range(n):
    item=int(input(f"Enter {i+1} item: "))
    numbers.append(item)
maxno=findmaxno.find_max(numbers)
print(f"The largest number in the given list is {maxno}")