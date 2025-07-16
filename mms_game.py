import random


def generate_random_number(min_val=100, max_val=200):
    """
    Generate a random number between 100 and 200.

    Function uses random.randint to generate the number.
    Number returned directly
    """
    random_number = random.randint(min_val, max_val)
    print(f"[DEBUG] Generated number: {random_number}")

    return random_number



def start_game():

    max_attempts = 5
    attempts= 0

    print("Welcome to the M&Ms Guessing Game!")
    target = generate_random_number()
    print(f"You have {max_attempts} guesses to find out how many M&Ms are in the jar.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1
        remaining = max_attempts - attempts
        print(f"You guessed {guess}.", end=' ')

        if guess < target:
            print("Too low!", end=' ')
        elif guess > target:
            print("Too high!", end=' ')
        else:
            print(f"You got it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            return

        if remaining > 0:
            print(f"You have {remaining} {'guess' if remaining == 1 else 'guesses'} left.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {target}.")



if __name__ == "__main__":
    start_game()