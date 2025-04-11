import requests as r
from bs4 import BeautifulSoup as bs

class BookScraper:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            self.soup = bs(response.text, 'html.parser')
        else:
            print('Не вдалося підключитись до сайту')
            return

    def getBooks(self):
        books = []
        bookTags = self.soup.find_all('article', class_='product_pod')[:8]
        for book in bookTags:
            titleTag = book.h3.a
            title = titleTag['title'] if titleTag else 'Назва відсутня'

            priceTag = book.find('p', class_='price_color')
            price = priceTag.text.replace('$', '').strip() if priceTag else 'Ціна відсутня'

            ratingTag = book.p
            rating = ratingTag['class'][1] if ratingTag else 'Рейтинг відсутній'

            books.append({
                'Назва': title,
                'Ціна': price,
                'Рейтинг': rating,
            })
        return books


url = 'http://books.toscrape.com'
parser = BookScraper(url)
parser.auditSite()
books = parser.getBooks()


print(books) if books else print("Жодної інформації не знайдено")
