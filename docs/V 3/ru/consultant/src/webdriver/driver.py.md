## Анализ кода модуля `driver.py`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Наличие документации к классам и методам.
  - Использование `logger` для логирования ошибок.
  - Обработка исключений при работе с WebDriver.
- **Минусы**:
  - Не везде используются аннотации типов.
  - Смешанный стиль кавычек (используются как одинарные, так и двойные).
  - Не все методы документированы в соответствии с заданным форматом.
  - Отсутствует использование `j_loads` или `j_loads_ns` для работы с JSON файлами.
  - Присутствуют закомментированные строки кода (`return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`).
  - В некоторых блоках `try-except` отсутствует конкретизация исключений.

**Рекомендации по улучшению:**

1.  **Приведение к единому стилю кавычек**:
    - Заменить все двойные кавычки на одинарные, где это необходимо.
2.  **Документирование методов**:
    - Привести все docstring к единому формату, используя Markdown.
    - Добавить примеры использования в docstring.
3.  **Использовать аннотации типов**:
    - Добавить аннотации типов для всех аргументов и возвращаемых значений функций и методов.
4.  **Удаление закомментированного кода**:
    - Убрать закомментированные строки (`return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`).
5.  **Конкретизация исключений**:
    - Указывать конкретные типы исключений в блоках `except`, чтобы избежать перехвата неожиданных ошибок.
6.  **Использовать `j_loads` или `j_loads_ns`**:
    - Заменить использование `open` и `json.load` на `j_loads` или `j_loads_ns`, если это необходимо.
7.  **Улучшение обработки ошибок**:
    - Добавить `exc_info=True` в вызовы `logger.error`, чтобы получать трассировку стека.

**Оптимизированный код:**

```python
## \file /src/webdriver/driver.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для работы с веб-драйверами Selenium.
=================================================

Модуль driver.py предназначен для работы с веб-драйверами Selenium.
Он предоставляет унифицированный интерфейс для взаимодействия с различными веб-браузерами,
такими как Chrome, Firefox и Edge. Драйверы находятся в подмодулях `chrome\\chrome.py`, `firefox\\firefox.py`, `edge\\edge.py`, `playwright\\playwright.py`.
Файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`.
Класс Driver упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

Пример использования
----------------------

>>> from selenium.webdriver import Chrome
>>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
>>> driver.get('https://www.example.com')
"""

import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional, Type
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)

import header  # FIXME: что это за модуль ?

from src import gs
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException


class Driver:
    """
    Унифицированный класс для взаимодействия с Selenium WebDriver.

    Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

    Attributes:
        driver (selenium.webdriver): Экземпляр Selenium WebDriver.

    Example:
        >>> from selenium.webdriver import Chrome
        >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """

    def __init__(self, webdriver_cls: Type, *args, **kwargs) -> None:
        """
        Инициализирует экземпляр класса Driver.

        Args:
            webdriver_cls (Type): Класс WebDriver, например Chrome или Firefox.
            *args: Позиционные аргументы для драйвера.
            **kwargs: Ключевые аргументы для драйвера.

        Raises:
            TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.

        Example:
            >>> from selenium.webdriver import Chrome
            >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs) -> None:
        """
        Автоматически вызывается при создании подкласса `Driver`.

        Args:
            browser_name (Optional[str]): Имя браузера.
            **kwargs: Дополнительные аргументы.

        Raises:
            ValueError: Если browser_name не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item: str):
        """
        Прокси для доступа к атрибутам драйвера.

        Args:
            item (str): Имя атрибута.

        Returns:
            Any: Значение атрибута драйвера.

        Example:
            >>> driver.current_url
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        Args:
            scrolls (int): Количество прокруток, по умолчанию 1.
            frame_size (int): Размер прокрутки в пикселях, по умолчанию 600.
            direction (str): Направление ('both', 'down', 'up'), по умолчанию 'both'.
            delay (float): Задержка между прокрутками, по умолчанию 0.3.

        Returns:
            bool: `True`, если успешно, иначе `False`.

        Example:
            >>> driver.scroll(scrolls=3, direction='down')
        """

        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Локальный метод для прокрутки экрана.

            Args:
                direction (str): Направление ('down', 'up').
                scrolls (int): Количество прокруток.
                frame_size (int): Размер прокрутки.
                delay (float): Задержка между прокрутками.

            Returns:
                bool: `True`, если успешно, иначе `False`.
            """
            try:
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка при прокрутке', ex, exc_info=True)  # Добавлено exc_info=True
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex, exc_info=True)  # Добавлено exc_info=True
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        Returns:
            Optional[str]: Код языка, если найден, иначе `None`.

        Example:
            >>> lang = driver.locale
            >>> print(lang)  # 'en' или None
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, 'meta[http-equiv="Content-Language"]')
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', ex, exc_info=True)  # Добавлено exc_info=True
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', ex, exc_info=True)  # Добавлено exc_info=True
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        Args:
            url (str): URL для перехода.

        Returns:
            bool: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

        Raises:
            WebDriverException: Если возникает ошибка с WebDriver.
            InvalidArgumentException: Если URL некорректен.
            Exception: Для любых других ошибок при переходе.
        """
        _previous_url: str = copy.copy(self.current_url)

        try:
            self.driver.get(url)

            attempts = 5
            while self.ready_state not in ('complete', 'interactive'):
                """ Ожидание завершения загрузки страницы """
                attempts -= 1  # fix: Было -= 5, а должно -= 1
                if attempts < 0:  # Если страница не загрузилась за 5 попыток, то цикл прерывается с выводом сообщения об ошибке
                    logger.error(f'Страница не загрузилась за 5 попыток: {url=}')
                    ...
                    break
                time.sleep(1)

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('WebDriverException', ex, exc_info=True)  # Добавлено exc_info=True
            return False

        except InvalidArgumentException as ex:
            logger.error(f'InvalidArgumentException {url}', ex, exc_info=True)  # Добавлено exc_info=True
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex, exc_info=True)  # Добавлено exc_info=True
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        Args:
            url (Optional[str]): URL для открытия в новой вкладке. По умолчанию `None`.
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        Args:
            delay (float): Время задержки в секундах. По умолчанию 0.3.

        Returns:
            None
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.

        Returns:
            None

        Raises:
            Exception: Если возникает ошибка при сохранении куки.
        """
        # return True  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug # fix: удалена закомментированная строка debug
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', ex, exc_info=True)  # Добавлено exc_info=True

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        Args:
            url (str): Путь к файлу или URL для извлечения HTML-контента.

        Returns:
            Optional[bool]: Возвращает `True`, если контент успешно получен, иначе `False`.

        Raises:
            Exception: Если возникает ошибка при извлечении контента.
        """
        if url.startswith('file://'):
            cleaned_url = url.replace('file://', '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Ошибка при чтении файла:', ex, exc_info=True)  # Добавлено exc_info=True
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path, exc_info=True)  # Добавлено exc_info=True
                    return False
            else:
                logger.error('Некорректный путь к файлу:', cleaned_url, exc_info=True)  # Добавлено exc_info=True
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f'Ошибка при получении {url}:', ex, exc_info=True)  # Добавлено exc_info=True
                return False
        else:
            logger.error('Ошибка: Неподдерживаемый протокол для URL:', url, exc_info=True)  # Добавлено exc_info=True
            return False