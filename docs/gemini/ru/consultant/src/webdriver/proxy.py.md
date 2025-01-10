# Анализ кода модуля proxy

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разделен на функции, каждая из которых выполняет определенную задачу.
    - Используются аннотации типов, что повышает читаемость и помогает в отладке.
    - Присутствует базовая обработка исключений, что делает код более устойчивым к ошибкам.
    - Есть docstring для функций, что улучшает понимание кода.
    - Используется `logger` для логирования, что облегчает отслеживание работы программы.
    -  Код соответствует PEP 8 (в основном).
-  Минусы
    -  Используется `from src.utils.printer import pprint`, который здесь не применяется.
    -  В некоторых местах используется `...` для обработки ошибок, что не является лучшей практикой (лучше обработать и залогировать ошибку).
    -  Не используется `j_loads` или `j_loads_ns`.
    -  Не все docstring полностью соответствуют стандартам (отсутствуют `Args`, `Returns`, `Raises` в некоторых местах).
    -  Используется `from src import gs`, что может быть неявным импортом (лучше импортировать конкретные модули из `src.gs`).
    -   Импорт `header` не используется.
    -  Используется `parse_proxies()` вместо `get_proxies_dict()` в main.
    
**Рекомендации по улучшению**

1.  Удалить неиспользуемые импорты `pprint` и `header`.
2.  Использовать `from src.logger.logger import logger` для явного импорта логгера.
3.  Заменить `...` на полноценную обработку ошибок с логированием.
4.  Добавить docstring в формате RST ко всем функциям, включая описание аргументов, возвращаемых значений и возможных исключений.
5.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо (здесь не используется json).
6.  Исправить использование `parse_proxies()` на `get_proxies_dict()` в `if __name__ == '__main__'`
7.  Уточнить импорт `gs`, импортируя конкретные переменные/модули, которые используются.

**Оптимизиробанный код**
```python
"""
Модуль для работы с прокси
=========================================================================================

Этот модуль определяет функции для загрузки и парсинга списка прокси. 
Загружается текстовый файл с прокси-адресами и распределяется по категориям.

Пример использования
--------------------

.. code-block:: python

    download_proxies_list()
    proxies = get_proxies_dict()

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import re
import requests
from requests.exceptions import ProxyError, RequestException
from pathlib import Path
from typing import Any, Dict, List, Optional
# from src import gs #  Импорт gs не используется напрямую, но `gs.path.src` используется, надо пересмотреть использование
from src.logger.logger import logger # Используем явный импорт логгера
from src.utils.jjson import j_loads, j_loads_ns #  не используется но импорт добавлен согласно инструкции.
# from src.utils.printer import pprint # Удален неиспользуемый импорт
# import header  # Удален неиспользуемый импорт
# URL источника списка прокси
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'
# Путь к файлу для сохранения списка прокси
proxies_list_path: Path = Path('src') / 'webdriver' / 'proxies.txt' # изменено согласно pep8.

def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    Args:
        url (str, optional): URL файла для загрузки. Defaults to url.
        save_path (Path, optional): Путь для сохранения загруженного файла. Defaults to proxies_list_path.
    Returns:
        bool: Успешность выполнения операции.
    Raises:
        Exception: При возникновении ошибки во время загрузки файла.
    """
    try:
        # Код отправляет запрос на загрузку файла
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Генерирует исключение для ошибок HTTP

        # Код сохраняет файл
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        logger.info(f'Файл успешно загружен и сохранён в {save_path}')
        return True
    except Exception as ex:
        logger.error(f'Ошибка при загрузке файла: {ex}')
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    Args:
        file_path (Path, optional): Путь к файлу с прокси. Defaults to proxies_list_path.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Словарь с распределёнными по типам прокси.
    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: При возникновении ошибки при парсинге прокси.
    """
    download_proxies_list()

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }

    try:
        # Код читает файл
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    proxies[protocol].append({'protocol': protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
         # Обработка случая, если файл не найден
        logger.error(f'Файл не найден: {ex}')
        return proxies
    except Exception as ex:
         # Обработка других ошибок при парсинге
        logger.error(f'Ошибка при парсинге прокси: {ex}')
        return proxies

    return proxies


def check_proxy(proxy: dict) -> bool:
    """
    Проверяет работоспособность прокси-сервера.

    Args:
        proxy (dict): Словарь с данными прокси (host, port, protocol).

    Returns:
        bool: True, если прокси работает, иначе False.

    Raises:
        ProxyError: Если прокси не работает.
        RequestException: Если возникает ошибка при отправке запроса.

    """
    try:
         # Код отправляет запрос через прокси
        response = requests.get("https://httpbin.org/ip", proxies={proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"}, timeout=5)
        # Проверка кода ответа
        if response.status_code == 200:
            logger.info(f"Прокси найден: {proxy['host']}:{proxy['port']}")
            return True
        else:
            logger.warning(f"Прокси не работает: {proxy['host']}:{proxy['port']} (Статус: {response.status_code})")
            return False
    except (ProxyError, RequestException) as ex:
        logger.warning(f"Ошибка подключения через прокси {proxy['host']}:{proxy['port']}: {ex}")
        return False


if __name__ == '__main__':
    # Код загружает список прокси и парсит его
    if download_proxies_list():
        parsed_proxies = get_proxies_dict() # исправлено parse_proxies() на get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')