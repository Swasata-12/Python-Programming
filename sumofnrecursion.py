# Write a recursive function to calculate the summation of first n natural numbers

def summation(n):
    if(n==1 or n==0):
        return n
    else:
        return n+summation(n-1)
    

n=int(input("Enter a number: "))
print(f"The summation of first {n} natural numbers is: {summation(n)}")


# Another approach by sum of all the list elements
s=[]
for i in range(n+1):
    s.append(i)
print(s)
print(f"The summation of first {n} natural numbers is: {sum(s)}")