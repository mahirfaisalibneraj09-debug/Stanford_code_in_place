from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while left_is_clear():
        fill_first_line()
        get_to_the_starting_position()
        go_to_the_new_line()
    fill_first_line()


    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
def fill_first_line():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
def get_to_the_starting_position():
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
def go_to_the_new_line():
    turn_right()
    move()
    turn_right()
def turn_right():
    for i in range(3):
        turn_left()
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()