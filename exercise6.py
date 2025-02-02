# Write a python code to print the below fig. using nested for loop.
# xxxxx
# xx
# xxxxx
# xx
# xx

numbers=[5,2,5,2,2]
#for i in numbers:
 #   print("x"*i)

for i in numbers:
    output=""
    for j in range(i):
        output += "x"
    print(output)

