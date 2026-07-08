import random

def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    print("Guess a number between 1 and 100")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break

def main():
    number_guessing_game()

main()
