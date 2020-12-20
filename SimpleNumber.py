your_number = input("Please enter a number  ")
your_number = int(your_number)
#if your_number > 1:
    for i in range(2, your_number//2): #Why do we use floor division?
        if (your_number % i) == 0:
            print(your_number, "is not a prime number")
            break
        else:
            print(your_number, "is a prime number")

#if your_number / your_number == 1 and your_number / 1 == your_number: #Как записать эту часть, чтобы делилось без остатка
    #print("This is the prime number")
#else:
    #print("This is not the prime number")







#if your_number/1 and your_number% your_number:
    #print("Your number is simple")
#else :
    #print("This is not a simple number")
