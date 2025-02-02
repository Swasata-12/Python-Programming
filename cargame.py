# Write a python code to implemment a car game using while loop.

flag_start=""
flag_stop=""    
while True:
    command=input("> ").lower()
    if command=="start":
        if flag_start==1:
            print("Car is already in motion")
        else:
            print("Car started...")
            flag_start=1                        # we can also use boolean value here
    elif command=="stop":
        if flag_stop==1:
            print("Car had already stopped")
        else:
            print("Car stopped")
            flag_stop=1
    elif command=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understannd that!")