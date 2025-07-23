from secrets import randbelow

from brain_games.cli import (
    congratulate_user,
    get_answer,
    print_right_message,
    print_rules,
    print_wrong_message,
    welcome_user,
)


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


def main() -> None:
    name = welcome_user()

    print_rules("gcd")

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


if __name__ == "__main__":
    main()
