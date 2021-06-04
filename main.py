#typewriter fancy stuff
import sys
import time


#starting the game
beginning = "Hi, welcome to hangman!\nLet's get started!\n"
for char in beginning: 
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep (0.05)

#list of words
import random
word_list = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

#choose word
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

#tell player to start guessing
startguessing = "Please guess a character you think is in the word."
for char in startguessing: 
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep (0.05)

#guessing
def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 5

+--
