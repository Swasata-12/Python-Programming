# Write a python program to implement star pattern using while loop.

i=1
while i<=5:
    print("*"*i)            # star pattern using while loop
    i=i+1
print("Done")

for j in range(11):         # star pattern using for loop
    print("*"*j)
for k in range(10,0,-1):    # reverse star pattern using for loop
    print("*"*k)

for k in range(5):          # star pattern using nested for loop
    star=""
    for l in range(k):
        star += "*"
    print(star)

for k in range(4,0,-1):     # reverse star pattern using nested for loop
    star=""
    for l in range(k):
        star += "*"
    print(star)