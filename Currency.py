import urllib.request #sends requests to certain web pages
import json #got it to transform a string into the dictionary

url = "http://data.fixer.io/api/latest?access_key=53d609ad140b77fa8bfaa08e912e13d6" #my key

raw_data = urllib.request.urlopen(url).read() #getting data based on the link and reading it, it's red, why it d-t work?
parsed_data = json.loads(raw_data) #turning raw data into dictionary if json format only

if not parsed_data['success']: exit("Не удалось загрузить курсы валют :(") #Haven't seen if not before #success != True
#Not sure how does success key work? если парст дата не саксес то выходитб Parsed data means data transformed from what to what?
print("Добро пожаловать! Курсы валют были обновлены", parsed_data['date'])

rates = parsed_data['rates'] # we get rates and success from the raw data, right? where success is a key
while True:
    eur = float(input("Введите сумму в евро: ")) #user input
    while True:
        currency = input("Введите код валюты для конвертации: ")
        if currency in rates: break #why do we break here and then print "К сожалению, мы не поддерживаем такую валюту. Попробуйте ещё раз
    # Shouldn't we print the correct result here print("Результат: ", eur * rates[currency])?

    #Homework part can I write it this way?
    #currency = input("Введите код валюты для конвертации: ")
    # if currency in rates:
    #    print("Результат: ", eur * rates[currency])
    #    print("Would you like to convert currency again?")
    #       user_input= input("Please enter yes or no")
    #           if user_input == yes:
    #               eur = float(input("Введите сумму в евро: "))
    #               while True:
    #               currency = input("Введите код валюты для конвертации: ")
    #                   if currency in rates:
    #                       print(print("Результат: ", eur * rates[currency]))
    #                   else: break
    # else:
    #    print("К сожалению, мы не поддерживаем такую валюту. Попробуйте ещё раз.")

        print("К сожалению, мы не поддерживаем такую валюту. Попробуйте ещё раз.")

    print("Результат: ", eur * rates[currency])
    print("Would you like to convert currency again?")
    user_input= input("Please enter yes or no")
    if user_input == "no": break
