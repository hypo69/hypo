## \file ../src/prestashop/_experiments/suppliers/kualastyle/kualastyle_get_site_structure.py
## \file src/prestashop/_experiments/suppliers/kualastyle/kualastyle_get_site_structure.py

import requests
from bs4 import BeautifulSoup
import re

def get_links_with_text(url):
    # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        return {}
    
    # Создаем объект BeautifulSoup для анализа содержимого страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все ссылки на странице
    links = soup.find_all('a', href=True)
    
    # Создаем словарь, где ключ - это ссылка, а значение - текст ссылки
    links_with_text = {link['href']: link.text.strip() for link in links if re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])}
    
    return links_with_text

def recursive_crawl(url, depth):
    if depth == 0:
        return {}
    
    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        # Рекурсивно вызываем функцию для каждой найденной ссылки на указанной глубине
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[link] = {
            "text": text,
            "children": child_links
        }
    
    return all_links_with_hierarchy

def get_site_structure():
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 5
    
    # Запускаем сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Выводим результаты в виде словаря с иерархией
    import json
    print(json.dumps(all_links_with_hierarchy, indent=5, ensure_ascii=False))


if __name__ == '__main__':
    get_site_structure()

get_site_structure())