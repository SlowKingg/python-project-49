import prompt


def welcome_user() -> None:
    """Gets user name and welcomes him."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
