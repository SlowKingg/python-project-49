from brain_games.cli import (
    print_rules,
    welcome_user,
)
from brain_games.engine import start_even_game


def main() -> None:
    name = welcome_user()

    print_rules("even")

    start_even_game(name)


if __name__ == "__main__":
    main()
