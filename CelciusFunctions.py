def get_farenheit():
    celcius = float(input("Please enter celcius degree "))
#    while celcius == nan :     Here I'm trying to prevent a user to enter anything except a number
#        print("Please enter a number") And then trying to create an infinite cycle, that will work until a user enters a number 
    f = (9/5 * celcius) + 32
    print("And the farenheit temperature is", f)
get_farenheit()

def get_celcius():
    farenheit = float(input("Please enter farenheit degree "))
    c = (farenheit-32)*5/9
    print("And the celcius temperture is", c)
get_celcius()




#F = (9/5)*C + 32
#C =(F-32)*5/9
