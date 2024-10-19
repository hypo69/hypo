## \file ../src/prestashop/_experiments/suppliers/hb/test_3_lxml_get_site_structure.py
## \file src/prestashop/_experiments/suppliers/hb/test_3_lxml_get_site_structure.py
import requests
import re
import json
from lxml import etree

import header
from header import pprint,  logger

def get_links_with_text(url):
    # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        return {}
    
    # Создаем объект lxml для анализа содержимого страницы
    lxml_tree = etree.HTML(response.text)
    
    # Выполняю поиск ссылок на странице, исключая адрес "https://hbdeadsea.co.il/product-category/allproducts/"
    links = lxml_tree.xpath('//a[@href and starts-with(@href, "https://hbdeadsea.co.il/product-category/") and not(contains(@href, "allproducts/"))]')
    
    # Создаем словарь, где ключ - это ссылка, а значение - текст ссылки
    links_with_text = {link.attrib['href']: link.text.strip() for link in links}
    
    return links_with_text

def recursive_crawl(url, depth):
    if depth == 0:
        return {}
    
    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        # Рекурсивно вызываем функцию для каждой найденной ссылки на указанной глубине
        logger.info(f"dept: {depth}")
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[text] = {
            "text": text,
            "children": child_links
        }
    
    return all_links_with_hierarchy

def save_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def start():
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il/'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 4
    
    # Запускаем сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Сохраняем JSON-файлы для каждого верхнего узла
    for top_node_text, top_node_data in all_links_with_hierarchy.items():
        file_name = f"{top_node_text}.json"
        save_json_file(top_node_data, file_name)

if __name__ == '__main__':
    start()

start()

