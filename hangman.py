import random
def display_welcome():
    print("=" * 35)
    print("       WELCOME TO HANGMAN!")
    print("          A Guessing Game")
    print( "=" * 35)
display_welcome()

def load_words():
   file = open("google-10000-english-no-swears.txt", "r")
   words = file.readlines()
   file.close()

   words = [word.strip() for word in words]
   return words
words = load_words()

secret_word = random.choice(words)
print("Length of word  = ",(len(secret_word)))

guessed_letters = set()
attempts = 6
wrong_guesses = 0
def display_hangman(wrong_guess):
    hangman_stages = [
           """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """

   ]  
    print (hangman_stages[wrong_guesses])
while attempts > 0:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.add(guess)
    if guess in secret_word:
         print("Correct guess!")
    else:
        attempts -= 1
        wrong_guesses += 1
        print("Wrong guess!")
        display_hangman(wrong_guesses)
    print(guessed_letters)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)
    if all(letter in guessed_letters for letter in secret_word):
          print("=" * 30)
          print("       CONGRATULATIONS!")
          print("=" * 30)
          print("You guessed the word correctly!")
          print("The word was:", secret_word.upper())
          print("You are a great guesser!")
          print("=" * 35)
          break
    if attempts == 0:
         print("=" * 30)
         print("           GAME OVER!")
         print("=" * 30)
         print("You ran out of attempts!")
         print("The correct word was:", secret_word.upper())
         print("Better luck next time!")
         print("=" * 35)
         break
        