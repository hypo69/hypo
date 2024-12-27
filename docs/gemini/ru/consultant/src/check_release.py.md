# Анализ кода модуля `check_release.py`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и легко читается.
    - Используется форматирование f-strings для создания URL.
    - Присутствует docstring для функции `check_latest_release`.
    - Используется `requests` для работы с API.

 -  Минусы
    - Отсутствует явная обработка ошибок при `requests.get`.
    - Закомментирована строка `logger.error` и `TODO` комментарий
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для обработки JSON.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для обработки ответа от API.
2.  Заменить стандартную обработку ошибок на `logger.error`.
3.  Убрать закомментированный код и `TODO` комментарии.
4.  Использовать RST для docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для проверки последней версии релиза на GitHub.
====================================================

Этот модуль предоставляет функцию :func:`check_latest_release`,
которая позволяет проверить последнюю версию релиза для заданного
репозитория на GitHub.

Пример использования
--------------------

.. code-block:: python

    from src.check_release import check_latest_release

    owner = 'owner'
    repo = 'repo'
    latest_version = check_latest_release(owner, repo)
    if latest_version:
        print(f"Последняя версия релиза: {latest_version}")
    else:
        print("Не удалось получить информацию о релизе.")
"""
MODE = 'dev'

import requests
# Добавлен импорт j_loads из src.utils.jjson
from src.utils.jjson import j_loads
from src.logger.logger import logger


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
    #  Выполняется запрос к API GitHub
    try:
        response = requests.get(url)
        #  Проверка статуса ответа. Если не 200 - логируем ошибку и возвращаем None
        response.raise_for_status()
        #  Загрузка JSON ответа с помощью j_loads
        latest_release = j_loads(response.text)
        #  Возвращает имя тега из JSON
        return latest_release['tag_name']
    except requests.exceptions.RequestException as e:
         #  Логируем ошибку, если не удалось получить данные от API
        logger.error(f"Ошибка получения данных: {e}")
        return None
    except (KeyError, TypeError) as e:
        #  Логируем ошибку, если не удалось получить tag_name из JSON
        logger.error(f"Ошибка обработки данных: {e}")
        return None
```