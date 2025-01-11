# Анализ кода модуля `url.py`

**Качество кода**
7
- Плюсы
    - Код выполняет поставленные задачи: извлечение параметров из URL, проверка валидности URL и сокращение ссылок.
    - Используются стандартные библиотеки для работы с URL (`urllib.parse`) и HTTP запросами (`requests`).
    - Присутствует проверка валидности URL с помощью библиотеки `validators`.
    - Есть документирование функций с описанием параметров и возвращаемых значений.
- Минусы
    - Отсутствует импорт `logger` из `src.logger`.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не все строки кода соответствуют стандарту оформления.
    - Не хватает подробных docstring и примеров использования для функций.
    - Использованы двойные кавычки в строках, где должны быть одинарные.
    - Нет обработки ошибок через logger.error.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger`.
2.  Использовать `logger.error` вместо стандартного `try-except` для обработки ошибок.
3.  Использовать одинарные кавычки в коде, где это требуется.
4.  Добавить подробные docstring для каждой функции, включая примеры использования.
5.  Добавить описание модуля.
6.  Заменить двойные кавычки в коде на одинарные.
7.  Добавить обработку возможных ошибок в `url_shortener`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для работы с URL строками
=========================================================================================

Этот модуль предоставляет функции для работы с URL, такие как:
    - извлечение параметров запроса,
    - проверка на валидность URL,
    - сокращение ссылок с использованием TinyURL.

Пример использования
--------------------

.. code-block:: python

    from src.utils.url import is_url, extract_url_params, url_shortener

    url = 'https://example.com/path?param1=value1&param2=value2'
    if is_url(url):
        params = extract_url_params(url)
        if params:
            print(f'Параметры: {params}')
        short_url = url_shortener(url)
        if short_url:
            print(f'Сокращенный URL: {short_url}')

"""
from urllib.parse import urlparse, parse_qs
import validators
import requests
from src.logger.logger import logger # Добавлен импорт logger

def extract_url_params(url: str) -> dict | None:
    """Извлекает параметры из строки URL.

    :param url: Строка URL для парсинга.
    :type url: str
    :return: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    :rtype: dict | None

    Пример:
        >>> extract_url_params('https://example.com/path?param1=value1&param2=value2')
        {'param1': 'value1', 'param2': 'value2'}
        >>> extract_url_params('https://example.com/path')
        None
    """
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    
    # Преобразуем значения из списка в строку, если параметр имеет одно значение
    if params:
        params = {k: v if len(v) > 1 else v[0] for k, v in params.items()}
        return params
    return None


def is_url(text: str) -> bool:
    """Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    :param text: Строка для проверки.
    :type text: str
    :return: `True` если строка является валидным URL, иначе `False`.
    :rtype: bool

    Пример:
        >>> is_url('https://example.com')
        True
        >>> is_url('not a url')
        False
    """
    return validators.url(text)


def url_shortener(long_url: str) -> str | None:
    """Сокращает длинный URL с использованием сервиса TinyURL.

    :param long_url: Длинный URL для сокращения.
    :type long_url: str
    :return: Сокращённый URL или `None`, если произошла ошибка.
    :rtype: str | None

    Пример:
        >>> url_shortener('https://www.example.com')
        'https://tinyurl.com/...'
    """
    url = f'http://tinyurl.com/api-create.php?url={long_url}' #  Использованы одинарные кавычки
    try: # Добавлена обработка исключений
        response = requests.get(url)
        response.raise_for_status() # Проверка на статус код
        if response.status_code == 200:
            return response.text
        else:
            logger.error(f'Ошибка при сокращении URL: статус код {response.status_code}') # Запись ошибки в лог
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f'Ошибка при выполнении запроса к TinyURL: {e}')
        return None


if __name__ == '__main__':
    # Получаем строку URL от пользователя
    url = input('Введите URL: ') #  Использованы одинарные кавычки
    
    # Проверяем валидность URL
    if is_url(url):
        params = extract_url_params(url)
        
        # Выводим параметры
        if params:
            print('Параметры URL:') #  Использованы одинарные кавычки
            for key, value in params.items():
                print(f'{key}: {value}') #  Использованы одинарные кавычки
        else:
            print('URL не содержит параметров.') #  Использованы одинарные кавычки
        
        # Предлагаем пользователю сократить URL
        shorten = input('Хотите сократить этот URL? (y/n): ').strip().lower() #  Использованы одинарные кавычки
        if shorten == 'y': #  Использованы одинарные кавычки
            short_url = url_shortener(url)
            if short_url:
                print(f'Сокращённый URL: {short_url}') #  Использованы одинарные кавычки
            else:
                print('Ошибка при сокращении URL.') #  Использованы одинарные кавычки
    else:
        print('Введенная строка не является валидным URL.') #  Использованы одинарные кавычки
```