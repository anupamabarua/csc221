from gasp import *

def place_player():
    print("here I am")

def move_player():
    print("im moving...")
    update_when('key_pressed')


begin_graphics()
finished = False

place_player()

while not finished:
    move_player()


end_graphics
