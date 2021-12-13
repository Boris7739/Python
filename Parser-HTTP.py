import requests
from bs4 import BeautifulSoup
import csv
file = 'cards2.csv'
HOST = 'https://www.avito.ru'
URL = 'https://www.avito.ru/saratov/avtomobili/toyota/camry-ASgBAgICAkTgtg20mSjitg3UoCg?cd=1&p=1&radius=200'
HEADERS = {'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
           }


def get_html(URL, params = None):
    r = requests.get(URL, headers= HEADERS, params= params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='iva-item-body-NPl6W')

    cards = []
    for item in items:
        cards.append({
            'title': item.find('div', class_='iva-item-titleStep-2bjuh').find('a').get_text(),
            'link_product': HOST + item.find('div', class_='iva-item-titleStep-2bjuh').find('a').get('href'),
            'car_price': item.find('span', class_='price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo').get_text(strip=True) + ' RUB',
            'discript': item.find('div', class_='iva-item-text-2xkfp text-text-1PdBw text-size-s-1PUdo').get_text(strip=True)

        })
    return cards

def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Заголовок', 'Ссылка на карту', 'Банк', 'Информация'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['car_price'], item['discript']])


def parse():
    #URL = URL.strip()
    html = get_html(URL)
    pages_count = input('Enter count of page for parsing: ')
    pages_count = int(pages_count.strip())
    if html.status_code == 200:
        cards = []
        for page in range(1, pages_count + 1):
            print(f'parsing {page} / {pages_count}')
            html = get_html(URL, params={'p': page})
            cards.extend(get_content(html.text))
            save_file(cards, file)
        print(cards)
    else:
        print('Error')
parse()