def run():
    value = 1 # 2
    inner_run() # 3
    print("Значение value внутри функции run(): " + str(value)) # 6

def inner_run():
    value = 100 # 4
    print("Значение value внутри функции inner_run(): " + str(value)) # 5

run() # 1
