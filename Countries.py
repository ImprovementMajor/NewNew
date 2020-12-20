import random
countries={
"USA":"Washinghton",
"Italy":"Rome",
"Japan":"Tokyo",
"Australia":"Sydney"
}
countries_keys=list(countries)
#print(countries2)
random_integer=random.randint(0,len(countries_keys)-1)
final_country=countries_keys[random_integer]
print("What is the capital of " + final_country)
answer=input(' ')
capital= countries[final_country]
if answer==capital:
    print('yes')
else:
    print('no')
