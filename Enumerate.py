#variable = ['c','a','t']
#for index, correct_character in enumerate(variable):
    #print(index, correct_character)
answer = ['c','a','t']
guess_character = "t"
user_answer = ["_", "_", "_"]
for index, correct_character in enumerate(answer):
# alwats have index in enumerate #What is index here again, and I know enumerate function, but I
# don't understand how it works. if it give us only numbers how do we know the letter is ther
#enumerate(answer) [cat]
    if correct_character == guess_character:
        print(index)
        user_answer[index] = guess_character #we can always access smth in the list using integer
print(user_answer)
