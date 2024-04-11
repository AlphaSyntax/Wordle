
WORD = "PYTHON"
# Ask the user six times t guess the word
for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if (guess == WORD):
        print("Correct")
        break

# user guess is "snake" and secret word is "PYTHON"
# correct letter, misplaced letter, wrong letter
    correct_letters = {letter for letter, correct in zip(guess, WORD)
                       if (letter == correct)}
    misplaced_letters = (set(guess) & set(WORD) - correct_letters)
    wrong_letters = set(guess) - set(WORD)

    print("Correct letters:",", ".join(sorted(correct_letters)))
    print("Misplaced letters:",", ".join(sorted(misplaced_letters)))
    print("Wrong letters:",", ".join(sorted(wrong_letters)))
