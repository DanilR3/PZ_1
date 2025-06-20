import json
import requests
import matplotlib.pyplot as plt

#1. Отримуємо курси євро за тиждень
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json"
nbu_response = requests.get(url)


if nbu_response.status_code == 200:
    converted_response = json.loads(nbu_response.content)

    print("Курс євро за тиждень:")
    for item in converted_response:
        date = item['exchangedate']
        rate = item['rate']
        print(f"Дата: {date}, Курс: {rate} грн")

    #2. Графік зміни курсу
    
    dates = [item['exchangedate'] for item in converted_response]
    rates = [item['rate'] for item in converted_response]

    
    plt.figure(figsize=(10, 5))  
    plt.plot(dates, rates, marker='o', linestyle='-', color='b')

    
    plt.title('Зміна курсу євро за тиждень')
    plt.xlabel('Дата')
    plt.ylabel('Курс (грн)')
    plt.grid(True)  
    plt.show()

else:
    print("Помилка. Код помилки:", nbu_response.status_code)