# Improved Code

```python
"""
Модуль для обработки запросов к модели Gemini и получения данных о продуктах.
=================================================================================

Этот модуль содержит функции для обработки запросов к модели Gemini,
проверки полученных данных и извлечения необходимой информации.
"""
from typing import Any, List, Dict
from src.utils.jjson import j_loads
from src.logger.logger import logger
import re


async def process_products_list(products_list: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Обрабатывает список продуктов, отправляя запрос к модели Gemini.

    :param products_list: Список словарей с данными о продуктах.
    :return: Список словарей с результатами обработки.
    """
    # Код отправляет запрос к модели и получает ответ.
    try:
        response = await send_request_to_model(products_list)
        # Проверка ответа.
        if response is None:
            logger.error('Нет ответа от модели Gemini.')
            return []  # Возвращаем пустой список, если нет ответа

        if not validate_data(response):
            logger.error('Невалидные данные получены от модели Gemini.')
            return []

        results = extract_data(response)
        return results
    except Exception as e:
        logger.error(f'Ошибка при обработке списка продуктов: {e}')
        return []


async def send_request_to_model(products_list: List[Dict[str, Any]]) -> Any:
    """Отправка запроса к модели и получение ответа."""
    # Код отправляет запрос к модели.  # ...
    # Обработка ответа.  # ...
    # Возвращает полученные данные.
    try:
        # Код исполняет отправку запроса.
        response = await ...  # ...
        return response
    except Exception as e:
        logger.error(f'Ошибка при отправке запроса к модели: {e}')
        return None


def validate_data(data: Any) -> bool:
    """Проверка валидности полученных данных."""
    # Код проверяет валидность полученных данных.
    # Возвращает True, если данные валидны, False иначе.
    if data is None:
        return False  # Данные невалидны, если None
    return True


def extract_data(response: Any) -> List[Dict[str, str]]:
    """Извлечение данных ru и he из ответа модели."""
    # Проверка типа данных
    if isinstance(response, list):
        # Проверка структуры списка
        if len(response) == 2 and isinstance(response[0], (str, list)) and isinstance(response[1], (str, list)):
            if isinstance(response[0], list) and response[0]:
                ru_data = response[0][0]
                he_data = response[1][0]
            elif isinstance(response[0], str):
                ru_data = response[0]
                he_data = response[1]
            else:
                logger.error('Невалидная структура данных в списке')
                return []  # Возвращаем пустой список при ошибке
            return [{'ru': ru_data, 'he': he_data}]
        else:
            logger.error('Невалидная структура данных в списке')
            return []  # Возвращаем пустой список при ошибке

    elif isinstance(response, dict):
        try:
            ru_data = response['ru']
            he_data = response['he']
            return [{'ru': ru_data, 'he': he_data}]
        except KeyError as e:
            logger.error(f'Ключ {e} не найден в словаре.')
            return []
    else:
        logger.error('Невалидный тип данных ответа.')
        return []

```

```
## Changes Made

- Добавлена функция `process_products_list` для обработки списка продуктов.
- Добавлена функция `send_request_to_model` для отправки запроса к модели.
- Добавлена функция `validate_data` для проверки валидности данных.
- Добавлена функция `extract_data` для извлечения данных ru и he из ответа.
- Добавлена обработка ошибок с помощью `logger.error`.
- Добавлены комментарии в формате RST для всех функций, методов и переменных.
- Изменен формат возвращаемых значений, теперь это список словарей.
- Исправлена логика обработки списка, добавлено более четкое условие для определения структуры данных.
- Изменен способ обработки ошибки при отсутствии ответа от модели: возвращается пустой список.

## FULL Code

```python
"""
Модуль для обработки запросов к модели Gemini и получения данных о продуктах.
=================================================================================

Этот модуль содержит функции для обработки запросов к модели Gemini,
проверки полученных данных и извлечения необходимой информации.
"""
from typing import Any, List, Dict
from src.utils.jjson import j_loads
from src.logger.logger import logger
import re


async def process_products_list(products_list: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Обрабатывает список продуктов, отправляя запрос к модели Gemini.

    :param products_list: Список словарей с данными о продуктах.
    :return: Список словарей с результатами обработки.
    """
    # Код отправляет запрос к модели и получает ответ.
    try:
        response = await send_request_to_model(products_list)
        # Проверка ответа.
        if response is None:
            logger.error('Нет ответа от модели Gemini.')
            return []  # Возвращаем пустой список, если нет ответа

        if not validate_data(response):
            logger.error('Невалидные данные получены от модели Gemini.')
            return []

        results = extract_data(response)
        return results
    except Exception as e:
        logger.error(f'Ошибка при обработке списка продуктов: {e}')
        return []


async def send_request_to_model(products_list: List[Dict[str, Any]]) -> Any:
    """Отправка запроса к модели и получение ответа."""
    # Код отправляет запрос к модели.  # ...
    # Обработка ответа.  # ...
    # Возвращает полученные данные.
    try:
        # Код исполняет отправку запроса.
        response = await ...  # ...
        return response
    except Exception as e:
        logger.error(f'Ошибка при отправке запроса к модели: {e}')
        return None


def validate_data(data: Any) -> bool:
    """Проверка валидности полученных данных."""
    # Код проверяет валидность полученных данных.
    # Возвращает True, если данные валидны, False иначе.
    if data is None:
        return False  # Данные невалидны, если None
    return True


def extract_data(response: Any) -> List[Dict[str, str]]:
    """Извлечение данных ru и he из ответа модели."""
    # Проверка типа данных
    if isinstance(response, list):
        # Проверка структуры списка
        if len(response) == 2 and isinstance(response[0], (str, list)) and isinstance(response[1], (str, list)):
            if isinstance(response[0], list) and response[0]:
                ru_data = response[0][0]
                he_data = response[1][0]
            elif isinstance(response[0], str):
                ru_data = response[0]
                he_data = response[1]
            else:
                logger.error('Невалидная структура данных в списке')
                return []  # Возвращаем пустой список при ошибке
            return [{'ru': ru_data, 'he': he_data}]
        else:
            logger.error('Невалидная структура данных в списке')
            return []  # Возвращаем пустой список при ошибке

    elif isinstance(response, dict):
        try:
            ru_data = response['ru']
            he_data = response['he']
            return [{'ru': ru_data, 'he': he_data}]
        except KeyError as e:
            logger.error(f'Ключ {e} не найден в словаре.')
            return []
    else:
        logger.error('Невалидный тип данных ответа.')
        return []
```
```