from secrets import randbelow

from brain_games.cli import (
    congratulate_user,
    get_answer,
    print_right_message,
    print_rules,
    print_wrong_message,
    welcome_user,
)


def main() -> None:
    name = welcome_user()

    print_rules("even")

    for _ in range(3):
        number = randbelow(100) + 1
        right_answer = "yes" if number % 2 == 0 else "no"
        user_answer = get_answer(f"Question: {number}")

        if str(right_answer) == user_answer:
            print_right_message()
        else:
            print_wrong_message(user_answer, right_answer, name)
            break
    else:
        congratulate_user(name)


if __name__ == "__main__":
    main()
