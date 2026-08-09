import random


def play_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = input("Please enter your guess (between 1 and 100): ")

        # Validate input
        if not user_guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
            )


play_game()
