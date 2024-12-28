# Анализ кода модуля `driver.py`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и использует объектно-ориентированный подход.
    -   Присутствует разделение на базовый класс `DriverBase` и метакласс `DriverMeta`, что способствует расширяемости и повторному использованию кода.
    -   Используются стандартные библиотеки `selenium` для управления браузером, а также собственные модули для логирования, выполнения JavaScript и обработки исключений.
    -   Логика работы с куками вынесена в отдельный метод.
    -   В целом код имеет хорошую читаемость.
-   Минусы
    -   Отсутствует docstring для модуля, что затрудняет понимание его назначения.
    -   В некоторых методах отсутствуют подробные docstring, особенно в `DriverBase`, что снижает понимание функциональности класса.
    -   Не везде используется `logger.error` для обработки исключений, что усложняет отладку.
    -   Использование `...` в коде в качестве заглушек усложняет отладку.
    -   Отсутствуют некоторые необходимые импорты.

**Рекомендации по улучшению**

1.  **Добавить docstring модуля**:
    -   Добавить подробное описание модуля в формате RST, включая примеры использования.
2.  **Улучшить docstring методов**:
    -   Добавить подробные описания для каждого метода в формате RST.
    -   Указать типы аргументов и возвращаемых значений.
3.  **Использовать `logger.error` для обработки исключений**:
    -   Заменить стандартные `try-except` блоки на обработку ошибок с помощью `logger.error`, добавив информацию об исключении.
4.  **Добавить импорты**:
    -   Добавить отсутствующие импорты, такие как `Any` из `typing`.
5.  **Убрать `...`**:
    -   Убрать `...` из кода и обработать ошибки используя `logger.error`, где это необходимо.
6.  **Унифицировать код**:
     -  Убедиться, что все комментарии, переменные и импорты соответствуют ранее обработанным файлам.
7.  **Добавить закрытие драйвера**:
    -  Добавить метод для закрытия драйвера.

**Оптимизированный код**

