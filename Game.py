import random
list = ["scissors", "stone", "paper"]
input('Please, enter your choice: ')
user_index = int(user_index)
user_choice= list[user_index]
random_index = random.randint(0,len(list)-1)
computer_choice = list[random_index]
print(computer_choice)
if computer_choice == user_choice:
    print("Draw")
elif computer_choice == "scissors" and user_choice=="stone":
    print("Victory!")
else:
    print("Try again")
