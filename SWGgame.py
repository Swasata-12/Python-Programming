# We all have played snake, water, gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user
import random
computer=random.choice([1,-1,0])
youstr=input("Enter your choice: ")
youDict={
    "s":1,
    "w":-1,
    "g":0
}
reverseDict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}
you = youDict[youstr]
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
    print("Its a Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Lose")
    else:
        print("Something went wrong")