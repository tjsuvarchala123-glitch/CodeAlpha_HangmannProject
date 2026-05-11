import random

words = ["python", "apple", "house", "tiger", "music"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

display_word = ["_"] * len(word)

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

while incorrect_guesses < max_incorrect and "_" in display_word:

    print(hangman_stages[incorrect_guesses])

    print("Word:", " ".join(display_word))

    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses += 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print(hangman_stages[incorrect_guesses])
    print("\nGame Over!")
    print("The correct word was:", word)
