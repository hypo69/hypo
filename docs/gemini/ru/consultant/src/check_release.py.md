# Анализ кода модуля `check_release`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Присутствует базовая структура модуля и функции.
    - Используется `requests` для получения данных с GitHub API.
    - Добавлены docstring для функции `check_latest_release`.
- **Минусы**:
    - Не используется `j_loads` или `j_loads_ns`.
    - Не используется `logger.error` для логирования ошибок.
    - В `return` в случае ошибки не возвращается `None`, а пустой `return`.
    - Не соблюдены требования к использованию кавычек.
    - Отсутствуют комментарии в формате RST для модуля.
    - Нет обработки ошибок при `response.json()`.

**Рекомендации по улучшению**:
- Необходимо использовать `j_loads` или `j_loads_ns` вместо `response.json()`.
- Заменить стандартный `try-except` на `logger.error` при возникновении ошибок.
- Заменить пустой `return` на `return None` в случае ошибки.
- Исправить использование кавычек в соответствии с инструкцией.
- Добавить RST-документацию для модуля.
- Выравнивать импорты в соответствии с остальным кодом.
- Добавить обработку возможных ошибок при разборе JSON.

**Оптимизированный код**:

```python
"""
Модуль для проверки последней версии релиза на GitHub.
====================================================

Этот модуль содержит функцию :func:`check_latest_release`, которая проверяет
последнюю версию релиза в указанном репозитории GitHub.

Пример использования
--------------------
.. code-block:: python

    from src.check_release import check_latest_release
    
    owner = 'owner_name'
    repo = 'repo_name'
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f"Последняя версия релиза: {latest_version}")
    else:
        print("Не удалось получить информацию о последнем релизе.")
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import requests  # Импортируем requests
from src.logger.logger import logger  # Импортируем logger из src.logger

from src.utils.jjson import j_loads_ns  # импортируем j_loads_ns для обработки json #
from typing import Optional  # импортируем Optional для обозначения типа возвращаемого значения


def check_latest_release(owner: str, repo: str) -> Optional[str]:
    """
    Проверяет последнюю версию релиза репозитория GitHub.

    :param owner: Владелец репозитория.
    :type owner: str
    :param repo: Название репозитория.
    :type repo: str
    :return: Последняя версия релиза, если она доступна, иначе None.
    :rtype: Optional[str]

    :raises Exception: В случае ошибки при получении или обработке данных.

    Пример:
    
    .. code-block:: python
    
        from src.check_release import check_latest_release
        
        owner = 'owner_name'
        repo = 'repo_name'
        latest_version = check_latest_release(owner, repo)
        if latest_version:
            print(f"Последняя версия релиза: {latest_version}")
        else:
            print("Не удалось получить информацию о последнем релизе.")

    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'  # Формируем URL для запроса к GitHub API
    try:
        response = requests.get(url)  # Отправляем GET-запрос
        response.raise_for_status()  # Проверяем статус код ответа
        
        json_data = j_loads_ns(response.text)  # Обрабатываем JSON-ответ с помощью j_loads_ns
        
        if json_data and 'tag_name' in json_data:  # Проверяем наличие tag_name
            return json_data['tag_name'] # Возвращаем tag_name
        else:
            logger.error(f'Неверный формат JSON ответа: {json_data}') # Логируем ошибку
            return None # Возвращаем None в случае ошибки
    except requests.exceptions.RequestException as e: # Ловим ошибки запроса
       logger.error(f'Ошибка при выполнении запроса: {e}') # Логируем ошибку
       return None # Возвращаем None в случае ошибки
    except Exception as e:
        logger.error(f'Неизвестная ошибка: {e}') # Логируем ошибку
        return None # Возвращаем None в случае ошибки
```