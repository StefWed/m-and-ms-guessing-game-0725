import time

def score_player(attempts, target, start_time, end_time):
    """
    Calculate a score for the player based on guess accuracy and speed.

    Parameters:
    - guesses: list of ints, the sequence of guesses made by the player.
    - target: int, the correct number of M&Ms.
    - start_time: float, the timestamp when the game started (time.time()).
    - end_time: float, the timestamp when the correct guess was made (time.time()).

    Returns:
    - score: float, higher is better. Combines closeness and speed.
    """
    # Total time taken in seconds
    duration = end_time - start_time

    # Accuracy component: sum of closeness of each guess (higher is better)
    # For each guess, closeness = max_range - abs(guess - target)
    max_range = 200 - 1  # assuming game range is 1 to 200
    accuracy_sum = sum(max(0, max_range - abs(g - target)) for g in attempts)
    accuracy_score = accuracy_sum / len(attempts)

    # Speed component: faster guesses yield higher score
    # We use an exponential decay: speed_score = 1 / (1 + duration)
    speed_score = 1 / (1 + duration)

    # Combine components: weight accuracy more than speed
    score = 0.7 * accuracy_score + 0.3 * speed_score * max_range
    return score

#----------------------------------------------------
# Example usage:
#----------------------------------------------------
# start = time.time()
# guesses = [50, 30, 45, 42]
# end = time.time()
# print(score_player(guesses, 42, start, end))

#----------------------------------------------------
def log_score(player_name, score, attempts, filename='leaderboard.json'):
    """
    Append a player's score to the leaderboard file.

    Parameters:
    - player_name: str, the name/ID of the player.
    - score: float, the player's score.
    - filename: str, path to JSON leaderboard file.

    If the file doesn't exist, create it. Entries are stored as a list of records:
      [{"player": ..., "score": ..., "timestamp": ...}, ...]
    """
    entry = {
        "player": player_name,
        "score": score,
        "tries": attempts,
        "timestamp": time.time()
    }
    # Load existing leaderboard
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    # Save updated leaderboard
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
#----------------------------------------------------

def get_leaderboard(filename='leaderboard.json', top_n=3):
    """
    Retrieve the top N scores from the leaderboard, sorted descending.

    Returns:
    - List of dicts: [{"player": ..., "score": ..., "tries": ..., "timestamp": ...}, ...]
    """
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Sort by score descending
    data.sort(key=lambda rec: rec['score'], reverse=True)
    return data[:top_n]
#----------------------------------------------------