# Анализ кода модуля proxy.py

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, функции выполняют конкретные задачи.
    - Используется `logger` для логирования, что способствует отладке и мониторингу.
    - Есть обработка исключений, что делает код более устойчивым к ошибкам.
    - Наличие документации к модулю и функциям.
-  Минусы
    -  Некоторые комментарии не соответствуют стандарту RST.
    -  Не везде используется явное указание типа в аннотации, что снижает читаемость.
    -  В функции `get_proxies_dict` повторно вызывается `download_proxies_list`, что излишне, если список уже загружен.
    -  Используется стандартный метод `json.load`, необходимо заменить на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все переменные имеют аннотацию типа.
    -  В `check_proxy` используется f-строка в логе, можно использовать форматированный вывод для логгера.

**Рекомендации по улучшению**

1.  **Улучшение документации**:
    -   Привести комментарии к стандарту RST.
    -   Добавить больше примеров использования в документацию.
    -   Уточнить назначение переменных и типов.
    -   Добавить документацию к переменным `url` и `proxies_list_path`
2.  **Улучшение обработки ошибок**:
    -   Уточнить обработку ошибок и использовать `logger.error` с выводом исключения.
    -   Добавить более конкретные сообщения об ошибках.
3.  **Рефакторинг**:
    -   Убрать повторный вызов `download_proxies_list` в `get_proxies_dict`.
    -   Вместо `response.status_code == 200`, использовать `response.ok`.
    -   Использовать f-строки с форматированным выводом для `logger` в `check_proxy`
    -   Переименовать `match` в `proxy_match` для большей ясности.
    -   Добавить аннотации типов для всех переменных.
4. **Импорты**
    -   Импортировать `j_loads_ns` из `src.utils.jjson`.
    -  Удалить импорт `header`, т.к он не используется.
5. **Соответствие стандарту**
    - Заменить все двойные кавычки на одинарные, кроме операций вывода `print`, `input`, `logger`

**Оптимизированный код**

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
    proxies = parse_proxies()

"""

import re
import requests
from requests.exceptions import ProxyError, RequestException
from pathlib import Path
from typing import Any, Dict, List, Optional
# from header import header # Удален неиспользуемый импорт
from src import gs
from src.utils.printer import pprint
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns # Добавлен импорт j_loads_ns

# URL источника списка прокси
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'

# Путь к файлу для сохранения списка прокси
proxies_list_path: Path = gs.path.src / 'webdriver' / 'proxies.txt'


def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    :param url: URL файла для загрузки.
    :param save_path: Путь для сохранения загруженного файла.
    :return: True, если загрузка и сохранение прошли успешно, False в противном случае.
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
        # Логирование ошибки загрузки файла
        logger.error(f'Ошибка при загрузке файла: {ex}')
        return False


def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    :param file_path: Путь к файлу с прокси.
    :return: Словарь с распределёнными по типам прокси.
    """
    # Инициализируется словарь для хранения прокси
    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }

    # Код загружает список прокси, если файла нет
    if not file_path.exists():
      download_proxies_list()
    try:
        # Код читает файл построчно
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Код ищет совпадения с регулярным выражением
                proxy_match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if proxy_match:
                    protocol, host, port = proxy_match.groups()
                    proxies[protocol].append({'protocol': protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
        # Логирование ошибки, если файл не найден
        logger.error(f'Файл не найден: {ex}')
        ...
    except Exception as ex:
        # Логирование ошибки парсинга прокси
        logger.error(f'Ошибка при парсинге прокси: {ex}')
        ...

    return proxies


def check_proxy(proxy: dict) -> bool:
    """
    Проверяет работоспособность прокси-сервера.

    :param proxy: Словарь с данными прокси (host, port, protocol).
    :return: True, если прокси работает, иначе False.
    """
    try:
        # Код отправляет запрос через прокси
        response = requests.get(
            "https://httpbin.org/ip",
            proxies={proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"},
            timeout=5
        )
        # Проверка статуса ответа
        if response.ok:
            logger.info('Прокси найден: {host}:{port}'.format(**proxy))
            return True
        else:
            logger.warning(f"Прокси не работает: {proxy['host']}:{proxy['port']} (Статус: {response.status_code})")
            return False
    except (ProxyError, RequestException) as ex:
        # Логирование ошибки подключения через прокси
        logger.warning(f"Ошибка подключения через прокси {proxy['host']}:{proxy['port']}: {ex}")
        return False


if __name__ == '__main__':
    # Загрузка списка прокси и парсинг
    if download_proxies_list():
        parsed_proxies = get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')