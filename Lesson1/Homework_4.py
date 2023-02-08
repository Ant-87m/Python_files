# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные новости в БД


import requests
from lxml import html
from datetime import datetime, timedelta
from pymongo import MongoClient


def to_date(date: list):
    date = date[0].split(' ')
    today = datetime.now().date()
    yesterday = (today - timedelta(days=1))
    if len(date) == 1:
        current_date = f'{today:%d.%m.%Y} {date[0]}'
    else:
        current_date = f'{yesterday:%d.%m.%Y} {date[-1]}'
    return current_date


def fill_mongo(data, data_base):
    contains = data_base.news.find_one({'link': data['link']})
    if not contains:
        data_base.news.insert_one(data)
        print('[INFO] add news')


if __name__ == '__main__':

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"}
    response = requests.get('https://yandex.ru/news/', headers=headers)

    client = MongoClient('localhost', 27017)
    db = client['news_data']

    dom = html.fromstring(response.text)

    items = dom.xpath('//section[@aria-labelledby]//div[contains(@class, "mg-card ")]')

    for item in items:
        root = response.url
        title = ''.join(item.xpath(".//h2[@class]/a/text()")).replace('\xa0', ' ')
        link = item.xpath(".//h2[@class]/a/@href")[0]
        date = to_date(item.xpath(".//*[@class='mg-card-source__time']/text()"))
        news_info = dict(root=root, title=title, link=link, date=date)
        fill_mongo(data=news_info, data_base=db)
