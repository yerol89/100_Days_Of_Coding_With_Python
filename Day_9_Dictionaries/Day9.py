# PYTHON DICTIONARIES

# Define a dictionary with key-value pairs
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# Get the value of a key
programming_dictionary["Bug"]

# Add a new item to dictionary
programming_dictionary["Loop"] = "Doing something over and over again"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Student Score Grading
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if 91 <= student_scores[key] < 100:
        student_scores[key] = "Outstanding"
    elif 81 <= student_scores[key] < 91:
        student_scores[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] < 81:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Failed"


# 🚨 Don't change the code below 👇
print(student_scores)

#Nesting => We can use nested lists and dictionaries within a dictionary
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

def add_new_country(country, total, cities = []):
    new_record = {"country": "", "cities_visited": [], "total_visits": 0}
    travel_log.append(new_record)
    new_record["country"] = country
    new_record["cities_visited"] = cities
    new_record["total_visits"] = total
    print(travel_log)
add_new_country("Russia", 2 , ["Moscow", "St. Petersburg"])

# DAY9 PROJECT => SECRET AUCTION
from replit import clear

def auction():
    all_bids = []
    new_bidder = {}
    bidder = "Y"
    i = 0
    highest_bid = 0
    while bidder == "Y":
        keep_going = input("Do you want to input new record(Y for yes or N for No):")
        if keep_going == "Y":
            clear()
            all_bids.append(new_bidder)
            new_bidder["name"] = input("What is your name: \n")
            new_bidder["bidder"] = int(input("What is the amount of your bid:\n"))
            new_bidder = {}
            if all_bids[i]["bidder"] > highest_bid:
                highest_bid = all_bids[i]["bidder"]
            i = i + 1

        else:
            bidder = "N"
    for element in all_bids:
        if element["bidder"] == highest_bid:
            name = element["name"]
            bid = element["bidder"]
            print(f"{name} win the auction with a bid of ${bid}")


auction()







