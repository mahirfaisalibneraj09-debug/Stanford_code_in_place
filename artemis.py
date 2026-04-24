from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    for i in range(3):
        building_columns()
        starting_position()
        go_to_the_next_column()
    building_columns()
    starting_position()
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
def building_columns():
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
def starting_position():
    turn_left()
    turn_left()
    for i in range(4):
        move()
    turn_left()
def go_to_the_next_column():
    for i in range(4):
        move()

        
if __name__ == '__main__':
    main()