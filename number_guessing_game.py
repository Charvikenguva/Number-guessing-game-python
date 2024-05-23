#number guessing game
#guess any number between 1-100(inclusive)

import random
num=random.randint(1,100)
guess=0
name=input("Enter your name: ")
print(f"Welcome {name}. Lets start the game!")
while guess!=num:
    guess=int(input("Guess the number: "))
    if guess < num:
        print("Guess Higher!!")
    elif guess > num:
        print("Guess Lower!!")
    else:
        print("Congratulations! You Won the game.")


