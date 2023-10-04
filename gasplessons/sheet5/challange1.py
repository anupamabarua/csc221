from gasp import *          # So that you can draw things
from random import randint

def place_player():
    print("Here I am!")
    player_x=randint(5,630)
    player_y=randint(5,470)
    c=Circle((player_x, player_y), 5, filled=True)

def move_player():
    print("I'm moving...")
    update_when('key_pressed')

begin_graphics()            # Create a graphics window
finished = False

place_player()

while not finished:
    move_player()

end_graphics()              
