from brain_games.cli import (
    print_rules,
    welcome_user,
)
from brain_games.engine import start_gcd_game


def main() -> None:
    name = welcome_user()

    print_rules("gcd")

    start_gcd_game(name)


if __name__ == "__main__":
    main()
