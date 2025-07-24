from secrets import choice, randbelow

OPERATIONS = ["+", "-", "*"]


def round_logic() -> tuple[str, str]:
    """Generates a question and its correct answer for a Calculation game.

    Returns:
        tuple[str, str]: A tuple containing the question string
        and the correct answer.
    """

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
            return "", ""

    return f"Question: {first_number} {operation} {second_number}", right_answer
