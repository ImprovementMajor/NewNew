import random
#First part generates a list of randomly selected 'heads' and 'tails'
numberOfStreaks = 0
totalStreaks = 0 # It's a 0 just because it's a 0 at this point and we don't have any matches found yet
coinFlip = [] # empty list because we don't have any coin flips at this moment
h = 0 #number appointed for heads
t = 1 #number appointed for tails
for experimentNumber in range(1):  # the purpose of the experiment number is to check how many t and h in 100, where is the end of this loop?
    #Code that creates a list of 100 'heads' or 'tails' values
    for i in range(100):  # iteration being repeated 100 times
        if random.randint(0,1) == 0: #if o we add h
            coinFlip.append('h')
            numberOfStreaks = numberOfStreaks + 1
            if numberOfStreaks >= 5:
                totalStreaks = totalStreaks +1
                print(totalStreaks)
        elif random.randint(0,1) == 1:
            coinFlip.append('t') # if something else or 1 in this case adding t to strike
            numberOfStreaks = numberOfStreaks + 1
            if numberOfStreaks >= 5:
                totalStreaks = totalStreaks +1
                print(totalStreaks)
        #else:
            #print("Your program doesn't wprk")
#         print(coinFlip) #for debugging purposes
# #Code that checks if there is a streak of 6 heads or tails in a row
# # row equals 10?
#     el = False # element is false just because it's false, why not True?
#     previous_el = False #same thing
#     matches_found = 1
#     target = 5
#     for i in range(100): #iteration being repeated 100 times
#         # ['t', 't', 'h', 'h', 't', 't', 't', 'h', 't', 't']
#         if i > 0:   # if iteration bigger than 0, which always be bigger in our case
#             el = coinFlip[i] # 't' checks whether it was t or h in the current iteration
#             previous_el = coinFlip[i-1] # 't' checks whether it was t or h in the previous iteration.
#             # Do both of them being checked 100 times? because we have 100 range
#             if el == previous_el:  # now it compares elememt and previous element and if they are equal we are getting tt or hh in a row
#                 print(f"Found {el} and {previous_el}") #For debugging purposes
#
#                 matches_found = matches_found + 1  #every time el == previous_el we add + 1 to matches_found
#                 print(f"MAtches found: {matches_found}") #for debugging purposes
#                 if matches_found >= target: #if we get more than 5 matches found then we getting streak
#                     print(f"We've reached the target {matches_found}")
#                     print(f"The last two elements we've found are {el} and {previous_el}")
#                     break #we stopping the program there
#             else:
#                 matches_found = 1
#     print(matches_found)
