from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    This program will find the middle point of the row by placing
    beepers at the corners and shrinking the distance between the beepers.
    When two adjacent beepers are found, removes the one at the right and places
    Karel at the leftmost cell with the remaining beeper, which will be the middle point.  
    """
    
    while front_is_clear() and no_beepers_present():
        move()
        #Shrinking the space between two beepers
        if beepers_present():
            pick_beeper()
            turn_and_move()
            if no_beepers_present():
                put_beeper()
                move()
                
        #Edge case: place a beeper in each corner
        #We only need to check twice for the 2x2 world 
        #(This could probably be avoided)
        for i in range(2):
            if front_is_blocked():
                put_beeper()
                turn_and_move()

    #Place Karel in the middle point
    if beepers_present():
        pick_beeper() 
        turn_and_move()
        if not_facing_east():
            turn_around()
            
def turn_around():
    turn_left()
    turn_left() 

def turn_and_move():
    turn_around()
    move()   

if __name__ == '__main__':
    main()
