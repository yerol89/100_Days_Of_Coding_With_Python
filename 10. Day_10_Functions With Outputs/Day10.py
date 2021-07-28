# Functions With Outputs

def formatted_name(f_name, l_name):
    new_fname = f_name.title()
    new_lname = l_name.title()
    return f"{new_fname} {new_lname}"

print(formatted_name("YuNuS", "EROL"))

# More Than One Return
def formatted_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please input a valid string"
    new_fname = f_name.title()
    new_lname = l_name.title()
    return f"{new_fname} {new_lname}"

print(formatted_name(input("FNAME?"), input("LNAME?")))

# Day10 Project => CALCULATOR
math_operations = {"+": "ADD", "-": "SUBSTRACT", "*": "MULTIPLY", "/": "DIVIDE"}
def calculate(num1, num2):
    for sign in math_operations:
        print(sign)
    operation = input("Input the operation sign: ")
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Wrong Operand!")
print(calculate(num1 = int(input("Input First Number: ")),
            num2 = int(input("Input Second Number: "))))

