import random
animals={
"polar bear" :"white",
"turtle" : "brown",
"tiger" : "orange",
"racoon" : "grey"
}
animals_keys=list(animals) #get all the keys from the dictionary
random_index=random.randint(0,len(animals_keys)-1)# picks random number
computer_picked_the_animal=animals_keys[random_index]#random choice by computer from the animals_keys
print("What color fur coat  " + computer_picked_the_animal + " has?")#input
answer=input(" ")
fur_coat=animals[computer_picked_the_animal]
if fur_coat== answer :
    print('Yes')
else:
    print('Try again')
