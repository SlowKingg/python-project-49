from secrets import randbelow

from brain_games.cli import (
    check_answer,
    congratulate_user,
    get_answer,
    print_rules,
    welcome_user,
)


def main() -> None:
    name = welcome_user()

    print_rules("even")

    for _ in range(3):
        question_number = randbelow(100) + 1
        right_answer = "yes" if question_number % 2 == 0 else "no"
        user_answer = get_answer(f"Question: {question_number}")

        if not check_answer(str(right_answer), user_answer, name):
            break
    else:
        congratulate_user(name)


if __name__ == "__main__":
    main()
