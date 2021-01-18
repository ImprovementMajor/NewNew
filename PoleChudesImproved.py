import random
list_levels= ["child", "teenager", "adult"]
print("Welcome to the field of magic game!")

while True: #forever loop until I break 
    difficulty_level= input("Choose the level of difficulty: child, teenager, adult. ")
    if difficulty_level in list_levels: break #Can I add == child, teenager, adult? or should I create separate cycle
    print("You didn't enter anything, please try again")

print("Here is the assignment for this tour, level of difficulty is ", difficulty_level)

# Create a dictionary with keys (level of difficulty) and values (assignment for the tour).
# Where do I write the answers for the assignments? Or can I make 3 different dictionaries under variables child, teenager, adult?
questions_levels = {
    "child":((task, answer)(task, answer),),
    "teeanager":("What color is the sun?", "yellow"),
    "adult":("What color is the vanila ice cream? ", "white")
}
questions= questions_levels[difficulty_level]
#Choice function, it works except it doesn't pick a question based on difficulty_level, have to connect it somehow
task = random.choice(questions)
#print(random_entry)

#print(task)
#
task = questions[random_index] #I don't know how to assign index to dictionary?????
#question=task[0]
#word = list(task[1])
#guess_word = ["_"] * len(word)

#print(question)
#print(guess_word)

# THAT's the beginning of the cycle
#while word != guess_word:
    #print("And the length of the answer is: ", guess_word)

    #while True:
        #guess_character = input("Your letter is: ")
        #if guess_character: break

    #guess_character=guess_character[0]#It takes the first letter from the user input, to prevent people typing more than one letter
    # guess_character => 'y'
    #guessed_any = False #  Just to check whether or not the user entered at least anything, it is just beginning of the cycle, and user didn't have a chance to enter anything else. That's why it has False value

    # word => 'yellow'
    # enumerate(word) => [0, 'y'], [1, 'e']
    # index => 0, 1 ,2
    # correct_character => 'y', 'e'
    #for index, correct_character in enumerate(word):
        # correct_character => 'y'
        # guess_character => 'y'
        #if correct_character == guess_character:
            #guessed_any = True # Question: Does it mean that if we choose any correct letter despite its position it will give us True? What does guessed_any mean exactly, what's the purpose of it?
            # ['_', '_'...]
            #guess_word[index] = guess_character
            # ['y', '_', '_' ... ]


    #if guessed_any:
        #print("Please show us the letter ", guess_character)
    #else:
        #print("There is no " + guess_character + " in this word")
# that's the end of the cycle

#print('done...')



#Once you get an assignment, write a new cycle that will give you only 5 attempts
#Smth like, you need to work on it look up dragon and polechudes
# Also how do I wrap it around the other code?
#attempts = 0
#while attempts < 5:
    #attempts = attempts + 1
    #if attempts == 5 : break
    #print("Try again")

#print("You have no attempts left. Computer has won")
