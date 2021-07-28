def move():
    print("Go Straight")


def turn_left():
    print("Turn Left!")


def turn_right():
    print("Turn Right!")


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def at_goal():
    print("You reached your goal")


def wall_in_front():
    print("There is a wall in front of you")


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


