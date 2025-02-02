# age=int(input("Age: "))
# print(age)
try:
    age=int(input("Age: "))         # try this code if fails then executes except block
    print(age)
except Exception as e:
    print(e)
else:                           # else block executes only when try executes successfully
    print("Thank You")
# except ValueError:
#     print("Invalid Error")