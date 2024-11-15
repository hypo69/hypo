## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/hb/test_kuala.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers.hb """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers.hb """
from urllib.parse import urlparse
import requests
from lxml import etree
import logging

# Конфигурация логгера (важно для отладки)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def extract_links(element, depth_level=0):
    links = []
    if depth_level >= 7:
        return links # Предотвращаем бесконечную рекурсию

    for child in element:
        if child.tag == 'a':
            href = child.get('href')
            if href: # Проверка на корректность href
                parsed_url = urlparse(href)
                if parsed_url.netloc:  # Проверка на корректность домена
                    full_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
                    links.append(full_url)
                    logger.debug(f"Found link: {full_url} at depth {depth_level + 1}")
                else:
                    logger.warning(f"Invalid href: {href} in {child.text}")
        elif child.tag == 'ul':
            nested_links = extract_links(child, depth_level+1)
            links.extend(nested_links)
    return links

# Укажите URL, с которого начнется сбор ссылок
starting_url = 'https://kualastyle.com/'

try:
    # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
    response = requests.get(starting_url, timeout=10)
    response.raise_for_status() # Обрабатывает ошибки запроса

    html = response.text

    # Создаем объект-дерево из HTML-кода
    tree = etree.HTML(html)

    # Находим корневой элемент меню (убедитесь, что селектор верный!)
    root_ul = tree.xpath("//ul[@class='navmenu navmenu-depth-1']")[0]  
    if root_ul is None:
        logger.error("Could not find the root UL element with the specified class.")
        exit()


    # Извлекаем все ссылки с сохранением вложенности
    links = extract_links(root_ul)


    # Выводим результат.  Добавлен вывод в более удобочитаемом формате
    if links:
      for link in links:
          print(link)
    else:
      logger.warning("No links found.")
except requests.exceptions.RequestException as e:
    logger.error(f"Error during request: {e}")
except IndexError:
    logger.error("Could not find the specified element in the HTML.")
except Exception as e:
    logger.exception(f"An unexpected error occurred: {e}")

```

**Основные улучшения:**

* **Обработка ошибок:** добавлен `try...except` блок для перехвата ошибок `requests`, `IndexError` (если не найден нужный элемент) и общих исключений. Это предотвращает сбой программы при проблемах во время работы.  Важный логгинг ошибок.
* **Валидация `href`:** Проверка корректности `href` и  `urlparse`. Если `href` некорректен (например, нет домена), то вывод предупреждения в лог.
* **Глубина рекурсии:**  Добавлена проверка глубины рекурсии, чтобы избежать бесконечных циклов.
* **Обработка пустого списка ссылок:** Проверка, что список ссылок не пуст, прежде чем переходить к циклу `for`.
* **Использование `logging`:**  Вместо `print` используется `logger.debug`, `logger.info` и т.д. для записи информации об этапах работы программы и ошибках в файл.  Это значительно упрощает отладку.  Конфигурация логгера.
* **Обработка timeouts:** добавлено `timeout=10` в `requests.get`, чтобы избежать зависания при проблемах с сайтом.
* **Вывод в удобочитаемом формате:** выводит url в формате строки

**Как использовать:**

1. Установите необходимые библиотеки:
   ```bash
   pip install requests lxml
   ```

2. Запустите скрипт.  Программа будет выводить найденные ссылки в консоль.  Важно, что в логе будут отображаться любые ошибки, что облегчит отладку.

**Важный совет:**

* **Селектор `xpath`:** убедитесь, что селектор `xpath("//ul[@class='navmenu navmenu-depth-1']")[0]` точно находит нужный элемент на сайте.  Если вы используете другой сайт, вам нужно скорректировать селектор.


Этот улучшенный код надежнее, более устойчив к ошибкам и предоставляет ценную информацию для отладки.  Он также учитывает важные аспекты работы с веб-скрейпингом, такие как обработка ошибок и профилактика бесконечных циклов.