import random

# 1. Predefined list of words
word_list = ["apple", "bananna", "guava", "mango", "orange"]

# 2. Choose a random word
secret_word = random.choice(word_list)

# 3. Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# 4. Create a display word (with _)
display_word = ["_" for _ in secret_word]

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# 5. Main game loop
while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f" Wrong guess! You have {max_guesses - incorrect_guesses} tries left.\n")

# 6. Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print(" You lost! The word was:", secret_word)