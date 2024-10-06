## \file ../src/prestashop/_experiments/suppliers/hb/test_5_lxml_get_unique_links_DFS_algoryphm_kuala.py
## \file src/prestashop/_experiments/suppliers/hb/test_5_lxml_get_unique_links_DFS_algoryphm_kuala.py
""" FROM openAI:
Если вам необходимо углубиться до глубины depth = 5, то вам понадобится оптимизировать рекурсивный алгоритм,
чтобы избежать переполнения стека вызовов и ускорить процесс сбора ссылок.

Вместо рекурсивного подхода можно использовать итеративный (нерекурсивный) алгоритм для обхода и сбора ссылок. 
Одним из наиболее распространенных алгоритмов обхода в глубину (DFS) является алгоритм с использованием стека.


В этом коде мы используем стек для хранения URL'ов, которые нужно обработать, и обходим сайт 
с использованием итеративного подхода вместо рекурсивного. При этом глубина обхода ограничивается заданным значением depth.

Теперь вы можете углубиться до глубины depth = 5 без опасения переполнения стека вызовов.
"""


import header
from header import pprint,  logger
import requests
import re
import json
from lxml import etree



def get_unique_links(response, visited_links):
    url = response.url
    if url in visited_links:
        return set()

    # Отмечаем URL как просмотренный
    visited_links.add(url)

    # Создаем объект lxml для анализа содержимого страницы
    lxml_tree = etree.HTML(response.text)

    # Выполняю поиск ссылок на странице, исключая адрес "https://hbdeadsea.co.il/product-category/allproducts/"
    links = lxml_tree.xpath(
        '//ul[contains(@aria-label,"Main menu")]//a'
    )

    unique_links = set()
    for link in links:
        href = link.attrib['href']
        try:
            link_text = link.attrib['title'].strip()

        except Exception:
            try:
                link_text = link.text
                if not link_text or link_text == '\n':
                    continue
            except Exception as ex:
                logger.error(f"{ex}\n{link}")
                continue
        if href not in unique_links:
            unique_links.add((href, link_text))

    return unique_links

def recursive_crawl(response, depth, visited_links, starting_url, link_text=None):
    if depth == 0:
        return {}

    logger.debug(f"depth: {depth}")
    unique_links = get_unique_links(response, visited_links)
    current_node_data = {}

    for link_data in unique_links:
        link, link_text = link_data
        link_hierarchy = link.replace(starting_url, "").rstrip("/").split("/")
        current_dict = current_node_data
        for part in link_hierarchy:
            current_dict = current_dict.setdefault(part, {})
        #current_dict["children"] = recursive_crawl(response, depth - 1, visited_links, starting_url, link_text)
        current_dict["children"]: dict = dict(recursive_crawl(response, depth - 1, visited_links, starting_url, link_text))
        current_dict["url"] = link  # Добавляем URL в текущий узел
        current_dict["name"] = link_text or get_link_name(response, link)  # Добавляем текст ссылки в текущий узел
        current_dict["condition"] = "new",
        current_dict["presta_categories"]: dict = {"default_category":{"11111": "presta_category"},"additional_categories": [ "" ]}

    return current_node_data

def get_link_name(response, url):
    # Воспользуемся объектом response, чтобы избежать дополнительного запроса
    lxml_tree = etree.HTML(response.text)

    # Выполняю поиск текста ссылки на странице
    link_text = lxml_tree.xpath('//a[@href="%s"]/text()' % url)
    return link_text[0].strip() if link_text else ""

def save_json_files(data, parent_key, depth):
    for key, value in data.items():
        #file_name = f"{parent_key}_{key}_depth{depth}.json"
        file_name = f"{key}.json"
        save_json_file(value, file_name)

def save_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://kualastyle.com/'

    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 7

    # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
    response = requests.get(starting_url)

    # Проверяем успешность запроса
    if response.status_code != 200 and response.status_code != 404:
        print("Ошибка при получении содержимого страницы.")
        exit()

    # Список для отслеживания просмотренных ссылок
    visited_links = set()

    # Запускаем сбор ссылок рекурсивно
    top_level_data = recursive_crawl(response, depth, visited_links, starting_url)

    # Сохраняем каждый узел верхнего уровня в отдельном файле
    for key, value in top_level_data.items():
        save_json_files(value, key, depth)

