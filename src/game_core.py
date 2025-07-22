import random
import time

from src.ui import  console, welcome_message, prompt_guess, feedback

def generate_random_number(min_val=100, max_val=200):
    """
    Generate a random number between min_val and max_val inclusive.
    """
    random_number = random.randint(min_val, max_val)
    print(f"[DEBUG] Generated number: {random_number}")
    return random_number

def play_game(max_attempts: int = 5):
    """
    Runs the guessing game and returns:
      - guesses (list[int])
      - target (int)
      - start_time (float)
      - end_time (float)
      - attempts (int)
    """

    target = generate_random_number()
    guesses: list[int] = []
    attempts = 0

    welcome_message(max_attempts)
    start_time = time.time()

    while attempts < max_attempts:
        guess = prompt_guess(attempts + 1, max_attempts)

        guesses.append(guess)
        attempts += 1
        remaining = max_attempts - attempts

        feedback(guess, target, remaining)
        if guess == target:
            won = True
            break
    else:
        won = False

    end_time = time.time()
    return guesses, target, start_time, end_time, attempts, won