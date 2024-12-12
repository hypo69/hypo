# Анализ кода модуля `driver.py`

**Качество кода**
7
 -  Плюсы
    - Код предоставляет абстракцию для работы с веб-драйверами Selenium, что упрощает взаимодействие с ними.
    - Присутствует обработка исключений, что делает код более устойчивым к ошибкам.
    - Используется логирование для отслеживания ошибок и отладки.
    - Есть механизм для работы с куки и сохранения их локально.
    - Реализован метод для прокрутки страницы с возможностью выбора направления и скорости прокрутки.
    - Методы хорошо документированы и понятны.
    - Структура кода логичная.
 -  Минусы
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - В коде присутствуют избыточные блоки `try-except`.
    - Присутствуют неиспользуемые переменные и конструкции (например, в методе `_save_cookies_localy`).
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Некоторые docstring требуют доработки.

**Рекомендации по улучшению**
1.  Привести все комментарии к стандарту reStructuredText (RST).
2.  Использовать `from src.logger.logger import logger` для логирования.
3.  Упростить обработку ошибок, используя `logger.error` вместо множественных `try-except`.
4.  Удалить неиспользуемые части кода и переменные.
5.  Использовать `j_loads` или `j_loads_ns` для загрузки файлов, если это необходимо.
6.  Дополнить docstring для всех методов и класса, где это необходимо.
7.  Добавить проверки на наличие необходимых параметров и выбрасывать исключения с информативным сообщением.
8.  Избегать использования `copy.copy` для URL.
9.  Удалить неиспользуемый debug в методе `_save_cookies_localy`.
10. Внести исправления в логику обработки ошибок при загрузке контента из файлов.

**Оптимизированный код**

```python
"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который предоставляет единый интерфейс
для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера,
навигации, управления куки, обработки исключений и других операций.

Пример использования
--------------------

Пример использования класса `Driver`:

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import time
import copy
import re
import pickle
from pathlib import Path
from typing import Optional, Any
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.logger.logger import logger
#from src.utils.jjson import j_loads # TODO: удалить если не используется.
from src.config import gs


class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    Предоставляет интерфейс для взаимодействия с веб-драйверами, включая навигацию, управление куки и обработку исключений.
    """
    def __init__(self, webdriver_cls: type, *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :type webdriver_cls: type
        :param args: Позиционные аргументы для инициализации драйвера.
        :type args: Any
        :param kwargs: Именованные аргументы для инициализации драйвера.
        :type kwargs: Any
        :raises TypeError: Если `webdriver_cls` не является допустимым классом веб-драйвера.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver: WebDriver = webdriver_cls(*args, **kwargs)
        self.previous_url: Optional[str] = None
        self.html_content: Optional[str] = None

    def __init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs: Any) -> None:
        """
        Автоматически вызывается при создании подкласса Driver.

        Устанавливает имя браузера для подкласса.

        :param browser_name: Имя браузера.
        :type browser_name: Optional[str]
        :param kwargs: Дополнительные аргументы.
        :type kwargs: Any
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
        cls.browser_name = browser_name

    def __getattr__(self, item: str) -> Any:
        """
        Перехватывает обращение к атрибутам и перенаправляет их к драйверу.

        :param item: Имя атрибута.
        :type item: str
        :return: Значение атрибута из драйвера.
        :rtype: Any
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет прокрутку страницы.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: True, если прокрутка выполнена успешно, False в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Внутренняя функция для выполнения прокрутки.
            
            :param direction: Направление прокрутки ('', '-').
            :type direction: str
            :param scrolls: Количество прокруток.
            :type scrolls: int
            :param frame_size: Размер прокрутки в пикселях.
            :type frame_size: int
            :param delay: Задержка между прокрутками.
            :type delay: float
            :return: True, если прокрутка выполнена успешно, False в противном случае.
            :rtype: bool
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
            if direction in ('forward', 'down'):
                return carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Error in scroll function', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы.

        :return: Языковой код, если найден, иначе None.
        :rtype: Optional[str]
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

        :param url: URL для перехода.
        :type url: str
        :return: True, если переход выполнен успешно, False в противном случае.
        :rtype: bool
        """
        try:
            _previous_url = self.current_url
        except Exception as ex:
            logger.error("Error getting current URL", exc_info=ex)
            return False
        
        try:
            self.driver.get(url)
            while self.ready_state != 'complete':
                """ ожидает пока страница полностью загрузится"""

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
            logger.error(f'Error navigating to URL: {url}', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новое окно браузера.

        :param url: URL для открытия в новом окне (необязательный).
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное время.

        :param delay: Время ожидания в секундах.
        :type delay: float
        """
        time.sleep(delay)

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
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: URL или путь к файлу для загрузки.
        :type url: str
        :return: True в случае успешной загрузки, иначе False.
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