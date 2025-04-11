#шаблон для парсингу
import requests as r
from bs4 import BeautifulSoup as bs
#class Name:
    #def __init__(self,url):
        #self.url =url
        #self.header ={
          #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #}
        #self.soup=None
    #def auditSite(self):
        #response=r.get(self.url,headers=self.header)
        #if response.status_code == 200:
            #self.soup=bs(response.text,'html.parser')
        #else:
            #print('Не вдалося підключитись до сайту')
            #return
    #def getInfo(self):
        #pass
    #def showInfo(self,txt):
        #pass
#url='посилання'
#obj=Name(url)
#obj.auditSite()
#txt=obj.getInfo()
#obj.showInfo(txt) if txt else print("жодної інфо не знайдено")
import requests as r
from bs4 import BeautifulSoup as bs
class Eldorado:
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
        tablet=[]
        tabletTag=self.soup.find_all('article',class_='OfferTilestyled__StyledArticle-sc-1lnuwp1-1 iBdafB')
        if not tabletTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return tablet
        for i in tabletTag[0:10]:
            nameTab=i.find('span',class_='ui-library-body2Medium-fa40 GoodsDescriptionstyled__StyledTypography-sc-1c1eyhs-1 bDXGew')
            name=nameTab.text.strip() if nameTab else 'назва відсутня'
            priceTab=i.find('span',class_='ui-library-subtitle1Bold-399e')
            price = priceTab.text.strip() if priceTab else 'ціна відсутня'
            tablet.append({
                'Назва':name,
                'Ціна':price,

            })
        return tablet
    def showInfo(self,txt):
        print('№\t','Назва','\t'*15,'Ціна')
        print('-'*80)
        num = 1
        for i in txt:
            print(num,i['Назва'],i['Ціна'])
            num += 1

url='https://eldorado.ua/uk/tablet_pc/c1039006/'
obj=Eldorado(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print("жодної інфо не знайдено")

