import random
health_hero = 30
health_dragon = 30
while health_hero != 0 and health_dragon != 0 : #First cycle
    health_hero = health_hero - 1
    health_dragon = health_dragon - 1
    print("The hero has " + str(health_hero) + " lives left")
    print("The dragon has " + str(health_dragon) + " lives left") #How do we insert health drinks here
    print("Keep playing")

print("Game over")

health_drink_hero = 2
health_drink_dragon = 2

for i in range(10) #  This cycle will show who attacks first, second and etc. I think I don't need 10 in range here
    if health_hero != 0 or health_dragon != 0 : continue
else:
    break 
