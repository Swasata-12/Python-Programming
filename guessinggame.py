# Write a  python code to implement a number guessing game using while loop.

secret_number=9
i=0
while i<3:
    guess=int(input("Guess: "))
    i += 1
    if guess==secret_number:
        print("You Win!")
        break
else:
    print("Sorry, You failed!")