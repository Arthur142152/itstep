import requests as r
from bs4 import BeautifulSoup as bs


class CoinMarketCap:
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
            print('Не вдалося підключитись до сайту')
            return

    def getInfo(self):
        coins = []
        coinTags = self.soup.find('tbody')
        if not coinTags:
            print('Не вдалося знайти необхідний тег/атрибут')
            return coins
        info=coinTags.find_all('tr')
        for coin in info[:5]:
            nameTab = coin.find('p', class_='sc-65e7f566-0 iPbTJf coin-item-name')
            name = nameTab.text.strip() if nameTab else 'Назва відсутня'
            priceTab = coin.find('div', class_='sc-142c02c-0 lmjbLF')
            price = priceTab.text.strip() if priceTab else 'Ціна відсутня'
            coins.append({
                'Назва': name,
                'Ціна': price,
            })
        return coins

    def showInfo(self, txt):
        print('№\t', 'Назва', '\t' * 15, 'Ціна')
        print('-' * 80)
        num = 1
        for coin in txt:
            print(num, coin['Назва'], coin['Ціна'])
            num += 1


url = 'https://coinmarketcap.com/'
obj = CoinMarketCap(url)
obj.auditSite()
txt = obj.getInfo()
obj.showInfo(txt) if txt else print("Жодної інформації не знайдено")