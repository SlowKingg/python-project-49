from brain_games.cli import (
    print_rules,
    welcome_user,
)
from brain_games.engine import start_calc_game


def main() -> None:
    name = welcome_user()

    print_rules("calc")

    start_calc_game(name)


if __name__ == "__main__":
    main()