```python
"""
Модуль для работы с веб-драйверами.
=========================================================================================

Этот модуль предоставляет базовые классы и метакласс для управления веб-драйверами,
такие как Chrome, Firefox и Edge, на основе библиотеки Selenium.
Модуль включает функциональность для взаимодействия с веб-страницами, выполнения JavaScript,
управления куками и обработки исключений.

Пример использования
--------------------

Пример использования класса `Driver`:

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome
    driver_instance = Driver(Chrome)
    driver_instance.get_url("https://example.com")
    driver_instance.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)

"""
import sys
import pickle
import time
import copy
from pathlib import Path
from typing import Type, Union, Any  # Добавлен импорт Any
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

from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript
from src.utils.printer import pprint
from src.logger.logger import logger
from src.logger.exceptions import WebDriverException


class DriverBase:
    """
    Базовый класс для веб-драйвера с общими атрибутами и методами.
    =========================================================================================

    Этот класс содержит методы и атрибуты, общие для всех реализаций WebDriver,
    включая функциональные возможности для взаимодействия со страницей,
    выполнения JavaScript и управления куками.
    """
    previous_url: str = ''
    referrer: str = ''
    page_lang: str = ''
    ready_state: str = 'complete'
    
    def get_page_lang(self) -> str:
        """
        Код исполняет получение языка текущей страницы.

        :return: Язык страницы.
        """
        return self.driver.execute_script('return document.documentElement.lang')

    def get_location(self) -> str:
        """
        Код исполняет получение текущего URL страницы.

        :return: URL текущей страницы.
        """
        return self.driver.execute_script('return document.location.href')

    def get_title(self) -> str:
        """
        Код исполняет получение заголовка текущей страницы.

        :return: Заголовок страницы.
        """
        return self.driver.execute_script('return document.title')

    def get_url_without_parameters(self, url: str) -> str:
        """
        Код исполняет удаление параметров из URL.

        :param url: URL для обработки.
        :return: URL без параметров.
        """
        return urllib.parse.urljoin(url, urllib.parse.urlparse(url).path)

    def get_url_parameters(self, url: str) -> dict:
        """
        Код исполняет извлечение параметров из URL.

        :param url: URL для обработки.
        :return: Словарь параметров URL.
        """
        return dict(urllib.parse.parse_qsl(urllib.parse.urlparse(url).query))

    def get_page_source(self) -> str:
        """
        Код исполняет получение исходного кода текущей страницы.

        :return: Исходный код страницы.
        """
        return self.driver.page_source

    def driver_payload(self):
        """
        Инициализация методов JavaScript и ExecuteLocator.
        """
        self.js = JavaScript(self.driver)
        self.executor = ExecuteLocator(self.driver)

    def scroll(self, scrolls: int = 3, frame_size: int = 500, direction: str = 'forward', delay: float = 0.5):
        """
        Выполняет прокрутку страницы.

        :param scrolls: Количество прокруток.
        :param frame_size: Размер прокрутки в пикселях.
        :param direction: Направление прокрутки ('forward' или 'backward').
        :param delay: Задержка между прокрутками в секундах.
        """
        try:
            if direction == 'forward':
                for _ in range(scrolls):
                    self.driver.execute_script(f'window.scrollBy(0,{frame_size});')
                    self.wait(delay)
            elif direction == 'backward':
                for _ in range(scrolls):
                    self.driver.execute_script(f'window.scrollBy(0,-{frame_size});')
                    self.wait(delay)
            else:
                logger.error(f'Неверное направление прокрутки {direction=}')
        except Exception as ex:
            logger.error(f'Ошибка при прокрутке страницы: {ex}')

    def locale(self) -> str:
        """
        Определение языка страницы.

        :return: Язык страницы.
        """
        try:
             lang = self.get_page_lang()
             self.page_lang = lang if lang else  self.page_lang
             return  self.page_lang
        except Exception as ex:
            logger.error(f'Ошибка определения языка страницы {ex}')
            return self.page_lang

    def get_url(self, url: str):
        """
        Код исполняет переход по указанному URL.

        :param url: URL для перехода.
        """
        try:
            self.previous_url = self.get_location() if self.get_location() else self.previous_url
            self.driver.get(url)
            if not self.get_location() == url:
                logger.error(f'Ошибка перехода на {url}')
        except Exception as ex:
            logger.error(f'Ошибка перехода по URL: {url} {ex}')

    def extract_domain(self, url: str) -> str:
        """
        Код исполняет извлечение доменного имени из URL.

        :param url: URL для обработки.
        :return: Доменное имя.
        """
        try:
            return urllib.parse.urlparse(url).netloc
        except Exception as ex:
            logger.error(f'Ошибка извлечения домена из URL: {url} {ex}')
            return ''

    def _save_cookies_localy(self, to_file: Union[str, Path]):
        """
        Код исполняет сохранение куки в локальный файл.

        :param to_file: Путь к файлу для сохранения куки.
        """
        try:
            cookies = self.driver.get_cookies()
            pickle.dump(cookies, open(to_file, 'wb'))
        except Exception as ex:
             logger.error(f'Ошибка при сохранении куки в файл: {to_file} {ex}')

    def page_refresh(self):
        """
        Код исполняет обновление текущей страницы.
        """
        try:
             self.driver.refresh()
        except Exception as ex:
            logger.error(f'Ошибка при обновлении страницы {ex}')

    def window_focus(self):
        """
        Код исполняет восстановление фокуса на текущем окне.
        """
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
        except Exception as ex:
            logger.error(f'Ошибка при переключении фокуса на окно {ex}')

    def wait(self, interval: float):
        """
        Код исполняет приостановку выполнения на указанное время.

        :param interval: Время приостановки в секундах.
        """
        try:
            time.sleep(interval)
        except Exception as ex:
            logger.error(f'Ошибка паузы {ex}')

    def delete_driver_logs(self):
        """
        Код исполняет удаление временных файлов и логов WebDriver.
        """
        try:
            if gs.temp_dir.exists():
                for item in gs.temp_dir.iterdir():
                     item.unlink()
        except Exception as ex:
            logger.error(f'Ошибка при удалении логов драйвера {ex}')

    def close_driver(self):
        """
        Код исполняет закрытие драйвера.
        """
        try:
            self.driver.quit()
        except Exception as ex:
            logger.error(f'Ошибка закрытия драйвера {ex}')


class DriverMeta(type):
    """
    Метакласс для динамического создания класса Driver.
    =========================================================================================
    """
    def __call__(cls, webdriver_cls: Type, *args, **kwargs):
        """
        Создает новый класс Driver, который наследует от DriverBase и указанного класса WebDriver.
        
        :param webdriver_cls: Класс WebDriver, от которого наследовать.
        :param args: Аргументы для инициализации класса WebDriver.
        :param kwargs: Именованные аргументы для инициализации класса WebDriver.
        """
        class Driver(DriverBase, webdriver_cls):
            """
            Динамически созданный класс WebDriver, который наследует от DriverBase и указанного класса WebDriver.
            """
            def __init__(self, *args, **kwargs):
                """
                Инициализация драйвера и вызов метода driver_payload.

                :param args: Аргументы для инициализации класса WebDriver.
                :param kwargs: Именованные аргументы для инициализации класса WebDriver.
                """
                webdriver_cls.__init__(self, *args, **kwargs)
                DriverBase.driver_payload(self)


        return Driver


class Driver(metaclass=DriverMeta):
    """
    Динамически созданный класс WebDriver, который наследует от DriverBase и указанного класса WebDriver.
    
    :code
    from src.webdriver.driver import Driver, Chrome, Firefox, Edge
    d = Driver(Chrome)
    :endcode
    """
    ...
```