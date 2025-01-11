# Анализ кода модуля `src.webdriver.driver`

**Качество кода: 7/10**
- Плюсы:
    -  Код предоставляет унифицированный интерфейс для работы с веб-драйверами Selenium.
    -  Реализованы основные функции для навигации, управления куками и обработки ошибок.
    -  Используется логирование ошибок для упрощения отладки.
    -  Есть поддержка чтения HTML из файлов и веб-страниц.
    -  Присутствуют проверки типов и базовые обработки ошибок.
- Минусы:
    -  Не все комментарии оформлены в формате RST.
    -  Используются стандартные блоки `try-except` вместо `logger.error` для обработки ошибок.
    -  В функции `_save_cookies_localy` есть закомментированный `return True`, что может говорить о проблемах в логике.
    -  Не хватает docstring для всех методов и классов.
    -  Импорты не оптимизированы.

**Рекомендации по улучшению**

1. **Форматирование документации**:
   -  Привести все комментарии и docstring к формату RST.
2. **Обработка ошибок**:
   -  Использовать `logger.error` для обработки ошибок вместо стандартных блоков `try-except`.
3. **Логирование**:
   -  Импортировать и использовать `logger` из `src.logger.logger`.
4. **Рефакторинг**:
   -  Удалить неиспользуемый `return True` в `_save_cookies_localy`.
   -  Добавить подробные docstring для всех методов и классов.
5. **Импорты**:
    - Оптимизировать импорты, расположив их в начале файла.

**Оптимизированный код**

```python
"""
Модуль для управления веб-драйверами Selenium.
=========================================================================================

Модуль :mod:`src.webdriver.driver` предоставляет класс :class:`Driver`, который обеспечивает
унифицированный интерфейс для работы с веб-драйверами Selenium. Он включает методы для
инициализации драйвера, навигации, управления куками, обработки исключений и других операций.

Пример использования
--------------------

Пример создания экземпляра класса `Driver` и открытия URL:

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""

import copy
import time
import pickle
import re
from pathlib import Path
from typing import Optional, Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By

from src.logger.logger import logger
from src.utils.settings import gs


class Driver:
    """
    Класс для управления веб-драйверами Selenium.

    :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
    :type webdriver_cls: class
    :param *args: Позиционные аргументы для инициализации драйвера.
    :param **kwargs: Именованные аргументы для инициализации драйвера.
    :raises TypeError: Если `webdriver_cls` не является валидным классом WebDriver.
    """
    def __init__(self, webdriver_cls: WebDriver, *args: Any, **kwargs: Any) -> None:
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver: WebDriver = webdriver_cls(*args, **kwargs)
        self.previous_url: Optional[str] = None
        self.html_content: Optional[str] = None
        self.browser_name: Optional[str] = None

    def __init_subclass__(cls, *, browser_name: str = None, **kwargs: Any) -> None:
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Название браузера.
        :type browser_name: str
        :param **kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
        cls.browser_name = browser_name

    def __getattr__(self, item: str) -> Any:
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
        Выполняет прокрутку страницы в указанном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: True, если прокрутка прошла успешно, иначе False.
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
            :param delay: Задержка между прокрутками.
            :type delay: float
            :return: True, если прокрутка прошла успешно, иначе False.
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
            logger.error('Ошибка в функции scroll', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе None.
        :rtype: Optional[str]
        """
        try:
            # код выполняет поиск элемента по CSS селектору
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
        :return: True, если навигация прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
             logger.error("Ошибка получения текущего URL", exc_info=ex)
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
            logger.error('WebDriverException', exc_info=ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка перехода по URL: {url}\\n', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на нее.

        :param url: URL для открытия в новой вкладке.
        :type url: Optional[str]
        """
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get_url(url)

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
            logger.error('Ошибка сохранения куки:', exc_info=ex)


    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для получения HTML-контента.
        :type url: str
        :return: True, если контент успешно извлечен, иначе False.
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
                         logger.error('Ошибка чтения файла:', exc_info=ex)
                         return False
                else:
                     logger.error('Локальный файл не найден:', file_path)
                     return False
            else:
                logger.error('Неверный путь к файлу:', cleaned_url)
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
```