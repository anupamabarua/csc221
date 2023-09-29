from random import randint

while True:
    x = randint(1, 10)
    print(x)
    if x == 5:
        break           #breaks the loop (ends it)
    print('x was not 5!')

