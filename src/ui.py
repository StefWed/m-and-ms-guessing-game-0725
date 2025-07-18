from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.table import Table
from rich.text import Text
from rich import box
import logging

console = Console()
logger = logging.getLogger(__name__)

def welcome_message(max_attempts: int):
    console.print(
            Panel.fit(
                "\n".join([
                    "[bold yellow]Welcome to our M&Ms Guessing Challenge![/bold yellow]",
                    "",
                    "Step up to the counter and take a shot at guessing how many ",
                    "normal‑sized M&Ms are tucked inside the jar. It holds somewhere ",
                    "between [bold cyan]100[/bold cyan] and [bold cyan]200[/bold cyan] pieces.",
                    "",
                    f"You have [bold magenta]{max_attempts}[/bold magenta] attempts,",
                    "nail the exact count and enjoy a complimentary coffee ☕ ",
                    "and a slice of cake 🍰 on us!",
                ]),
                title="[bold green]🍬 Coffee Shop Giveaway 🍬[/bold green]",
                border_style="bright_blue",
                box=box.ROUNDED,
            )
    )

def prompt_guess(attempt: int, total: int) -> int:
    prompt_text = Text.assemble(
        ("Attempt ", "white"),
        (f"{attempt}", "bold cyan"),
        (f"/{total}", "white"),
        (" - Enter your guess:", "green"),
    )
    return IntPrompt.ask(prompt_text)

def feedback(guess: int, target: int, remaining: int):
    if guess < target:
        msg = Text(f"You guessed {guess}. Too low!", style="bold red")
    elif guess > target:
        msg = Text(f"You guessed {guess}. Too high!", style="bold red")
    else:
        msg = Text(f"🎉 {guess} is correct! 🎉", style="bold green")
    console.print(msg)
    if guess != target:
        console.print(f"You have [bold magenta]{remaining}[/bold magenta] guesses left.\n")

def show_result(target: int, won: bool, attempts: int, score: float):
    """Display end‐of‐game result, taking (target, won, attempts, score)."""
    if won:
        panel = Panel(
            Text.from_markup(
                f"[bold green]Congratulations![/bold green]\n"
                f"You guessed [cyan]{target}[/cyan] in [bold]{attempts}[/bold] "
                f"{'try' if attempts == 1 else 'tries'}!\n"
                f"Your score: [bold yellow]{score:.2f}[/bold yellow]"
            ),
            title="Result",
            border_style="green",
            box=box.ROUNDED,
        )
    else:
        panel = Panel(
            Text.from_markup(
                f"[bold red]Game over![/bold red]\n"
                f"Sorry, you've used all your attempts.\n"
                f"The correct number was [cyan]{target}[/cyan].\n"
                f"[italic]Better luck next time! Thanks for playing.[/italic]"
            ),
            title="Result",
            border_style="red",
            box=box.ROUNDED,
        )
    console.print(panel)

def display_leaderboard(entries: list[dict]):
    """
    Display the top-n leaderboard. Expects each entry to have at least:
      - 'score'
      - 'attempts'
      - 'timestamp'
    and one of:
      - 'name'
      - 'player'
      - 'player_name'
    """
    table = Table(title="Leaderboard (Top 5)", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Name", style="bold")
    table.add_column("Score", justify="right", style="yellow")
    table.add_column("Attempts", justify="center", style="cyan")
    table.add_column("Timestamp", style="dim")

    for entry in entries:
        # look for a name in several possible keys
        name = (
            entry.get("name")
            or entry.get("player")
            or entry.get("player_name")
            or entry.get("username")
        )
        if name is None:
            name = "Unknown"
            logger.warning(
                "Leaderboard entry missing name field, keys are: %s", list(entry.keys())
            )

        score = entry.get("score", 0.0)
        attempts = entry.get("attempts", entry.get("tries", 0))
        timestamp = entry.get("timestamp", "—")

        table.add_row(
            str(name),
            f"{score:.2f}",
            str(attempts),
            str(timestamp),
        )

    console.print(table)
