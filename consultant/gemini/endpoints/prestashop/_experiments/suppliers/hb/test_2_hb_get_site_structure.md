## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/hb/test_2_hb_get_site_structure.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers.hb """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers.hb """
import requests
from bs4 import BeautifulSoup
import re
import json
import logging

# Важно!  Установите уровень логгирования для вашей программы.
# Этот блок делает вывод логов в консоль.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def jprint(obj):
    #  Функция для красивой печати объекта
    text = json.dumps(obj.json(), indent=4)
    return text

def get_links_with_text(url):
    logger.info(f"URL {url}")
    try:
        response = requests.get(url, timeout=10)  # Добавили таймаут
        response.raise_for_status() # Обрабатывает ошибки ответа (4xx или 5xx)
        logger.info(f"response status code: {response.status_code}")
        logger.info(f"response content length: {len(response.content)}") # Добавлена информация о длине ответа
        
        if response.status_code != 200:
            logger.error(f"Ошибка при запросе {url}. Код статуса: {response.status_code}.")
            return {}

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        links_with_text = {link['href']: link.text.strip() for link in links if re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])}
        logger.info(f"links: {links_with_text}")
        return links_with_text
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе {url}: {e}")
        return {}
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
        return {}

def recursive_crawl(url, depth):
    if depth <= 0:
        return {}
    
    links_with_text = get_links_with_text(url)
    if not links_with_text:
        return {}  # Возвращаем пустой словарь, если get_links_with_text вернул пустой

    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[text] = {
            "text": text,
            "children": child_links
        }
    return all_links_with_hierarchy


def save_json_file(data, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        logger.info(f"Файл {file_name} сохранён успешно.")
    except Exception as e:
        logger.error(f"Ошибка при сохранении файла {file_name}: {e}")


def start():
    starting_url = 'https://hbdeadsea.co.il'
    depth = 4
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    if all_links_with_hierarchy:
        for top_node_text, top_node_data in all_links_with_hierarchy.items():
            file_name = f"{top_node_text.replace(' ', '_').replace('/', '_')}.json"  # обработка пробелов и /
            save_json_file(top_node_data, file_name)

if __name__ == '__main__':
    start()

```

**Изменения и объяснения:**

* **Обработка ошибок:** Добавлена обработка исключений `requests.exceptions.RequestException` и общих исключений. Это критически важно, чтобы скрипт не падал при проблемах с подключением к сайту или другими ошибками.  Теперь скрипт выводит подробные сообщения об ошибках, что помогает в отладке.
* **Таймаут запроса:** Добавлена функция `timeout=10` в `requests.get()`. Это предотвращает зависание программы при медленном ответе сайта.
* **Проверка статуса ответа:** `response.raise_for_status()`  необходимо для того, чтобы обрабатывать ошибки статуса ответа.
* **Проверка пустого результата:**  Проверка `if not links_with_text: return {}`  в функции `recursive_crawl`  важна, чтобы избежать ошибок, если  `get_links_with_text` вернула пустой словарь.
* **Логирование:** Логирование улучшено, чтобы выводить больше информации, включая коды ответов, длину ответа и сообщения об ошибках.
* **Обработка названий файлов:** Функция `save_json_file` исправлена для обработки названий файлов, так чтобы не было проблем с именами файлов, содержащими пробелы или символы '/', что предотвращает ошибки при сохранении.
* **Временные метки:**  Логирование теперь включает временные метки, что улучшает отслеживание процесса.
* **Функция `jprint`:** Добавлена функция `jprint(obj)`, которая позволяет более наглядно вывести объект в отладке, избегая проблем с выводом больших объектов (как объектов `response`).

**Как запустить:**

1.  Убедитесь, что у вас установлены необходимые библиотеки:
    ```bash
    pip install requests beautifulsoup4 json
    ```
2.  Замените `venv/Scripts/python.exe` на правильный путь к исполняемому файлу Python вашей виртуальной среды.
3.  Запустите скрипт из командной строки:
    ```bash
    python test_2_hb_get_site_structure.py
    ```


Этот улучшенный код более устойчив к ошибкам и предоставляет более полезную информацию для отладки.  Он обрабатывает различные потенциальные проблемы и выводит более информативные сообщения, облегчая диагностику проблем. Не забывайте проверять логи.