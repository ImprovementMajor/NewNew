errands = ["do your homework", "buy swarovski", "eat", "wash your car", "get cat food"]

errand=input("please enter the errand name: " )
if errand in errands:
    print("This errand was planned")
else:
    print("This errand wasn't planned")


from itertools import chain

dinner = {
    "today": ["salad", "dessert"],
    "tomorrow": ["pizza", "chocolate"]
}
print(dinner.values()) # => [['salad', 'dessert'], ['pizza', 'chocolate']]
all_items = list(chain(*dinner.values()))
print(all_items) # => ['salad', 'dessert', 'pizza', 'chocolate'
food = input("Please enter the food item: ")

if food in all_items:
    print("You can start your dinner")
else:
    print("You need to get groceries")
