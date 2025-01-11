# Анализ кода модуля `driver`

**Качество кода**
8
-  Плюсы
    -  Хорошо структурированный код с четким разделением на классы и методы.
    -  Используется логирование для отслеживания ошибок и предупреждений.
    -  Реализовано управление cookies.
    -  Поддержка проксирования доступа к атрибутам `webdriver`.
    -  Асинхронный скролл.
    -  Обработка URL для локальных файлов и web-адресов.
 -  Минусы
    -  Отсутствует документация в формате RST для функций, методов и классов.
    -  Не все исключения обрабатываются с помощью `logger.error`.
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Некоторые комментарии не соответствуют формату.
    -   Использование `copy.copy` для `current_url` выглядит избыточным, можно просто присвоить.
    -   Блок `wait` простая задержка `time.sleep`.
    -   `_save_cookies_localy` не сохраняет cookies.
    -   Слишком много  `try-except`  блоков.

**Рекомендации по улучшению**
1. **Документация**: Добавить документацию в формате RST для всех функций, методов и классов.
2. **Импорты**: Добавить недостающие импорты `copy`, `time`, `re`, `pickle`, `Optional`, `Path`, `By`, `WebDriverException`, `InvalidArgumentException`,  `from src.logger.logger import logger`,  `from pathlib import Path`.
3. **Логирование**: Использовать `logger.error` для всех обработок исключений, убрать лишние `try-except` блоки.
4. **Cookies**: исправить сохранение cookies.
5. **Обработка данных**: не применимо.
6. **Рефакторинг**: Упростить код с `copy.copy`, заменить `time.sleep` на `asyncio.sleep`.
7. **Комментарии**: переделать комментарии в соответствии с инструкцией.

**Оптимизированный код**
```python
"""
Модуль для работы с веб-драйверами Selenium
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который обеспечивает унифицированный интерфейс
для взаимодействия с веб-драйверами Selenium.

Пример использования
--------------------

Пример создания и использования драйвера Chrome:

.. code-block:: python

    from selenium.webdriver import Chrome
    from src.webdriver.driver import Driver
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import time
import re
import pickle
from typing import Optional
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from src.logger.logger import logger # импортируем logger
#from src.utils.jjson import j_loads # пока не используется
import asyncio

class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    Предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами,
    включая инициализацию, навигацию, управление куками и обработку ошибок.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует драйвер веб-браузера.

        Args:
            webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
            *args: Позиционные аргументы для инициализации драйвера.
            **kwargs: Именованные аргументы для инициализации драйвера.
        Raises:
            TypeError: Если `webdriver_cls` не является допустимым классом веб-драйвера.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.
        
        Args:
            browser_name (str): Имя браузера.
            **kwargs: Дополнительные именованные аргументы.
        Raises:
            ValueError: Если не указан аргумент `browser_name`.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Перенаправляет доступ к атрибутам драйвера.
        
        Args:
            item (str): Имя атрибута.
        Returns:
             Любой: Значение атрибута или вызывает исключение.
        """
        return getattr(self.driver, item)

    async def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет скроллинг страницы в указанном направлении.

        Args:
            scrolls (int, optional): Количество прокруток. По умолчанию 1.
            frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
            direction (str, optional): Направление прокрутки ('both', 'down', 'up'). По умолчанию 'both'.
            delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.
        Returns:
             bool: `True` если скроллинг успешен, `False` в противном случае.
        """
        async def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Внутренняя функция для выполнения скроллинга.
            
            Args:
                direction (str, optional): Направление прокрутки. По умолчанию ''.
                scrolls (int, optional): Количество прокруток. По умолчанию 1.
                frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
                delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.
            Returns:
                bool: `True` если скроллинг успешен, `False` в противном случае.
            """
            try:
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    await asyncio.sleep(delay) # Заменено time.sleep на asyncio.sleep
                return True
            except Exception as ex:
                logger.error('Error while scrolling', exc_info=ex)
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return await carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return await carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return await carousel('', scrolls, frame_size, delay) and await carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Error in scroll function', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        Returns:
            Optional[str]: Код языка, если найден, иначе None.
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Failed to determine site language from META', exc_info=ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Failed to determine site language from JavaScript', exc_info=ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        Args:
            url (str): URL для перехода.
        Returns:
            bool: `True`, если переход успешен и текущий URL соответствует ожидаемому, `False` в противном случае.
        """
        try:
            previous_url = self.current_url # Заменено copy.copy на прямое присваивание
        except Exception as ex:
            logger.error("Error getting current URL", exc_info=ex)
            return False
        
        try:
            self.driver.get(url)
            while self.ready_state != 'complete':
                """  Ожидание полной загрузки страницы """

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
            logger.error(f'Error navigating to URL: {url}\n', exc_info=ex)
            return False
        
    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на нее.

        Args:
            url (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию None.
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
         """
         Ожидает указанное время.
         
         Args:
             delay (float, optional): Время задержки в секундах. По умолчанию 0.3.
         """
         asyncio.sleep(delay) # Заменено time.sleep на asyncio.sleep

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Error saving cookies:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Получает HTML-контент из файла или веб-страницы.

        Args:
            url (str): Путь к файлу или URL для получения HTML-контента.
        Returns:
            Optional[bool]: True, если контент успешно получен, иначе None.
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
                        logger.error('Error reading file:', exc_info=ex)
                        return False
                else:
                     logger.error('Local file not found:', file_path)
                     return False
            else:
                logger.error('Invalid file path:', cleaned_url)
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Error fetching {url}:", exc_info=ex)
                return False
        else:
            logger.error("Error: Unsupported protocol for URL:", url)
            return False
```