# Write a program to print multiplication table of a given number using for loop.

n=int(input("Enter the number: "))
print(f"The multiplication table of {n} is:")
for i in range(1,11):
    print(f"{n}x{i}={n*i}")

print(f"The multiplication table of {n} in reverse order is:")
for i in range(10,0,-1):
    print(f"{n}x{i}={n*i}")

# Another approach
for i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")