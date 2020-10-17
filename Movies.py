age = float(input('Please, enter your age and film rating: '))
film_rating= input(" ")
if film_rating == "NC-17" and age >= 17:
                print("Choose your seat")
elif film_rating == "PG" and age < 17 :
                print("Small children must be accompanied by adults")
elif film_rating == "PG-13" and age < 13:
                print("This movie is not recommended for viewing by children under the age of 13")
elif film_rating == "R" and age < 17:
                print("This movie is not recommended for viewiig by children under the age of 17 without adults")
else:
                print("Enjoy your movie!")
