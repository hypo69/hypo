# Анализ кода модуля `post_event.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на функции, каждая из которых выполняет определенную задачу.
    - Используется `j_loads_ns` для загрузки локаторов, что соответствует рекомендациям.
    - Присутствует логирование ошибок с помощью `logger.error`.
    - Используются docstring для описания функций.
 -  Минусы
    -  Не все docstring соответствуют стандарту reStructuredText (RST).
    -  Много повторяющегося кода в функциях `post_title`, `post_date`, `post_time`, `post_description`.
    - Отсутствуют необходимые импорты, например `Any` из `typing`.
    -  В некоторых docstring отсутствуют типы параметров.
    - В функциях `post_date` и `post_time` повторяется docstring из `post_title`.
    - Отсутствует обработка исключений в блоке `try-except`.

**Рекомендации по улучшению**
1.  **Документация RST:** Переписать docstring в формате reStructuredText (RST) для всех функций, методов и модуля.
2.  **Улучшение docstring:** Добавить типы для параметров в docstring и убедиться в их корректности.
3.  **Устранение дублирования кода:** Вынести общую логику для отправки текста в поле ввода в отдельную функцию.
4. **Обработка ошибок:** Добавить обработку исключений с помощью try-except в `execute_locator`.
5. **Импорты:** Добавить отсутствующие импорты.
6.  **Логирование:** Использовать `logger.debug` для логирования успешных операций и `logger.error` для ошибок.
7.  **Удалить лишние `...`**: Убрать точки остановки из кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для публикации календарного события в группах Facebook.
=========================================================================================

Этот модуль содержит функции для автоматизации процесса публикации календарных событий в группах Facebook,
используя Selenium для взаимодействия с веб-интерфейсом.

Функции модуля:
    - :func:`post_title`: Отправляет заголовок события.
    - :func:`post_date`: Отправляет дату начала события.
    - :func:`post_time`: Отправляет время начала события.
    - :func:`post_description`: Отправляет описание события.
    - :func:`post_event`: Координирует публикацию события, вызывая вспомогательные функции.

Пример использования:
--------------------

.. code-block:: python

    from src.webdriver.driver import Driver
    from types import SimpleNamespace

    driver = Driver(...)
    event_data = SimpleNamespace(
        title="Заголовок события",
        start="2024-07-28 10:00",
        description="Описание события",
        promotional_link="https://example.com"
    )
    post_event(driver, event_data)
"""
MODE = 'dev'

from socket import timeout
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Any
from urllib.parse import urlencode
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns, pprint
from src.logger.logger import logger

# Загрузка локаторов из JSON файла.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_event.json')
)

def _send_text_to_locator(d: Driver, locator: SimpleNamespace, message: str) -> bool:
    """
    Отправляет текст в поле ввода, используя указанный локатор.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param locator: Локатор элемента, в который нужно отправить текст.
    :type locator: SimpleNamespace
    :param message: Текст, который необходимо отправить.
    :type message: str
    :return: `True`, если текст успешно отправлен, `False` в противном случае.
    :rtype: bool
    """
    try:
        if not d.execute_locator(locator=locator, message=message):
            logger.error(f"Не удалось отправить текст в поле с локатором {locator}", exc_info=False)
            return False
        logger.debug(f"Текст успешно отправлен в поле с локатором {locator}")
        return True
    except Exception as ex:
        logger.error(f"Ошибка при отправке текста в поле с локатором {locator}", exc_info=True)
        return False

def post_title(d: Driver, title: str) -> bool:
    """
    Отправляет заголовок события.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param title: Заголовок события.
    :type title: str
    :return: `True`, если заголовок успешно отправлен, `False` в противном случае.
    :rtype: bool

    Примеры:
        >>> driver = Driver(...)
        >>> post_title(driver, "Заголовок события")
        True
    """
    # Отправка заголовка события
    return _send_text_to_locator(d, locator.event_title, title)


def post_date(d: Driver, date: str) -> bool:
    """
    Отправляет дату начала события.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param date: Дата начала события.
    :type date: str
    :return: `True`, если дата успешно отправлена, `False` в противном случае.
    :rtype: bool

    Примеры:
        >>> driver = Driver(...)
        >>> post_date(driver, "2024-07-28")
        True
    """
    # Отправка даты события
    return _send_text_to_locator(d, locator.start_date, date)


def post_time(d: Driver, time: str) -> bool:
    """
    Отправляет время начала события.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param time: Время начала события.
    :type time: str
    :return: `True`, если время успешно отправлено, `False` в противном случае.
    :rtype: bool

    Примеры:
        >>> driver = Driver(...)
        >>> post_time(driver, "10:00")
        True
    """
    # Отправка времени события
    return _send_text_to_locator(d, locator.start_time, time)


def post_description(d: Driver, description: str) -> bool:
    """
    Отправляет описание события.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param description: Описание события.
    :type description: str
    :return: `True`, если описание успешно отправлено, `False` в противном случае.
    :rtype: bool

    Примеры:
        >>> driver = Driver(...)
        >>> post_description(driver, "Описание события")
        True
    """
    # Прокрутка страницы вниз
    d.scroll(1, 300, 'down')
    # Отправка описания события
    return _send_text_to_locator(d, locator.event_description, description)


def post_event(d: Driver, event: SimpleNamespace) -> bool:
    """
    Управляет процессом публикации события, включая заголовок, дату, время, описание и ссылку.

    :param d: Экземпляр драйвера для взаимодействия с веб-страницей.
    :type d: Driver
    :param event: Объект SimpleNamespace, содержащий данные события (заголовок, дату, время, описание, рекламная ссылка).
    :type event: SimpleNamespace
    :return: `True`, если событие успешно опубликовано, `False` в противном случае.
    :rtype: bool

    Примеры:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Заголовок", start="2024-07-28 10:00", description="Описание", promotional_link="https://example.com")
        >>> post_event(driver, event)
        True
    """
    # Отправка заголовка
    if not post_title(d, event.title):
        return False

    # Разбиение даты и времени
    dt, tm = event.start.split()
    # Отправка даты
    if not post_date(d, dt.strip()):
        return False
    # Отправка времени
    if not post_time(d, tm.strip()):
        return False

    # Отправка описания и рекламной ссылки
    if not post_description(d, f"{event.description}\\n{event.promotional_link}"):
        return False
    
    # Отправка события
    if not d.execute_locator(locator = locator.event_send):
        return False
    
    time.sleep(30)

    return True
```