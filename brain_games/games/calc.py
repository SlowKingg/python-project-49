from secrets import choice, randbelow

RULES = "What is the result of the expression?"
OPERATIONS = ["+", "-", "*"]


def round_logic() -> tuple[str, int]:
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
            return "", 0

    return f"{first_number} {operation} {second_number}", right_answer
