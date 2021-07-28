import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["bear", "wolf", "fish"]
x = random.randint(0, len(word_list) - 1)
chosen_word = word_list[x]
list_of_blanks = []
for n in range(0, len(chosen_word)):
    list_of_blanks.append("_")
list_of_blanks

# Find out if the guessed letter in the chosen_word or not

chars = list(chosen_word)
print(chars)
life = 6
while life > 0:
    guess = (input("Input a letter: ")).lower()
    if guess in chars:
        i = chars.index(guess)
        list_of_blanks[i] = guess
        #chars.remove(chars[i])
        print(list_of_blanks)
    else:
        life = life - 1
        print(stages[life])
    if life == 0:
        print("You LOSE!")
        break
    if "_" not in list_of_blanks:
        print("YOU WIN!")
        break




