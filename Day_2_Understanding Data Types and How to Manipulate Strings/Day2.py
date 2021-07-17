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