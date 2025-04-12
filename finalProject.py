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
        res = r.get(self.url, headers=self.header)
        if res.status_code == 200:
            self.soup = bs(res.text, 'html.parser')
        else:
            print('Помилка з’єднання')

    def getInfo(self):
        currencies = []
        table = self.soup.find('table')
        rows = table.find_all('tr')[1:6]
        for row in rows:
            cols = row.find_all('td')
            name = cols[0].text.strip()
            buy = cols[1].text.strip()
            sell = cols[2].text.strip()
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
info = obj.getInfo()
obj.showInfo(info)