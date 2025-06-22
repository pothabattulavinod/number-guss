import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare guess to secret number
            if guess < secret_number:
                print("🔽 Too low! Try again.")
            elif guess > secret_number:
                print("🔼 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
