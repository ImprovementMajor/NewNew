import random

c_c = {
    "Russia": "Moscow",
    "Ukraine": "Kiev",
    "United States": "Washington"
}
countries=list(c_c)#['Russia'. 'Ukraine', 'United States']
index=random.randint(0, len(countries)-1)#this is the random integer
country=countries[index]#random element from the list
print('What is the capital of ' + country + "?")
answer = input(" ")
capital= c_c[country]#Capital of the country
if capital == answer:
    print("That's the right answer")
else:
    print("This answer is incorrect") #write steps first
