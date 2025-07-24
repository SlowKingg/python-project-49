from secrets import randbelow


def round_logic() -> tuple[str, str]:
    """Generates a question and its correct answer for the Even game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer.
    """

    number = randbelow(100) + 1
    right_answer = "yes" if number % 2 == 0 else "no"

    return f"Question: {number}", right_answer
