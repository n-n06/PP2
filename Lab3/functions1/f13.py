from random import randint
# Hello! What is your name?
# KBTU

# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12

# Your guess is too low.
# Take a guess.
# 16

# Your guess is too low.
# Take a guess.
# 19

# Good job, KBTU! You guessed my number in 3 guesses!
def guess_game():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess.", end = "\n")
    ans = randint(1,20)
    guess = int(input())
    num_guess = 1
    
    while guess != ans:
        if guess > ans:
            print("\nYour guess is too big.\nTake a guess.", end = "\n")
        elif guess < ans:
            print("\nYour guess is too low.\nTake a guess.", end = "\n")
        guess = int(input())
        num_guess += 1
    else:
        if num_guess == 1:
            print(f"\nGood job, {name}! You guessed my number in 1 guess!")
        else:
            print(f"\nGood job, {name}! You guessed my number in {num_guess} guesses!")


