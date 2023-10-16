# using random function
import random

roll = random.randint(1,6)

guess = int(input('guess the dice roll:\n'))

if guess == roll:
    print("correct, they rolled a " + str(roll))
else:
    print("guess was wrong, they rolled " + str(roll))
