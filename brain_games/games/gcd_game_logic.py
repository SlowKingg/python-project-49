from secrets import randbelow


def gcd_euclidean(a, b):
    """Calculates the greatest common divisor (GCD) of two integers.

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


def round_logic() -> tuple[str, str]:
    """Generates a question and its correct answer for a GCD game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer.
    """

    first_number = randbelow(100) + 1
    second_number = randbelow(100) + 1
    right_answer = str(gcd_euclidean(first_number, second_number))

    return f"Question: {first_number} {second_number}", right_answer
