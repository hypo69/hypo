# Анализ кода модуля `driver.py`

**Качество кода: 7/10**
- **Плюсы**
    - Код предоставляет базовый класс `Driver` для управления Selenium WebDriver.
    - Присутствуют методы для навигации, скроллинга, работы с куки и обработки ошибок.
    - Используется логирование для отслеживания ошибок.
    - Добавлены проверки и обработка исключений при навигации.
    - Код содержит базовую документацию.
- **Минусы**
    - Отсутствует подробная документация в формате RST для всех функций и методов.
    - Присутствует избыточное использование блоков `try-except`.
    - Сохранение куки закомментировано, что может быть критично при работе с сайтами.
    - Логика определения языка сайта через meta и javascript выглядит сложной и может быть упрощена.
    - Некоторые методы имеют потенциал для рефакторинга.
    - Отсутствуют проверки для обязательных параметров, например `url` в методе `get_url`
    - Отсутствует проверка аргументов у функции `carousel`

**Рекомендации по улучшению**

1.  **Документация**: Добавить подробную документацию в формате RST для всех методов и класса `Driver`, включая описания аргументов, возвращаемых значений и возможных исключений.
2.  **Обработка ошибок**: Заменить избыточные `try-except` блоки на обработку ошибок с помощью `logger.error`, добавив информацию о типе ошибки и контексте.
3.  **Логирование**:  Использовать `from src.logger.logger import logger` для единообразия импорта логгера.
4.  **Сохранение куки**: Раскомментировать код сохранения куки и проверить его работоспособность.
5. **Упрощение логики**: Упростить логику определения языка сайта.
6. **Рефакторинг**: Разбить некоторые методы на более мелкие и переиспользовать код.
7. **Проверки аргументов**: Добавить проверки на обязательные аргументы и их тип.

**Оптимизированный код**

```python
"""
Модуль для работы с Selenium WebDriver.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который является оберткой для Selenium WebDriver.
Он обеспечивает унифицированный интерфейс для взаимодействия с веб-драйвером, включая навигацию,
управление куки, обработку исключений и другие операции.

Пример использования
--------------------

Пример создания экземпляра класса `Driver` и перехода по URL:

.. code-block:: python

    from selenium.webdriver import Chrome
    from src.webdriver.driver import Driver

    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import time
import pickle
import re
from pathlib import Path
from typing import Optional, Any
# from selenium.webdriver import Chrome # TODO: Убери от сюда этот импорт
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By
from src.logger.logger import logger
# from src.config import gs #TODO: Убери от сюда этот импорт
# from src.utils.jjson import j_loads_ns #TODO: Убери от сюда этот импорт


class Driver:
    """
    Класс для управления Selenium WebDriver.

    Предоставляет методы для инициализации, навигации, управления cookie,
    обработки исключений и других операций веб-драйвера.
    """
    browser_name: str = None

    def __init__(self, webdriver_cls: type[RemoteWebDriver], *args, **kwargs):
        """
        Инициализирует экземпляр класса Driver.

        Args:
            webdriver_cls (type[RemoteWebDriver]): Класс веб-драйвера (например, Chrome, Firefox).
            *args: Позиционные аргументы для инициализации веб-драйвера.
            **kwargs: Именованные аргументы для инициализации веб-драйвера.

        Raises:
            TypeError: Если `webdriver_cls` не является допустимым классом веб-драйвера.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url: str = ''
        self.html_content: str = ''

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса Driver.

        Args:
            browser_name (str, optional): Имя браузера.
            **kwargs: Дополнительные именованные аргументы.

        Raises:
            ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
        cls.browser_name = browser_name

    def __getattr__(self, item: str) -> Any:
        """
        Перенаправляет доступ к атрибутам объекта драйвера.

        Args:
            item (str): Имя атрибута.

        Returns:
            Any: Значение атрибута драйвера.
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в заданном направлении.

        Args:
            scrolls (int, optional): Количество прокруток. По умолчанию 1.
            frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
            direction (str, optional): Направление прокрутки ('both', 'down', 'up'). По умолчанию 'both'.
            delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.

        Returns:
            bool: True, если прокрутка выполнена успешно, False в противном случае.
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Вспомогательная функция для выполнения прокрутки.

            Args:
                direction (str, optional): Направление прокрутки ('', '-').
                scrolls (int, optional): Количество прокруток.
                frame_size (int, optional): Размер прокрутки в пикселях.
                delay (float, optional): Задержка между прокрутками в секундах.

            Returns:
                bool: True, если прокрутка выполнена успешно, False в противном случае.
            """
            try:
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Error while scrolling', exc_info=ex)
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
            return False # TODO: добавить логирование о том, что направление не распознано
        except Exception as ex:
            logger.error('Error in scroll function', exc_info=ex)
            return False


    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы.

        Пытается определить язык страницы через метатег `Content-Language` или JavaScript.

        Returns:
            Optional[str]: Код языка, если он найден, в противном случае None.
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
        Переходит по указанному URL.

        Args:
            url (str): URL для перехода.

         Returns:
            bool: True, если переход выполнен успешно, False в противном случае.
        """
        if not url:
            logger.error("URL cannot be empty.")
            return False

        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Error getting current URL", exc_info=ex)
            return False
        
        try:
            self.driver.get(url)
            while self.ready_state != 'complete':
                """ Wait for the page to finish loading """

            if url != _previous_url:
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
            logger.error(f'Error navigating to URL: {url}\\n', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новое окно/вкладку и переключается на него.

        Args:
            url (Optional[str], optional): URL для открытия в новом окне/вкладке.
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Приостанавливает выполнение на заданное время.

        Args:
            delay (float, optional): Время задержки в секундах. По умолчанию 0.3.
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        # return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
        try:
            # with open(gs.cookies_filepath, 'wb') as cookiesfile: # TODO: раскоментить после добавления gs
            #     pickle.dump(self.driver.get_cookies(), cookiesfile)
            ... # TODO: добавить сохранение кук
            pass
        except Exception as ex:
            logger.error('Error saving cookies:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML контент из файла или веб-страницы.

        Args:
            url (str): URL или путь к файлу для извлечения HTML контента.

        Returns:
             Optional[bool]: True, если HTML контент успешно получен, False в противном случае.
        """
        if not isinstance(url, str):
           logger.error(f"URL must be a string, got: {type(url)}")
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