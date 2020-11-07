import random

shells = {
    "L": 0,
    "C": 0,
    "R": 0
}
all_keys=list(shells.keys())
shell_num=random.randint(0,len(all_keys)-1)
shells[all_keys[shell_num]]=1
guess=input("Please  choose a shell from L, C, R ")
if guess in shells.keys() :
    if shells[guess]==1:
        print("You found the ball")
    else:
        print("Try again")
else:
    print("Please input shell name from the following: L, C, R")
