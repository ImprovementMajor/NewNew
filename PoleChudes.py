import random   #got it
print("Welcome to the field of magic game! And the main prize is a car") #got it
print("Here is the assignment for this tour: ") #got it
questions=(
("What color is a tabby cat?", "Grey"), #got it
("What color is the sun?", "Yellow"),
("What color is the vanila ice cream? ", "White") #got it
 )
random_index=random.randint(0, len(questions)-1) #got it
task=questions[random_index] #got it
question=task[0] #got it
word=list(task[1]) #we turn the string into the list, got it
guess_word=["_"]*len(word) #we have to have same amount of empty spaces according to the list, got it
#print(question)  having problem here, getting infinite cycle
#print(guess_word)  #having problem here, getting infinite cycle
while word != guess_word:  #got it
    print("And the length of your word is: ", guess_word) # It's used to demonstrate the lenghth of the word, which should be equal to the length of the answer
    while True: #got it
        guess_character=input("Your letter is: ") #got it
        if guess_character : #
            break
    guess_character=guess_character[0]# Does it mean that we are asking for the first letter only, but not any one letter?
guessed_any=False #Not sure what is that?
for index, correct_character in enumerate(word): #a letter will be stored in correct_character, and number in index
    if correct_character== guess_character:
        #guessed_any = True #not following here
        guess_word[index]=guess_character
if guessed_any:
    print("Please show us the letter ", guess_character)
else:
    print("There is no " + guess_character + " in this word")

        #guess_word[index]=guess_character
for index, correct_character in enumerate(word):
    if correct_character==guess_character:
        print("Please, show a letter "+ guess_character + " to us")
        guess_word[index]=guess_character
guessed_any=False
for index, correct_character in enumerate(word):
    if correct_character==guess_character:
        guessed_any=True
        guess_word[index]=guess_character
if guessed_any:
    print("Please, open the letter ", guess_character)
else:
    print("There is no letter " + guess_character + " in this word")
