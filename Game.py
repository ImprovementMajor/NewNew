list = ["scissors", "stone", "paper"]
your_choice = input('Please, enter scissors, stone or paper: ')
import random
computer_choice = random.randint("scissors", "stone", "paper")
print(day)
if computer_choice == your_choice:
    print("Victory!")
else:
    print("Try again")
