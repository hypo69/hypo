# Анализ кода модуля `driver.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и документирован в формате RST.
    - Присутствует обработка исключений и логирование ошибок.
    - Используется проксирование атрибутов для доступа к драйверу.
    - Реализована поддержка прокрутки страницы в разных направлениях.
    - Есть методы для сохранения куки и извлечения HTML контента.
- Минусы
    - Некоторые блоки `try-except` можно заменить на обработку ошибок через `logger.error`.
    - В некоторых местах используется стандартный `Exception`, что делает отладку более сложной, лучше использовать более конкретные исключения.
    - Метод `_save_cookies_localy` закомментирован для отладки и не выполняет свою функцию.
    - Не везде используется форматирование f-string.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить отсутствующие импорты, такие как `copy`, `time`, `pickle`, `re`, `Path` и `By` из `selenium.webdriver.common.by`.
2.  **Логирование ошибок**: Заменить некоторые стандартные блоки `try-except` на использование `logger.error` с передачей исключения и контекстной информацией.
3.  **Использование `f-string`**: Использовать `f-string` для более удобного форматирования строк.
4.  **Обработка исключений**: Использовать более конкретные исключения вместо общего `Exception`, где это возможно.
5.  **Метод `_save_cookies_localy`**: Раскомментировать и убедиться в корректной работе метода сохранения куки.
6.  **Улучшить документацию**: Добавить более подробные описания для некоторых методов и переменных в формате reStructuredText.
7.  **Унификация именования**: Привести в соответствие имена переменных и функций с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который обеспечивает унифицированный интерфейс
для взаимодействия с веб-драйверами Selenium.
Класс предоставляет методы для инициализации драйвера, навигации по веб-страницам, работы с куки,
обработки исключений и других операций.

Пример использования
--------------------

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
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By
from src.logger.logger import logger
from src.config.settings import gs



class Driver:
    """
    Класс для управления веб-драйвером Selenium.

    :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
    :param *args: Позиционные аргументы для инициализации драйвера.
    :param **kwargs: Ключевые аргументы для инициализации драйвера.
    :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        # Проверка, является ли `webdriver_cls` допустимым классом WebDriver.
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        # Инициализация экземпляра веб-драйвера.
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url: Optional[str] = None
        self.html_content: Optional[str] = None

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Автоматически вызывается при создании подкласса `Driver`.

        :param browser_name: Имя браузера.
        :param **kwargs: Дополнительные аргументы.
        :raises ValueError: Если `browser_name` не указан.
        """
        super().__init_subclass__(**kwargs)
        # Проверка наличия имени браузера
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        # Установка имени браузера в класс
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Прокси для доступа к атрибутам драйвера.

        :param item: Имя атрибута.
        :return: Атрибут драйвера.
        """
        # Возвращает запрошенный атрибут драйвера
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток.
        :param frame_size: Размер прокрутки в пикселях.
        :param direction: Направление прокрутки ('both', 'down', 'up').
        :param delay: Задержка между прокрутками.
        :return: True, если прокрутка выполнена успешно, False в противном случае.
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Внутренняя функция для выполнения прокрутки.

            :param direction: Направление прокрутки ('', '-').
            :param scrolls: Количество прокруток.
            :param frame_size: Размер прокрутки в пикселях.
            :param delay: Задержка между прокрутками.
            :return: True, если прокрутка выполнена успешно, False в противном случае.
            """
            try:
                # Выполнение прокрутки указанное количество раз
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка при прокрутке', exc_info=ex)
                return False

        try:
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
        """
        try:
            # Попытка получения языка из мета-тега
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', exc_info=ex)
            try:
                 # Попытка получения языка через JavaScript
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', exc_info=ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        :param url: URL для перехода.
        :return: True, если переход успешен, False в противном случае.
        """
        try:
            # Сохранение предыдущего URL
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False
        
        try:
            # Переход по URL
            self.driver.get(url)

            # Ожидание полной загрузки страницы
            while self.ready_state != 'complete':
               ...

            # Сохранение предыдущего URL, если он отличается от текущего
            if url != _previous_url:
                self.previous_url = _previous_url
            
            # Сохранение куки
            self._save_cookies_localy()
            return True
        
        except WebDriverException as ex:
            logger.error('WebDriverException', exc_info=ex)
            return False
        
        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        :param url: URL для открытия в новой вкладке.
        """
        # Открывает новую вкладку
        self.execute_script('window.open();')
        # Переключается на новую вкладку
        self.switch_to.window(self.window_handles[-1])
        # Переходит по URL, если он указан
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах.
        """
        # Приостанавливает выполнение на указанное время
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        try:
            # Сохранение куки в файл
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', exc_info=ex)


    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :return: True, если контент успешно получен, None в случае ошибки.
        """
        if url.startswith('file://'):
            # Обработка локального файла
            cleaned_url = url.replace('file://', '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        # Чтение HTML-контента из файла
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
            # Обработка URL
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