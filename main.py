#starting the game
print ("Hi, welcome to hangman! Let's get started!")

#list of words
import random
word_list = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

#choose word
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

#tell player to start guessing
print ("Please guess a character you think is in the word!")

#guessing
def play(word):
  print("word_completion")