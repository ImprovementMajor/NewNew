import math
print("please enter the length " )
length = input(" ")
AVG_CAT_HEIGHT = 15
def circle_radius(length):
    return length/(2 * 3.14)
#print(float(circle_radius)) #TypeError: float() argument must be a string or a number, not 'function' How and when do I apply float function and integer for the length?
# float idn't work this way as well length = input(float(" "))
def cat_passes(height): #checks if the cat fits the given heights
    return height >= 15 #same question where do I apply float here and integer ? and I don't understand what is the purpose of this function if we already have AVG_CAT_HEIGHT. 
#Will it give us false if there is a taller cat?
space_for_cat  = circle_radius(1001)- circle_radius(1000) * 100 #Why do we multiply it by 100? I also got a negative answer is it normal?
print("Space for the cat equala", space_for_cat)
if cat_passes(space_for_cat):
    print("There is enough room for the cat")
else:
    print("There is not enough room for the cat ")
