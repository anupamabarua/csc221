from gasp import *

def place_player():
    print("Here I am")

def move_player():
    print("Im moving...")
    update_when('key_pressed')


begin_graphics()
finished = False

place_player()

while not finished:
    move_player()


end_graphics
