# Write a program to find whether a given number is prime or not

n=int(input("Enter number: "))
count=0
i=2
while(i<=n/2):
    if(n%i==0):
        count+=1
    i+=1
if(count>0):
    print("It is not a Prime number")
else:
    print("It is a Prime number")

# Another approach
for i in range(2,n):
    if(n%i)==0:
        print("Number is not Prime")
        break
else:
    print("Number is Prime")