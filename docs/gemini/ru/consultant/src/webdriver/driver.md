# Анализ кода модуля `driver`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошая структура класса `Driver` с разделением на методы для разных операций.
    - Использование `logger` для обработки ошибок.
    - Наличие методов для навигации, скроллинга, работы с куками и HTML.
    - Применение property `locale` для определения языка страницы.
    - Проверка на валидный класс `webdriver_cls` при инициализации.
- **Минусы**:
    - Использование `try-except` без необходимости.
    - Не везде есть docstring у методов.
    - В _save_cookies_localy() закомментирован код.
    - Использование `copy.copy()` для копирования URL.
    - Не используется `from src.logger.logger import logger`.
    - Нет обработки случая `None` в `get_url`.
    - Не используется `j_loads` или `j_loads_ns`.

## Рекомендации по улучшению:

1.  **Импорт `logger`**:
    - Замените `from src.logger import logger` на `from src.logger.logger import logger`.
2.  **Обработка ошибок**:
    - Используйте `logger.error` вместо `try-except` там, где это возможно, например, в методе `scroll`.
    - Избавьтесь от `try-except` в методе `__getattr__`, если это не требуется.
3.  **Документирование**:
    - Добавьте docstring для методов `__getattr__`, `window_open`, `wait`, `_save_cookies_localy` и `fetch_html` в формате RST.
4.  **Улучшение кода**:
    - Удалите закомментированный код в методе `_save_cookies_localy` или перенесите его в debug.
    - Избавьтесь от `copy.copy()` в `get_url` так как `current_url` всегда возвращает строку, и нет необходимости использовать копию.
    - Проверьте, что url является строкой в `get_url`, чтобы не обрабатывать `None`.
    - Добавьте проверку `if url` в методе `window_open` чтобы исключить ошибки, в случае если url нет.
    - Удалите лишний `try-except` в методе `scroll`.
5. **Использование j_loads/j_loads_ns**:
    - В данном модуле не используется, но следует помнить при работе с json.
6. **Форматирование**:
   - Используйте одинарные кавычки (`'`) для строк в коде и двойные кавычки (`"`) только для операций вывода.

## Оптимизированный код:

```python
"""
Модуль для работы с веб-драйвером.
======================================

Этот модуль содержит класс :class:`Driver`, который обеспечивает
унифицированный интерфейс для взаимодействия с Selenium веб-драйверами.
Класс предоставляет методы для инициализации драйвера, навигации,
управления cookie, обработки исключений и других операций.

Пример использования
----------------------
.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import copy
import time
from pathlib import Path
import re
import pickle

from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By
from src.logger.logger import logger # Изменено: импорт logger
import src.config.global_settings as gs # type: ignore # noqa: F401
from typing import Optional

class Driver:
    """
    Класс для взаимодействия с Selenium веб-драйверами.

    :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
    :type webdriver_cls: selenium.webdriver
    :param *args: Позиционные аргументы для инициализации драйвера.
    :type *args: list
    :param **kwargs: Именованные аргументы для инициализации драйвера.
    :type **kwargs: dict
    :raises TypeError: Если `webdriver_cls` не является валидным классом WebDriver.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url: Optional[str] = None
        self.html_content: Optional[str] = None


    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :type browser_name: str, optional
        :param **kwargs: Дополнительные аргументы.
        :type **kwargs: dict
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Прокси для доступа к атрибутам драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Значение атрибута драйвера.
        :rtype: Any
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
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: True, если прокрутка выполнена успешно, иначе False.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
             for _ in range(scrolls):
                 try:
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                 except Exception as ex:
                     logger.error('Error while scrolling', exc_info=ex)
                     return False
             return True
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе None.
        :rtype: str, optional
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Failed to determine site language from META', ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Failed to determine site language from JavaScript', ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и cookie.

        :param url: URL для перехода.
        :type url: str
        :return: True, если переход успешен, иначе False.
        :rtype: bool
        """
        if not isinstance(url, str):
            logger.error(f"URL is not string: {url}")
            return False
        _previous_url = self.current_url #  Изменено: удалено копирование url

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
             logger.error(f'Error navigating to URL: {url}\n', exc_info=ex)
             return False


    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        :param url: URL для открытия в новой вкладке.
        :type url: str, optional
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
        Сохраняет текущие cookie веб-драйвера в локальный файл.
        """
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Error saving cookies:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Получает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для получения HTML-контента.
        :type url: str
        :return: True, если контент успешно получен, иначе None.
        :rtype: bool, optional
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