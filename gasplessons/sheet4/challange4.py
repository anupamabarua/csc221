from random import randint

while True:
    num1 = int(input("enter a number"))
    x = randint(1, 10)
    print(x)
    if x == 5:
        break
    print('x was not 5!')
