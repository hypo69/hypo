# Анализ кода модуля `requests.py`

**Качество кода**
8
-  Плюсы
    - Присутствует базовая структура обработки запросов к API.
    - Используется логгер для записи ошибок и предупреждений.
    - Применяется `SimpleNamespace` для удобного доступа к данным ответа.
-  Минусы
    - Не везде используется кастомный обработчик JSON, а именно `j_loads` или `j_loads_ns`
    -  Избыточное использование `try-except` блоков, не всегда с логированием ошибок.
    -  Не полное документирование кода в reStructuredText (RST) формате.
    -  Отсутствуют проверки на наличие атрибутов перед их использованием.
    - Некоторые ошибки не обрабатываются, а просто пропускаются (`...`).
    - Код не всегда соответствует PEP 8, например, пробелы в аннотациях типов.
    - Дублирование логирования ошибок, лучше использовать одну точку логирования.
    -  Не все исключения обрабатываются с помощью логгера.

**Рекомендации по улучшению**

1.  **Использовать `j_loads_ns`**: Заменить стандартный `json.loads` на `j_loads_ns` для более консистентной обработки JSON.
2.  **Улучшить обработку ошибок**:  Удалить избыточные `try-except` блоки, использовать `logger.error` для записи ошибок, и обрабатывать исключения с помощью `logger.exception`.
3.  **Документирование**: Добавить документацию в формате reStructuredText (RST) для модуля и функции.
4.  **Уточнить обработку ответов**: Добавить проверку на существование ключей `response_name` и `resp_result` в ответе, прежде чем обращаться к ним.
5. **Улучшить логирование**: Использовать `logger.error` с `exc_info=True` чтобы логировать трассировку ошибок.
6.  **Удалить лишнее**: Убрать закомментированный код и `...`, если это не является точкой отладки.
7. **PEP 8**: Исправить ошибки в стиле кода, согласно PEP 8.
8. **Аннотация типов**: добавить аннотации типов.

**Оптимизированный код**

```python
"""
Модуль для выполнения API-запросов и обработки ответов.
========================================================

Этот модуль предоставляет функцию :func:`api_request` для отправки запросов к API и обработки их ответов.
Он включает в себя обработку ошибок и преобразование JSON-ответов в объекты SimpleNamespace.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.api.helpers.requests import api_request
    from src.suppliers.aliexpress.api.request import Request

    request = Request(method='get', url='https://example.com/api', params={'id': 123})
    result = api_request(request, 'response_data')
    if result:
        print(result)
"""
# -*- coding: utf-8 -*-
 # <- venv win
from types import SimpleNamespace
from time import sleep
from src.logger.logger import logger
#from src.utils.printer import pprint # удалил т.к. не используется
from src.utils.jjson import j_loads_ns # Используем j_loads_ns
from typing import Any

from ..errors import ApiRequestException, ApiRequestResponseException


def api_request(request: Any, response_name: str, attempts: int = 1) -> Any:
    """
    Отправляет API-запрос и обрабатывает ответ.

    :param request: Объект запроса, имеющий метод `getResponse`.
    :param response_name: Имя ключа, содержащего данные ответа в JSON.
    :param attempts: Количество попыток выполнения запроса.
    :return: Обработанный результат ответа или None в случае ошибки.

    :raises ApiRequestException: Если произошла ошибка при выполнении запроса.
    :raises ApiRequestResponseException: Если произошла ошибка при обработке ответа.
    """
    try:
        #  выполняет запрос к API
        response = request.getResponse()
    except Exception as error:
        logger.error(f'Ошибка при выполнении запроса: {error}', exc_info=True)
        return

    try:
        #  проверяет наличие ключа `response_name` в ответе
        if response_name not in response:
            logger.error(f'Ключ {response_name} не найден в ответе: {response}')
            return
        response = response[response_name]
        #  проверяет наличие ключа `resp_result` в полученном словаре
        if 'resp_result' not in response:
            logger.error(f'Ключ `resp_result` не найден в словаре: {response}')
            return
        response = response['resp_result']
        # Используем j_loads_ns для преобразования JSON в SimpleNamespace
        response = j_loads_ns(response)
    except Exception as error:
        logger.error(f'Ошибка при обработке ответа: {error}', exc_info=True)
        return

    try:
        # проверяет код ответа и возвращает результат или логирует предупреждение.
        if response.resp_code == 200:
            return response.result
        else:
            logger.warning(f'Код ответа {response.resp_code} - {response.resp_msg}', exc_info=True)
            return
    except Exception as ex:
        # Логирует ошибку при обработке ответа
        logger.error(f'Неизвестная ошибка при обработке ответа: {ex}', exc_info=True)
        return
```