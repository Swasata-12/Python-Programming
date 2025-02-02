# Python Program to Measure the Elapsed Time in Python
import time

start=time.time()
for i in range(1,11):
    print(i)
end=time.time()
print(f"Time Taken: {end-start}")