## \file ../src/prestashop/_experiments/suppliers/hb/test_4_lxml_get_unique_links.py
## \file src/prestashop/_experiments/suppliers/hb/test_4_lxml_get_unique_links.py
import requests
import re
import json
from lxml import etree

import header
from header import pprint,  logger

def get_unique_links(url):
    # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        return set(), set()
    
    # Создаем объект lxml для анализа содержимого страницы
    lxml_tree = etree.HTML(response.text)
    
    # Выполняю поиск ссылок на странице, исключая адрес "https://hbdeadsea.co.il/product-category/allproducts/"
    links = lxml_tree.xpath('//a[@href and starts-with(@href, "https://hbdeadsea.co.il/product-category/") and not(contains(@href, "allproducts/"))]')
    
    unique_links = set()
    duplicate_links = set()
    for link in links:
        href = link.attrib['href']
        if href not in unique_links:
            unique_links.add(href)
        else:
            duplicate_links.add(href)
    
    return unique_links, duplicate_links

def recursive_crawl(url, depth):
    if depth == 0:
        return set(), set()
    


    unique_links, duplicate_links = get_unique_links(url)
    all_unique_links = unique_links.copy()
    all_duplicate_links = duplicate_links.copy()
    
   

    for link in unique_links:
        child_unique_links, child_duplicate_links = recursive_crawl(link, depth - 1)
        all_unique_links.update(child_unique_links)
        all_duplicate_links.update(child_duplicate_links)
        logger.info(f"\t\tUnique links: {len(all_unique_links)}")
        logger.info(f"\t\tDuplicate links: {len(all_unique_links)}")
    
    return all_unique_links, all_duplicate_links

def save_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il/'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 3
    
    # Запускаем сбор ссылок рекурсивно
    all_unique_links, all_duplicate_links = recursive_crawl(starting_url, depth)
    
    # Сохраняем JSON-файл для уникальных ссылок
    unique_links_dict = {link: {"url": link} for link in all_unique_links}
    save_json_file(unique_links_dict, "unique_links.json")
    
    # Сохраняем JSON-файл для повторяющихся ссылок
    duplicate_links_dict = {link: {"url": link} for link in all_duplicate_links}
    save_json_file(duplicate_links_dict, "duplicate_links.json")

