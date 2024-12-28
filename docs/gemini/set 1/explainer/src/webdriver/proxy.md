# <input code>

```python
## \file /src/webdriver/proxy.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с прокси
=========================================================================================

Этот модуль определяет функции для загрузки и парсинга списка прокси. 
Загружается текстовый файл с прокси-адресами и распределяется по категориям.

Пример использования
--------------------

.. code-block:: python

    download_proxies_list()
    proxies = parse_proxies()

"""



import re
import requests
from requests.exceptions import ProxyError, RequestException
from pathlib import Path
from typing import Any, Dict, List, Optional
import header
from src import gs
from src.utils.printer import pprint
from src.logger import logger

# URL источника списка прокси
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'

# Путь к файлу для сохранения списка прокси
proxies_list_path: Path = gs.path.src / 'webdriver' / 'proxies.txt'


def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    :param url: URL файла для загрузки.
    :param save_path: Путь для сохранения загруженного файла.
    :return: Успешность выполнения операции.
    """
    try:
        # Отправка запроса на загрузку файла
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Генерирует исключение для ошибок HTTP

        # Сохранение файла
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        logger.info(f'Файл успешно загружен и сохранён в {save_path}')
        return True
    except Exception as ex:
        logger.error('Ошибка при загрузке файла: ', ex)
        ...
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    :param file_path: Путь к файлу с прокси.
    :return: Словарь с распределёнными по типам прокси.
    """

    download_proxies_list()

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }

    try:
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\\d\\.]+):(\\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    proxies[protocol].append({'protocol':protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
        logger.error('Файл не найден: ', ex)
        ...
    except Exception as ex:
        logger.error('Ошибка при парсинге прокси: ', ex)
        ...

    return proxies


def check_proxy(proxy: dict) -> bool:
    """
    Проверяет работоспособность прокси-сервера.
    
    :param proxy: Словарь с данными прокси (host, port, protocol).
    :return: True, если прокси работает, иначе False.
    """
    try:
        # Попытка сделать запрос через прокси
        response = requests.get("https://httpbin.org/ip", proxies={proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"}, timeout=5)
        # Проверка кода ответа
        if response.status_code == 200:
            logger.info(f"Прокси найден: {proxy['host']}:{proxy['port']}")
            return True
        else:
            logger.warning(f"Прокси не работает: {proxy['host']}:{proxy['port']} (Статус: {response.status_code})", None, False)
            return False
    except (ProxyError, RequestException) as ex:
        logger.warning(f"Ошибка подключения через прокси {proxy['host']}:{proxy['port']} :",ex)
        return False

if __name__ == '__main__':
    # Загрузка списка прокси и парсинг
    if download_proxies_list():
        parsed_proxies = get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')
```

# <algorithm>

**Шаг 1. Загрузка списка прокси:**

* Функция `download_proxies_list` загружает файл прокси из указанного URL (`url`).
* Данные передаются в `requests.get`.
* Ответ (если успешен) сохраняется в `proxies.txt`.
* Функция возвращает `True` в случае успеха, иначе `False`.

**Шаг 2. Парсинг списка прокси:**

* Функция `get_proxies_dict` загружает список прокси из файла `proxies.txt`.
* Использует регулярное выражение (`re.match`) для извлечения протокола, хоста и порта из каждой строки.
* Прокси распределяются по категориям (`http`, `socks4`, `socks5`) в словарь `proxies`.
* Функция возвращает словарь `proxies`.

**Шаг 3. Проверка прокси:**

* Функция `check_proxy` проверяет работоспособность каждого прокси.
* Используется `requests.get` с заданными параметрами прокси.
* Если запрос успешен (код ответа 200), прокси считается работоспособным и возвращает `True`.
* В противном случае возвращается `False`.

**Шаг 4. Обработка результатов:**

* В блоке `if __name__ == '__main__':` происходит загрузка списка прокси и парсинг.
* Выводится информация об обработанном количестве прокси.

**Пример данных:**

Входные данные для `download_proxies_list`:
* `url`: `https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt`
* `save_path`: `gs.path.src / 'webdriver' / 'proxies.txt'`

