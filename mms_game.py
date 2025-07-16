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
    print("Welcome to the M&Ms Guessing Game!")
    random_number = generate_random_number()
    print("You guessed 50.")               # Hardcoded guess
    print("Sorry, that's too high!")       # Hardcoded feedback


if __name__ == "__main__":
    start_game()


