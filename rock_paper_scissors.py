import random

computers_choice = random.choice(['rock', 'paper', 'scissors'])

uers_choice = input('do you want rock, paper, or scissors? ')

print("computer's choice: " + str(computers_choice))

if uers_choice == computers_choice:
    print('tie')
elif uers_choice == 'rock' and computers_choice == 'scissors' :
    print('win')
elif uers_choice == 'paper' and computers_choice == 'rock' :
    print('win')   
elif uers_choice == 'scissors' and computers_choice == 'paper' :
    print('win')
else:
    print('computer win, you lose')              