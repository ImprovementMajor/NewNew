errands = {
"11-02-20": ["buy a ticket", "pack your suitcase"],
"11-03-20": ["get pesents", "exchange dollars to rubles"],
"11-04-20": ["visit your grandma", "go shopping with mom"]
}

date=input("Please enter the date in format dd-mm-yy:  ")
if date in errands.keys():
    print("For this day you have the following errands")
    errand_list=errands[date]
    print(errand_list)
else:
    print("The date "  + date + " is a not valid date")
    print("The valid dates are " + list(errands)
