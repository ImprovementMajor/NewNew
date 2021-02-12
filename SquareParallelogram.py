#a = int(input("Please enter the length (meters): "))
#b = int(input("Please enter the width (meters: "))

#result = a * b

#print("Total square: " + str(result) + "м^2")

def ask_for_length():
    length = input("Please enter the length ")
    return(int(length) if length else ask_for_input()) #shows error


def ask_for_width():
    width = input("Please enter the width ")  #Why I'm getting only lwngth and not width?
    return(int(width) if width else ask_for_input())

#length = ask_for_length()

#width= ask_for_width()

def total_square(length, width):
    total_square = length * width #This is not right because variables length and width are unknown
    return(total_square)

#print(total_square(length, width))

def ask_for_another():
    length = ask_for_length()
    width= ask_for_width()
    print(total_square(length, width))
    ask_for_input= input("Would you like to calculate another square? Please enter yes or no ")
    if ask_for_input == "yes":
        ask_for_another()
    else:
        print("Good bye")
        return

ask_for_another()
