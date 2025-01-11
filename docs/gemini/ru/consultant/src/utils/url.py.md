# Анализ кода модуля `url`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет заявленные функции: извлечение параметров URL, проверка валидности URL и сокращение URL.
    - Используются стандартные библиотеки `urllib.parse`, `validators` и `requests`.
    - Присутствует основная часть для тестирования функций.
- **Минусы**:
    - Отсутствует RST-документация для модуля.
    - Не все функции имеют подробные RST-комментарии.
    - В коде присутствуют двойные кавычки для вывода, что не соответствует стандарту.
    - Отсутствует обработка ошибок в `url_shortener`, что может приводить к непредсказуемым ситуациям.
    - Не используется `logger` для вывода ошибок.
    - Проверка на длину списка `v` в функции `extract_url_params` не очень явная.
    - Есть проблема с импортом и использованием `logger`.

## Рекомендации по улучшению:
- Добавить RST-документацию для модуля, описывающую его назначение и основные функции.
- Добавить полные RST-комментарии к каждой функции, включая описание параметров, возвращаемых значений, возможных исключений и примеры использования.
- Использовать одинарные кавычки для строковых литералов в коде и двойные кавычки только для вывода.
- В функции `url_shortener` добавить обработку исключений, чтобы избежать падения программы при ошибках сети или сервиса.
- Добавить логирование ошибок с помощью `logger.error` вместо простого возврата `None`.
- Улучшить проверку на длину списка в `extract_url_params` для большей читаемости.
- Использовать `from src.logger import logger` для импорта `logger`.
- Использовать f-строки для форматирования URL в `url_shortener`.
- Применять `input()` и `print()` для интерактивного взаимодействия в блоке `if __name__ == "__main__":`.

## Оптимизированный код:
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с URL строками
===================================

Этот модуль предоставляет функции для извлечения параметров запроса из URL,
проверки валидности URL и сокращения длинных ссылок с помощью TinyURL.

Пример использования
----------------------
.. code-block:: python

    from src.utils.url import extract_url_params, is_url, url_shortener

    url = "https://example.com/path?param1=value1&param2=value2"
    params = extract_url_params(url)
    print(params)  # Выведет: {'param1': 'value1', 'param2': 'value2'}

    is_valid = is_url(url)
    print(is_valid)  # Выведет: True

    short_url = url_shortener(url)
    print(short_url) # Выведет сокращенный url
"""

from urllib.parse import urlparse, parse_qs # импорт необходимых модулей
import validators # импорт модуля для валидации
import requests # импорт модуля для http-запросов
from src.logger import logger # импорт логера

def extract_url_params(url: str) -> dict | None:
    """
    Извлекает параметры из строки URL.

    :param url: Строка URL для парсинга.
    :type url: str
    :return: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    :rtype: dict | None

    Пример:
        >>> url = 'https://example.com/path?param1=value1&param2=value2'
        >>> extract_url_params(url)
        {'param1': 'value1', 'param2': 'value2'}
    """
    parsed_url = urlparse(url) # парсим url
    params = parse_qs(parsed_url.query) # извлекаем параметры
    
    if params: # проверяем наличие параметров
        # Преобразуем значения из списка в строку, если параметр имеет одно значение
        params = {k: v[0] if len(v) == 1 else v for k, v in params.items()} # исправляем проверку на единичное значение
        return params
    return None


def is_url(text: str) -> bool:
    """
    Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    :param text: Строка для проверки.
    :type text: str
    :return: `True`, если строка является валидным URL, иначе `False`.
    :rtype: bool
    
    Пример:
       >>> is_url('https://example.com')
       True
       >>> is_url('not a url')
       False
    """
    return validators.url(text) # проверяем валидность url


def url_shortener(long_url: str) -> str | None:
    """
    Сокращает длинный URL с использованием сервиса TinyURL.

    :param long_url: Длинный URL для сокращения.
    :type long_url: str
    :return: Сокращённый URL или `None`, если произошла ошибка.
    :rtype: str | None
    :raises requests.exceptions.RequestException: Если во время запроса произошла ошибка.

    Пример:
        >>> url_shortener('https://www.google.com')
        'https://tinyurl.com/...'
    """
    url = f'http://tinyurl.com/api-create.php?url={long_url}' # используем f-строку
    try: # обрабатываем возможные ошибки
        response = requests.get(url) # отправляем get-запрос
        response.raise_for_status() # проверяем статус ответа
        return response.text # возвращаем сокращенный url
    except requests.exceptions.RequestException as e: # ловим ошибки http-запроса
        logger.error(f"Ошибка при сокращении URL: {e}") # логируем ошибку
        return None # возвращаем None в случае ошибки


if __name__ == "__main__":
    # Получаем строку URL от пользователя
    url = input("Введите URL: ") # запрашиваем ввод url
    
    # Проверяем валидность URL
    if is_url(url): # проверяем url на валидность
        params = extract_url_params(url) # извлекаем параметры
        
        # Выводим параметры
        if params: # если параметры есть
            print("Параметры URL:") # выводим сообщение
            for key, value in params.items(): # проходим по всем параметрам
                print(f"{key}: {value}") # выводим ключ и значение
        else:
            print("URL не содержит параметров.") # если параметров нет, выводим сообщение
        
        # Предлагаем пользователю сократить URL
        shorten = input("Хотите сократить этот URL? (y/n): ").strip().lower() # запрашиваем сокращение url
        if shorten == 'y': # если пользователь согласен
            short_url = url_shortener(url) # сокращаем url
            if short_url: # если сокращение успешно
                print(f"Сокращённый URL: {short_url}") # выводим сокращенный url
            else:
                print("Ошибка при сокращении URL.") # выводим сообщение об ошибке
    else:
        print("Введенная строка не является валидным URL.") # выводим сообщение о невалидном url