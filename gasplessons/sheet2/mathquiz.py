from random import randint

correct = 0

for q in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = f"What is {num1} times {num2}? "
    answer = num1 * num2
    response = int(input(question))
    if answer == response:
        print("Thats right - you slayed!. ")
        correct += 1
    else:
        print(f"No, your wrong {answer}.")
if correct >= 5:
    print(f"I asked you 10 questions. You got {correct} of them right.\nWell done!")
else:
    print(f"I asked you 10 questions. You got {correct} of them right.\nTry again for a higher score!")

