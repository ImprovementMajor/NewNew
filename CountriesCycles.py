c_c = {
"USA" : "Washington",
"France": "Paris",
"England": "London",
"Japan": "Tokyo",
"Ukraine": "Kiev",
"Germany": "Berlin",
"Australia": "Canberra",
"Canada": "Ottawa"
}
#countries.items()
#countries=list(c_c)
#print(list(c_c))
user_points=0
for country, capital in c_c.items():
    print(" Your current amount of points is  "  +  str(user_points))
    print(" What is the capital of  " + country + "?")
    user_guess=input("Your answer is  ")
    if capital == user_guess:
        print("That's the correct answer")
        user_points += 1
    else:
        print("The correct answer is " +  capital)
        user_points -=1
