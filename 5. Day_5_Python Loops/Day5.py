# For Loop

fruits = ["Apple", "Peach", "Pear"]
for f in fruits:
    print(f)

# Average Height Of Students Using For Loop

student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum_of = 0
for h in student_heights:
    sum_of += h
print(f"Sum of students height is {sum_of}")
number_of_students = 0
for l in student_heights:
    number_of_students += 1
print(f"Number of students is {number_of_students}")
average = sum_of / number_of_students
print(f"Average of student heights is {average}")

# Find The Highest Score In a List Using For Loop
student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]
for i in range(0, len(student_scores) - 1):
    if student_scores[i+1] > highest_score:
        highest_score = student_scores[i+1]
print(highest_score)

# For Loop With Range
for number in range(0, 10):
    print(number + 1)

# We can also add step size as a parameter for the "range" function
for number in range(0, 10, 2):
    print(number + 1)

# Sum of all the even numbers between the range of 1 to 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(f"Sum of even numbers between 1-100 is {total}")

# FIZZ_BUZZ Game

for i in range(1, 101):
    if i % 15 == 0:
        print(f"{i} => FIZZ_BUZZ")
    elif i % 3 == 0:
        print(f"{i} => FIZZ")
    elif i % 5 == 0:
        print(f"{i} => BUZZ")
    else:
        print(i)

# DAY5 PROJECT => PYPASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Define a list to save password elements choosen randomly
password = []
for i in range(0, nr_letters):
    rnd_letter = random.randint(0, 51)
    password.append(letters[rnd_letter])
for i in range(0, nr_symbols):
    rnd_symbol = random.randint(0, 8)
    password.append(symbols[rnd_symbol])
for i in range(0, nr_numbers):
    rnd_numbers = random.randint(0, 9)
    password.append(numbers[rnd_numbers])
print("BEFORE SHUFFLING:\n")
print(password)
random.shuffle(password)
print("AFTER SHUFFLING:\n")
print(password)


