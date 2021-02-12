def run(value):
    value = value + 1
    print("Value inside this function: "+ str(value))

run(2)  #we get three by adding 1 to this function
#print("Value outside this function "+ str(value))
def second_run():
    print(value)
run(2)
second_run()
