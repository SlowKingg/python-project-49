import prompt


def welcome_user() -> str | None:
    """Gets user name and welcomes him.

    Returns:
        str | None: Name of user.
    """

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_rules(game: str):
    """Prints rules of games.

    Args:
        game (str): Name of game.
    """
    match game:
        case "even":
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case "calc":
            print("What is the result of the expression?")
        case "gcd":
            print("Find the greatest common divisor of given numbers.")


def get_answer(question: str) -> str | None:
    """Gets answer from user to a question.

    Args:
        question (str): Asked question.

    Returns:
        str | None: Answer.
    """

    print(question)

    return prompt.string("Your answer: ")


def print_right_message():
    """Print message for right answer."""
    print("Correct!")


def print_wrong_message(
    user_answer: str | None, right_answer: str, name: str | None
):
    """Print message for wrong answer.

    Args:
        user_answer (str | None): User answer.
        right_answer (str): Right answer.
        name (str | None): User name.
    """
    print(
        (
            f"'{user_answer}' is wrong answer ;(.\n"
            f"Correct answer was '{right_answer}'.\n"
            f"Let's try again, {name}!"
        )
    )


def congratulate_user(name: str | None):
    print(f"Congratulations, {name}!")
