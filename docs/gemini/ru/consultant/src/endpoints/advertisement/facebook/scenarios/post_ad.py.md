# Анализ кода модуля `post_ad.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и логически разделен на функции.
    - Используется `SimpleNamespace` для передачи данных, что упрощает доступ к атрибутам.
    - Присутствует обработка ошибок с использованием `logger.error`
    - Используются комментарии, объясняющие назначение кода.
    - Используется `j_loads_ns` для загрузки локаторов из JSON.

- Минусы
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - Отсутствует общая документация модуля в формате RST.
    - Не все функции документированы в формате RST.
    - Используется глобальная переменная `fails`, что может затруднить отладку и масштабирование.
    - Отсутствуют проверки на типы данных.
    - Присутсвует заглушка `...`
    - Отсутсвует обработка `timeout` и других исключений.
    - Присутсвует вывод в консоль  `print(f"{fails=}")` вместо логирования.
    - Ожидание `time.sleep(1)` не желательно.
    - Нет проверки на наличие `description` и `image_path` в message.
    - Функция возвращает `None` без предупреждения, хотя указан `bool`

**Рекомендации по улучшению**

1.  Добавить документацию модуля в формате RST.
2.  Переписать все docstring функций в формате RST.
3.  Убрать глобальную переменную `fails` и сделать её локальной.
4.  Исключить использование `time.sleep(1)` заменив его ожиданиями.
5.  Заменить `print(f"{fails=}")` на `logger.debug(f"fails={fails}")`.
6.  Добавить валидацию типов данных в функциях.
7.  Добавить обработку исключений `timeout`
8.  Добавить проверки на наличие атрибутов `description` и `image_path` в message.
9.  Убрать заглушку `...`
10. Улучшить обработку ошибок, чтобы не возвращать `None` там, где ожидается `bool`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для публикации рекламных сообщений в группах Facebook.
============================================================

Этот модуль содержит функцию :func:`post_ad`, которая используется для публикации рекламных сообщений в группах Facebook.
Используется  `selenium` для взаимодействия с веб-страницей.

Пример использования
--------------------

Пример использования функции `post_ad`:

.. code-block:: python

    driver = Driver(...)
    message = SimpleNamespace(
        description="Текст сообщения",
        image_path="путь/к/изображению.jpg",
    )
    result = post_ad(driver, message)
    if result:
        print("Сообщение опубликовано успешно")
    else:
        print("Ошибка публикации сообщения")
"""

import time
from pathlib import Path
from types import SimpleNamespace
from typing import  Optional
from socket import timeout


from src import gs
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.scenarios import post_message_title, upload_post_media, message_publish
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger



# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_ad(d: Driver, message: SimpleNamespace) -> bool:
    """
    Публикует рекламное сообщение в группе Facebook.

    :param d: Драйвер Selenium для взаимодействия с веб-страницей.
    :type d: src.webdriver.driver.Driver
    :param message: Объект SimpleNamespace, содержащий текст сообщения и путь к изображению.
    :type message: types.SimpleNamespace
    :return: `True`, если сообщение было успешно опубликовано, в противном случае `False`.
    :rtype: bool

    :raises TypeError: Если `d` не является экземпляром `Driver` или `message` не является экземпляром `SimpleNamespace`.
    :raises ValueError: Если `message` не содержит необходимых атрибутов.
    :raises timeout: При таймауте соединения.

    Пример:
    
    .. code-block:: python

        driver = Driver(...)
        message = SimpleNamespace(
            description="Текст сообщения",
            image_path="путь/к/изображению.jpg",
        )
        result = post_ad(driver, message)
        if result:
            print("Сообщение опубликовано успешно")
        else:
            print("Ошибка публикации сообщения")
    """
    if not isinstance(d, Driver):
        logger.error(f"Ожидался тип Driver, получен {type(d)}")
        raise TypeError(f"Ожидался тип Driver, получен {type(d)}")
    if not isinstance(message, SimpleNamespace):
        logger.error(f"Ожидался тип SimpleNamespace, получен {type(message)}")
        raise TypeError(f"Ожидался тип SimpleNamespace, получен {type(message)}")

    fails = 0
    max_fails = 15

    if not hasattr(message, 'description') or not message.description:
            logger.error("Сообщение не содержит описание")
            return False
    
    try:
        # Код отправляет заголовок сообщения
        if not post_message_title(d, f"{message.description}"):
            logger.error("Не удалось отправить заголовок сообщения")
            fails += 1
            if fails < max_fails:
                 logger.debug(f"Количество неудачных попыток {fails=}")
                 return False
            else:
                logger.error(f"Достигнуто максимальное количество попыток ({max_fails=}).")
                return False
    except timeout as ex:
         logger.error("Таймаут при отправке заголовка сообщения", exc_info=True)
         return False
    except Exception as ex:
        logger.error(f"Неизвестная ошибка при отправке заголовка сообщения {ex=}", exc_info=True)
        return False

    # Код ожидает 1 секунду
    # time.sleep(1)

    if hasattr(message, 'image_path') and message.image_path:
        try:
           # Код загружает медиа файл если он есть
           if not upload_post_media(d, media=message.image_path, without_captions=True):
               logger.error("Не удалось загрузить медиа файл")
               return False
        except timeout as ex:
            logger.error("Таймаут при загрузке медиа файла", exc_info=True)
            return False
        except Exception as ex:
            logger.error(f"Неизвестная ошибка при загрузке медиа {ex=}", exc_info=True)
            return False
    try:
       # Код публикует сообщение
       if not message_publish(d):
          logger.error("Не удалось опубликовать сообщение")
          return False
    except timeout as ex:
        logger.error("Таймаут при публикации сообщения", exc_info=True)
        return False
    except Exception as ex:
        logger.error(f"Неизвестная ошибка при публикации сообщения {ex=}", exc_info=True)
        return False
    # Код сбрасывает счетчик неудач
    fails = 0
    return True
```