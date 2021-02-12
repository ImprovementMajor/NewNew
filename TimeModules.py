import time
number=int(input("Please enter a number: ")) #why do we need a number? 
result = 1
start_time =time.time() #Why do we need this part  time.time() Is it a Unix number from 1970-s?
print("Starting time", start_time)
for i in range(1, number +1): result *= i
end_time = time.time()
print("End time is ", end_time)
print("Time spent", end_time - start_time)
print("and the result is: ", result)
