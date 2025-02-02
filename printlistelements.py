# Write a program to print all the elements of a list using while loop and for loop.

l1=[1,"Harry",False,"This","Rohan","Shubham","Shubhi"]
i=0
print(l1)
while i<len(l1):
    print(l1[i])
    i+=1
else:
    print("Done")


for i in l1:
    print(i)
else:
    print("Done")