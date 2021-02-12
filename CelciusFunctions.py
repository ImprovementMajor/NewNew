def user_input(message):
    while True :
        value = input(message)
        if value.isdigit()== True:
            break
    value=float(value)
    return value
def get_farenheit():
    celcius = user_input("Please enter celcius degree ") #It worked as an infinite cycle if I entered a numbr
    f = (9/5 * celcius) + 32               # but when I change it to this:  while "1".isdigit(): and entered a letter it wont let me to change it because of the float
    print("And the farenheit temperature is", f)
get_farenheit()

def get_celcius():
    farenheit= user_input("Please enter farenhaeit degree ")
    c = (farenheit-32)*5/9
    print("And the celcius temperture is", c)
get_celcius()




#F = (9/5)*C + 32
#C =(F-32)*5/9
