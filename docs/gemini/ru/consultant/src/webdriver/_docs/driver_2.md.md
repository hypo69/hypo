# Анализ кода модуля `driver`

**Качество кода: 8/10**
-   **Плюсы**
    -   Хорошая структура, разделение на классы `DriverBase` и `DriverMeta`, что обеспечивает гибкость и расширяемость.
    -   Используется метакласс для динамического создания классов драйверов.
    -   Наличие базовых методов для управления браузером, таких как переходы по URL, скроллинг, сохранение куки и т.д.
    -   Присутствует логирование и обработка исключений.
-   **Минусы**
    -   Не все методы класса `DriverBase` имеют docstring в формате RST.
    -   Отсутствуют docstring для класса `Driver`.
    -   Импорты не отсортированы по алфавиту, и не хватает импорта `Any` из `typing`.
    -   Используются стандартные блоки `try-except` для обработки исключений, которые можно заменить на `logger.error` для большей читаемости.
    -   В методе `scroll` используется `time.sleep` для задержки, что не является лучшей практикой в асинхронных операциях.
    -   Некоторые комментарии могут быть более информативными.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате RST ко всем методам и классам.
    -   Использовать docstring Sphinx для более ясной документации.
2.  **Импорты**:
    -   Отсортировать импорты в алфавитном порядке.
    -   Добавить `Any` из `typing`.
3.  **Логирование**:
    -   Заменить стандартные `try-except` на `logger.error` для обработки исключений.
4.  **Обработка ошибок**:
    -   Добавить более подробное логирование ошибок.
5.  **Рефакторинг**:
    -   Удалить неиспользуемый импорт `sys`.
    -   Переименовать переменную `to_file` в методе `_save_cookies_localy` на `file_path`, чтобы подчеркнуть ее назначение.
    -   Избегать использования `time.sleep`, если есть возможность использовать другие методы задержки.
6.  **Комментарии**:
    -   В комментариях после `#` давать более подробное объяснение следующего за ними кода.
    -   Удалить лишние комментарии.

**Оптимизированный код**

