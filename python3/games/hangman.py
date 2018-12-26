import random


def play():
    print_init_message()
    secret_word = create_secret_word()
    guessed_right_letters = create_guessed_right_letters(secret_word)

    print(guessed_right_letters)

    is_hanged = False
    is_correct = False
    current_errors = 0
    max_errors = 6

    while not is_hanged and not is_correct:

        guess = input_guess()

        if guess in secret_word:
            mark_right_guesses(guess, guessed_right_letters, secret_word)
        else:
            current_errors += 1

        print(guessed_right_letters)
        is_hanged = current_errors == max_errors
        is_correct = "_" not in guessed_right_letters

    print_final_message(is_correct)


def print_init_message():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")


def create_secret_word():
    words = []

    with open("words.txt", "r") as file:
        for line in file:
            words.append(line.strip().upper())

    return words[random.randrange(0, len(words))]


def create_guessed_right_letters(secret_word):
    return ["_" for letter in secret_word]


def input_guess():
    guess = input("Input a letter: ")
    return guess.strip().upper()


def mark_right_guesses(guess, guessed_right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            guessed_right_letters[index] = letter
        index += 1


def print_final_message(is_correct):
    if is_correct:
        print("You win!")
    else:
        print("You lose!")
    print("End of the game")


if __name__ == "__main__":
    play()
