def recur():    # I don't understand lines 1-3
    print("Hi")
    recur()

def ask_for_input():
    value = input("Please enter anything ")
    return(value if value else ask_for_input())
user_input = ask_for_input()