```python
"""
Модуль для создания и управления веб-драйверами.
=========================================================================================

Этот модуль предоставляет базовый класс `DriverBase` для работы с веб-драйверами,
а также метакласс `DriverMeta`, позволяющий динамически создавать классы драйверов
для различных браузеров (например, Chrome, Firefox, Edge).

Класс `Driver` создается с помощью метакласса `DriverMeta`, который принимает класс
веб-драйвера (например, `Chrome`) и создает класс драйвера, который наследует
функциональность `DriverBase`.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome, Firefox, Edge

    # Создание экземпляра драйвера для Chrome
    d = Driver(Chrome)
    d.get_url("https://example.com")

"""
import copy
import pickle
import time
import urllib.parse
from pathlib import Path
from typing import Any, Type, Union

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException,
    InvalidArgumentException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src import gs
from src.logger.exceptions import WebDriverException
from src.logger.logger import logger
from src.utils.printer import pprint
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript


class DriverBase:
    """
    Базовый класс для веб-драйвера с общими атрибутами и методами.

    Этот класс содержит методы и атрибуты, общие для всех реализаций веб-драйверов,
    включая функциональность для взаимодействия со страницей, выполнение JavaScript
    и управление куками.
    """

    previous_url: str = ''
    referrer: str = ''
    page_lang: str = ''

    def __init__(self):
        """
        Инициализирует методы JavaScript и ExecuteLocator.
        """
        self.js = JavaScript()
        self.driver_execute = ExecuteLocator(self)

    def driver_payload(self) -> None:
        """
        Инициализирует необходимые методы для работы с драйвером.
        """
        self.js = JavaScript()
        self.driver_execute = ExecuteLocator(self)

    def scroll(self, scrolls: int = 3, frame_size: int = 500, direction: str = 'forward', delay: float = 0.5) -> None:
        """
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток.
        :param frame_size: Размер прокрутки в пикселях.
        :param direction: Направление прокрутки ('forward' или 'back').
        :param delay: Задержка между прокрутками.
        """
        try:
            # код исполняет прокрутку страницы
            for _ in range(scrolls):
                if direction == 'forward':
                    self.js.scroll_down(frame_size)
                elif direction == 'back':
                    self.js.scroll_up(frame_size)
                else:
                   logger.error(f'Неверно указано направление прокрутки: {direction}')
                   return
                time.sleep(delay)
        except Exception as ex:
             logger.error(f'Ошибка при прокрутке страницы', ex)

    def locale(self) -> str:
        """
        Определяет язык текущей страницы.

        :return: Язык страницы.
        """
        try:
            # код исполняет получение языка страницы
            lang = self.js.get_page_lang()
            if lang:
                self.page_lang = lang
            return self.page_lang
        except Exception as ex:
             logger.error(f'Ошибка при определении языка страницы', ex)

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и проверяет успешность перехода.

        :param url: URL для перехода.
        :return: True, если переход успешен, иначе False.
        """
        try:
            # код исполняет переход по указанному URL
            self.referrer = self.current_url
            self.previous_url = self.current_url
            self.driver.get(url)
            # Проверка успешности перехода
            if self.current_url == url:
                return True
            else:
                logger.error(f'Не удалось перейти на страницу {url}')
                return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе на страницу {url}', ex)
            return False

    def extract_domain(self, url: str) -> str:
        """
        Извлекает доменное имя из URL.

        :param url: URL для извлечения домена.
        :return: Доменное имя.
        """
        try:
            # код исполняет извлечение доменного имени из URL
            parsed_url = urllib.parse.urlparse(url)
            return parsed_url.netloc
        except Exception as ex:
            logger.error(f'Ошибка при извлечении домена из URL {url}', ex)
            return ''

    def _save_cookies_localy(self, file_path: Union[str, Path]) -> None:
        """
        Сохраняет куки в файл.

        :param file_path: Путь к файлу для сохранения куки.
        """
        try:
            # код исполняет сохранение куки в файл
            with open(file_path, 'wb') as file:
                pickle.dump(self.driver.get_cookies(), file)
        except Exception as ex:
             logger.error(f'Ошибка при сохранении куки в файл {file_path}', ex)

    def page_refresh(self) -> None:
        """
        Обновляет текущую страницу.
        """
        try:
            # код исполняет обновление текущей страницы
            self.driver.refresh()
        except Exception as ex:
            logger.error(f'Ошибка при обновлении страницы', ex)

    def window_focus(self) -> None:
        """
        Восстанавливает фокус на странице.
        """
        try:
           # код исполняет восстановление фокуса на странице
           self.driver.switch_to.window(self.driver.current_window_handle)
        except Exception as ex:
            logger.error(f'Ошибка при восстановлении фокуса на странице', ex)

    def wait(self, interval: float) -> None:
        """
        Делает паузу на указанное время.

        :param interval: Время паузы в секундах.
        """
        try:
            # код исполняет паузу на указанное время
            time.sleep(interval)
        except Exception as ex:
            logger.error(f'Ошибка при ожидании', ex)

    def delete_driver_logs(self) -> None:
        """
        Удаляет временные файлы и логи WebDriver.
        """
        try:
            # код исполняет удаление временных файлов и логов WebDriver
            if hasattr(self.driver, 'close'):
                self.driver.close()
            if hasattr(self.driver, 'quit'):
                self.driver.quit()
        except Exception as ex:
             logger.error(f'Ошибка при удалении логов и файлов драйвера', ex)

class DriverMeta(type):
    """
    Метакласс для создания класса Driver.

    Этот метакласс используется для динамического создания класса `Driver`,
    который наследует от `DriverBase` и указанного класса веб-драйвера.
    """
    def __call__(cls, webdriver_cls: Type, *args, **kwargs):
        """
        Создает новый класс `Driver`, наследуемый от `DriverBase` и указанного класса веб-драйвера.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :param args: Позиционные аргументы для конструктора веб-драйвера.
        :param kwargs: Именованные аргументы для конструктора веб-драйвера.
        :return: Новый класс `Driver`.
        """
        class Driver(DriverBase, webdriver_cls):
            """
            Динамически созданный класс WebDriver, наследуемый от DriverBase и указанного класса WebDriver.
            """
            def __init__(self, *args, **kwargs):
                """
                Инициализирует новый драйвер и вызывает driver_payload.
                """
                DriverBase.__init__(self)
                webdriver_cls.__init__(self, *args, **kwargs)
                self.driver_payload()
        return Driver


class Driver(metaclass=DriverMeta):
    """
    Динамически созданный класс WebDriver, наследуемый от DriverBase и указанного класса WebDriver.

    .. code-block:: python

        from src.webdriver.driver import Driver, Chrome, Firefox, Edge
        d = Driver(Chrome)

    """
    ...
```