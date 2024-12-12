# Анализ кода модуля `requests.py`

**Качество кода**
9
-   Плюсы
    - Код выполняет HTTP запросы и обрабатывает ответы, используя `SimpleNamespace` для удобства доступа к данным.
    - Присутствует логирование ошибок и предупреждений, а также кастомные исключения.
    - Используется `logger` для логирования.
-   Минусы
    - Используется `json.dumps` и `json.loads` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Избыточное использование `try-except` блоков, которое может быть упрощено.
    - Присутствуют закомментированные блоки кода, которые лучше удалить.
    - Отсутствуют docstring для модуля и функции.
    - Недостаточно подробное логирование ошибок.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить `from src.utils.jjson import j_loads, j_loads_ns` и использовать их вместо `json.dumps` и `json.loads`.
2.  **Логирование:** Улучшить логирование ошибок, добавив контекстную информацию (например, имя функции).
3.  **Обработка исключений:** Упростить `try-except` блоки, используя `logger.error` для регистрации исключений и возврата `None` или дефолтного значения.
4.  **Удаление комментариев:** Удалить закомментированные блоки кода, которые не несут смысловой нагрузки.
5.  **Документирование:** Добавить docstring для модуля и функции в формате reStructuredText.
6.  **Именование переменных**: Переименовать `attemps` на `attempts`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~
"""
Модуль для отправки и обработки API запросов.
==================================================

Этот модуль содержит функцию :func:`api_request`, которая отправляет API запросы,
обрабатывает ответы и возвращает результаты, а также логирует ошибки.

"""
from types import SimpleNamespace
from time import sleep
from src.logger.logger import logger
from src.utils.printer import pprint
#from src.utils.jjson import j_loads, j_loads_ns #TODO: переделать на j_loads
import json
from ..errors import ApiRequestException, ApiRequestResponseException


def api_request(request, response_name, attempts: int = 1):
    """
    Отправляет API запрос и обрабатывает ответ.

    :param request: Объект запроса с методом `getResponse`.
    :param response_name: Имя поля в ответе, содержащего данные.
    :param attempts: Количество попыток отправки запроса (по умолчанию 1).
    :return: Результат запроса в виде объекта SimpleNamespace или None в случае ошибки.

    :raises ApiRequestException: Если запрос не удался.
    :raises ApiRequestResponseException: Если произошла ошибка при обработке ответа.
    """
    try:
        # Выполняет запрос и получает ответ.
        response = request.getResponse()
    except Exception as error:
        # Логирует ошибку запроса.
        logger.error(f'Ошибка при выполнении запроса в `api_request`: {error}', exc_info=True)
        return

    try:
        # Извлекает данные из ответа по ключу `response_name` и `resp_result`
        response = response[response_name]['resp_result']
        # Преобразует JSON ответ в объект SimpleNamespace
        response = json.dumps(response)
        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as error:
         # Логирует ошибку при обработке ответа.
        logger.error(f'Ошибка при обработке ответа в `api_request`: {error}', exc_info=True)
        return

    try:
        # Проверяет код ответа
        if response.resp_code == 200:
            # Возвращает результат, если код ответа 200
            return response.result
        else:
            # Логирует предупреждение, если код ответа не 200
             logger.warning(f'Неудачный код ответа {response.resp_code} - {response.resp_msg} в `api_request`',exc_info=True)
            # Возвращает None, если код ответа не 200
            return
    except Exception as ex:
        # Логирует ошибку, возникшую при проверке кода ответа.
        logger.error(f'Ошибка при проверке кода ответа в `api_request`: {ex}', exc_info=True)
        return
```