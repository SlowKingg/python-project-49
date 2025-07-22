from secrets import choice, randbelow

from brain_games.cli import (
    check_answer,
    congratulate_user,
    get_answer,
    print_rules,
    welcome_user,
)

OPERATIONS = ["+", "-", "*"]


def main() -> None:
    name = welcome_user()

    print_rules("calc")

    for _ in range(3):
        operation = choice(OPERATIONS)
        match operation:
            case "+":
                first_number = randbelow(100) + 1
                second_number = randbelow(100) + 1
                right_answer = first_number + second_number
            case "-":
                first_number = randbelow(100) + 1
                second_number = randbelow(first_number) + 1
                right_answer = first_number - second_number
            case "*":
                first_number = randbelow(25) + 1
                second_number = randbelow(10) + 1
                right_answer = first_number * second_number
            case _:
                break

        user_answer = get_answer(
            f"Question: {first_number} {operation} {second_number}"
        )

        if not check_answer(str(right_answer), user_answer, name):
            break
    else:
        congratulate_user(name)


if __name__ == "__main__":
    main()
