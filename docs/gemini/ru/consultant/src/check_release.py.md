# Анализ кода модуля `check_release.py`

**Качество кода**
9
-   Плюсы
    - Код соответствует PEP 8, понятен и хорошо структурирован.
    - Используется `logger` для логирования.
    - Функция имеет docstring, описывающий её назначение и аргументы.
-   Минусы
    - Отсутствует обработка исключений при запросе к API GitHub.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - В коде есть `#TODO`, который следует проработать.
    - Есть неиспользуемые строки с комментариями.

**Рекомендации по улучшению**

1.  **Обработка ошибок**: Добавить обработку исключений при выполнении HTTP запроса для более устойчивой работы.
2.  **Логирование**: Использовать `logger.error` для записи ошибок, а также  `from src.logger.logger import logger` .
3.  **Использование `j_loads`**:  В данном коде не требуется использовать `j_loads`, так как JSON обрабатывается библиотекой `requests`.
4.  **Комментарии**: Убрать неиспользуемые закомментированные строки и проработать  `#TODO`.
5.  **Формат Docstring**: Уточнить формат docstring в соответствии с RST.
6.  **Улучшить `return`**: Добавить возвращение `None` при неудачном запросе.
7.  **Удалить неиспользуемый import `json`**: `json` не используется в коде, поэтому его следует удалить.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для проверки последней версии релиза в GitHub репозитории.
==================================================================

Этот модуль содержит функцию :func:`check_latest_release`, которая позволяет
получить последнюю версию релиза из GitHub API.

Пример использования
--------------------

.. code-block:: python

    from src.check_release import check_latest_release

    owner = "test_owner"
    repo = "test_repo"
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f"Latest release: {latest_version}")
    else:
        print("Failed to fetch the latest release.")
"""
MODE = 'dev'

import requests
from src.logger.logger import logger


def check_latest_release(owner: str, repo: str) -> str | None:
    """
    Проверяет последнюю версию релиза в GitHub репозитории.

    :param owner: Владелец репозитория.
    :type owner: str
    :param repo: Название репозитория.
    :type repo: str
    :return: Последняя версия релиза, если доступна, иначе None.
    :rtype: str | None
    :raises requests.exceptions.RequestException: Если происходит ошибка при выполнении запроса.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    try:
        # Выполняется GET запрос к GitHub API для получения информации о последнем релизе
        response = requests.get(url)
        # Код проверяет статус ответа HTTP
        response.raise_for_status() # Raises an exception for 4xx/5xx status codes
        # Код преобразовывает ответ в формат JSON
        latest_release = response.json()
        # Код возвращает значение ключа 'tag_name' из JSON объекта
        return latest_release['tag_name']
    except requests.exceptions.RequestException as ex:
        # Код логирует ошибку, если произошла проблема с запросом
        logger.error(f"Error fetching data for {owner}/{repo}: {ex}")
        return None
    except KeyError as ex:
        # Код логирует ошибку, если поле 'tag_name' не найдено
        logger.error(f"Error getting tag_name from response: {ex}")
        return None

```