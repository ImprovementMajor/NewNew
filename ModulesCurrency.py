import urllib.request #sends requests to certain web pages
import json #got it to transform a string into the dictionary

url = "http://data.fixer.io/api/latest?access_key=53d609ad140b77fa8bfaa08e912e13d6" #my key

raw_data = urllib.request.urlopen(url).read() #getting data based on the link and reading it
parsed_data = json.loads(raw_data) #turning raw data into dictionary if json format only

if not parsed_data['success']: exit("Не удалось загрузить курсы валют :(") #Haven't seen if not before
#Not sure how does success key work?
print("Добро пожаловать! Курсы валют были обновлены", parsed_data['date'])

rates = parsed_data['rates'] #What does it do? what does coefficients of currencies mean? It gets us the keys?

eur = float(input("Введите сумму в евро: ")) #user input
while True:
    currency = input("Введите код валюты для конвертации: ")
    if currency in rates: break
    print("К сожалению, мы не поддерживаем такую валюту. Попробуйте ещё раз.")

print("Результат: ", eur * rates[currency])
