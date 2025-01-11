# Анализ кода модуля `driver.py`

**Качество кода**
8
-  Плюсы
     -  Хорошая структура кода, с разделением на базовый класс `DriverBase` и метакласс `DriverMeta` для динамического создания драйверов.
     -  Использование `ActionChains`, `WebDriverWait` и других стандартных средств `selenium` для взаимодействия с браузером.
     -  Реализованы общие методы для работы с веб-страницами, такие как прокрутка, определение языка, сохранение куки.
     -  Используется `logger` для логирования ошибок.
-  Минусы
    -  Отсутствует документация в формате RST.
    -  Некоторые методы имеют избыточную обработку исключений с использованием `try-except`.
    -  Не все импорты оптимизированы.
    -  Не хватает docstring для классов, методов, переменных.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для всех классов, методов и переменных.
2.  Использовать `logger.error` для обработки исключений вместо стандартных блоков `try-except`.
3.  Уточнить docstring для класса `Driver` и добавить примеры использования.
4.  Привести все импорты в соответствие с принятыми стандартами проекта.
5.  Убрать `print`  использовать  `logger` вместо.
6.  Оптимизировать методы `scroll`, `_save_cookies_localy`, `get_url`.

**Оптимизированный код**

```python
"""
Модуль для управления веб-драйверами
=========================================================================================

Этот модуль предоставляет базовый класс :class:`DriverBase` и метакласс :class:`DriverMeta`
для динамического создания веб-драйверов. Класс :class:`Driver` используется для взаимодействия
с различными браузерами, такими как Chrome, Firefox и Edge.

Пример использования
--------------------

Пример создания драйвера и выполнения базовых операций:

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome, Firefox, Edge

    # Создание драйвера Chrome
    driver = Driver(Chrome)

    # Переход на страницу
    driver.get_url("https://example.com")

    # Прокрутка страницы
    driver.scroll(scrolls=2, frame_size=500, direction='forward', delay=0.5)

    # Получение языка страницы
    lang = driver.locale()

"""
import sys
import pickle
import time
import copy
from pathlib import Path
from typing import Type, Union, Any
import urllib.parse

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)

from src import gs # импорт gs не используется в коде
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript
from src.utils.printer import pprint
from src.logger.logger import logger
from src.logger.exceptions import WebDriverException


class DriverBase:
    """
    Базовый класс для веб-драйверов с общими атрибутами и методами.

    Этот класс содержит методы и атрибуты, общие для всех реализаций веб-драйверов,
    включая функциональность для взаимодействия со страницей, выполнения JavaScript и управления куки.

    Attributes:
        previous_url (str): URL предыдущей страницы.
        referrer (str): Реферер страницы.
        page_lang (str): Язык текущей страницы.
    """
    previous_url: str = ''
    referrer: str = ''
    page_lang: str = ''

    def __init__(self, webdriver):
        """
        Инициализирует объект DriverBase.

        Args:
            webdriver: Экземпляр веб-драйвера.
        """
        self.driver = webdriver
        self.js = None  # Инициализируется в driver_payload
        self.execute_locator = None # Инициализируется в driver_payload

    def driver_payload(self):
        """
        Инициализирует методы JavaScript и ExecuteLocator.
        """
        self.js = JavaScript(self.driver)
        self.execute_locator = ExecuteLocator(self.driver)

    def scroll(self, scrolls: int = 1, frame_size: int = 500, direction: str = 'forward', delay: float = 0.5) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        Args:
            scrolls (int): Количество прокруток.
            frame_size (int): Размер кадра прокрутки в пикселях.
            direction (str): Направление прокрутки ('forward' или 'backward').
            delay (float): Задержка между прокрутками.

        Returns:
            bool: True, если прокрутка выполнена успешно, False в противном случае.
        """
        try:
            # Код исполняет прокрутку страницы
            for _ in range(scrolls):
                if direction == 'forward':
                    self.js.execute(f'window.scrollBy(0, {frame_size});')
                elif direction == 'backward':
                    self.js.execute(f'window.scrollBy(0, -{frame_size});')
                else:
                     logger.error(f'Неверное направление {direction=}, используйте forward или backward')
                     return False
                time.sleep(delay)
            return True
        except Exception as ex:
           logger.error('Ошибка прокрутки страницы', ex)
           return False


    def locale(self) -> str:
        """
        Определяет язык страницы.

        Returns:
            str: Язык страницы, если он определен, иначе пустая строка.
        """
        # Код исполняет получение языка страницы
        self.page_lang = self.js.execute('return document.documentElement.lang') or ''
        return self.page_lang

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и проверяет успешность перехода.

        Args:
            url (str): URL для перехода.

        Returns:
            bool: True, если переход выполнен успешно, False в противном случае.
        """
        try:
            # Код исполняет переход на указанную страницу
            self.referrer = self.driver.current_url
            self.driver.get(url)
            current_url = self.driver.current_url
            if current_url != url:
                logger.error(f'Не удалось перейти по ссылке: {url=}, текущий адрес: {current_url=}')
                return False
            self.previous_url = url
            return True
        except Exception as ex:
           logger.error(f'Ошибка при переходе на страницу {url=}', ex)
           return False


    def extract_domain(self, url: str) -> str:
        """
        Извлекает доменное имя из URL.

        Args:
            url (str): URL для извлечения домена.

        Returns:
            str: Доменное имя или пустая строка, если URL недействителен.
        """
        try:
            # Код исполняет извлечение домена из URL
            parsed_url = urllib.parse.urlparse(url)
            return parsed_url.netloc
        except Exception as ex:
            logger.error(f'Не удалось извлечь домен из {url=}', ex)
            return ''

    def _save_cookies_localy(self, to_file: Union[str, Path]) -> bool:
        """
        Сохраняет куки в файл.

        Args:
            to_file (Union[str, Path]): Путь к файлу для сохранения куки.

        Returns:
            bool: True, если куки успешно сохранены, False в противном случае.
        """
        try:
            # Код исполняет получение куки
            cookies = self.driver.get_cookies()
            # Код исполняет сохранение куки в файл
            with open(to_file, 'wb') as file:
                pickle.dump(cookies, file)
            return True
        except Exception as ex:
            logger.error(f'Не удалось сохранить cookies в файл {to_file=}', ex)
            return False


    def page_refresh(self) -> bool:
        """
        Обновляет текущую страницу.

        Returns:
            bool: True, если страница успешно обновлена, False в противном случае.
        """
        try:
            # Код исполняет обновление текущей страницы
            self.driver.refresh()
            return True
        except Exception as ex:
            logger.error('Не удалось обновить страницу', ex)
            return False


    def window_focus(self) -> bool:
        """
        Восстанавливает фокус на странице.

         Returns:
            bool: True, если фокус на странице успешно восстановлен, False в противном случае.
        """
        try:
            # Код исполняет восстановление фокуса на странице
            self.driver.switch_to.window(self.driver.current_window_handle)
            return True
        except Exception as ex:
            logger.error('Не удалось восстановить фокус на странице', ex)
            return False


    def wait(self, interval: float) -> None:
        """
        Делает паузу на указанное время.

        Args:
            interval (float): Время паузы в секундах.
        """
        time.sleep(interval)


    def delete_driver_logs(self) -> None:
        """
        Удаляет временные файлы и логи WebDriver.
        """
        # TODO: Реализовать удаление логов, если требуется
        ...



class DriverMeta(type):
    """
    Метакласс для создания классов Driver.

    Этот метакласс динамически создает класс Driver, который наследует от DriverBase
    и указанного класса веб-драйвера.
    """
    def __call__(cls, webdriver_cls: Type, *args, **kwargs) -> type:
        """
        Создает новый класс Driver, который наследует от DriverBase и указанного класса WebDriver.

        Args:
            webdriver_cls (Type): Класс веб-драйвера (например, Chrome, Firefox, Edge).
            *args: Позиционные аргументы для инициализации веб-драйвера.
            **kwargs: Именованные аргументы для инициализации веб-драйвера.

        Returns:
             type: Новый класс Driver.
        """
        # Код исполняет создание класса Driver
        class Driver(DriverBase, webdriver_cls):
            """
            Динамически созданный класс WebDriver, который наследует от DriverBase и указанного класса WebDriver.

            Example:
                >>> from src.webdriver.driver import Driver, Chrome
                >>> d = Driver(Chrome)
            """
            def __init__(self, *args, **kwargs):
                """
                Инициализирует драйвер.
                """
                webdriver_cls.__init__(self, *args, **kwargs)
                DriverBase.__init__(self, self)
                self.driver_payload()
        return Driver


class Driver(metaclass=DriverMeta):
    """
    Динамически созданный класс WebDriver, который наследует от DriverBase и указанного класса WebDriver.

    Этот класс создается с использованием метакласса `DriverMeta`.
    """
    ...
```