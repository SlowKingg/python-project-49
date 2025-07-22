from secrets import randbelow

from brain_games.cli import get_answer, welcome_user


def main() -> None:
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        question_number = randbelow(100) + 1
        print(f"Question: {question_number}")
        right_answer = "yes" if question_number % 2 == 0 else "no"
        user_answer = get_answer()

        if right_answer == user_answer:
            print("Correct!")
        else:
            print(
                (
                    f"'{user_answer}' is wrong answer ;(.\n"
                    f"Correct answer was '{right_answer}'.\n"
                    f"Let's try again, {name}!"
                )
            )
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
