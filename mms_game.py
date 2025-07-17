import time
import random
from score import score_player, log_score, get_leaderboard

def generate_random_number(min_val=100, max_val=200):
    """
    Generate a random number between min_val and max_val inclusive.
    """
    random_number = random.randint(min_val, max_val)
    print(f"[DEBUG] Generated number: {random_number}")
    return random_number


def play_game(max_attempts=5):
    """
    Runs the guessing game and returns:
      - guesses (list[int])
      - target (int)
      - start_time (float)
      - end_time (float)
      - attempts (int)
    """
    target = generate_random_number()
    guesses = []
    attempts = 0

    print("Welcome to the M&Ms Guessing Game!")
    print(f"You have {max_attempts} guesses to find out how many M&Ms are in the jar.")

    start_time = time.time()
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        guesses.append(guess)
        attempts += 1
        remaining = max_attempts - attempts
        print(f"You guessed {guess}.", end=' ')

        if guess < target:
            print("Too low!", end=' ')
        elif guess > target:
            print("Too high!", end=' ')
        else:
            print(f"You got it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            break

        if remaining > 0:
            print(f"You have {remaining} {'guess' if remaining == 1 else 'guesses'} left.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {target}.")

    end_time = time.time()
    return guesses, target, start_time, end_time, attempts


if __name__ == "__main__":
    # Play game
    guesses, target, start_time, end_time, attempts = play_game()

    # Score the player
    score = score_player(guesses, target, start_time, end_time)
    print(f"Your score: {score:.2f}")

    # Log the score (including attempts)
    player_name = input("Enter your name for the leaderboard: ")
    log_score(player_name, score, attempts)

    # Display top 5 leaderboard
    print("\nLeaderboard (Top 5):")
    for rec in get_leaderboard(top_n=5):
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(rec['timestamp']))
        attempts_info = rec.get('attempts', 'N/A')
        print(f"{rec['player']} - {rec['score']:.2f} (Attempts: {attempts_info}) [{ts}]")
