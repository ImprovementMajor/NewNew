To_do_list={
"2020-09-04": ["meet with friends", "go to the theater"],
"2020-02-01": ["get ready for the trip", "buy cat food"]
}
To_do_list_keys=list(To_do_list)
print(To_do_list_keys)
date=input("Please enter the date in format yyyy-mm-dd: ")
#answer=input(" ")
if date in To_do_list_keys:
    print("For this day you have the following errands")
    errand_list=To_do_list[date]
    print(errand_list)
else:
    print("Update your calendar")
