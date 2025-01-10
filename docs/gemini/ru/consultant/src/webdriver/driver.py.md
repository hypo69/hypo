# Анализ кода модуля `driver`

**Качество кода**
9
- Плюсы
    - Код хорошо документирован с использованием docstrings в формате reStructuredText (RST).
    - Присутствует обработка основных исключений.
    - Используется logging для отслеживания ошибок и отладки.
    - Применяются `Path` для работы с путями файлов.
    - Использованы `typing` для аннотации типов.
- Минусы
    - Не всегда используется `logger.error` с `exc_info=ex` для вывода полной трассировки.
    - В некоторых местах используется `try-except` без конкретной обработки ошибок, что может усложнить отладку.
    - Не всегда проводится проверка на существование элементов перед взаимодействием с ними (нужно добавить `try - except` при использовании методов `find_element` и других для элементов).
    - Недостаточно проверок на корректность входных данных (например, `url` и `direction`).
    - Функция `_save_cookies_localy` возвращает `True`, хотя должна сохранять куки.

**Рекомендации по улучшению**

1.  **Импорты:**
    - Добавьте `from src.utils.jjson import j_loads, j_loads_ns`, если планируется использование `j_loads` или `j_loads_ns`.
    - Убедитесь, что все необходимые модули импортированы (например, если вы используете `j_loads` или `j_loads_ns`).

2.  **Логирование:**
    - В `try-except` блоках, где используется `logger.error`, добавляйте `exc_info=ex` для полного вывода трассировки ошибки. Например: `logger.error('Ошибка при ...', exc_info=ex)`.
    - Измените `logger.debug` на `logger.info` в тех местах, где вы хотите вывести информационные сообщения.

3.  **Обработка ошибок:**
    - Избегайте `try-except` без конкретной обработки, особенно в функциях `scroll` и `fetch_html`.
    - Добавьте проверку на существование элементов перед взаимодействием (с помощью `try-except`).
    -  В функции `get_url` перенесите получение `_previous_url` в начало `try` блока, чтобы избежать `NameError` если вызов `self.current_url` бросит исключение.

4.  **Функция `_save_cookies_localy`:**
    - Уберите `return True` и реализуйте сохранение куки в файл.

5.  **Проверки:**
    - Добавьте проверки на корректность входных данных в функциях `scroll` и `fetch_html`.

6.  **Комментарии:**
     - Добавьте комментарии с помощью `#` для объяснения логики кода там, где это необходимо.
     - Пересмотрите docstring для соответствия стандартам Python.

**Оптимизированный код**

```python
"""
.. module::  src.webdriver.driver
   :platform: Windows, Unix
   :synopsis: Модуль для работы с веб-драйверами Selenium.

   Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium.

   Основные функции:
   
   1. **Инициализация драйвера**: создание экземпляра Selenium WebDriver.
   2. **Навигация**: переход по URL, прокрутка и извлечение контента.
   3. **Работа с куки**: сохранение и управление куки.
   4. **Обработка исключений**: логирование ошибок.

Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    >>> driver.get_url('https://example.com')
"""

import copy
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
import header
from src import gs
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException
from src.utils.jjson import j_loads, j_loads_ns # добавлены импорты j_loads, j_loads_ns


class Driver:
    """
    .. class:: Driver
       :platform: Windows, Unix
       :synopsis: Унифицированный класс для взаимодействия с Selenium WebDriver.

    Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

    Атрибуты:
        driver (selenium.webdriver): Экземпляр Selenium WebDriver.
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        .. method:: __init__(self, webdriver_cls, *args, **kwargs)
        
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        :type webdriver_cls: type
        :param args: Позиционные аргументы для драйвера.
        :param kwargs: Ключевые аргументы для драйвера.

        Пример:
            >>> from selenium.webdriver import Chrome
            >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        .. method:: __init_subclass__(cls, *, browser_name=None, **kwargs)

        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param kwargs: Дополнительные аргументы.

        Исключение:
            ValueError: Если browser_name не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        .. method:: __getattr__(self, item)

        Прокси для доступа к атрибутам драйвера.

        :param item: Имя атрибута.
        :type item: str

        Пример:
            >>> driver.current_url
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        .. method:: scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)

        Прокручивает страницу в указанном направлении.

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
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            .. method:: carousel(direction='', scrolls=1, frame_size=600, delay=.3)

            Локальный метод для прокрутки экрана.

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
                logger.error('Ошибка при прокрутке', exc_info=ex) # добавлено exc_info=ex
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
            else:
                 logger.error(f"Некорректное направление прокрутки: {direction}") # проверка на корректное направление
                 return False
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', exc_info=ex) # добавлено exc_info=ex
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        .. method:: locale(self)

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
            logger.info('Не удалось определить язык сайта из META', exc_info=ex) # logger.debug -> logger.info , exc_info=ex
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.info('Не удалось определить язык сайта из JavaScript', exc_info=ex) # logger.debug -> logger.info , exc_info=ex
                return


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
        _previous_url = None # инициализация для избежания `UnboundLocalError`
        try:
             #  перенесено сюда для избежания `NameError`
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex) # добавлено exc_info=ex
            #return False
        
        try:
            self.driver.get(url)
            
            while self.ready_state != 'complete':
                """ Ожидаем завершения загрузки страницы """

            if _previous_url and url != _previous_url: # проверка на существование _previous_url
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True
            
        except WebDriverException as ex:
            logger.error('WebDriverException', exc_info=ex) # добавлено exc_info=ex
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", exc_info=ex) # добавлено exc_info=ex
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\\n', exc_info=ex) # добавлено exc_info=ex
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """Open a new tab in the current browser window and switch to it.

        Args:
            url (Optional[str]): URL to open in the new tab. Defaults to `None`.
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        Args:
            delay (float, optional): Время задержки в секундах. По умолчанию 0.3.

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
        # return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug # удалено
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile: # сохранение куки в файл
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', exc_info=ex) # добавлено exc_info=ex

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        Args:
            url (str): Путь к файлу или URL для извлечения HTML-контента.

        Returns:
            Optional[bool]: Возвращает `True`, если контент успешно получен, иначе `None`.

        Raises:
            Exception: Если возникает ошибка при извлечении контента.
        """
        if not isinstance(url, str): # проверка типа url
             logger.error(f"Неверный тип данных для url: {type(url)}")
             return False

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
                        logger.error('Ошибка при чтении файла:', exc_info=ex) # добавлено exc_info=ex
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path) # добавлено file_path
                    return False
            else:
                logger.error('Некорректный путь к файлу:', cleaned_url) # добавлено cleaned_url
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при получении {url}:", exc_info=ex) # добавлено exc_info=ex
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url) # добавлено url
            return False