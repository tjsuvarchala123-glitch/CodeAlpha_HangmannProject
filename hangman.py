import random

# List of words
words = ["python", "apple", "house", "tiger", "music"]

# Random word selection
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Hidden word display
display_word = ["_"] * len(word)

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("===== HANGMAN GAME =====")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:

    # Show hangman drawing
    print(hangman_stages[incorrect_guesses])

    # Show current word
    print("Word:", " ".join(display_word))

    # Show remaining guesses
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    # Wrong guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Final result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print(hangman_stages[incorrect_guesses])
    print("\nGame Over!")
    print("The correct word was:", word)
