from secrets import choice, randbelow

from brain_games.cli import get_answer, welcome_user

OPERATIONS = ["+", "-", "*"]


def main() -> None:
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print("What is the result of the expression?")

    for _ in range(3):
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
                break

        print(f"Question: {first_number} {operation} {second_number}")

        user_answer = get_answer()

        if str(right_answer) == user_answer:
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
