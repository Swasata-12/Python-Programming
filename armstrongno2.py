# Program to check Armstrong numbers in a certain interval

lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
print(f"The Armstrong numbers between {lower} and {upper} are: ")
for num in range(lower,upper+1):
    n=len(str(num))
    sum=0
    for ch in str(num):
        sum += int(ch)**n
    if(sum==num):
        print(num)


# Another approach
lower = 100
upper = 2000
for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)