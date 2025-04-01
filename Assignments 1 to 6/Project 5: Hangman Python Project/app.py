import random

# Hangman Project 🎩💀
words = ['enum', 'python', 'colab', 'vscode', 'game']
word = random.choice(words)
guessed_letters = []
attempts = 6

# Welcome message
print("🎩 Welcome to the Hangman Game! 💀")
print("_ " * len(word))  # Display underscores for the word

# Game loop
while attempts > 0:
    guess = input("\n🔤 Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter!")
        continue

    if guess in guessed_letters:
        print("⛔ You've already guessed this letter. Try another!")
        continue

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempts left.")

    # Display guessed letters in word
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    # Check if the user has guessed the word
    if "_" not in displayed_word:
        print(f"🎉 Congratulations! The correct word is: {word}")
        break

# If user runs out of attempts
if attempts == 0:
    print(f"💀 Game Over! The correct word was: {word}")


