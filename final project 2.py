import requests as r
from bs4 import BeautifulSoup as bs

class MinfinCurrency:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
        else:
            print('Помилка з’єднання')

    def cleanCurrency(self, currency_str):
        # Очищаємо значення від зайвих символів (наприклад, ком, пробіли)
        return float(currency_str.replace(",", ".").strip() if currency_str else 0)

    def getInfo(self):
        currencies = []
        table = self.soup.find('table')
        currency_rows = table.find_all('tr')[1:6]  # Перша п'ятірка валют
        for currency_row in currency_rows:
            find = currency_row.find_all('td')
            name = find[0].text.strip()
            buy = self.cleanCurrency(find[1].text.strip())  # Очищаємо курс купівлі
            sell = self.cleanCurrency(find[2].text.strip())  # Очищаємо курс продажу
            currencies.append({
                'Назва': name,
                'Купівля': buy,
                'Продаж': sell
            })
        return currencies

    def showInfo(self, info):
        for idx, minfin in enumerate(info, start=1):
            print(f"{idx}. {minfin['Назва']} - Купівля: {minfin['Купівля']} Продаж: {minfin['Продаж']}")

    def convertCurrency(self, action, currency, amount):
        if action == 'купити':
            result = amount * currency['Купівля']
        elif action == 'продати':
            result = amount * currency['Продаж']
        return result


# Створення об'єкта та отримання даних з сайту
url = 'https://minfin.com.ua/ua/currency/'
obj = MinfinCurrency(url)
obj.auditSite()

while True:
    info = obj.getInfo()
    obj.showInfo(info)

    # Запит користувача на вибір операції
    action = input("Що ви хочете зробити? (купити/продати): ").lower()

    if action not in ['купити', 'продати']:
        print("Введіть правильну дію (купити або продати).")
        continue

    # Вибір валюти
    try:
        currency_choice = int(input("Оберіть валюту за номером (1-5): "))
        if currency_choice < 1 or currency_choice > 5:
            raise ValueError
    except ValueError:
        print("Невірний вибір, будь ласка, оберіть номер валюти від 1 до 5.")
        continue

    # Вибір суми
    try:
        amount = float(input("Введіть кількість грошей для конвертації: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Будь ласка, введіть коректну кількість грошей.")
        continue

    # Виконання конвертації
    selected_currency = info[currency_choice - 1]
    result = obj.convertCurrency(action, selected_currency, amount)

    # Виведення результату
    print(f"Результат: {amount} одиниць валюти = {result:.2f} UAH за операцією {action}.")

    # Запит користувача на продовження
    print("Бажаєте завершити програму чи показати валюту ще раз?")
    print("1. Завершити")
    print("2. Показати валюти ще раз")

    choice = input("> ")

    if choice == '1':
        print("Програма завершена.")
        break
    elif choice == '2':
        continue
    else:
        print("Введіть коректне значення (1 або 2).")