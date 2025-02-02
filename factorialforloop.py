# Write a program to calculate the factorial of a given number using for loop.

n=int(input("Enter the number whose factorial you want to find: "))
m=1
for i in range(1,n+1):
    m=m*i
print(f"The Factorial of {n} is: {m}")