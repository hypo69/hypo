# Анализ кода модуля `proxy.py`

**Качество кода**
8
-  Плюсы
    -   Код разбит на функции, что улучшает читаемость и поддержку.
    -   Используется `logger` для логирования, что помогает в отладке и мониторинге.
    -   Присутствуют docstring для функций.
    -   Используется `Path` из `pathlib` для работы с путями, что является хорошей практикой.
-  Минусы
    -   Не все комментарии в коде соответствуют стандарту reStructuredText (RST).
    -   Используются стандартные блоки `try-except`, которые можно заменить на `logger.error`.
    -   Импорт `header` не используется.
    -   Функция `parse_proxies` не используется, что делает код менее понятным.
    -   Используется глобальная переменная `MODE`, что может быть нежелательно в больших проектах.
    -   В `check_proxy` избыточная проверка `if response.status_code == 200:`.
    -   Проверка существования файла `proxies.txt` перед его открытием отсутствует.

**Рекомендации по улучшению**
1.  Привести все комментарии к формату reStructuredText (RST).
2.  Заменить стандартные блоки `try-except` на `logger.error` там, где это возможно.
3.  Удалить неиспользуемый импорт `header`.
4.  Переименовать `parse_proxies` в `get_proxies_dict`.
5.  Удалить глобальную переменную `MODE` если она не используется.
6.  Убрать избыточную проверку `if response.status_code == 200:` в `check_proxy`.
7.  Добавить проверку существования файла `proxies.txt` перед его открытием.
8.  Добавить проверки на валидность данных, например, при парсинге прокси.
9.  Удалить `...` в обработчиках исключений.

**Оптимизиробанный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с прокси.
=========================================================================================

Этот модуль определяет функции для загрузки и парсинга списка прокси.
Загружается текстовый файл с прокси-адресами и распределяется по категориям.

Пример использования
--------------------

.. code-block:: python

    download_proxies_list()
    proxies = get_proxies_dict()

"""
import re
import requests
from requests.exceptions import ProxyError, RequestException
from pathlib import Path
from typing import Any, Dict, List, Optional
# from header import header
from src import gs
# from src.utils.printer import pprint # не используется
from src.logger.logger import logger

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
        # Логирование ошибки загрузки файла
        logger.error('Ошибка при загрузке файла: ', ex)
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    :param file_path: Путь к файлу с прокси.
    :return: Словарь с распределёнными по типам прокси.
    """
    # загрузка файла если его нет
    download_proxies_list()

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }
    # проверяем наличие файла
    if not file_path.exists():
        logger.error(f'Файл не найден: {file_path}')
        return proxies
    try:
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    # проверка валидности данных
                    if protocol and host and port:
                         proxies[protocol].append({'protocol': protocol, 'host': host, 'port': port})
    except Exception as ex:
        # Логирование ошибки парсинга прокси
        logger.error('Ошибка при парсинге прокси: ', ex)

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
        response.raise_for_status() # проверяем на 200 ok
        # Логирование успешного подключения через прокси
        logger.info(f"Прокси найден: {proxy['host']}:{proxy['port']}")
        return True
    except (ProxyError, RequestException) as ex:
        # Логирование ошибки подключения через прокси
        logger.warning(f"Ошибка подключения через прокси {proxy['host']}:{proxy['port']}:", ex)
        return False


if __name__ == '__main__':
    # Загрузка списка прокси и парсинг
    if download_proxies_list():
        parsed_proxies = get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')
```