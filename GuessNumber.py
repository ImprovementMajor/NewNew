import random

answer = random.randint(0, 20)

while True:
    user_guess = input("Please enter your guess from 0 to 20...") #Problem is here, I need to turn user_guess into integer format  to be able to compare it with the answer and  give a hint later
    user_guess = int(user_guess)
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
#How to insert this part?
attempt = 0
while attempt < 5 :
    attempt = attempt + 1
    print ("You've wasted " + str(attempt) + "  attempt")
print("Game over")
