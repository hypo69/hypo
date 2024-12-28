## Анализ кода модуля `src.webdriver.driver`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, с разделением на классы и методы.
    - Используется reStructuredText для документирования классов и методов.
    - Присутствует логирование ошибок с использованием `src.logger.logger`.
    - Код поддерживает работу с различными типами веб-драйверов.
    - Обработка исключений выполняется с использованием `try-except` блоков.
-  Минусы
    - В некоторых местах есть избыточное использование `try-except`.
    - Не везде используется явное указание типов для переменных в docstring.
    - Присутствует хардкод ``, который лучше вынести в конфиг.
    - Есть закомментированный `return True`  в `_save_cookies_localy`  что является отладкой.

**Рекомендации по улучшению**

1.  **Улучшить обработку исключений**:
    -   Использовать `logger.exception` для логирования ошибок вместе с трассировкой.
    -   Упростить блоки `try-except` там, где это возможно, перенеся общую обработку в `finally` блок.
2.  **Улучшить документацию**:
    -   Добавить типы переменных в docstring, где они не указаны.
    -   Убедиться, что все docstring соответствуют стандарту reStructuredText.
3.  **Рефакторинг `scroll`**:
    -   Метод `carousel` можно вынести в отдельную функцию и сделать более читаемым.
    -   Проверить логику обработки направления прокрутки.
4.  **Рефакторинг `get_url`**:
    -   Убрать избыточные `copy.copy` так как  `_previous_url`  используется только для сравнения.
    -   Проверка `url != _previous_url` избыточна так как  `self.previous_url`  не будет присвоен, если url не изменится.
5.  **Конфигурация**:
    -   Перенести хардкод `MODE` в конфигурационный файл.
6.  **Удаление отладочного кода**:
    -   Убрать закомментированный `return True`  в  `_save_cookies_localy`
7. **Применить форматирование кода**:
   -   Использовать `black` или `ruff` для автоматического форматирования кода.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который предоставляет унифицированный интерфейс
для взаимодействия с веб-драйверами Selenium, такими как Chrome, Firefox и Edge.

Основные возможности:
    - Инициализация и настройка веб-драйвера.
    - Навигация по веб-страницам.
    - Управление куки.
    - Прокрутка страниц.
    - Извлечение HTML-контента.
    - Обработка исключений.

Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    >>> driver.get_url('https://example.com')
"""

  # TODO: Перенести в конфигурационный файл

import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional, Any
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)
import header
from src import gs

from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException


class Driver:
    """
    Унифицированный класс для взаимодействия с Selenium WebDriver.
    =========================================================================================

    Этот класс предоставляет удобный интерфейс для управления веб-драйвером,
    включая навигацию, прокрутку, управление куки и извлечение контента.

    :param webdriver_cls: Класс WebDriver, например, Chrome или Firefox.
    :type webdriver_cls: type
    :param args: Позиционные аргументы для драйвера.
    :type args: tuple
    :param kwargs: Ключевые аргументы для драйвера.
    :type kwargs: dict

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: selenium.webdriver.remote.webdriver.WebDriver

    Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр класса Driver.
        =========================================================================================

        :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        :type webdriver_cls: type
        :param args: Позиционные аргументы для драйвера.
        :type args: tuple
        :param kwargs: Ключевые аргументы для драйвера.
        :type kwargs: dict

        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.

        Пример:
            >>> from selenium.webdriver import Chrome
            >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.
        =========================================================================================

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param kwargs: Дополнительные аргументы.
        :type kwargs: dict

        :raises ValueError: Если `browser_name` не указан.

        Пример:
        >>> class MyDriver(Driver, browser_name='chrome'):
        ...     pass
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Прокси для доступа к атрибутам драйвера.
        =========================================================================================

        :param item: Имя атрибута.
        :type item: str
        :return: Значение атрибута драйвера.
        :rtype: Any

        Пример:
            >>> driver.current_url
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в указанном направлении.
        =========================================================================================

        :param scrolls: Количество прокруток, по умолчанию 1.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях, по умолчанию 600.
        :type frame_size: int
        :param direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
        :type direction: str
        :param delay: Задержка между прокрутками, по умолчанию 0.3.
        :type delay: float
        :return: True, если успешно, иначе False.
        :rtype: bool

        Пример:
            >>> driver.scroll(scrolls=3, direction='down')
        """
        def _carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Локальный метод для прокрутки экрана.
            =========================================================================================

            :param direction: Направление ('down', 'up').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки.
            :type frame_size: int
            :param delay: Задержка между прокрутками.
            :type delay: float
            :return: True, если успешно, иначе False.
            :rtype: bool
            """
            try:
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка при прокрутке', exc_info=ex)
                return False

        try:
            if direction in ('forward', 'down'):
                return _carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                return _carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return _carousel('', scrolls, frame_size, delay) and _carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.
        =========================================================================================

        :return: Код языка, если найден, иначе None.
        :rtype: Optional[str]

        Пример:
            >>> lang = driver.locale
            >>> print(lang)  # 'en' или None
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', exc_info=ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', exc_info=ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
        =========================================================================================

        :param url: URL для перехода.
        :type url: str
        :return: True, если переход успешен и текущий URL совпадает с ожидаемым, False в противном случае.
        :rtype: bool

        :raises WebDriverException: Если возникает ошибка с WebDriver.
        :raises InvalidArgumentException: Если URL некорректен.
        :raises Exception: Для любых других ошибок при переходе.

        Пример:
            >>> driver.get_url('https://example.com')
        """
        _previous_url = self.current_url if hasattr(self, 'current_url') else None
        try:
           self.driver.get(url)
           while self.ready_state != 'complete':
                """Ожидаем завершения загрузки страницы"""
           if _previous_url and url != _previous_url:
                self.previous_url = _previous_url
           self._save_cookies_localy()
           return True
        except WebDriverException as ex:
            logger.error('WebDriverException', exc_info=ex)
            return False
        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на нее.
        =========================================================================================

        :param url: URL для открытия в новой вкладке.
        :type url: Optional[str]

        Пример:
            >>> driver.window_open('https://example.com')
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.
        =========================================================================================

        :param delay: Время задержки в секундах.
        :type delay: float

        Пример:
            >>> driver.wait(1)
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        =========================================================================================

        :raises Exception: Если возникает ошибка при сохранении куки.

        Пример:
            >>> driver._save_cookies_localy()
        """
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.
        =========================================================================================

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: True, если контент успешно получен, иначе None.
        :rtype: Optional[bool]

        :raises Exception: Если возникает ошибка при извлечении контента.

        Пример:
            >>> driver.fetch_html('file:///path/to/file.html')
            >>> driver.fetch_html('https://example.com')
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
                        logger.error('Ошибка при чтении файла:', exc_info=ex)
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path)
                    return False
            else:
                logger.error('Некорректный путь к файлу:', cleaned_url)
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при получении {url}:", exc_info=ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False