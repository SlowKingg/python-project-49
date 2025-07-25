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


def get_answer(question: str) -> str | None:
    """Gets answer from user to a question.

    Args:
        question (str): Asked question.

    Returns:
        str | None: Answer.
    """

    print("Question: " + question)

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
