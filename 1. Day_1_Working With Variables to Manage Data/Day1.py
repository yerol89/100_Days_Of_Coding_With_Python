print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print("New lines can be created with a backslash.")
print("Hello" + " " + "Everyone")
print("Hello Python\nHello 100 Days of Coding")
print("Hello" + " " + input("What is your name?\n"))
name = input("What is your name? ")
print("Length of your name is " + str(len(name)))

#Swapping variables with each other
a = input("a: ")
b = input("b: ")
print("BEFORE SWAP")
print("a is equal to " + a)
print("b is equal to " + b)
c = a
a = b
b = c
print("AFTER SWAP")
print("a is equal to " + a)
print("b is equal to " + b)

# DAY1 PROJECT : BAND NAME GENERATOR
print("Welcome to Band Name Generator")
city = input("What is the name of city that you borned?\n")
pet = input("What is the name of your first pet?\n")
print("The name of the band is " + city +"_" + pet + " BAND")