# Анализ кода модуля `post_ad`

**Качество кода**
7
-  Плюсы
    - Код содержит docstring для модуля и функции.
    - Используется `SimpleNamespace` для хранения данных.
    - Логирование ошибок с помощью `logger.error`.
    - Повторные попытки выполнения с ограничением по количеству ошибок.
    - Применяется `j_loads_ns` для загрузки данных.
-  Минусы
    -  Используется глобальная переменная `fails`.
    -  Не всегда используется `logger` для логирования (например, используется `print`).
    -  Не используется обработка исключений с помощью try-except, а просто `return`.
    -  `...` используется как заглушка в коде.
    -  Не все комментарии соответствуют стандарту RST.

**Рекомендации по улучшению**

1.  **Глобальная переменная `fails`**:
    -   Избегать использования глобальных переменных. Передать счетчик ошибок в функцию или использовать класс.

2.  **Логирование**:
    -   Использовать `logger.debug` для отладочных сообщений и `logger.error` для ошибок.
    -   Заменить `print` на `logger.debug` для вывода отладочной информации.
    
3.  **Обработка ошибок**:
    -   Использовать `try-except` блоки для обработки ошибок.
    -   Логировать исключения с помощью `logger.error(f'Сообщение об ошибке', exc_info=True)`.

4.  **`...`**:
    -   Заменить `...` на более конкретную обработку или логику.

5.  **Комментарии**:
    -   Пересмотреть и улучшить docstring для соответствия RST.

6.  **Импорты**:
    -   Удалить неиспользуемые импорты.
    -   Импортировать `logger` как `from src.logger.logger import logger`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для публикации рекламных сообщений в группах Facebook.
=========================================================================================

Этот модуль содержит функцию :func:`post_ad`, которая используется для публикации рекламного сообщения
в группах Facebook, включая отправку заголовка, загрузку медиафайлов и публикацию сообщения.

Пример использования
--------------------

Пример использования функции `post_ad`:

.. code-block:: python

    from src.webdriver.driver import Driver
    from types import SimpleNamespace

    driver = Driver(...)
    message = SimpleNamespace(
        description='Текст рекламного сообщения',
        image_path='/path/to/image.jpg'
    )
    result = post_ad(driver, message)
    print(result)
"""

import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
from urllib.parse import urlencode

from src import gs
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.scenarios import post_message_title, upload_post_media, message_publish
from src.utils.jjson import j_loads_ns, pprint
from src.logger.logger import logger


# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_ad(d: Driver, message: SimpleNamespace, max_fails: int = 15) -> bool:
    """Отправляет рекламное сообщение в Facebook.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace): Сообщение, содержащее описание и путь к изображению.
            Обязательные поля: `description` - текст сообщения.
            Необязательные поля: `image_path` - путь к изображению.
        max_fails (int, optional): Максимальное количество неудачных попыток. По умолчанию 15.

    Returns:
        bool: `True`, если сообщение было успешно опубликовано, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при отправке сообщения.
    
    Example:
        >>> from src.webdriver.driver import Driver
        >>> from types import SimpleNamespace
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(
        ...     description='Текст рекламного сообщения',
        ...     image_path='/path/to/image.jpg'
        ... )
        >>> result = post_ad(driver, message)
        >>> print(result)
        True
    """
    fails = 0
    while fails < max_fails:
        # Код отправляет заголовок сообщения
        if not post_message_title(d, f"{message.description}"):
             logger.error("Ошибка при отправке заголовка сообщения", exc_info=True)
             fails += 1
             logger.debug(f"{fails=}")
             time.sleep(1)
             continue # Код переходит к следующей итерации цикла если отправка заголовка неудачна.

        time.sleep(1)
        # Код проверяет наличие изображения и загружает его
        if hasattr(message, 'image_path') and message.image_path:
            if not upload_post_media(d, media=message.image_path, without_captions=True):
                logger.error("Ошибка при загрузке медиа", exc_info=True)
                return False
        
        # Код выполняет публикацию сообщения.
        if not message_publish(d):
            logger.error("Ошибка при публикации сообщения", exc_info=True)
            return False
        
        return True
    logger.error(f"Превышено максимальное количество попыток ({max_fails}) при отправке сообщения.")
    return False
```