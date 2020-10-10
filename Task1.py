temp = float(input("Welcome to the temperature converter! Please enter a temperature and its units: "))
units = input(" ")
if units=='F':
    temp_f=(9/5) * temp + 32
    print(temp_f)
else :
    temp_c = (5/9) * temp - 32
    print(temp_c)
