import prompt


def get_answer() -> str | None:
    """Gets answer from user.

    Returns:
        str | None: Answer.
    """

    return prompt.string("Your answer: ")


def welcome_user() -> str | None:
    """Gets user name and welcomes him.

    Returns:
        str | None: Name of user.
    """

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
