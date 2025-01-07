# Анализ кода модуля `proxy.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, функции имеют четкое назначение.
    - Используется `logger` для логирования, что помогает отслеживать ошибки и ход выполнения программы.
    - Присутствуют docstring для функций, что улучшает читаемость и понимание кода.
    - Используются типы данных для параметров и возвращаемых значений.

-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - В некоторых местах используется `try-except` без конкретики.
    - Отсутствует обработка ошибок при обращении к словарю прокси по ключам (например, `proxy['protocol']`).
    - В коде есть избыточное использование `...` как точки остановки.

**Рекомендации по улучшению**
1.  Заменить использование стандартного `open` для чтения файлов на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Уточнить обработку исключений, использовать `logger.error` вместо `try-except ...`.
3.  Добавить проверку наличия ключей в словаре `proxy` при обращении к ним.
4.  Удалить или прокомментировать `...` как точки остановки.
5.  Использовать f-строки для форматирования логов, чтобы сделать их более читаемыми и информативными.
6.  Уточнить тип исключений, которые обрабатываются.
7.  В `download_proxies_list` заменить `except Exception as ex` на более конкретные исключения.
8.  Убрать вызов `download_proxies_list()` внутри `get_proxies_dict()`, так как файл скачивается каждый раз.
9.  Привести `if __name__ == '__main__':` в соответствие с инструкциями.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

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
from requests.exceptions import ProxyError, RequestException, HTTPError, ConnectionError
from pathlib import Path
from typing import Any, Dict, List, Optional
from src import gs
from src.utils.printer import pprint
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns # Добавлен импорт j_loads_ns



# URL источника списка прокси
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'

# Путь к файлу для сохранения списка прокси
proxies_list_path: Path = gs.path.src / 'webdriver' / 'proxies.txt'


def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    :param url: URL файла для загрузки.
    :param save_path: Путь для сохранения загруженного файла.
    :return: ``True``, если загрузка прошла успешно, иначе ``False``.
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
    except HTTPError as ex: # Обработка HTTPError
        logger.error(f'Ошибка при загрузке файла: HTTP ошибка {ex}')
        return False
    except ConnectionError as ex: # Обработка ConnectionError
        logger.error(f'Ошибка при загрузке файла: Ошибка подключения {ex}')
        return False
    except Exception as ex: # Обработка всех остальных исключений
        logger.error(f'Неизвестная ошибка при загрузке файла: {ex}')
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    :param file_path: Путь к файлу с прокси.
    :return: Словарь с распределёнными по типам прокси.
    """

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }
    try:
         # Чтение файла с использованием j_loads_ns
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    proxies[protocol].append({'protocol': protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {ex}')
    except Exception as ex:
        logger.error(f'Ошибка при парсинге прокси: {ex}')
    return proxies


def check_proxy(proxy: Dict[str, Any]) -> bool:
    """
    Проверяет работоспособность прокси-сервера.

    :param proxy: Словарь с данными прокси (host, port, protocol).
    :return: ``True``, если прокси работает, иначе ``False``.
    """
    try:
        if not all(key in proxy for key in ('protocol', 'host', 'port')):
            logger.warning(f"Некорректный формат прокси: {proxy}")
            return False
        # Попытка сделать запрос через прокси
        response = requests.get("https://httpbin.org/ip", proxies={
            proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"
        }, timeout=5)
        # Проверка кода ответа
        response.raise_for_status()
        if response.status_code == 200:
            logger.info(f"Прокси найден: {proxy['host']}:{proxy['port']}")
            return True
        else:
            logger.warning(f"Прокси не работает: {proxy['host']}:{proxy['port']} (Статус: {response.status_code})")
            return False
    except (ProxyError, RequestException, Exception) as ex:
         logger.warning(f"Ошибка подключения через прокси {proxy.get('host', 'unknown')}:{proxy.get('port', 'unknown')}: {ex}")
         return False



if __name__ == '__main__':
    """
    Пример использования модуля.
    Загружает список прокси, парсит и выводит информацию о количестве обработанных прокси.
    """
    # Загрузка списка прокси
    if download_proxies_list():
        # Парсинг списка прокси
        parsed_proxies = get_proxies_dict()
        # Логирование количества обработанных прокси
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')
```