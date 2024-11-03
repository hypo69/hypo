## \file ../src/prestashop/_experiments/suppliers/hb/test_kuala.py
## \file src/prestashop/_experiments/suppliers/hb/test_kuala.py
from urllib import response
import header
from header import pprint,  logger
import requests
import re
import json
from lxml import etree

def extract_links(element):
    links = []

    for child in element:
        if child.tag == 'a':
            href = child.get('href')
            links.append(href)
        elif child.tag == 'ul':
            nested_links = extract_links(child)
            links.extend(nested_links)

    return links

# Здесь предполагается, что у вас уже есть HTML-код страницы.
# Замените переменную 'html' на HTML-код или загрузите его с помощью requests или другого метода.


# Укажите URL, с которого начнется сбор ссылок
starting_url = 'https://kualastyle.com/'

# Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
depth = 7

# Отправляем GET-запрос к указанному URL и получаем содержимое страницы
response = requests.get(starting_url)

html = response.text
# Создаем объект-дерево из HTML-кода
tree = etree.HTML(html)

# Находим корневой элемент меню
root_ul = tree.xpath("//ul[@class='navmenu navmenu-depth-1']")[0]

# Извлекаем все ссылки с сохранением вложенности
links = extract_links(root_ul)

# Выводим результат
for link in links:
    print



# Для получения URL-ов с доменом и протоколом (например, "https://example.com/some-page"):
# Вам нужно добавить этот код после получения 'href' в функции extract_links
# url_parsed = urlparse(href)
# full_url = f"{url_parsed.scheme}://{url_parsed.netloc}{url_parsed.path}"
# links.append(full_url)

