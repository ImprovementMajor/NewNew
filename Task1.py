temp = float(input("Welcome to the temperature converter! Please enter a temperature and its units: "))

if units == F :
    print(temp_f)
else :
    print(temp_c)

temp_f = (9/5) * temp_c + 32
print(temp_f)

temp_c = temp_f - 32 * 5/9
print(temp_c)
