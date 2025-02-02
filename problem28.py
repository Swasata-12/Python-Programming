# Write a program to filter a list of numbers which are divisible by 5

l=[1,5,15,75,14,52,7,10]
def divisible(n):
    if(n%5==0):
        return True
    return False
divisibleList=filter(divisible,l)
print(f"The filtered list divisible by 5 is: {list(divisibleList)}")