# Анализ кода модуля `post_event.py`

**Качество кода**
8
-  Плюсы
    - Код достаточно хорошо структурирован, функции разделены по логическим блокам (отправка заголовка, даты, времени, описания).
    - Используется `SimpleNamespace` для хранения данных, что удобно.
    - Присутствует логирование ошибок с помощью `logger.error`.
    - Применены docstring для функций, что улучшает читаемость.
    - Использование `j_loads_ns` для загрузки локаторов.
-  Минусы
    - Отсутствует описание модуля в формате RST.
    - Docstring не полностью соответствуют стандарту RST (не хватает описания параметров и возвращаемых значений).
    - Присутствуют `...` как точки остановки.
    - Дублирование docstring в функциях `post_date` и `post_time`.
    - В функциях `post_date`, `post_time` и `post_description` дублируется код отправки ошибки, можно вынести в общую функцию.
    - Используется `time.sleep(30)` для ожидания, что не является лучшей практикой.
    - Нет обработки `Exception` в общих функциях отправки данных.
    -  Некоторые комментарии не информативны.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Улучшить docstring функций, добавив описания параметров и возвращаемых значений в формате RST.
3.  Заменить `...` на логику или удалить их, если они не нужны.
4.  Убрать дублирование docstring в функциях `post_date` и `post_time`.
5.  Вынести общий код обработки ошибок в отдельную функцию, чтобы избежать дублирования.
6.  Заменить `time.sleep(30)` на более подходящий механизм ожидания (например, явное ожидание с использованием `WebDriverWait`).
7.  Добавить обработку исключений в общих функциях отправки данных.
8.  Сделать комментарии более информативными.
9.  Добавить общие импорты в начало файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для публикации календарного события в группах Facebook.
=========================================================================================

Этот модуль содержит функции для отправки заголовка, даты, времени и описания
календарного события в группах Facebook с использованием Selenium WebDriver.

Пример использования
--------------------

Пример публикации события:

.. code-block:: python

    driver = Driver(...)
    event_data = SimpleNamespace(
        title="Название события",
        start="2024-07-28 12:00",
        description="Описание события",
        promotional_link="https://example.com"
    )
    post_event(driver, event_data)
"""
import time
from pathlib import Path
from types import SimpleNamespace
from typing import List
from selenium.webdriver.remote.webelement import WebElement

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_event.json')
)

def _execute_and_check(d: Driver, locator: SimpleNamespace, message: str = None) -> bool:
    """
    Выполняет отправку значения в поле и проверяет результат.

    :param d: Экземпляр драйвера.
    :param locator: Локатор элемента.
    :param message: Сообщение для отправки (опционально).
    :return: `True`, если отправка прошла успешно, `False` в противном случае.
    """
    try:
        # Код отправляет значение в поле, используя execute_locator.
        if not d.execute_locator(locator=locator, message=message):
            logger.error(f"Не удалось отправить данные в поле {locator=}", exc_info=False)
            return False
        return True
    except Exception as ex:
        logger.error(f"Ошибка отправки данных в поле {locator=}: {ex}", exc_info=True)
        return False


def post_title(d: Driver, title: str) -> bool:
    """
    Отправляет заголовок события.

    :param d: Экземпляр драйвера.
    :param title: Заголовок события.
    :return: `True`, если заголовок отправлен успешно, `False` в противном случае.

    Примеры:
        >>> driver = Driver(...)
        >>> post_title(driver, "Campaign Title")
        True
    """
    # Код отправляет заголовок события, используя _execute_and_check.
    return _execute_and_check(d, locator.event_title, title)


def post_date(d: Driver, date: str) -> bool:
    """
    Отправляет дату события.

    :param d: Экземпляр драйвера.
    :param date: Дата события.
    :return: `True`, если дата отправлена успешно, `False` в противном случае.

     Примеры:
        >>> driver = Driver(...)
        >>> post_date(driver, "2024-07-28")
        True
    """
    # Код отправляет дату события, используя _execute_and_check.
    return _execute_and_check(d, locator.start_date, date)


def post_time(d: Driver, time: str) -> bool:
    """
    Отправляет время события.

    :param d: Экземпляр драйвера.
    :param time: Время события.
    :return: `True`, если время отправлено успешно, `False` в противном случае.

    Примеры:
        >>> driver = Driver(...)
        >>> post_time(driver, "12:00")
        True
    """
    # Код отправляет время события, используя _execute_and_check.
    return _execute_and_check(d, locator.start_time, time)


def post_description(d: Driver, description: str) -> bool:
    """
    Отправляет описание события.

    :param d: Экземпляр драйвера.
    :param description: Описание события.
    :return: `True`, если описание отправлено успешно, `False` в противном случае.

    Примеры:
        >>> driver = Driver(...)
        >>> post_description(driver, "Event Description")
        True
    """
    # Код прокручивает страницу вниз на 300 пикселей.
    d.scroll(1, 300, 'down')
    # Код отправляет описание события, используя _execute_and_check.
    return _execute_and_check(d, locator.event_description, description)


def post_event(d: Driver, event: SimpleNamespace) -> bool:
    """
    Управляет процессом публикации события с заголовком, описанием и ссылкой.

    :param d: Экземпляр драйвера.
    :param event: Объект SimpleNamespace, содержащий данные события (title, start, description, promotional_link).
    :return: `True`, если публикация прошла успешно, `False` в противном случае.

    Примеры:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", start="2024-07-28 12:00", description="Event Description", promotional_link="https://example.com")
        >>> post_event(driver, event)
    """
    # Код отправляет заголовок события, если отправка не удалась, функция возвращает False.
    if not post_title(d, event.title):
        return False

    # Код разделяет дату и время из строки event.start.
    dt, tm = event.start.split()
    # Код отправляет дату события, если отправка не удалась, функция возвращает False.
    if not post_date(d, dt.strip()):
        return False
     # Код отправляет время события, если отправка не удалась, функция возвращает False.
    if not post_time(d, tm.strip()):
        return False
    # Код отправляет описание и ссылку, если отправка не удалась, функция возвращает False.
    if not post_description(d, f"{event.description}\\n{event.promotional_link}"):
        return False
    # Код кликает по кнопке отправки события, если отправка не удалась, функция возвращает False.
    if not d.execute_locator(locator=locator.event_send):
         return False
    try:
        # Код ожидает пока не появится элемент после отправки.
        WebDriverWait(d.instance, 30).until(
            EC.presence_of_element_located(locator.event_sended)
        )
    except TimeoutException:
        logger.error("Время ожидания отправки события истекло", exc_info=True)
        return False
    return True
```