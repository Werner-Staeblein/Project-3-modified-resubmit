import sys
import time
import random
import os
import hangman_stages
from opening import opening_image, instructions
from colorama import Fore
import capitalcities
from hangman_stages import get_hangman_stage


def typewriter(textentered):
    """
    Creates typewriter effect for text displayed.
    """
    for letter in textentered:
        if letter == '\n':
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
        time.sleep(0.04)
    print()


def select_word():
    """"
    Step 1: selects a random city from the list in capitalcities
    """
    return random.choice(capitalcities.capital_cities)
    print("Selected city:", selected_city)
    return selected_city


def get_unique_letters(word):
    """
    Step 2: Convert the secret word into a set to remove duplicates.
    """
    return "".join(set(word))


def is_guess_in_secret_word(guess, secret_city):
    """
    Step 3: Check if the guessed letter is in the secret city.
    """
    guess = guess.upper()
    secret_city = secret_city.upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Only single letters are allowed")
        return False
    elif guess.upper() in secret_city:
        return True
    else:
        return False


def print_secret_word(secret_city, guessed_letters):
    """
    Step 4: Show guessed letters and leave underscore for letters\
    not guessed and misssing
    """
    for letter in secret_city:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")


def screen_clearance():
    typewriter("Press 'c' and then Enter to clear the screen")
    clear = input().lower()
    if clear == 'c':
        os.system("cls" if os.name == "nt" else "clear")
        secret_word = ""
    else:
        print("Screen will not be cleared.")


def ask_yes_no_question(prompt):
    """
    Step 6: Ask the user a yes/no question and return True\
    for 'yes' and False for 'no' to (not) play game again.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in {'yes', 'ye', 'y'}:
            return True
        elif response in {'no', 'n'}:
            return False
        else:
            print("Please enter either 'yes' or 'no'.")


def start_game(secret_city, username):
    """
    Step 1 for start of game as per functions above: Start the hangman game.
    Input validation for length of input (no more than one character) and input
    validation for the input to be alpha, i.e. a character. The "try" block
    includes user input validation. The "except" is executed when user makes
    invalid input (such as two characters/numbers).
    """
    while True:
        secret_city = select_word()
        remaining_attempts = 6
        guessed_letters = set()
        unique_secret_letters = set(secret_city)

        while remaining_attempts > 0:
            try:
                guess = input("Guess a letter of the secret city: ").upper()

                # Input validation (<2 characters/must be characters)
                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError(
                        "Input not valid! Please enter a single letter (a-z)."
                    )

                # Check if letter has already been guessed
                if guess in guessed_letters:
                    print(f"You have already guessed the letter {guess}")
                    continue

                # Add the guessed letter to guessed_letters set
                guessed_letters.add(guess)

                if guess in unique_secret_letters:
                    print(
                        f"Yes! The letter {guess} is part of the secret city."
                    )
                else:
                    print(
                        f"No! Letter {guess} is not part of the secret city."
                    )
                    remaining_attempts -= 1

                print(f"\n{remaining_attempts} attempts remaining\n")
                print(hangman_stages.get_hangman_stage(remaining_attempts))
                print_secret_word(secret_city, guessed_letters)
                print(
                    f"\n\nNumber of correct letters guessed: "
                    f"{len(guessed_letters & unique_secret_letters)}\n"
                )

                if unique_secret_letters <= guessed_letters:
                    print("Seems you are a master in geography!\n")
                    break

            except ValueError as e:
                print(e)

        if remaining_attempts == 0:
            print("--- Sorry, you have lost this game! ---\n")
            print(f"The secret city was: {secret_city}")

        play_again = ask_yes_no_question(
            "Do you want to play again? (yes/no): "
        )

        if play_again:
            print("Starting a new game...")
            screen_clearance()
        else:
            typewriter(
                f"Thanks for putting your knowledge to the test, "
                f"{username}"
            )
            sys.exit("If you still want to play, click 'Run Program'")


def main():
    """
    Function to start and run the capital cities guessing game.

    This function starts by displaying the opening image, welcoming the player
    to the game, and obtaining the player's name. If no name is provided,\
    the player is assigned the default name "Geo, the champ of capital\
    cities knowledge, aka G3C". The function proceeds to display instructions\
    and start the game by selecting a secret city for the player to guess.
    """
    opening_image()

    print()
    print()
    typewriter("Welcome to capital cities guessing")
    typewriter("We will put your geography knowledge to the test")
    time.sleep(1)

    while True:
        print(Fore.GREEN)
        username = input("Please provide your name \n")

        if username == "":
            typewriter("Looks like you want to play anonymously")
            typewriter("Ok, we will call you Geo, the champ "
                       "of capital cities knowledge, aka G3C")

            username = "G3C"
            break
        elif not username.isalpha():
            print(Fore.RED)
            typewriter("Please enter a name using only alphabetic characters.")
        else:
            print(Fore.GREEN)
            typewriter(f"Let's get started {username.upper().strip()}")
            time.sleep(0.5)
            instructions()
            time.sleep(0.5)
            break

    while True:
        secret_city = select_word()
        start_game(secret_city, username)


if __name__ == "__main__":
    main()
