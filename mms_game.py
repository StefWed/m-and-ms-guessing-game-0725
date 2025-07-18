from src.score import score_player, log_score, get_leaderboard
from rich.prompt import Prompt
from src.game_core import play_game
from src.ui import console, show_result, display_leaderboard


if __name__ == "__main__":
    # 1) Play the game
    guesses, target, start_time, end_time, attempts, won = play_game()

    # 2) Score the player
    score = score_player(guesses, target, start_time, end_time)
    show_result(target, won, attempts, score)
    
    # 3) Log & show the leaderboard
    player_name = Prompt.ask("Enter your name for the leaderboard", default="Anonymous")
    log_score(player_name, score, attempts)

    console.print()  # blank line
    display_leaderboard(get_leaderboard(top_n=5))
