from screen_output import *

def init(wire):
    output(wire)
    if (wire[0] == 0):
        key = input("Press any key to enter game!!")
        wire[0] = 1
    
