#Guessing Game
from random import *
import sys

words = {
    1: "peng",
    2: "wagwan",
    3: "pifting",
    4: "benjamin",
    5: "gamer",
    6: "toll",
    7: "tune",
    8: "meal",
    9: "christmas",
    10: "rock",
    11: "custard",
}
secret_word = words.get(randint(1,11))
guess = ""
guesses = 0
guess_guesses = ""
guess_guessses = ""
guess_limit = int(input("How many guesses? "))
out_of_guesses = False
if guess_limit == 0:
    print("invalid limit")
    sys.exit()
elif guess_limit == 1:
    guess_guessses = "guess"
elif guess_limit >= 2:
    guess_guessses = "guesses"
print("")
print("You have,", guess_limit, guess_guessses,"to guess the word!")

while guess != secret_word:
    guess = input("Enter Guess: ")
    guesses += 1
    if guess == "debug":
        print(secret_word)
    if guesses == guess_limit and guess != secret_word:
        out_of_guesses = True
        break

if guesses == 1:
    guess_guesses = "guess"
elif guesses >= 2:
    guess_guesses = "guesses"
if out_of_guesses == False:
    print("You Guessed the correct word!", "It  was,", secret_word)
    print("You did it in,", guesses, guess_guesses)
elif out_of_guesses == True:
    print("You did not guess the word, it was", "'",secret_word,"'")
