import random
# Loads all tasks for the game. A task is represented as a tuple with two elements : a question and an answer.
# @return [Tuple]
def load_tasks():
    return (
        (
        "What color is the sun?",
        "yellow"
        ),
        (
        "What color is the ice cream?",
        "white"
        ),
        (
        "What color is the peach",
        "orange"
        )
    )
# Returns a random question, answer, and an answer with hidden letters from the collection of tasks
# !!!!!! @params collection [Tuple, List] - why do we have a list here? To get the all the keys from tuples?
# !!!!!  I don't see variable or tuple called collection
# @retun [Tuple] why do we use @ sign?
def get_random_question_and_words(tasks_collection):
    random_index= random.randint(0, len(tasks_collection)-1) # just choosing a random number that matches the length of the collection
    task = tasks_collection[random_index] # assigning a random number we got before to a matching tuple number
    # Can I add a variable "question" that equals question = list(task[0])
    # Line 25 gives an error as well
    question = task[0]
    answer = list(task[1]) # Why don't we write same for the question part?
    return (
        question, # gives us a # QUESTION: or just quesion
        answer,  # gives us an answer
        ["_"] * len(answer) # gives us closed letters
    )
print("Welcome to the field of magic game")
print("Here is the challenge : ")
tasks= load_tasks()
question, answer, guess_word = get_random_question_and_words(tasks) #we don't have a variable "tasks", should we use a Function
# load_tasks instead??
print(question)
# Invites the user to print his guess (1 letter)
# @return [String] !!! I don't understand this line
def ask_for_character():
    user_guess = input(" Type your letter please ")
    return(user_guess[0] if user_guess else ask_for_character()) # this function let us just to type a one letter, we arent
    # even checking if the letter in this word, it can be a wrong guess as well
    # why do we type user_guess[0]? The user won't necessarily guess the first letter) Also we don't have a variable user_guess,
    # we only have "answer" variable, and it's not connected to the user_guess variable

#Checks if the user entered a correct guess and returns
# a new word with these guessed characters open
# @params user_answer[List]
# @params answer[List ]
# params guess_character[String]
# return [List]
def open_characters_in(user_answer, answer, guess_character): #we don't have a variable user_answer, we
# we  have it locally
    for index, correct_character in enumerate(answer):
    # alwats have index in enumerate #What is index here again, and I know enumerate function, but I
    # don't understand how it works. if it give us only numbers how do we know the letter is ther
    #enumerate(answer) [cat]
        if correct_character == guess_character:
            user_answer[index] = guess_character #we can always access smth in the list using integer
    return user_answer
#Core function which starts a new turn and ties the same logic together
# @params answer [List]
# @params guess_word [List]
def next_turn(answer, guess_word, number_of_tries=5):
    print("Your word", guess_word)
    if number_of_tries <= 0:
        print("You've lost")
        return False
    guess_character = ask_for_character()
    new_guess_word = open_characters_in(guess_word.copy(), answer, guess_character) # we don't want to modify, modify inside open c-s
    if new_guess_word == guess_word:
        print("There is no letter " + guess_character + " in this word")
        number_of_tries= number_of_tries - 1
    else:
        print("Please show us the letter " + guess_character)
    return(
    True if answer == new_guess_word else next_turn(answer, new_guess_word, number_of_tries)
    )

result = next_turn(answer, guess_word)


if result:
    print("And it's a right word", answer)
    print("You have won")
else:
    print("The right word was ", answer)
    #define and call after 
