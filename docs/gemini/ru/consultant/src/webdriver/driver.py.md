## Анализ кода модуля src.webdriver.driver

**Качество кода**
8
-   Плюсы
        - Код имеет docstring для классов, методов и функций, что облегчает понимание его назначения и использования.
        - Используются логи для отслеживания ошибок, что помогает при отладке и мониторинге работы программы.
        - Применение `try-except` блоков для обработки исключений и предотвращения сбоев в работе программы.
        - Код структурирован, разбит на классы и методы, что повышает его читаемость и поддерживаемость.
-   Минусы
    -  Не все исключения обрабатываются с помощью `logger.error`, некоторые перехватываются и просто игнорируются.
    -  Отсутствует проверка на корректность `webdriver_cls` в `__init__`.
    -  В некоторых местах используется `Exception` без конкретизации, что затрудняет отладку.
    -  Метод `_save_cookies_localy` закомментирован, что делает его нерабочим.
    -  Не всегда используется явное указание типов.
    -  Дублирование кода в методе `scroll` с вызовом `carousel`.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Уточнить docstring для метода `scroll` и `carousel`, указав, что происходит при `direction='both'`.
    -   Добавить описание возможных исключений в docstring методов `get_url` и `fetch_html`.
    -   Использовать reStructuredText (RST) для всех комментариев и docstring.

2.  **Обработка ошибок**:
    -   Использовать `logger.error` для всех исключений, чтобы сохранить полную информацию об ошибках.
    -   Перехватывать более конкретные исключения, а не просто `Exception`, когда это возможно.
    -   В методе `__init__` добавить проверку наличия метода `get` у `webdriver_cls` для предотвращения ошибок.

3.  **Логирование**:
    -   Добавить больше информативных сообщений в логи, чтобы понимать, на каком этапе возникла ошибка.

4.  **Рефакторинг**:
    -   Упростить метод `scroll`, объединив логику прокрутки в один метод.
    -   Переименовать `_previous_url` в более информативное имя, например, `previous_url`.
    -   Снять комментарий с `_save_cookies_localy`, исправить ошибки и добавить логирование.
    -   Добавить проверки на пустые значения или некорректные данные.

5.  **Улучшения**:
    -   Добавить возможность настраивать таймауты ожидания загрузки страницы.
    -   Использовать `from src.utils.jjson import j_loads, j_loads_ns` если нужно будет работать с json.
    -   Добавить проверки входных параметров, например, `url` в `get_url` и `fetch_html`.
    -  Использовать `isinstance` вместо проверки через `startswith` для url в `fetch_html`
    -  Применять `Path` для создания путей к файлам.
    -  Использовать константы для magic strings.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
# file hypotez/src/webdriver/driver.py
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который обеспечивает унифицированный интерфейс для работы с веб-драйверами Selenium.

Основные возможности включают:
  - Инициализация и настройка веб-драйвера.
  - Навигация по веб-страницам.
  - Прокрутка страниц.
  - Управление cookie.
  - Обработка исключений и логирование.

Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    >>> driver.get_url('https://example.com')
"""

MODE = 'dev'
_FILE_PROTOCOL = 'file://'
_HTTP_PROTOCOL = 'http://'
_HTTPS_PROTOCOL = 'https://'

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

from src import gs
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException
# from src.utils.jjson import j_loads, j_loads_ns # TODO add if json will used


class Driver:
    """
    Унифицированный класс для взаимодействия с Selenium WebDriver.
    =========================================================================================

    Предоставляет интерфейс для работы с различными веб-драйверами, такими как Chrome, Firefox и Edge.

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: selenium.webdriver
    """

    def __init__(self, webdriver_cls: type, *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс WebDriver, например, Chrome или Firefox.
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
        if not hasattr(webdriver_cls, 'get'): # Проверка наличия метода get у webdriver_cls
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs: Any) -> None:
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str, optional
        :param kwargs: Дополнительные аргументы.
        :type kwargs: dict
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item: str) -> Any:
        """
        Прокси для доступа к атрибутам драйвера.

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

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками в секундах.
        :type delay: float
        :return: True, если прокрутка выполнена успешно, иначе False.
        :rtype: bool
        """
        def _scroll_direction(direction: str, scrolls: int, frame_size: int, delay: float) -> bool:
            """
            Выполняет прокрутку в одном направлении.

            :param direction: Направление прокрутки ('', '-').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки в пикселях.
            :type frame_size: int
            :param delay: Задержка между прокрутками в секундах.
            :type delay: float
            :return: True, если прокрутка выполнена успешно, иначе False.
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
            if direction in ['forward', 'down']:
                return _scroll_direction('', scrolls, frame_size, delay)
            elif direction in ['backward', 'up']:
                return _scroll_direction('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return _scroll_direction('', scrolls, frame_size, delay) and _scroll_direction('-', scrolls, frame_size, delay)
            else:
                logger.error(f'Неизвестное направление прокрутки: {direction}')
                return False
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex)
            return False


    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

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

        :param url: URL для перехода.
        :type url: str
        :return: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.
        :rtype: bool
        :raises WebDriverException: Если возникает ошибка с WebDriver.
        :raises InvalidArgumentException: Если URL некорректен.
        :raises Exception: Для любых других ошибок при переходе.
        """
        if not isinstance(url, str) or not url: # Проверка валидности URL
           logger.error(f'Некорректный URL: {url}')
           return False

        try:
            previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False

        try:
            self.driver.get(url)

            while self.ready_state != 'complete':
                """ Ожидание завершения загрузки страницы """

            if url != previous_url:
                self.previous_url = previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('Ошибка WebDriver', exc_info=ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"Некорректный URL: {url}", exc_info=ex)
            return False

        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """Открывает новую вкладку в текущем окне браузера и переключается на нее.

        :param url: URL для открытия в новой вкладке.
        :type url: str, optional
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.

        :raises Exception: Если возникает ошибка при сохранении куки.
        """
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
                logger.debug('Куки успешно сохранены в файл')
        except Exception as ex:
            logger.error('Ошибка при сохранении куки', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
        :raises Exception: Если возникает ошибка при извлечении контента.
        """
        if not isinstance(url, str) or not url:  # Проверка валидности URL
           logger.error(f'Некорректный URL: {url}')
           return False

        if url.startswith(_FILE_PROTOCOL):
            cleaned_url = url.replace(_FILE_PROTOCOL, '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                         logger.error(f'Ошибка при чтении файла: {file_path}', exc_info=ex)
                         return False
                else:
                    logger.error(f'Локальный файл не найден: {file_path}')
                    return False
            else:
                logger.error(f'Некорректный путь к файлу: {cleaned_url}')
                return False

        elif url.startswith(_HTTP_PROTOCOL) or url.startswith(_HTTPS_PROTOCOL):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при получении {url}", exc_info=ex)
                return False
        else:
            logger.error(f"Неподдерживаемый протокол для URL: {url}")
            return False