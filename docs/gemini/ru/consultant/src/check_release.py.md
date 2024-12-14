# Анализ кода модуля `check_release.py`

**Качество кода**
8
- Плюсы
    - Код написан на Python и соответствует PEP 8.
    - Присутствует docstring для функции.
    - Используется f-строка для форматирования URL.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` для обработки JSON.
    - Обработка ошибок происходит с помощью `if/else`, а не с помощью логирования через `logger.error`.
    - Возврат `None` происходит без явного указания.
    - Не хватает RST документации для модуля.

**Рекомендации по улучшению**
1. Добавить RST документацию для модуля.
2. Использовать `j_loads` или `j_loads_ns` для обработки JSON ответа.
3. Использовать `logger.error` для логирования ошибок при запросе.
4. Явно возвращать `None` в случае ошибки.
5. Добавить комментарии в формате RST к каждой строке кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для проверки последней версии релиза на GitHub
====================================================

Этот модуль содержит функцию :func:`check_latest_release`, которая проверяет последнюю версию релиза
репозитория на GitHub.

Пример использования
--------------------

.. code-block:: python

    from src.check_release import check_latest_release

    owner = "your_repo_owner"
    repo = "your_repo_name"
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f"Последняя версия релиза: {latest_version}")
    else:
        print("Не удалось получить информацию о последней версии релиза.")

"""
MODE = 'dev'

import requests # Импорт библиотеки requests для выполнения HTTP-запросов
from src.logger.logger import logger # Импорт логгера из src.logger.logger
from src.utils.jjson import j_loads # импорт j_loads для обработки json

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
    # Формирование URL для запроса к API GitHub
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    # Выполнение GET запроса к API GitHub
    response = requests.get(url)

    # Проверка кода ответа
    if response.status_code == 200:
        try:
            # Десериализация JSON-ответа с помощью j_loads
            latest_release = j_loads(response.text)
            # Возврат имени тега последнего релиза
            return latest_release['tag_name']
        except Exception as ex:
            # Логирование ошибки при обработке JSON
            logger.error(f'Ошибка при десериализации JSON: {ex}', exc_info=True)
            return None
    else:
        # Логирование ошибки при получении ответа от GitHub API
        logger.error(f'Ошибка при выполнении запроса: {response.status_code}')
        return None # Возврат None в случае ошибки

```