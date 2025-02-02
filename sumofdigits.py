# Write a function to calculate the sum of all digits in a given number.

def sum_of_digits(n):
    sum=0
    for ch in str(n):
        sum+=int(ch)
    print(f"The sum of all digits of {n} is {sum}")
    
n=int(input("Enter a number: "))
sum_of_digits(n)