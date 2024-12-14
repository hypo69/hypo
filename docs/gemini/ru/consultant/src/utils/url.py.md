# Анализ кода модуля `url.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет поставленные задачи.
    - Используются аннотации типов.
    - Присутствует документация в формате docstring.
    - Есть пример использования в блоке `if __name__ == "__main__":`.
- Минусы
    - Отсутствует использование `logger` для логирования ошибок или отладочной информации.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не все комментарии в формате reStructuredText.
    - Необходим рефакторинг обработки параметров для большей наглядности.
    - Отсутствует импорт `from src.logger.logger import logger`.

**Рекомендации по улучшению**
1. Добавить импорт `from src.logger.logger import logger`.
2. Заменить стандартный `print` на использование `logger.debug` для вывода отладочной информации и `logger.error` для ошибок.
3. Переписать docstring в формате reStructuredText для модуля и функций.
4.  Переписать комментарии в формате reStructuredText.
5.  Избегать использования `if params:` для проверки наличия параметров, использовать `if not params is None`
6.  Использовать `return {}` вместо `return None` для случая, когда нет параметров.
7.  Добавить try-except блок в функции `extract_url_params` для обработки возможных ошибок при парсинге URL.
8.  Добавить комментарий `# Код проверяет URL на валидность` и `# Код извлекает параметры из URL`
9.  Изменить проверку на None на `if params is not None:`
10. Добавить docstring для модуля.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с URL строками
=================================

Этот модуль предоставляет функции для извлечения параметров из URL и проверки валидности URL.

Функции
-------
    :func:`extract_url_params`: Извлекает параметры запроса из URL.
    :func:`is_url`: Проверяет, является ли строка валидным URL.

Пример использования
--------------------

.. code-block:: python

    url = "https://example.com/path?param1=value1&param2=value2"
    params = extract_url_params(url)
    if params:
        print(params)  # Выведет: {'param1': 'value1', 'param2': 'value2'}

"""
MODE = 'dev'

from urllib.parse import urlparse, parse_qs
import validators
from src.logger.logger import logger # Добавлен импорт logger

def extract_url_params(url: str) -> dict | None:
    """
    Извлекает параметры из строки URL.

    :param url: Строка URL для парсинга.
    :type url: str
    :return: Словарь параметров запроса и их значений или пустой словарь, если URL не содержит параметров.
    :rtype: dict | None
    :raises Exception: Если происходит ошибка при парсинге URL.
    """
    try: # Блок try-except для обработки ошибок парсинга URL
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)

        if params:
            # Преобразуем значения из списка в строку, если параметр имеет одно значение
            params = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
            return params
        return {}
    except Exception as ex: # Логирование ошибки парсинга URL
        logger.error(f'Ошибка при парсинге URL: {url}', exc_info=ex)
        return None


def is_url(text: str) -> bool:
    """
    Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    :param text: Строка для проверки.
    :type text: str
    :return: `True`, если строка является валидным URL, иначе `False`.
    :rtype: bool
    """
    return validators.url(text)


if __name__ == "__main__":
    # Получаем строку URL от пользователя
    url = input("Введите URL: ")

    # Код проверяет URL на валидность
    if is_url(url):
        # Код извлекает параметры из URL
        params = extract_url_params(url)

        # Выводим параметры
        if params is not None:
            if params:
                logger.debug("Параметры URL:")
                for key, value in params.items():
                    logger.debug(f"{key}: {value}")
            else:
                logger.debug("URL не содержит параметров.")
        else:
             logger.error("Не удалось извлечь параметры URL")
    else:
        logger.debug("Введенная строка не является валидным URL.")
```