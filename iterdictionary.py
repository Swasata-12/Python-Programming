# Python Program to Iterate Over Dictionaries Using for Loop

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for key,value in dt.items():
    print(f"{key} {value}")

# Another approach
for key in dt.keys():
    print(f"{key} {dt[key]}")



# Python Program to Check If a List is Empty
my_list=[]
if (len(my_list)==0):
    print("List is Empty")
else:
    print("List is not empty")