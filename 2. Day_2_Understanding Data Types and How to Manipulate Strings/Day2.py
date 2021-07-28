city = input("Where did you born?")
lenght = len(city)
# "length is an integer variable, I have to convert it to a string to concatenate"
#Type-casting
str_length = str(lenght)
print("My hometown has " + str_length + " characters.")
print(70 + float("123.5"))

# String Subscripting
two_digit_number = input("Input a two digit number:\n")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print("Addition of " + two_digit_number + "'s digits is " + str(result))

# Calculate BMI Value
weight = input("What is your weight in Kg.\n")
height = input("What is your height in m.\n")
weight = float(weight)
height = float(height)
BMI = weight/(height * height)
print("Your BMI is " + str(BMI))

# f_String => We can use many primitive data types with f_string
score = input("Your Score:\n")
height2 = input("Your height:\n")
married = input("Marrial Status:\n")
print(f"Your score is {score}, your height is {height} and marial status is {married}")

# Calculate rest of your life in days, months and weeks assume you will live until 90
age = input("How old are you?\n")
left = 90 - int(age)
days = left * 365
weeks = left * 52
months = left * 12
print(f"You have {days} days, {weeks} weeks or {months} months to live")

# DAY2 PROJECT: TIP CALCULATOR AT A RESTAURANT
print("Welcome to tip calculator\n")
total_bill = input("What is the total bill:\n")
percentage_tip = input("What percentage of the bill would you like to give as tip:\n ")
people_to_split = input("How many people to share bill and tip:\n")
bill_plus_tip = float(total_bill) + (float(total_bill) * float(percentage_tip)) / 100
payment_per_person = float(bill_plus_tip) / int(people_to_split)
payment = round(float(payment_per_person), 2)
print("Each person pays " + str(payment))
