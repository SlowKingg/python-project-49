from secrets import randbelow


def is_prime(number: int) -> bool:
    """Checks if a number is prime using a straightforward brute-force approach.

    Args:
        number (int): The integer to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def round_logic() -> tuple[str, str]:
    """Generates a question and its correct answer for a Prime game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer as a string.
    """

    number = randbelow(100) + 1
    right_answer = "yes" if is_prime(number) else "no"
    return f"{number}", right_answer
