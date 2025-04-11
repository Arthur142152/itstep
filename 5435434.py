import requests as r
from bs4 import BeautifulSoup as bs
class Coinmarket:
    def __init__(self,url):
        self.url =url
        self.header ={
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response=r.get(self.url,headers=self.header)
        if response.status_code == 200:
            self.soup=bs(response.text,'html.parser')
        else:
            print('Не вдалося підключитись до сайту')
            return
    def getInfo(self):
        coin=[]
        coinTag=self.soup.find_all('article',class_='OfferTilestyled__StyledArticle-sc-1lnuwp1-1 iBdafB')
        if not coinTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return coin
        for i in coinTag[0:5]:
            nameTab=i.find('span',class_='ui-library-body2Medium-fa40 GoodsDescriptionstyled__StyledTypography-sc-1c1eyhs-1 bDXGew')
            name=nameTab.text.strip() if nameTab else 'назва відсутня'
            priceTab=i.find('span',class_='ui-library-subtitle1Bold-399e')
            price = priceTab.text.strip() if priceTab else 'ціна відсутня'
            coin.append({
                'Назва':name,
                'Ціна':price,

            })
        return coin
    def showInfo(self,txt):
        print('№\t','Назва','\t'*15,'Ціна')
        print('-'*80)
        num = 1
        for i in txt:
            print(num,i['Назва'],i['Ціна'])
            num += 1

url='https://coinmarketcap.com/'
obj=Coinmarket(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print("жодної інфо не знайдено")