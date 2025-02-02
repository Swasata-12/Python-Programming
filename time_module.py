# Create a python program capable of greeting you with Good morning,Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour.

import time 
t=time.strftime("%H:%M:%S")
print(t)
hour=int(time.strftime("%H"))
print(f"It's {hour} O'Clock now!")
if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")

# time.sleep() function 
print(4)
time.sleep(3)
print("This is printed after 3 seconds")

# time.time() function 
p=time.time()   # print the current time
print(p)