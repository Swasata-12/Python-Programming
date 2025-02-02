# Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks=[]
for i in range(6):
    stumarks=int(input(f"Enter the marks of {i+1} student: "))
    marks.append(stumarks)
marks.sort()
print(marks)

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))