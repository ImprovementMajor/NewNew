import random
choices=["stone", "paper", "scissors"]
computer_choice=random.randint(0,len(choices)-1)
user_choice=input("please enter stone, paper or scissors :")
if user_choice=="stone" and computer_choice=="paper":
    print("You have won")
elif computer_choice=="stone" and user_choice=="paper":
    print("You've lost")
elif computer_choice=="stone" and user_choice=="stone":
    print("You got the same values")
elif computer_choice=="paper" and user_choice=="paper":
    print("You got the same values")

elif user_choice=="scissors" and computer_choice=="paper":
    print("You've won")
elif user_choice=="paper" and computer_choice=="scissors":
    print("You've lost")
elif user_choice=="scissors" and computer_choice=="scissors":
    print("You got the same values")

elif user_choice=="stone" and computer_choice=="scissors":
    print("You've won")
elif computer_choice=="stone" and user_choice=="scissors":
    print("You've lost")
else:
    print("Try again")
