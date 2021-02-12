# Calculates factorial
def factorial(number):
    print("This is a module", __name__ )
    result=1 #Why do we use result? What's the purpose of it?
    for i in range(1, number+1): result *= i
    return result
print("Please call the module", my_math.__name__)
print("The result is: ", my_math.factorial(number))
#the code doesn't work 