Входные данные для `get_proxies_dict`:
* `file_path`: `proxies.txt`

**Пример вывода:**

Если прокси успешно загружен и обработан:
`Обработано 100 прокси.`


# <mermaid>

```mermaid
graph TD
    A[download_proxies_list] --> B{Прокси успешно загружен?};
    B -- Да --> C[get_proxies_dict];
    B -- Нет --> D[Обработка ошибок];
    C --> E[Проверка прокси];
    E --> F{Прокси рабочие?};
    F -- Да --> G[Лог успеха];
    F -- Нет --> H[Лог ошибки];
    D --> H;
    subgraph Функции
        A --> |requests.get|
        C --> |open|
        C --> |re.match|
        E --> |requests.get|
    end
    
    subgraph Классы и модули
        A --> |requests|
        C --> |Path|
        C --> |logger|
        C --> |re|
        E --> |requests|
        E --> |logger|
    end
```

# <explanation>

**Импорты:**

* `import re`:  Модуль для работы с регулярными выражениями, используется для парсинга строк с прокси-адресами.
* `import requests`: Библиотека для работы с HTTP-запросами, используется для загрузки файла прокси.
* `from requests.exceptions import ProxyError, RequestException`: Импортируются исключения, связанные с ошибками при работе с прокси.
* `from pathlib import Path`:  Для работы с путями файлов в системе.
* `from typing import Any, Dict, List, Optional`:  Добавляет типы данных для улучшения читабельности и безопасности кода (Any, Dict, List).
* `import header`:  Возможно, файл заголовков, необходимых для обработки.
* `from src import gs`:  Модуль `gs`, скорее всего, содержит конфигурацию или пути, связанные с проектом.
* `from src.utils.printer import pprint`:  Модуль для печати данных.
* `from src.logger import logger`: Модуль для логирования, используемый для вывода сообщений об успехе и ошибках.

**Классы:**

Код не содержит классов, но использует классы из `requests` для работы с запросами и `Path`.

**Функции:**

* `download_proxies_list(url, save_path)`: Загружает файл прокси по указанному URL и сохраняет его в заданный путь. Принимает URL и путь сохранения, возвращает `True` при успехе, `False` в противном случае. Исключения обрабатываются.
* `get_proxies_dict(file_path)`: Парсит файл с прокси-адресами и распределяет их по категориям (HTTP, SOCKS4, SOCKS5). Принимает путь к файлу прокси, возвращает словарь, где ключи – типы прокси, значения – списки словарей с данными прокси. Обрабатывает `FileNotFoundError` и исключения.
* `check_proxy(proxy)`: Проверяет работоспособность прокси-сервера. Принимает словарь с данными прокси, возвращает `True` или `False`. Использует `requests.get` для проверки работоспособности. Обрабатывает ошибки `ProxyError` и `RequestException`.

**Переменные:**

* `url`, `proxies_list_path`:  Строка и объект пути к файлу, хранящие URL и путь к файлу прокси.

**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Обработка исключений (try-except блоки) важна для надежности. Но в некоторых местах есть `...`, что указывает на возможную неполную обработку ошибок. Лучше явно указывать тип ожидаемого исключения.
* **Добавить кэширование:** Загрузка файла прокси может быть медленной. Добавление кэширования (например, используя `lru_cache` из `functools`) может ускорить выполнение, если прокси не меняются часто.
* **Проверка на валидность данных:**  Добавить проверку на корректность формата данных прокси в файле.
* **Модульность:** Возможно, функции `download_proxies_list` и `get_proxies_dict` можно разделить на меньшие, более специализированные функции для лучшей структуры.
* **Параметры таймаута и количества попыток:**  Добавление параметров таймаута и количества попыток в функции `check_proxy` повысит устойчивость к нестабильным прокси.


**Взаимосвязи с другими частями проекта:**

Из кода видно, что проект использует модули `gs` для работы с путями, `logger` для логирования и, возможно, `header` для управления заголовками. Функции взаимодействуют друг с другом, передавая данные, и результат работы с прокси может использоваться в других частях проекта.