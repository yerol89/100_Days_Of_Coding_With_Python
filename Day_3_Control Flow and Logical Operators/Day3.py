# If/Else Statements
print("Welcome To RollerCoaster!")
height = int(input("What is your height?\n"))
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller to ride rollercoaster")

# Odd or Even Number
number = int(input("Enter a number\n"))
if number % 2 == 0:
    print("EVEN number")
else:
    print("ODD number")


# BMI Calculator

weight = float(input("Enter your weight in kg. :\n"))
height = float(input("Enter your height in meters:\n"))
BMI = weight / (height ** 2)
BMI_float = round(float(BMI), 2)
if BMI_float < 18.5:
    print("Your BMI is equal to " + str(BMI_float) + " and you are underweight.")
elif 18.5 <= BMI_float < 25.0:
    print("Your BMI is equal to " + str(BMI_float) + " and you have a normal weight.")
elif 25.0 <= BMI_float < 30.0:
    print("Your BMI is equal to " + str(BMI_float) + " and you are overweight.")
elif 30.0 <= BMI_float < 35.0:
    print("Your BMI is equal to " + str(BMI_float) + " and you are obese.")
else:
    print("Your BMI is equal to " + str(BMI_float) + " and you are clinically obese.")

# Determine "Leap Year" or not

year = int(input("Enter the year:\n"))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is  a leap year")
        else:
            print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

# Order Pizza
print("Welcome to Pizza Python!")
size = input("Enter pizza size(S, M or L):\n")
add_pepperoni = input("Do you want pepperoni?(Y or N)\n")
extra_cheese = input("Do you want extra cheese?(Y or N)\n")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill = bill + 2
    if extra_cheese == "Y":
        bill = bill + 1
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill = bill + 2
    if extra_cheese == "Y":
        bill = bill + 1
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1
print("Total bill is: " + str(bill) + "$")

# Day3 Project

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")






