# Анализ кода модуля `src.webdriver.driver`

**Качество кода**
8
-   Плюсы
    *   Код хорошо структурирован, с использованием классов и методов для организации функциональности.
    *   Присутствует базовая обработка исключений, что помогает избежать сбоев при выполнении операций.
    *   Используется `logger` для вывода ошибок.
    *   Есть документация к методам и классам, что упрощает понимание кода.
-   Минусы
    *   Не все docstrings соответствуют стандарту reStructuredText.
    *   Используются избыточные блоки `try-except`.
    *   Отсутствует проверка корректности входных данных.
    *   Не везде используются f-строки для форматирования строк.
    *   `_save_cookies_localy` временно отключен и возвращает `True`.
    *   Используется `copy.copy`, но не ясно зачем.

**Рекомендации по улучшению**

1.  **Приведение документации к стандарту reStructuredText (RST):**
    *   Переписать docstrings в формате RST, как указано в инструкции.
    *   Добавить описание параметров и возвращаемых значений для всех функций и методов.
2.  **Обработка ошибок:**
    *   Заменить избыточные `try-except` на обработку ошибок через `logger.error` с последующим возвратом `False` или `None` в зависимости от контекста.
    *   Удалить `copy.copy(self.current_url)`, так как это не нужно.
3.  **Использование `j_loads` или `j_loads_ns`:**
    *   В данном файле отсутствуют операции с JSON, поэтому это изменение не требуется.
4.  **Рефакторинг:**
    *   Переименовать переменные для большей ясности (например, `_previous_url` в `previous_url`).
    *   Использовать f-строки для форматирования строк, где это возможно.
    *   Провести ревизию кода для улучшения читаемости и производительности.
5.  **Улучшение `_save_cookies_localy`:**
    *   Восстановить работоспособность метода `_save_cookies_localy`, удалив  `return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`.
6.  **Дополнительно**:
    *   Добавить проверку на тип входных данных (например, url) для предотвращения ошибок.
    *   Добавить описание для константы `MODE`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который предоставляет унифицированный интерфейс
для взаимодействия с веб-драйверами Selenium.

Основные функции:
    1. Инициализация драйвера: создание экземпляра Selenium WebDriver.
    2. Навигация: переход по URL, прокрутка и извлечение контента.
    3. Работа с куки: сохранение и управление куки.
    4. Обработка исключений: логирование ошибок.

Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    >>> driver.get_url('https://example.com')
"""

MODE = 'dev'
"""Режим работы драйвера."""

import pickle
import time
import re
from pathlib import Path
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)
# from src.utils.jjson import j_loads, j_loads_ns # TODO: нет необходимости в данном модуле
from src import gs
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException


class Driver:
    """
    Класс для взаимодействия с Selenium WebDriver.
    =========================================================================================

    Предоставляет удобный интерфейс для работы с различными драйверами,
    такими как Chrome, Firefox и Edge.

    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: selenium.webdriver
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс WebDriver, например, Chrome или Firefox.
        :type webdriver_cls: type
        :param args: Позиционные аргументы для драйвера.
        :param kwargs: Ключевые аргументы для драйвера.
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

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Прокси для доступа к атрибутам драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Атрибут драйвера.

        Пример:
            >>> driver.current_url
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = 0.3) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление ('both', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: `True`, если прокрутка прошла успешно, иначе `False`.
        :rtype: bool

        Пример:
            >>> driver.scroll(scrolls=3, direction='down')
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = 0.3) -> bool:
            """
            Локальный метод для прокрутки экрана.

            :param direction: Направление ('down', 'up').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки.
            :type frame_size: int
            :param delay: Задержка между прокрутками.
            :type delay: float
            :return: `True`, если прокрутка прошла успешно, иначе `False`.
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
                return carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', exc_info=ex)
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
        try:
            previous_url = self.current_url
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False

        try:
            self.driver.get(url)

            while self.ready_state != 'complete':
                """Ожидаем завершения загрузки страницы"""

            if url != previous_url:
                self.previous_url = previous_url

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
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        :param url: URL для открытия в новой вкладке. По умолчанию `None`.
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = 0.3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах. По умолчанию 0.3.
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
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: Возвращает `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
        :raises Exception: Если возникает ошибка при извлечении контента.
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