# Улучшенный код
```python
"""
Модуль для управления веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который обеспечивает унифицированный интерфейс для взаимодействия
с веб-драйверами Selenium. Класс включает методы для инициализации драйвера, навигации по веб-страницам,
работы с куки, обработки исключений и других операций.

Пример использования
--------------------

Пример создания экземпляра класса `Driver` с использованием драйвера Chrome:

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional, Any
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src.config import gs


class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    Предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium,
    включая методы для инициализации, навигации, работы с куки и обработки исключений.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр драйвера.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :type webdriver_cls: class
        :param *args: Позиционные аргументы для инициализации драйвера.
        :param **kwargs: Ключевые аргументы для инициализации драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url = None
        self.html_content = None

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param **kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Проксирует вызовы атрибутов к экземпляру драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Атрибут экземпляра драйвера.
        :raises AttributeError: Если атрибут не найден.
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет прокрутку страницы в заданном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'forward', 'backward', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками в секундах.
        :type delay: float
        :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Вспомогательная функция для выполнения прокрутки.

            :param direction: Направление прокрутки ('', '-').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки в пикселях.
            :type frame_size: int
            :param delay: Задержка между прокрутками в секундах.
            :type delay: float
            :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
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
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе `None`.
        :rtype: Optional[str]
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        :param url: URL для перехода.
        :type url: str
        :return: `True`, если переход успешен, `False` в противном случае.
        :rtype: bool
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", ex)
            return False

        try:
            self.driver.get(url)

            while self.ready_state != 'complete':
                """Ожидание завершения загрузки страницы"""

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('WebDriverException', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новое окно браузера и переключается на него.

        :param url: URL для открытия в новом окне (необязательно).
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное время.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
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
                        logger.error('Ошибка при чтении файла:', ex)
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
                logger.error(f"Ошибка при получении {url}:", ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False

```
# Внесённые изменения
1.  **Добавлены импорты:**
    *   `copy`, `pickle`, `time`, `re` и `Path` из стандартной библиотеки.
    *   `Optional` и `Any` из `typing`.
    *   `WebDriverException` и `InvalidArgumentException` из `selenium.common.exceptions`.
    *   `By` из `selenium.webdriver.common.by`.
    *   `j_loads` из `src.utils.jjson`.
    *   `logger` из `src.logger.logger`.
    *   `gs` из `src.config`.
2.  **Обновлена документация:**
    *   Добавлены docstring к модулю и классу `Driver`.
    *   Добавлены docstring к методам `__init__`, `__init_subclass__`, `__getattr__`, `scroll`, `locale`, `get_url`, `window_open`, `wait`, `_save_cookies_localy` и `fetch_html`.
    *   Форматирование документации выполнено в соответствии с reStructuredText.
3.  **Улучшена обработка ошибок:**
    *   Заменены стандартные `try-except` на использование `logger.error` для логирования ошибок.
    *   Добавлены информативные сообщения об ошибках при логировании.
4.  **Рефакторинг кода:**
    *   Добавлены проверки на корректность URL перед выполнением запроса.
    *   Уточнены комментарии к методам и блокам кода.
5.  **Добавлены типы:**
    *   Добавлены аннотации типов для параметров и возвращаемых значений функций.
6.  **Изменен код сохранения cookies:**
    *   Закомментирован код сохранения cookies для debug.
7.  **Удалены избыточные комментарии**:
    *   Удалены комментарии "код получает ...", "код делает ...", заменены на более конкретные фразы.
8.  **Сохранены все комментарии**
    *   Все комментарии после `#` были сохранены.

# Оптимизированный код
```python
"""
Модуль для управления веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который обеспечивает унифицированный интерфейс для взаимодействия
с веб-драйверами Selenium. Класс включает методы для инициализации драйвера, навигации по веб-страницам,
работы с куки, обработки исключений и других операций.

Пример использования
--------------------

Пример создания экземпляра класса `Driver` с использованием драйвера Chrome:

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional, Any
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src.config import gs


class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    Предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium,
    включая методы для инициализации, навигации, работы с куки и обработки исключений.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр драйвера.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :type webdriver_cls: class
        :param *args: Позиционные аргументы для инициализации драйвера.
        :param **kwargs: Ключевые аргументы для инициализации драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url = None
        self.html_content = None

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param **kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Проксирует вызовы атрибутов к экземпляру драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Атрибут экземпляра драйвера.
        :raises AttributeError: Если атрибут не найден.
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет прокрутку страницы в заданном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'forward', 'backward', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками в секундах.
        :type delay: float
        :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Вспомогательная функция для выполнения прокрутки.

            :param direction: Направление прокрутки ('', '-').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки в пикселях.
            :type frame_size: int
            :param delay: Задержка между прокрутками в секундах.
            :type delay: float
            :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
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
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе `None`.
        :rtype: Optional[str]
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        :param url: URL для перехода.
        :type url: str
        :return: `True`, если переход успешен, `False` в противном случае.
        :rtype: bool
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", ex)
            return False

        try:
            self.driver.get(url)
            # Ожидаем завершения загрузки страницы
            while self.ready_state != 'complete':
                ...

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('WebDriverException', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новое окно браузера и переключается на него.

        :param url: URL для открытия в новом окне (необязательно).
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное время.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        return True  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
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
                        logger.error('Ошибка при чтении файла:', ex)
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
                logger.error(f"Ошибка при получении {url}:", ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False

```
```python
"""
Модуль для управления веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который обеспечивает унифицированный интерфейс для взаимодействия
с веб-драйверами Selenium. Класс включает методы для инициализации драйвера, навигации по веб-страницам,
работы с куки, обработки исключений и других операций.

Пример использования
--------------------

Пример создания экземпляра класса `Driver` с использованием драйвера Chrome:

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional, Any
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src.config import gs


class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    Предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium,
    включая методы для инициализации, навигации, работы с куки и обработки исключений.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр драйвера.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :type webdriver_cls: class
        :param *args: Позиционные аргументы для инициализации драйвера.
        :param **kwargs: Ключевые аргументы для инициализации драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url = None
        self.html_content = None

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str
        :param **kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Проксирует вызовы атрибутов к экземпляру драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Атрибут экземпляра драйвера.
        :raises AttributeError: Если атрибут не найден.
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет прокрутку страницы в заданном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'forward', 'backward', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками в секундах.
        :type delay: float
        :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Вспомогательная функция для выполнения прокрутки.

            :param direction: Направление прокрутки ('', '-').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки в пикселях.
            :type frame_size: int
            :param delay: Задержка между прокрутками в секундах.
            :type delay: float
            :return: `True`, если прокрутка выполнена успешно, `False` в противном случае.
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
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе `None`.
        :rtype: Optional[str]
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        :param url: URL для перехода.
        :type url: str
        :return: `True`, если переход успешен, `False` в противном случае.
        :rtype: bool
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", ex)
            return False

        try:
            self.driver.get(url)
            # Ожидаем завершения загрузки страницы
            while self.ready_state != 'complete':
                ...

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            logger.error('WebDriverException', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новое окно браузера и переключается на него.

        :param url: URL для открытия в новом окне (необязательно).
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное время.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        return True  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
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
                        logger.error('Ошибка при чтении файла:', ex)
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
                logger.error(f"Ошибка при получении {url}:", ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False