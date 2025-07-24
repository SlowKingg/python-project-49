from secrets import choice, randbelow


def round_logic() -> tuple[str, int]:
    """Generates a question and its correct answer for a Progression game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer as a string.
    """

    start = randbelow(25) + 1
    step = randbelow(10) + 1
    progression = [start + x * step for x in range(1, 11)]
    right_answer = choice(progression)

    return " ".join(map(str, progression)).replace(
        f"{right_answer}", ".."
    ), right_answer
