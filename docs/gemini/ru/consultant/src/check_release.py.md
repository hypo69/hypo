# Анализ кода модуля `check_release.py`

**Качество кода**
8
- Плюсы
    - Код выполняет поставленную задачу - проверку последней версии релиза репозитория на GitHub.
    - Используется `logger` для логирования ошибок.
    - Наличие docstring для функции.
    - Использование f-строк для форматирования URL.
- Минусы
    - Не используется `j_loads` для обработки ответа JSON.
    - Обработка ошибок не полная, используется комментарий `TODO: Код не проверен`.
    - Не хватает проверок на наличие необходимых данных в ответе от GitHub.

**Рекомендации по улучшению**
1.  Использовать `j_loads` для обработки JSON ответа.
2.  Улучшить обработку ошибок, логировать ошибку с использованием `logger.error`.
3.  Добавить проверки на наличие необходимых данных в JSON ответе от GitHub.
4.  Убрать закомментированный `logger.error` и `TODO` комментарий, добавить полноценную обработку ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для проверки последней версии релиза на GitHub.
=========================================================================================

Этот модуль содержит функцию `check_latest_release`, которая используется для проверки последней версии релиза репозитория на GitHub.

Пример использования
--------------------

Пример использования функции `check_latest_release`:

.. code-block:: python

    from src.check_release import check_latest_release

    owner = 'user'
    repo = 'repository'
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f"Последняя версия релиза: {latest_version}")
    else:
        print("Не удалось получить данные о последнем релизе.")
"""
import requests
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


def check_latest_release(owner: str, repo: str) -> str | None:
    """Проверяет последнюю версию релиза репозитория на GitHub.

    Args:
        owner (str): Владелец репозитория.
        repo (str): Название репозитория.

    Returns:
        str | None: Последняя версия релиза, если доступна, иначе None.

    Raises:
         requests.exceptions.RequestException: Если произошла ошибка при запросе к GitHub API.
         KeyError: Если в ответе от GitHub API отсутствует поле 'tag_name'.

    Example:
        >>> from src.check_release import check_latest_release
        >>> owner = 'user'
        >>> repo = 'repository'
        >>> latest_version = check_latest_release(owner, repo)
        >>> if latest_version:
        ...     print(f"Последняя версия релиза: {latest_version}")
        ... else:
        ...     print("Не удалось получить данные о последнем релизе.")
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    try:
        # Код выполняет GET-запрос к GitHub API.
        response = requests.get(url)
        response.raise_for_status()  # Код проверяет статус ответа, выбрасывая исключение для ошибок.
    except requests.exceptions.RequestException as ex:
        logger.error(f'Ошибка при запросе к GitHub API: {ex}')
        return None

    try:
         # Код преобразует JSON-ответ в словарь, используя j_loads_ns.
        latest_release = j_loads_ns(response.text)
         # Код извлекает имя тега из ответа.
        return latest_release['tag_name']
    except KeyError as ex:
        logger.error(f'Ошибка при извлечении tag_name из ответа: {ex}')
        return None
    except Exception as ex:
         # Логирование любой другой ошибки.
         logger.error(f'Неизвестная ошибка при обработке ответа: {ex}')
         return None
```