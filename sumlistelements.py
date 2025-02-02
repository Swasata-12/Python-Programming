# Write a program to sum a list with 4 numbers.

number=[5,45,12,47]
sum=0
for i in number:
    sum+=i
print(f"The sum of the list elements are: {sum}")

print(sum(number))      # we can also get sum using sum function
