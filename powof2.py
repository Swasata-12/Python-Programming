# Display the powers of 2 using anonymous function

value = lambda x:2**x
terms=int(input("Enter terms: "))
result=list(map(value,range(terms)))
for i in range(terms):
    print(f"2 raised to power {i} is {result[i]}")