
from random import randint

ran1 = randint(0,1000)

ran2 = int(input("Guess a number between 1 and 1000"))
if ran2 == ran1:
    print("Wow good job")
else:
    print(f"Nope you were close! The number was {ran1}! Better Luck next time!")
