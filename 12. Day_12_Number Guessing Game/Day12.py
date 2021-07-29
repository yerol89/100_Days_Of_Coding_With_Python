import random
def number_guess():
    num = random.randint(1, 100)
    print(num)
    difficulty = input("Choose game difficulty => 'easy' or 'hard'")
    i = 0
    if difficulty == "easy":
        while i < 10:
            guessed_num = int(input("Input a number: "))
            i = i + 1
            if guessed_num > num:
                print(f"Too High!!!, you have {10 - i} try left")
            elif guessed_num < num:
                print(f"Too Low!!!, you have {10 - i} try left")
            else:
                print("You WIN")
                break
        print("OUT OF YOUR CHANCES")
    elif difficulty == "hard":
        while i < 5:
            guessed_num = int(input("Input a number: "))
            i = i + 1
            if guessed_num > num:
                print(f"Too High!!!, you have {5 - i} try left")
            elif guessed_num < num:
                print(f"Too Low!!!, you have {5 - i} try left")
            else:
                print("You WIN")
                break
        print("OUT OF YOUR CHANCES")
    else:
        print("Wrong Choice!!!")
        number_guess()

number_guess()