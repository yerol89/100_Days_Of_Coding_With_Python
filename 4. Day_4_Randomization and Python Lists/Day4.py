# Random Module
import random
rnd_int = random.randint(1, 10)
print(rnd_int)

#Python Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting a position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
#Nested List
vegetables = ["potatoes", "onion", "carrot", "spinach"]
foods = [vegetables, fruits]
vegetables[-1]
# Who is going to pay the bill?
names = ["Ali", "Ahmet", "Almila", "Yunus"]
rnd_int = random.randint(0, len(names) - 1)
print(f"{names[rnd_int]} will pay the bill")

# Treasure Map
row1 = ["😀", "😀", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# Day4 Project : Rock_Paper_Scissors Game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
user_choice = int(input("What do you choose?(0 for ROCK, 1 for PAPER and 2 for SCISSORS)\n"))
if user_choice >= 3 or user_choice <= -1:
    print("Invalid Choice, You Loose!")
print("USER CHOOSE:\n")
print(options[user_choice])
print("\n\n")
print("COMPUTER CHOOSE:\n")
computer_choice = random.randint(0, 2)
print(options[computer_choice])


if user_choice == computer_choice:
    print("DRAW")
elif user_choice == 0 and computer_choice != 1:
    print("User Wins!")
elif user_choice == 1 and computer_choice != 2:
    print("User Wins!")
elif user_choice == 2 and computer_choice != 0:
    print("User Wins!")
else:
    print("Computer Wins!!!")
