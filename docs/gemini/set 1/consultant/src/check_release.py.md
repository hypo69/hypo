# Анализ кода модуля `check_release.py`

**Качество кода**
6
-  Плюсы
    - Код выполняет поставленную задачу по проверке последней версии релиза на GitHub.
    - Используются `f-строки` для форматирования URL.
    - Присутствует документирование функции в формате docstring.

-  Минусы
    - Отсутствует обработка ошибок, а именно использование `logger.error` вместо простого возврата `None`.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используются одинарные кавычки в строках.
    - Комментарии к модулю не соответствуют формату reStructuredText.

**Рекомендации по улучшению**

1.  **Формат документации:**
    - Переписать комментарии к модулю в формате reStructuredText.
    - Использовать одинарные кавычки (`'`) в строках кода.

2.  **Обработка ошибок:**
    -  Использовать `logger.error` для записи ошибок вместо простого возврата `None`.
    - Использовать `try-except` для обработки возможных исключений при выполнении запроса.

3.  **Использование `j_loads`:**
    - Заменить `response.json()` на использование `j_loads` для обработки JSON ответа.

4.  **Логирование:**
    -  Добавить логирование для успешного получения версии релиза.

5. **Импорты**:
    - Добавить отсутствующие импорты, такие как `src.utils.jjson`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для проверки последней версии релиза на GitHub.
====================================================

Этот модуль содержит функцию :func:`check_latest_release`,
которая используется для получения последней версии релиза
из репозитория на GitHub.

Пример использования
--------------------

Пример использования функции `check_latest_release`:

.. code-block:: python

    owner = 'owner_name'
    repo = 'repo_name'
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f'Последняя версия релиза: {latest_version}')
    else:
        print('Не удалось получить версию релиза.')
"""



import requests
from src.logger.logger import logger
from src.utils.jjson import j_loads


def check_latest_release(owner: str, repo: str) -> str | None:
    """
    Проверяет последнюю версию релиза репозитория на GitHub.

    :param owner: Владелец репозитория.
    :type owner: str
    :param repo: Название репозитория.
    :type repo: str
    :return: Последняя версия релиза, если доступна, иначе None.
    :rtype: str | None
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    try:
        # Код выполняет GET запрос к API GitHub для получения информации о последнем релизе
        response = requests.get(url)
        response.raise_for_status() # выбрасывает исключение для плохих ответов (4xx or 5xx)

        # Код преобразует JSON ответ в словарь
        latest_release = j_loads(response.text)
        # Код извлекает название тега из словаря и возвращает его
        tag_name = latest_release['tag_name']
        logger.info(f'Успешно получена последняя версия релиза: {tag_name}')
        return tag_name
    except requests.exceptions.RequestException as ex:
        # Код обрабатывает ошибки при выполнении запроса
        logger.error(f'Ошибка при получении данных: {ex}')
        return None
    except (KeyError, TypeError) as ex:
        # Код обрабатывает ошибки при разборе JSON
        logger.error(f'Ошибка при разборе JSON: {ex}')
        return None
```