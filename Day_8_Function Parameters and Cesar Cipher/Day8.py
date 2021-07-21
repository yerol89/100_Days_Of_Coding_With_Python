import math
# "name" is the PARAMETER for this function
def greeting(name):
    print(f"Hello {name}")
    print(f"How do you  do {name}?")

# We call the function here with the "Almila" argument
greeting("Almila")


# Function to calculate number of cans we need for painting an area=> Assume a can paints 5m^2 area
def paint():
    height = int(input("Height of the wall: "))
    width = int(input("Width of the wall: "))
    need = math.ceil(height * width / 5)
    print(f"We need {need} can of paint")

paint()

# Function to check whether an argument is a prime number or not
def primeChecker(x):
    y = True
    for p in range(2, x - 1):
        if x % p == 0:
            print("NOT PRIME")
            y = False
            break
    if y == True:
        print(f"{x} is a prime number")

primeChecker(11)

# Day8 Project => Caesar Cipher


def caesarCipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encoded = []
    decoded = []
    if direction == "encode":
        chars = list(text)
        for c in chars:
            i = alphabet.index(c)
            if i < (26 - shift):
                encoded.append(alphabet[i + shift])
            else:
                j = alphabet.index(c)
                m = (j + shift + 1) % 26
                encoded.append(alphabet[m])
    print(encoded)
    if direction == "decode":
        chars2 = list(text)
        for c in chars2:
            i = alphabet.index(c)
            if i < shift:
                decoded.append(alphabet[i - shift + 25])
            else:
                j = alphabet.index(c)
                m = (j - shift)
                decoded.append(alphabet[m])
    print(decoded)

    if direction not in ["encode", "decode"]:
        print("INVALID CHOICE")

caesarCipher()









