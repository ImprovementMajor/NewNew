import math
def get_user_input():
    a = input("Please enter a quadratic coefficients: ")
    b = input("Please enter b  quadratic coefficients: ")
    c - input("Please enter  c quadratic coefficients: ") 
    return (int(a), int(b), int(c)) #tuple

def print_quad_solutions(coefficients):
    a= coefficients[0]
    b = coefficients[1]
    c=coefficients[2]
    print(a, b, c)
    if a == 0:
        print("Function with a = 0 isn't a quadratic function")
        return
    under_sqrt = (b**2) - 4*a*c
    if under_sqrt < 0:
        print("This quadratic function has no real roots")
        return
    root_1 = (-b + math.sqrt(under_sqrt))/(2*a)
    root_2 = (-b - math.sqrt(under_sqrt))/(2*a)
    print(root_1, root_2)


print_quad_solutions(get_user_input())
