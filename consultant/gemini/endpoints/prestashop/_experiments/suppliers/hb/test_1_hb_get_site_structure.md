## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/hb/test_1_hb_get_site_structure.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers.hb """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers.hb """

import requests
from bs4 import BeautifulSoup
import re


def get_links_with_text(url):
    """
    Получает ссылки со страницами и их тексты.

    Args:
        url: URL страницы.

    Returns:
        Словарь, где ключ - ссылка, а значение - текст ссылки.
        Возвращает пустой словарь, если запрос не удался.
    """
    try:
        response = requests.get(url, timeout=10)  # Добавлено ограничение на время ожидания
        response.raise_for_status()  # Обработка ошибок запроса
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {url}: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    links_with_text = {
        link['href']: link.text.strip()
        for link in links
        if link['href'] and re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])
    }
    
    return links_with_text


def recursive_crawl(url, depth):
    """
    Рекурсивно собирает ссылки на указанной глубине.

    Args:
        url: Стартовая ссылка.
        depth: Глубина рекурсии.

    Returns:
        Словарь с иерархией ссылок.
    """
    if depth <= 0:
        return {}  # Базовый случай: глубина достигнута, возвращаем пустой словарь
    
    links_with_text = get_links_with_text(url)
    if not links_with_text:
        return {}  #Если нет ссылок, прекращаем рекурсию

    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[link] = {
            "text": text,
            "children": child_links
        }
    return all_links_with_hierarchy


def get_site_structure():
    starting_url = 'https://hbdeadsea.co.il'
    depth = 3
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    try:
        print(json.dumps(all_links_with_hierarchy, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Ошибка при выводе JSON: {e}")


import json

if __name__ == '__main__':
    get_site_structure()
```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка `requests.exceptions.RequestException` для перехвата ошибок при запросе к URL.  Это предотвращает сбой программы при проблемах с подключением.  Также добавлена проверка `response.raise_for_status()` для обработки ошибок HTTP-статусов (например, 404).  При ошибке возвращается пустой словарь.
* **Ограничение времени запроса:** Добавлено `timeout=10` к `requests.get`, чтобы предотвратить зависание программы при медленном или некорректном ответе сервера.
* **Проверка существования ссылки:** Проверка `link['href']` в цикле для предотвращения ошибок, если href отсутствует.
* **Обработка пустого словаря:**  Функция `recursive_crawl` проверяет, не пустой ли полученный словарь `links_with_text`.  Если он пустой (т.е. нет подходящих ссылок на странице), рекурсия завершается.  Этот шаг важен для предотвращения бесконечной рекурсии.
* **Базовый случай:** добавлен базовый случай в `recursive_crawl`, где рекурсия прекращается, когда глубина достигла нуля.
* **Обработка ошибок JSON:** Обёртка `try...except` вокруг `print(json.dumps(...))` чтобы предотвратить остановку программы при ошибке форматирования JSON.
* **Улучшенная читаемость:**  Добавлены docstrings для функций, что улучшает понимание их работы.

**Как использовать:**

Запустите этот код. Он выведет иерархию ссылок в формате JSON в консоль.


**Важные замечания:**

* **Время выполнения:**  Обработка глубоких страниц может занять много времени.  Рассмотрите возможность ограничения глубины рекурсии, особенно если сайт имеет сложную структуру.
* **Правила роботов:** Убедитесь, что ваш скрипт не нарушает правила роботов сайта `hbdeadsea.co.il`.  Необходимо быть аккуратным и следить за частотой запросов и нагрузкой на сервер.
* **Обработка HTTP кодов:**  По возможности, обрабатывайте все HTTP коды ответа (например, 403, 500, 429). Это позволит вам получить более полную картину состояния веб-сайта.
* **Дополнительно:**  Рассмотрите возможность использования библиотеки `aiohttp` для асинхронных запросов, чтобы увеличить скорость сканирования в многопоточном режиме (при условии, что это разрешено правилами робота сайта).

Этот улучшенный код более надежен и устойчив к различным проблемам, которые могут возникнуть при парсинге веб-страниц. Remember to respect the website's robots.txt and rate limits.