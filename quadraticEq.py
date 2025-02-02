# Python Program to Solve Quadratic Equation

import cmath
print("""
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0""")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=(b**2)-(4*a*c)
sol1=(b+cmath.sqrt(d))/(2*a)
sol2=(b-cmath.sqrt(d))/(2*a)
print(f"The solutions are {sol1} and {sol2}")