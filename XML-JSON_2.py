import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_news_short():
    news = []
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    for item in ET.fromstring(data)[0].findall('item'):
        news_info = {}
        for field in item:
            news_info[field.tag] = field.text
        news.append(news_info)
    return news


def save_json(news):
    json_file = json.dumps(news, ensure_ascii=False).encode('utf8')
    with open("news-full.json", 'wb') as file:
        file.write(json_file)


save_json(get_news_short())