import random
turn = True       #Will help to show who has the next turn
health_hero = 30
health_dragon = 30
health_drink_hero = 2
while health_hero > 0 and health_dragon > 0 : #First main cycle means that the game is not over until health > 0
    if turn == True:   # True turn means it's hero's turn
        print("It's heroe's turn ")
        print(" Would you like to attack or drink a potion?")
        print("The amount of your potion is ", health_drink_hero)
        while True: # This cycle won't end until you choose drink or attack
            action = input("Choose either attack or drink ")
            if action == "attack" or (action == "drink" and health_drink_hero > 0): # This cycle will end if you choose attack or drink, and you should have enough health and drink
                break


        if action == "attack" :  # If you choose to attack then random damage will affect the dragon
            damage_to_dragon = random.randint(1, 9)
            health_dragon= health_dragon - damage_to_dragon # This will display damage made to dragon
        else:
            health_restore = random.randint(0, 7) # if you choose a drink it will give you random health restore
            health_hero = health_hero + health_restore # this will display health_hero after drink
            health_drink_hero = health_drink_hero - 1 # This will show amount of drinks left
            if health_hero > 30:
                health_hero = 30
            print("The hero's health is ", health_hero)
        print("The Dragon health equals ", health_dragon)
        turn = False # Dragon's turn because hero's turn = True and new cycle for dragon with his options
    else:
        print("It's dragon's turn")
        damage_to_hero = random.randint(0, 11)
        health_hero = health_hero - damage_to_hero
        print("The hero's health equals ", health_hero)
        turn = True # Hero's turn again 

    #health_hero = health_hero - 1
    #health_dragon = health_dragon - 1
    #print("The hero has " + str(health_hero) + " lives left")
    #print("The dragon has " + str(health_dragon) + " lives left") #How do we insert health drinks here
    #print("Keep playing")

print("Game over")

#
#health_drink_dragon = 2

#for i in range(10) #  This cycle will show who attacks first, second and etc. I think I don't need 10 in range here
    #i#f health_hero != 0 or health_dragon != 0 : continue
#else:
    #break
