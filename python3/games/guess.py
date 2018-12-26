import random


def play():
    print("*************************")
    print("Welcome to the guess game")
    print("*************************")

    secret_number = random.randrange(1, 101)
    points = 1000

    print("Choose the difficulty level:")
    print("(1) Easy \n(2) Medium \n(3) Hard")

    difficulty_level = int(input("Difficulty: "))
    if difficulty_level == 1:
        max_tries = 20
    elif difficulty_level == 2:
        max_tries = 10
    else:
        max_tries = 5

    for current_try in range(1, max_tries + 1):
        print("Current try: {} of {}".format(current_try, max_tries))
        guess_str = input("Input a number in the range of 1 to 100: ")

        guess = int(guess_str)
        if guess < 1 or guess > 100:
            print("You must input a number in the range of 1 to 100: ")
            continue

        print("You inputted number: ", guess)

        if secret_number == guess:
            print("You inputted the right number. Score: {}".format(points))
            break
        else:
            points_to_be_removed = abs(secret_number - guess)
            points = points - points_to_be_removed
            if guess > secret_number:
                print("You inputted a number greater than the secret one")
            else:
                print("You inputted a number lesser than the secret one")

    print("End of the game")


if __name__ == "__main__":
    play()
