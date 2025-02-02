# Write a python program to print fibonacci series using recursion.


def fibonacciSeries(i):
    if(i<=1):
        return i
    else:
        return (fibonacciSeries(i-1)+fibonacciSeries(i-2))

n=int(input("Enter index: "))
for i in range(n+1):
    print(fibonacciSeries(i),end=" ")