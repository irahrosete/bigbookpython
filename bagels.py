"""In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
The game offers one of the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place,
“Fermi” when your guess has a correct digit in the correct place, and
“Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    """main game"""
    print("Bagels, a deductive logic game.\n")
    print(f"I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.")
    print("Try to guess what it is. Here are some clues:")
    print("When I say:\tThat means:")
    print(" Pico\t\t One digit is correct but in the wrong position.")
    print(" Fermi\t\t One digit is correct and in the right position.")
    print(" Bagels\t\t No digit is correct.\n")
    print("For example, if the secret number is 248 and your guess was 843,")
    print("the clues would be Fermi Pico.\n")

    while True:
        secret_num = get_secret_num()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}")
                guess = input("> ")
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        print("Do you want to play again? (yes/no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")

def get_secret_num():
    """returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    """returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == "__main__":
    main()
