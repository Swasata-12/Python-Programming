# Python program to check if the number is an Armstrong number or not

num=input("Enter a number: ")
sum=0
for ch in num:
    sum += int(ch)**len(num)
if(sum==int(num)):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


# Another approach
num = 1634
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
