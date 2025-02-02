# Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter number: "))
sum=0
i=0
while(i<=n):
    sum+=i
    i+=1
print(f"The sum is: {sum}")

# Another approach by for loop
sum1=0
for i in range(n+1):
    sum1+=i
print(f"The sum is: {sum1}")