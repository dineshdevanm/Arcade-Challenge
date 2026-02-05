import random


def check_guess(secret: int, guess: int) -> str:
    """
    Compare secret and guess.

    :param secret: the actual number to guess
    :param guess: the user's guess
    """
    return "word"


def calculate_score(attempts: int) -> int:
    """
    Score calculation based on attempts.

    :param attempts: Number of attempts made by the user
    """

    return "score"


def give_hint(secret: int, guess_history: list) -> str:
    """
    Provide a hint based on the secret number and the history of guesses.

    :param secret: the actual number to guess
    :param guess_history: list of previous guesses
    """

    return "hint"

    # -------- CLI PART (DO NOT MODIFY) ---------


def play():
    secret = random.randint(1, 100)
    attempts = 0
    history = []

    print("Welcome to Smart Number Guessing Game!")

    while True:
        guess = int(input("Enter guess: "))
        attempts += 1
        history.append(guess)

        result = check_guess(secret, guess)

        if result == "CORRECT":
            print("Correct!")
            print("Score:", calculate_score(attempts))
            break

        print(result)
        print("Hint:", give_hint(secret, history))


if __name__ == "__main__":
    play()
