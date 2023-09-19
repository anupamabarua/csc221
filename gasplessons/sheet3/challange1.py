from gasp import *

begin_graphics()

Circle((300, 200), 100)
Circle((230,220),20)
Circle((360,220),20)

Arc((300, 200), 50, 225, 315)


update_when('key_pressed') 

end_graphics()
