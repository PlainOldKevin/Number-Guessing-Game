# Imports
import random
import art

# Return an answer function
def answer(guess, randNum):
    # Number is too high
    if guess > randNum:
        print(f"Too high.")
    # Number is too low
    elif guess < randNum:
        print(f"Too low.")
    # Correct answer
    elif guess == randNum:
        print(f"You got it! The answer was {randNum}.")
    # Invalid input
    else:
        print("Invalid input. Try again.")

# Difficulty selector function
def difficulty(ans):
    # Easy
    if ans == 'easy':
        return 10
    # Hard
    elif ans == 'hard':
        return 5
    # User messes up idk
    elif ans != 'easy' or 'hard':
        print("Invalid input. 'Easy' difficulty has been selected for you.")
        return 10


# Start game function
def play():
    # Print logo
    print(art.logo)

    # Generate random number
    randNum = random.randint(1, 100)

    # Prompt user
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficultyChoice = input("Choose a difficulty: Type 'easy' or 'hard': ")
    lives = difficulty(difficultyChoice)

    # Guessing portion while user has attempts remaining
    while lives > 0:
        # Inform user of attempts remaining 
        print(f"You have {lives} attempts remaining.\n")

        # User's guess to be compared
        guess = int(input("Make a guess: "))
        
        # Answer function from above
        answer(guess, randNum)

        # End game if correct answer
        if guess == randNum:
            break

        # Subtract lives
        lives -= 1

        # Prompt user
        if lives > 0:
            print("Guess again.\n")

    # User lost
    if lives == 0:
        print("You've run out of guesses. You lose.")

# Play game
play()
