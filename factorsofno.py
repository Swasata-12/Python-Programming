# Python Program to find the factors of a number

def factors(n):
    print(f"The factors of {n} are: ")
    for i in range(1,n+1):
        if(n%i==0):
            print(i)


n=int(input("Enter a number: "))
factors(n)