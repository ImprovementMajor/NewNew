import random

answer = random.randint(0, 20)

while True:
    input("Please enter your guess from 0 to 20...")
    user_guess = int(user_guess) #Problem is here, I need to turn user_guess into integer format  to be able to compare it with the answer and  give a hint later
    if user_guess == answer:
        print("You've guessed right")
        break
    else :
        print("Here is the hint")
        if user_guess > answer :
            print("Your guess is bigger than the answer")
        else :
            print("Your guess is smaller than the answer")
    # check if the guess equals to the answer
    # if yes, then break from the loop
    # if no, give the user a hint saying whether his/her guess is less than or greater than the answer
