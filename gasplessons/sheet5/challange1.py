from gasp import *          

begin_graphics()
finished = False


def place_player():
    player_x = (1,10)
    player_y = (10,1)
    print("Here I am!")
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    print("I'm moving...")
    update_when('key_pressed')


while not finished:
    move_player()


end_graphics()   
