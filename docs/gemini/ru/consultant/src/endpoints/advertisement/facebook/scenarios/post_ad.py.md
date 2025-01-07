# Анализ кода модуля `post_ad.py`

**Качество кода**

6
- Плюсы
    - Код использует `SimpleNamespace` для передачи данных, что упрощает работу с параметрами.
    - Используется логгер для записи ошибок.
    - Присутствует базовая обработка ошибок.
    -  Есть описание модуля и функций в формате docstring.
- Минусы
    - Не все импорты используются.
    - Некоторые комментарии отсутствуют или недостаточно подробны.
    - Используется глобальная переменная `fails`, что может усложнить отладку.
    - Логика обработки ошибок может быть улучшена.
    - Формат docstring не полностью соответствует стандарту reStructuredText (RST).
    -  Отсутствуют комментарии в коде, объясняющие логику работы.
    -  Используется `print` вместо `logger.debug/info`.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки файла `post_message.json`.

**Рекомендации по улучшению**

1.  Удалить неиспользуемые импорты.
2.  Использовать `j_loads_ns` для загрузки `post_message.json`.
3.  Переписать комментарии и docstring в формате RST, как указано в инструкции.
4.  Убрать глобальную переменную `fails` и заменить ее на возвращаемое значение.
5.  Избегать `print` и использовать `logger.debug/info` для отладочной информации.
6.  Добавить обработку ошибок с использованием `logger.error`.
7.  Добавить комментарии в коде, описывающие логику работы.
8.  Добавить более подробные описания функций в docstring.
9.  Использовать константы для магических чисел (например, 15).
10. Заменить множественные `return` на более читаемый код.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для публикации рекламных сообщений в группах Facebook.
=============================================================

Этот модуль содержит функцию :func:`post_ad`, которая автоматизирует процесс публикации
рекламных сообщений в группах Facebook, включая добавление текста и медиафайлов.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.driver import Driver
    from types import SimpleNamespace

    driver = Driver(...)
    message = SimpleNamespace(description="Текст сообщения", image_path="path/to/image.jpg")
    result = post_ad(driver, message)
    if result:
        print("Реклама успешно опубликована")
    else:
        print("Не удалось опубликовать рекламу")
"""
import time
from pathlib import Path
from types import SimpleNamespace

from src import gs
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.scenarios import post_message_title, upload_post_media, message_publish
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)

MAX_FAILS: int = 15  # Максимальное количество неудачных попыток

def post_ad(d: Driver, message: SimpleNamespace) -> bool:
    """
    Публикует рекламное сообщение, включая заголовок, медиа и само сообщение.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param message: Объект SimpleNamespace, содержащий текст и путь к изображению (если есть).
                  Обязательные поля: `description` (текст сообщения), `image_path` (путь к медиафайлу).
    :type message: SimpleNamespace
    :return: True в случае успешной публикации, False в противном случае.
    :rtype: bool

    :raises Exception: В случае ошибок при публикации сообщения.

    :Example:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(description="Рекламный текст", image_path="image.jpg")
        >>> post_ad(driver, message)
        True
    """
    fails: int = 0
    while fails < MAX_FAILS:
        # Отправка заголовка сообщения
        if not post_message_title(d, f"{message.description}"):
            logger.error("Не удалось отправить заголовок сообщения.", exc_info=True)
            fails += 1
            logger.debug(f"Количество неудачных попыток: {fails}")
            time.sleep(1)
            continue  # Переход к следующей итерации цикла

        time.sleep(1)
        # Загрузка медиа, если есть путь к изображению
        if hasattr(message, 'image_path') and message.image_path:
            if not upload_post_media(d, media=message.image_path, without_captions=True):
                logger.error(f"Не удалось загрузить медиа файл: {message.image_path}", exc_info=True)
                return False
        # Публикация сообщения
        if not message_publish(d):
            logger.error("Не удалось опубликовать сообщение.", exc_info=True)
            return False

        return True
    # Если количество неудачных попыток превышено.
    logger.error(f"Превышено максимальное количество неудачных попыток ({MAX_FAILS}).")
    return False
```