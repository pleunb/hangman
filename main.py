import random 
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


def galgjes(tries):
  stages = [ """
            +---+
            |   o
            |  /|\\
            |  / \\
            ===
            ""","""
            +---+
            |   o
            |  /|\\
            |  
            ===
            ""","""
            +---+
            |   o
            |  
            |  
            ===
            ""","""
            +---+
            |   
            |  
            |  
            ===
            ""","""
            +---+
            |   
            |  
            |  
            
          """, """
            +---+
          """
  ]
  return stages[tries]

#guessing
def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 5
  print("Hi, welcome to Hangman! Let's get started. You have 5 oppurtunities to guess a letter (or the word). The word is in Dutch. \n")
  print(galgjes(tries))
  print(word_completion)
  while not guessed and tries > 0:
    guess = input("Please guess a letter that you think is in the word we chose:").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You've already guessed this letter. Try a letter you haven't tried before this time:")
        print ("You have " ,tries, " guesses left.")
      elif guess not in word:
        print(guess, "is not in the word. Try again!")
        tries -=1
        print ("You have " ,tries, " guesses left.")
        guessed_letters.append(guess)
      else:
        "Well done!"
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True 
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words: 
        print("You've already guessed this letter. Try a letter you haven't tried before this time:")
        print ("You have " ,tries, " guesses left.")
      elif guess != word:
        print(guess, "is not in the word. Try again!")
        tries -=1
        print ("You have " ,tries, " guesses left.")
        guessed_letters.append(guess)
      else:
        guessed = True
        word_completion = word 
    else: 
      print("Sorry! Please make sure you're guessing a letter or word, and not a number or other figure. Try again:\n")
      print ("You have " ,tries, " guesses left.")
    print(galgjes(tries))
    print(word_completion)
  if guessed:
    print("Well done! You guessed the word and won the game.")
  else:
    print("Unfortunately you ran out of turns. The word was " + word + ". You lost!")



def main ():
  word = get_word()
  play(word)
  if input("Would you like to play again? (y/n)") == "y":
    main()

main()


