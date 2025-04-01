## Анализ кода модуля `proxy`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Четкая структура модуля, разделение на функции для загрузки, парсинга и проверки прокси.
  - Использование логирования для отслеживания работы модуля.
  - Обработка исключений при загрузке и парсинге прокси.
- **Минусы**:
  - Не все функции имеют подробное описание в формате docstring.
  - В некоторых блоках `try-except` отсутствует полная обработка ошибок (используются `...`).
  - Использование устаревшего `header` вместо `src.header`.
  - Дублирование вызова `download_proxies_list` в `get_proxies_dict`.
  - В `check_proxy` передается `None` и `False` при логировании, что не соответствует стандарту логирования.

**Рекомендации по улучшению**:

1. **Документация**:
   - Добавить подробные docstring-описания для всех функций, включая описание аргументов, возвращаемых значений и возможных исключений.
   - Оформить примеры использования в docstring.

2. **Обработка ошибок**:
   - Заменить `...` в блоках `try-except` на полноценную обработку ошибок, логирование с использованием `logger.error` и traceback.

3. **Импорты**:
   - Обновить импорт `header` на `src.header`.

4. **Оптимизация**:
   - Убрать дублирование вызова `download_proxies_list` в функции `get_proxies_dict`, чтобы избежать лишней загрузки списка прокси.

5. **Логирование**:
   - В функции `check_proxy` при логировании использовать правильный формат логирования ошибок `logger.warning(message, exc_info=True)` или `logger.error(message, ex, exc_info=True)`.

6. **Форматирование**:
   - Использовать f-строки для форматирования строк.
   - Улучшить читаемость кода, добавив пробелы вокруг операторов.

**Оптимизированный код**:

```python
## \file /src/webdriver/proxy.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для работы с прокси
=========================================================================================

Модуль определяет функции для загрузки и парсинга списка прокси.
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

from src.header import __root__
from src import gs
from src.utils.printer import pprint
from src.logger.logger import logger

# URL источника списка прокси
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'

# Путь к файлу для сохранения списка прокси
proxies_list_path: Path = __root__ / 'src' / 'webdriver' / 'proxies.txt'


def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    Args:
        url (str): URL файла для загрузки.
        save_path (Path): Путь для сохранения загруженного файла.

    Returns:
        bool: Успешность выполнения операции.

    Example:
        >>> download_proxies_list()
        True
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
        logger.error('Ошибка при загрузке файла:', ex, exc_info=True)  # Логируем ошибку с traceback
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    Args:
        file_path (Path): Путь к файлу с прокси.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Словарь с распределёнными по типам прокси.

    Example:
        >>> proxies = get_proxies_dict()
        >>> print(proxies.keys())
        dict_keys(['http', 'socks4', 'socks5'])
    """

    # download_proxies_list() # убираем дублирующий вызов

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }

    try:
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    proxies[protocol].append({'protocol': protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
        logger.error('Файл не найден:', ex, exc_info=True)  # Логируем ошибку с traceback
    except Exception as ex:
        logger.error('Ошибка при парсинге прокси:', ex, exc_info=True)  # Логируем ошибку с traceback

    return proxies


def check_proxy(proxy: dict) -> bool:
    """
    Проверяет работоспособность прокси-сервера.

    Args:
        proxy (dict): Словарь с данными прокси (host, port, protocol).

    Returns:
        bool: True, если прокси работает, иначе False.

    Example:
        >>> proxy = {'protocol': 'http', 'host': '1.2.3.4', 'port': '8080'}
        >>> check_proxy(proxy)
        False
    """
    try:
        # Попытка сделать запрос через прокси
        response = requests.get(
            'https://httpbin.org/ip',
            proxies={proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"},
            timeout=5
        )
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
    # Загрузка списка прокси и парсинг
    if download_proxies_list():
        parsed_proxies = get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')