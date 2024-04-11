
# Ask the user six times t guess the word
for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if (guess == "PYTHON"):
        print("Correct")
        break

    print("Wrong")