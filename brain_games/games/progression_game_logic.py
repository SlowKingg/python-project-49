from secrets import choice, randbelow


def round_logic() -> tuple[str, str]:
    """Generates a question and its correct answer for a Progression game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer as a string.
    """

    start = randbelow(25) + 1
    step = randbelow(10) + 1
    progression = [start + x * step for x in range(1, 11)]
    right_answer = str(choice(progression))

    return "Question: " + " ".join(map(str, progression)).replace(
        f"{right_answer}", ".."
    ), right_answer
