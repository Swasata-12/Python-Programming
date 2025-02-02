# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s=set()
for i in range(8):
    n=int(input(f"Enter {i+1} number: "))
    s.add(n)
print(s)

e=set()              # it is an empty set
e.add(18)
e.add("18")
print(e)             # a set can contain different types of data

v = set()
v.add(20)
v.add(20.0)
v.add('20')
print(len(v))         # it returns 2 cause python comparison operator compare the values irespective of types