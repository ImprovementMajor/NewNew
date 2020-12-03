import random   #got it

print("Welcome to the field of magic game! And the main prize is a car")
print("Here is the assignment for this tour: ")

questions = (
    ("What color is a tabby cat?", "grey"),
    ("What color is the sun?", "yellow"),
    ("What color is the vanila ice cream? ", "white")
)

random_index = random.randint(0, len(questions) - 1)
task = questions[random_index]
question=task[0]
word = list(task[1])
guess_word = ["_"] * len(word)

print(question)
print(guess_word)

# THAT's the beginning of the cycle
while word != guess_word:
    print("And the length of the answer is: ", guess_word)

    while True:
        guess_character = input("Your letter is: ")
        if guess_character: break

    guess_character=guess_character[0]# Question: I know it means that a certain letter should be open on the certain position, but how does the program knows how to do that? How does the program know that not only "y" is on "0" position, but "e" is on the "1" position and etc
    # guess_character => 'y'
    guessed_any = False #  Question: what is the purpose of this False?

    # word => 'yellow'
    # enumerate(word) => [0, 'y'], [1, 'e']
    # index => 0, 1 ,2
    # correct_character => 'y', 'e'
    for index, correct_character in enumerate(word):
        # correct_character => 'y'
        # guess_character => 'y'
        if correct_character == guess_character:
            guessed_any = True # Question: Does it mean that if we choose any correct letter despite its position it will give us True? What does guessed_any mean exactly, what's the purpose of it?
            # ['_', '_'...]
            guess_word[index] = guess_character
            # ['y', '_', '_' ... ]


    if guessed_any:
        print("Please show us the letter ", guess_character)
    else:
        print("There is no " + guess_character + " in this word")
# that's the end of the cycle

print('done...')
