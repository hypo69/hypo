## Анализ кода модуля `driver.py`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован, используются классы и методы для инкапсуляции логики работы с веб-драйвером.
    - Присутствует базовая документация к классам и методам, хоть и не всегда полная.
    - Используется `logger` для логирования ошибок.
    - Есть обработка базовых исключений, связанных с Selenium.
 - Минусы
    - Некоторые docstring не соответствуют стандарту RST.
    - Не везде используются `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствует обработка ошибок в `_save_cookies_localy` (закомментировано).
    - В методе `get_url` отсутствует возврат `False` в блоке `except` для `Exception`.
    - Используется избыточный блок `try-except` в методе `scroll` для обработки ошибок.
    - Не всегда есть проверки на валидность данных.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать docstring в соответствии с RST ( reStructuredText ) для генерации документации.
    -   Добавить более подробные описания для всех методов и переменных, включая параметры и возвращаемые значения.
    -   Уточнить примеры использования в docstring.
2.  **Обработка ошибок**:
    -   Удалить избыточное использование `try-except` в `scroll`, заменив на `logger.error`.
    -   В методе `get_url` добавить `return False` в блоке `except Exception as ex`, для корректного возврата значения.
    -   Добавить обработку ошибок в `_save_cookies_localy`.
    -   Добавить проверку `self.driver` на `None` перед выполнением действий.
3.  **Импорты**:
    -   Убрать лишний импорт `header`.
4.  **Логирование**:
    -   Уточнить сообщения логгера, добавив контекст.
5.  **Код**:
    -   Использовать `j_loads` для чтения файлов.
    -   Добавить проверку на валидность данных в разных методах.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс `Driver`, который обеспечивает унифицированный интерфейс для взаимодействия
с веб-драйверами Selenium. Основные функции включают инициализацию драйвера, навигацию, управление куками и
обработку исключений.

Пример использования:
--------------------

.. code-block:: python

    from selenium.webdriver import Chrome
    from src.webdriver.driver import Driver

    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
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
# from header import header  #  Удален неиспользуемый импорт
from src import gs
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException
from src.utils.jjson import j_loads  #  Импорт j_loads для работы с json

class Driver:
    """
    Класс для взаимодействия с Selenium WebDriver.
    =========================================================================================

    Предоставляет унифицированный интерфейс для работы с различными веб-драйверами, такими как Chrome, Firefox и Edge.

    :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
    :type webdriver_cls: type
    :param args: Позиционные аргументы для драйвера.
    :param kwargs: Ключевые аргументы для драйвера.
    :ivar driver: Экземпляр Selenium WebDriver.
    :vartype driver: selenium.webdriver
    :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализация экземпляра класса Driver.

        :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        :type webdriver_cls: type
        :param args: Позиционные аргументы для драйвера.
        :param kwargs: Ключевые аргументы для драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
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
        :raises AttributeError: Если атрибут не найден.
        :return: Атрибут драйвера.
        :rtype: Any
        """
        if not self.driver:
            raise AttributeError(f'Драйвер не инициализирован, доступ к атрибуту {item} невозможен.')
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток, по умолчанию 1.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях, по умолчанию 600.
        :type frame_size: int
        :param direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
        :type direction: str
        :param delay: Задержка между прокрутками, по умолчанию 0.3.
        :type delay: float
        :return: `True`, если прокрутка успешна, `False` в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Локальный метод для выполнения прокрутки.

            :param direction: Направление прокрутки ('down', 'up').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки.
            :type frame_size: int
            :param delay: Задержка между прокрутками.
            :type delay: float
            :return: `True`, если прокрутка успешна, `False` в противном случае.
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

        if not self.driver:
            logger.error('Драйвер не инициализирован, прокрутка невозможна.')
            return False
        try:
            if direction in ('forward', 'down'):
                return carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
            return False
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе `None`.
        :rtype: Optional[str]
        """
        if not self.driver:
            logger.error('Драйвер не инициализирован, определение локали невозможно.')
            return None
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
        if not self.driver:
            logger.error('Драйвер не инициализирован, переход по URL невозможен.')
            return False
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            _previous_url = None
        try:
            self.driver.get(url)

            while self.ready_state != 'complete':
                """ Ожидание завершения загрузки страницы """

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('Ошибка WebDriver при переходе по URL', exc_info=ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"Некорректный URL: {url}", exc_info=ex)
            return False

        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на нее.

        :param url: URL для открытия в новой вкладке.
        :type url: Optional[str]
        """
        if not self.driver:
            logger.error('Драйвер не инициализирован, открытие нового окна невозможно.')
            return None
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get_url(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах, по умолчанию 0.3.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        if not self.driver:
           logger.error('Драйвер не инициализирован, сохранение куки невозможно.')
           return None
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
        :return: `True`, если контент успешно получен, `False` в противном случае, `None` если драйвер не инициализирован.
        :rtype: Optional[bool]
        """
        if not self.driver:
            logger.error('Драйвер не инициализирован, получение HTML невозможно.')
            return None
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