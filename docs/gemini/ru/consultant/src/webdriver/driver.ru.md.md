# Анализ кода модуля `driver.py`

**Качество кода**
7
-   Плюсы
    -   Код имеет четкую структуру и разделен на методы.
    -   Присутствует обработка исключений с логированием ошибок.
    -   Используется `reStructuredText` для документации.
    -   Есть проверка на валидность класса веб-драйвера.
    -   Реализована прокрутка страницы, открытие новой вкладки, ожидание и сохранение куки.
-   Минусы
    -   Отсутствуют некоторые импорты, которые используются в коде.
    -   В некоторых местах используются стандартные `try-except`, которые можно заменить на `logger.error`.
    -   Присутствует `...` в обработке ошибок, которые нужно убрать.
    -   Некоторые docstring можно улучшить, добавив больше конкретики.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов (хотя в данном случае этого и не требуется).
    -   Много комментариев `#` не соответствуют стандарту RST.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить недостающие импорты `time`, `copy`, `pickle`, `re`, `Optional`, `Any`, `Path`, `By`, `WebDriverException`, `InvalidArgumentException` из соответствующих библиотек.
2.  **Логирование**: Заменить стандартные `try-except` на `logger.error` с передачей исключения.
3.  **Удаление `...`**: Убрать точки остановки `...` из обработки ошибок и заменить их на `return` или `continue`, если это требуется.
4.  **Docstring**: Улучшить docstring, добавив более конкретное описание параметров и возвращаемых значений, а также использование reStructuredText.
5.  **Удалить лишнее**: Убрать лишний комментарий `# <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`.
6.  **Комментарии:** Переписать комментарии в стиле RST.

**Оптимизированный код**

```python
"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль содержит класс :class:`Driver`, который обеспечивает унифицированный интерфейс для
взаимодействия с веб-драйверами Selenium, упрощая навигацию, работу с куки, обработку исключений и другие операции.

Пример использования
--------------------

.. code-block:: python

    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    driver.get_url('https://example.com')
"""
import time
import copy
import pickle
import re
from pathlib import Path
from typing import Optional, Any
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from src.logger.logger import logger
from src.config.settings import gs

class Driver:
    """
    Класс для управления веб-драйвером Selenium.

    Предоставляет методы для инициализации драйвера, навигации по веб-страницам,
    работы с куки, обработки исключений и других операций.
    """

    def __init__(self, webdriver_cls: WebDriver, *args, **kwargs):
        """
        Инициализирует драйвер.

        :param webdriver_cls: Класс WebDriver (например, Chrome, Firefox).
        :type webdriver_cls: WebDriver
        :param *args: Позиционные аргументы для инициализации драйвера.
        :param **kwargs: Ключевые аргументы для инициализации драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name: str = None, **kwargs):
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
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'down', 'up', 'forward', 'backward').
        :type direction: str
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: True, если прокрутка выполнена успешно, False в противном случае.
        :rtype: bool
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
             Выполняет прокрутку страницы в заданном направлении.
            
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
                     # Код исполняет прокрутку страницы на заданный frame_size
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка при прокрутке', exc_info=ex)
                return False

        try:
             # Проверка и выбор направления прокрутки
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
        """
        try:
            # Код исполняет поиск элемента META
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
        :return: True, если переход успешен, False в противном случае.
        :rtype: bool
        """
        try:
            # Код сохраняет текущий url перед переходом
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False

        try:
            # Код выполняет переход по url
            self.driver.get(url)

            while self.ready_state != 'complete':
                """ Ожидаем завершения загрузки страницы """
            
            # Проверка, что url изменился
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
            logger.error(f'Ошибка при переходе по URL: {url}\\n', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        :param url: URL для открытия в новой вкладке.
        :type url: Optional[str]
        """
         # Код исполняет открытие новой вкладки и переключение на нее
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        # Удаление лишнего комментария
        try:
            # Код исполняет сохранение куки в локальный файл
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: True, если контент успешно получен, иначе None.
        :rtype: Optional[bool]
        """
        if url.startswith('file://'):
            cleaned_url = url.replace('file://', '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                         # Код исполняет чтение html контента из файла
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
                # Код исполняет получение html контента из url
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