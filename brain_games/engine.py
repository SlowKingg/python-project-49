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


def is_valid_answer(
    right_answer: str, user_answer: str | None, name: str | None
) -> bool:
    """Check is answer for question is valid.

    Args:
        right_answer (str): Right answer for question.
        user_answer (str | None): User entered answer.
        name (str | None): Name of user

    Returns:
        bool: True if the user's answer is correct, false otherwise.
    """
    if right_answer == user_answer:
        print_right_message()
        return True
    else:
        print_wrong_message(user_answer, right_answer, name)
        return False


def start_even_game(name: str | None):
    """Starts even game.

    Args:
        name (str | None): Name of user.
    """
    for _ in range(3):
        number = randbelow(100) + 1
        right_answer = "yes" if number % 2 == 0 else "no"
        user_answer = get_answer(f"Question: {number}")

        if not is_valid_answer(right_answer, user_answer, name):
            break
    else:
        congratulate_user(name)


def start_calc_game(name: str | None):
    """Starts calculation game.

    Args:
        name (str | None): Name of user.
    """
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

        if not is_valid_answer(right_answer, user_answer, name):
            break
    else:
        congratulate_user(name)


def start_gcd_game(name: str | None):
    """Starts game of GCD.

    Args:
        name (str | None): Name of user.
    """
    for _ in range(3):
        first_number = randbelow(100) + 1
        second_number = randbelow(100) + 1
        right_answer = str(gcd_euclidean(first_number, second_number))
        user_answer = get_answer(f"{first_number} {second_number}")

        if not is_valid_answer(right_answer, user_answer, name):
            break
    else:
        congratulate_user(name)
