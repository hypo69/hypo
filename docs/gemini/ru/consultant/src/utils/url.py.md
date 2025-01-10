# Анализ кода модуля `url.py`

**Качество кода**
10
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Присутствует документация для модуля и функций.
    - Используются стандартные библиотеки для работы с URL.
    - Есть проверка на валидность URL.
    - Присутствует пример использования в `if __name__ == "__main__":`
- Минусы
    - Нет обработки ошибок при запросе к сервису TinyURL, что может привести к неожиданному завершению программы.
    - Нет логирования ошибок.
    - Отсутствует импорт `Path` из модуля `pathlib`

**Рекомендации по улучшению**

1.  Добавить импорт `from src.logger.logger import logger`.
2.  Использовать `logger.error` для логирования ошибок вместо простого возврата `None` в `url_shortener`.
3.  Уточнить документацию к функциям, особенно про возвращаемое значение, указав его тип (например, `dict`, `bool` и т.д).
4.  Добавить проверку на корректность URL перед отправкой запроса к TinyURL в функции `url_shortener`.
5.  Изменить тип возвращаемого значения в функции `extract_url_params` на `dict | None`, чтобы соответствовать docstring.
6.  Обработать возможные исключения при работе с `requests` в `url_shortener`.
7.  Использовать одинарные кавычки в коде.
8.  Добавить описание модуля.

**Оптимизированный код**

```python
"""
Модуль для работы с URL
=========================================================================================

Этот модуль содержит функции для работы с URL строками, включая извлечение параметров запроса,
проверку на валидность URL и сокращение ссылок.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from src.utils.url import extract_url_params, is_url, url_shortener

    url = 'https://example.com/path?param1=value1&param2=value2'
    params = extract_url_params(url)
    print(f'Params: {params}')

    is_valid = is_url(url)
    print(f'Is valid URL: {is_valid}')

    short_url = url_shortener(url)
    print(f'Short URL: {short_url}')
"""
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

from urllib.parse import urlparse, parse_qs
import validators
import requests
from src.logger.logger import logger #  Импортируем logger из src.logger
from pathlib import Path  # Импортируем Path из модуля pathlib


def extract_url_params(url: str) -> dict | None:
    """
    Извлекает параметры из строки URL.

    Args:
        url (str): Строка URL для парсинга.

    Returns:
        dict | None: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    """
    # Парсим URL
    parsed_url = urlparse(url)
    # Извлекаем параметры запроса
    params = parse_qs(parsed_url.query)
    
    # Преобразовываем значения параметров из списка в строку, если значение одно
    if params:
        params = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
        return params
    return None


def is_url(text: str) -> bool:
    """
    Проверяет, является ли переданный текст валидным URL.

    Args:
        text (str): Строка для проверки.

    Returns:
        bool: `True`, если строка является валидным URL, иначе `False`.
    """
    #  Проверка валидности URL с использованием библиотеки validators
    return validators.url(text)


def url_shortener(long_url: str) -> str | None:
    """
    Сокращает длинный URL с использованием сервиса TinyURL.

    Args:
        long_url (str): Длинный URL для сокращения.

    Returns:
        str | None: Сокращённый URL или `None`, если произошла ошибка.
    """
    #  Формирование URL для TinyURL API
    url = f'http://tinyurl.com/api-create.php?url={long_url}'
    try:
        # Отправка GET запроса к TinyURL
        response = requests.get(url)
        #  Проверка статуса ответа
        if response.status_code == 200:
            return response.text
        #  Логирование ошибки, если статус ответа не 200
        logger.error(f'Ошибка при сокращении URL. Статус код: {response.status_code}')
        return None
    except requests.exceptions.RequestException as e:
        #  Логирование ошибки при запросе
        logger.error(f'Ошибка при запросе к TinyURL: {e}')
        return None


if __name__ == '__main__':
    # Получаем строку URL от пользователя
    url = input("Введите URL: ")
    
    #  Проверяем валидность URL
    if is_url(url):
        #  Извлекаем параметры URL
        params = extract_url_params(url)
        
        # Выводим параметры URL
        if params:
            print("Параметры URL:")
            for key, value in params.items():
                print(f"{key}: {value}")
        else:
            print("URL не содержит параметров.")
        
        #  Предлагаем пользователю сократить URL
        shorten = input("Хотите сократить этот URL? (y/n): ").strip().lower()
        if shorten == 'y':
            #  Сокращаем URL
            short_url = url_shortener(url)
            if short_url:
                print(f"Сокращённый URL: {short_url}")
            else:
                print("Ошибка при сокращении URL.")
    else:
        print("Введенная строка не является валидным URL.")
```