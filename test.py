import random

def guess_the_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    
    print("Welcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 20. Can you guess it?")
    
    attempts = 0
    while True:
        # Get user's guess
        guess = int(input("Enter your guess (between 1 and 20): "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

# Call the function to play the game
guess_the_number()