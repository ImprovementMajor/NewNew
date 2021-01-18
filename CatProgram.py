import math
print("please enter the length " )
length = float(input(" ")) #float goes first               This code still doesn't work, when I enter 0 for length it still says there is enough
AVG_CAT_HEIGHT = 15                                         #space for the cat
def circle_radius(length):
    return length/(2 * 3.14)
print(float(circle_radius)) #TypeError: float() argument must be a string or a number, not 'function' #How and when do I apply float function and integer for the length?
# float idn't work this way as well length = input(float(" "))
#def cat_passes(height): #Cat passes if height is equal or bigger than the average cat height
    #return height >= AVG_CAT_HEIGHT #Yes or no #same question where do I apply float here and integer ? and I don't understand what is the purpose of this function if we already have AVG_CAT_HEIGHT.
#Will it give us false if there is a taller cat?
#space_for_cat  = (circle_radius(length+1)- circle_radius(length)) * 100 #meters circle_radius(length + 1) - circle_radius(length)
#print("Space for the cat equala", space_for_cat)
#if cat_passes(space_for_cat): #> average height
    #print("There is enough room for the cat")
#else:
    #print("There is not enough room for the cat ")
