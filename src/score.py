import time
import json
import os


def score_player(guesses, target, start_time, end_time):
    """
    Calculate a score for the player based on guess accuracy and speed.

    Parameters:
    - guesses: list of ints, the sequence of guesses made by the player.
    - target: int, the correct number of M&Ms.
    - start_time: float, timestamp when the game started.
    - end_time: float, timestamp when the correct guess was made.

    Returns:
    - score: float, higher is better. Combines closeness and speed.
    """
    if end_time < start_time:
        raise ValueError("end_time must be greater than or equal to start_time")

    duration = end_time - start_time
    max_range = 200 - 1
    accuracy_sum = sum(max(0, max_range - abs(g - target)) for g in guesses)
    accuracy_score = accuracy_sum / len(guesses) if guesses else 0
    speed_score = 1 / (1 + duration)
    score = 0.7 * accuracy_score + 0.3 * speed_score * max_range
    return score


def log_score(player_name, score, attempts, filename='leaderboard.json'):
    """
    Append a player's score and attempts to the leaderboard file.

    Parameters:
    - player_name: str, the name/ID of the player.
    - score: float, the player's score.
    - attempts: int, number of attempts the player used.
    - filename: str, path to JSON leaderboard file.

    If the file doesn't exist, create it. Entries are stored as a list of records:
      [{"player": ..., "score": ..., "attempts": ..., "timestamp": ...}, ...]
    """
    entry = {
        "player": player_name,
        "score": score,
        "attempts": attempts,
        "timestamp": time.time()
    }
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def get_leaderboard(filename='leaderboard.json', top_n=5):
    """
    Retrieve the top N scores from the leaderboard, sorted descending.

    Returns:
    - List of dicts: [{"player": ..., "score": ..., "attempts": ..., "timestamp": ...}, ...]
    """
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data.sort(key=lambda rec: rec['score'], reverse=True)
    return data[:top_n]


def _test_score_and_logging(tmp_path):
    # Test scoring
    fast = score_player([42], 42, start_time=0, end_time=0.5)
    slow = score_player([42], 42, start_time=0, end_time=5)
    assert fast > slow, "Faster guess should score higher"

    # Test logging with attempts
    lb_file = tmp_path / 'lb.json'
    log_score('Alice', 100.0, attempts=2, filename=str(lb_file))
    log_score('Bob', 150.0, attempts=4, filename=str(lb_file))
    lb = get_leaderboard(filename=str(lb_file), top_n=2)
    assert lb[0]['player'] == 'Bob' and lb[0]['attempts'] == 4, "Leaderboard highest score incorrect or missing attempts"
    assert lb[1]['player'] == 'Alice' and lb[1]['attempts'] == 2, "Leaderboard order incorrect or missing attempts"

    print("All tests passed.")


if __name__ == "__main__":
    _test_score_and_logging(__import__('pathlib').Path('.'))

    # Example usage
    import time
    start = time.time()
    guesses = [50, 30, 45, 42]
    end = time.time()
    s = score_player(guesses, 42, start, end)
    print(f"Your score: {s}")
    log_score('Player1', s, attempts=4)
    print(get_leaderboard(top_n=5))
