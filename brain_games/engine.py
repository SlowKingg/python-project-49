from brain_games.cli import (
    congratulate_user,
    get_answer,
    print_right_message,
    print_rules,
    print_wrong_message,
    welcome_user,
)


def is_valid_answer(
    right_answer: str, user_answer: str | None, name: str | None
) -> bool:
    """Check is answer for question is valid and prints message in console.

    Args:
        right_answer (str): Right answer for question.
        user_answer (str | None): User entered answer.
        name (str | None): Name of user

    Returns:
        bool: True if the user's answer is correct, false otherwise.
    """
    if right_answer == user_answer:
        print_right_message()
        return True
    else:
        print_wrong_message(user_answer, right_answer, name)
        return False


def run_game(game_logic):
    """Runs a game using the provided game logic function.

    Args:
        game_logic_module: A module that generates the question and correct
        answer for a single round.
        name (str | None): The name of the user playing the game.
    """

    name = welcome_user()

    print_rules(game_logic.__name__.split(".")[-1].split("_")[0])

    for _ in range(3):
        question, right_answer = game_logic.round_logic()
        user_answer = get_answer(question)

        if not is_valid_answer(str(right_answer), user_answer, name):
            break
    else:
        congratulate_user(name)
