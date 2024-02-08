import random

def GuessTheNumber():
    random_number = random.randint(1, 20)
    print("Hello! What is your name?")
    username = str(input())
    print("Well, " + username + ", I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        usernum = int(input())
        attempts += 1
        if(usernum < random_number):
            print("Your guess is too low. \nTake a guess.")
        elif(usernum > random_number):
            print("Your guess is too high. \nTake a guess.")
        else:
            print(f"Good job, {username}! You guessed my number in {attempts} guesses!")
            break

GuessTheNumber()
'''
Hello! What is your name?
Altynay
Well, Altynay, I am thinking of a number between 1 and 20.
3
Your guess is too low. 
Take a guess.
7
Your guess is too low. 
Take a guess.
8
Your guess is too low. 
Take a guess.
9
Your guess is too low. 
Take a guess.
15
Your guess is too high. 
Take a guess.
10
Good job, Altynay! You guessed my number in 6 guesses!
'''