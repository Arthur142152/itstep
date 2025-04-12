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

    def getInfo(self):
        currencies = []
        table = self.soup.find('table')
        currency_rows = table.find_all('tr')[1:6]
        for currency_row in currency_rows:
            find = currency_row.find_all('td')
            name = find[0].text.strip()
            buy = find[1].text.strip()
            sell = find[2].text.strip()
            currencies.append({
                'Назва': name,
                'Купівля': buy,
                'Продаж': sell
            })
        return currencies

    def showInfo(self, info):
        for minfin in info:
            print(minfin['Назва'], minfin['Купівля'], minfin['Продаж'])


url = 'https://minfin.com.ua/ua/currency/'
obj = MinfinCurrency(url)
obj.auditSite()

while True:

    info = obj.getInfo()
    obj.showInfo(info)

    print('Виберіть дію:')
    print('1 - Купити')
    print('2 - Продати')
    currencies = {
        '1': 'USD',
        '2': 'EUR',
        '3': 'PLN',
        '4': 'CHF',
        '5': 'GBP'
    }
    answer = input(':')
    if answer == '1':
        print('Виберіть валюту (введіть номер із списку):')
        currency_number = input(':')
        if currency_number in currencies:
            print('Ваша валюта:', currencies[currency_number])
            print('Введіть суму:')
            sum = int(input(':'))
            print('Ваша сума:', sum)
            print('Ви хочете купити:', currencies[currency_number], 'на', sum, 'грн')