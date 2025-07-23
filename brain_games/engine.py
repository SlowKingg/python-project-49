from secrets import choice, randbelow

from brain_games.cli import (
    congratulate_user,
    get_answer,
    print_right_message,
    print_wrong_message,
)

OPERATIONS = ["+", "-", "*"]


def gcd_euclidean(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers.

    Utilizes the Euclidean algorithm, which is an efficient method
    for finding the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def start_even_game(name: str | None):
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


def start_calc_game(name: str | None):
    for _ in range(3):
        operation = choice(OPERATIONS)
        match operation:
            case "+":
                first_number = randbelow(100) + 1
                second_number = randbelow(100) + 1
                right_answer = str(first_number + second_number)
            case "-":
                first_number = randbelow(100) + 1
                second_number = randbelow(first_number) + 1
                right_answer = str(first_number - second_number)
            case "*":
                first_number = randbelow(25) + 1
                second_number = randbelow(10) + 1
                right_answer = str(first_number * second_number)
            case _:
                break

        user_answer = get_answer(
            f"Question: {first_number} {operation} {second_number}"
        )

        if right_answer == user_answer:
            print_right_message()
        else:
            print_wrong_message(user_answer, right_answer, name)
            break
    else:
        congratulate_user(name)


def start_gcd_game(name: str | None):
    for _ in range(3):
        first_number = randbelow(100) + 1
        second_number = randbelow(100) + 1
        right_answer = str(gcd_euclidean(first_number, second_number))
        user_answer = get_answer(f"{first_number} {second_number}")

        if right_answer == user_answer:
            print_right_message()
        else:
            print_wrong_message(user_answer, right_answer, name)
            break
    else:
        congratulate_user(name)
