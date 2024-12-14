# Анализ кода модуля `src.webdriver.driver`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание и поддержку.
    - Используется логирование для отслеживания ошибок и отладки.
    - Присутствует базовая обработка исключений для предотвращения сбоев программы.
    - Реализована возможность загрузки HTML контента как с веб-страниц, так и из локальных файлов.
- Минусы
    - Некоторые функции могут быть переработаны для более эффективного и читаемого кода.
    - Отсутствуют docstring для классов и методов, что затрудняет понимание их назначения и параметров.
    - В некоторых местах используется избыточный `try-except`.
    - В функции `_save_cookies_localy` есть заглушка `return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`, её необходимо удалить.

**Рекомендации по улучшению**

1.  **Добавить docstring:** Необходимо добавить документацию в формате reStructuredText (RST) для всех классов, методов и функций, чтобы сделать код более понятным и удобным в использовании.
2.  **Улучшить обработку ошибок:** Избегать избыточного использования `try-except`, предпочитать обработку с помощью `logger.error`.
3.  **Упростить функцию `scroll`:** Функция `scroll` может быть упрощена и оптимизирована.
4.  **Улучшить именование:** Привести имена функций и переменных к общему стилю, принятому в проекте.
5.  **Убрать заглушку:** Убрать заглушку `return True` в функции `_save_cookies_localy` и включить сохранение cookies.
6.  **Улучшить чтение файлов:** Использовать `j_loads` или `j_loads_ns` при чтении файлов.

**Оптимизированный код**

```python
"""
Модуль для работы с Selenium WebDriver.
========================================

Этот модуль предоставляет класс `Driver`, который упрощает взаимодействие с веб-драйверами Selenium.
Он включает методы для инициализации драйвера, навигации, управления cookie, обработки ошибок и других операций.

Пример использования
--------------------

Пример инициализации и использования класса `Driver`:

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

class Driver:
    """
    Класс для управления Selenium WebDriver.

    Предоставляет интерфейс для взаимодействия с веб-драйвером, включая навигацию,
    управление cookie и обработку ошибок.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        :type webdriver_cls: class
        :param *args: Позиционные аргументы для инициализации веб-драйвера.
        :type *args: tuple
        :param **kwargs: Именованные аргументы для инициализации веб-драйвера.
        :type **kwargs: dict
        :raises TypeError: Если `webdriver_cls` не является допустимым классом веб-драйвера.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Инициализирует подкласс `Driver`.

        Проверяет наличие обязательного аргумента `browser_name` при создании подкласса.
        :param browser_name: Название браузера.
        :type browser_name: str
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
        Перенаправляет запросы атрибутов к внутреннему объекту драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Атрибут объекта драйвера.
        :rtype: Any
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Выполняет прокрутку страницы в заданном направлении.

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
                    # код исполняет прокрутку страницы на заданное количество пикселей
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    # код исполняет ожидание
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка прокрутки', exc_info=ex)
                return False

        try:
            if direction in ('forward', 'down'):
                return carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции scroll', exc_info=ex)
            return False


    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы, используя метатеги или JavaScript.

        :return: Код языка, если он найден, иначе None.
        :rtype: Optional[str]
        """
        try:
            # Код ищет элемент meta с атрибутом http-equiv='Content-Language'
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            # Код возвращает значение атрибута 'content'
            return meta_language.get_attribute('content')
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из META', exc_info=ex)
            try:
                # Код вызывает метод для определения языка через JavaScript
                return self.get_page_lang()
            except Exception as ex:
                logger.debug('Не удалось определить язык сайта из JavaScript', exc_info=ex)
                return None


    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL, сохраняет cookie и предыдущий URL.

        :param url: URL для перехода.
        :type url: str
        :return: True, если переход успешен, иначе False.
        :rtype: bool
        """
        try:
            # Код копирует текущий URL
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False

        try:
            # Код выполняет переход по указанному URL
            self.driver.get(url)
            # Код ожидает загрузки страницы
            while self.ready_state != 'complete':
                ...
            # Код сохраняет предыдущий URL, если текущий URL изменился
            if url != _previous_url:
                self.previous_url = _previous_url
            # Код сохраняет cookie
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
        Открывает новое окно или вкладку и переключается на него.

        :param url: URL для открытия в новом окне.
        :type url: Optional[str]
        """
        # Код открывает новое окно
        self.execute_script('window.open();')
        # Код переключается на последнее открытое окно
        self.switch_to.window(self.window_handles[-1])
        # Если передан URL, код открывает его в новом окне
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает заданное время.

        :param delay: Время ожидания в секундах.
        :type delay: float
        """
        # Код выполняет ожидание
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет cookie веб-драйвера в локальный файл.
        """
        try:
            # Код открывает файл для записи cookie
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                # Код сохраняет cookie в файл
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении cookie:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Загружает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL веб-страницы.
        :type url: str
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: Optional[bool]
        """
        if url.startswith('file://'):
            # Код обрабатывает загрузку HTML из локального файла
            cleaned_url = url.replace('file://', '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        # Код открывает и читает файл
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
            # Код обрабатывает загрузку HTML с веб-страницы
            try:
                # Код выполняет переход по URL и сохраняет HTML
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при загрузке {url}:", exc_info=ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False
```