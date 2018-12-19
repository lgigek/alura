import hangman
import guess

print("*************")
print("Choose a game")
print("*************")
print("(1) Hangman \n(2) Guess")

game = int(input("Which game: "))

if game == 1:
    hangman.play()
elif game == 2:
    guess.play()
