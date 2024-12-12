# Анализ кода модуля `driver.py`

**Качество кода: 7/10**

*   **Плюсы**
    *   Код имеет хорошую структуру и разделение на методы.
    *   Используется логгирование для отслеживания ошибок.
    *   Присутствует обработка исключений.
    *   Реализована возможность прокрутки страницы в разных направлениях.
    *   Реализовано сохранение куки.
    *   Поддержка открытия новой вкладки.
    *   Доступ к атрибутам драйвера через `__getattr__`
    *   Унифицированный интерфейс для работы с веб-драйверами Selenium.
*   **Минусы**
    *   Не все методы и функции имеют docstring.
    *   Используется `time.sleep` для задержки, что не является лучшей практикой.
    *   В `_save_cookies_localy` заглушка `return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`
    *   Некоторые try-except блоки можно заменить на логирование ошибок через `logger.error`.
    *   Отсутствуют проверки на None для некоторых переменных.
    *   Не используется `j_loads` или `j_loads_ns` для чтения файлов.

**Рекомендации по улучшению**

1.  Добавить docstring к каждому методу и функции, включая описание параметров и возвращаемых значений в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `time.sleep` на более подходящий способ ожидания (например, `WebDriverWait` из Selenium, если необходимо).
4.  Удалить заглушку `return True` из `_save_cookies_localy` и реализовать сохранение куки.
5.  Пересмотреть блоки try-except, заменяя их на вызовы `logger.error` для упрощения кода.
6.  Добавить проверки на `None` для переменных перед их использованием.
7.  Избегать использования `copy.copy` без крайней необходимости, т.к. это лишняя операция.
8.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо.
9.  Уточнить, является ли обязательным использование `pickle.dump`, если да то добавить проверку на наличие файла.
10. Добавить комментарии после каждого `#`
11. Переписать все комментарии в формате RST

**Оптимизированный код**

```python
"""
Модуль для работы с веб-драйверами Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Driver`, который используется для унифицированного взаимодействия с веб-драйверами Selenium.
Класс включает методы для инициализации драйвера, навигации по веб-страницам, работы с куки,
обработки исключений и других операций.

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
from pathlib import Path
import pickle
from typing import Optional, Any
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By
from src.logger.logger import logger


class Driver:
    """
    Класс для унифицированного взаимодействия с веб-драйверами Selenium.
    """
    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует экземпляр драйвера.

        :param webdriver_cls: Класс WebDriver (например, Chrome, Firefox).
        :type webdriver_cls: class
        :param *args: Позиционные аргументы для инициализации драйвера.
        :param **kwargs: Ключевые аргументы для инициализации драйвера.
        :raises TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        #  создание экземпляра драйвера
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url: Optional[str] = None
        self.html_content: Optional[str] = None

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
        #  установка имени браузера для класса
        cls.browser_name = browser_name

    def __getattr__(self, item):
        """
        Проксирует доступ к атрибутам драйвера.

        :param item: Имя атрибута.
        :type item: str
        :return: Значение атрибута драйвера.
        """
        #  возвращение атрибута драйвера
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает страницу в указанном направлении.

        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки в пикселях.
        :type frame_size: int
        :param direction: Направление прокрутки ('both', 'forward', 'backward', 'down', 'up').
        :type direction: str
        :param delay: Задержка между прокрутками в секундах.
        :type delay: float
        :return: `True`, если прокрутка прошла успешно, иначе `False`.
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
            :param delay: Задержка между прокрутками в секундах.
            :type delay: float
            :return: `True`, если прокрутка прошла успешно, иначе `False`.
            :rtype: bool
            """
            try:
                for _ in range(scrolls):
                     #  выполнение javascript для прокрутки страницы
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                 #  логирование ошибки прокрутки
                logger.error('Ошибка при прокрутке', exc_info=ex)
                return False

        try:
            if direction in ('forward', 'down'):
                 #  прокрутка вниз
                return carousel('', scrolls, frame_size, delay)
            elif direction in ('backward', 'up'):
                 #  прокрутка вверх
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                #  прокрутка вниз и вверх
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
             #  логирование ошибки в функции прокрутки
            logger.error('Ошибка в функции прокрутки', exc_info=ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Определяет язык страницы на основе мета-тегов или JavaScript.

        :return: Код языка, если найден, иначе `None`.
        :rtype: Optional[str]
        """
        try:
             #  поиск мета-тега с языком
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
             #  возвращение значения атрибута content
            return meta_language.get_attribute('content')
        except Exception as ex:
             #  логирование ошибки при определении языка из мета-тега
            logger.debug('Не удалось определить язык сайта из META', exc_info=ex)
            try:
                 #  попытка определить язык из javascript
                return self.get_page_lang()
            except Exception as ex:
                 #  логирование ошибки при определении языка из javascript
                logger.debug('Не удалось определить язык сайта из JavaScript', exc_info=ex)
                return None

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        :param url: URL для перехода.
        :type url: str
        :return: `True`, если переход успешен, иначе `False`.
        :rtype: bool
        """
        try:
             #  копирование текущего url
            _previous_url = self.current_url
        except Exception as ex:
            #  логирование ошибки при получении текущего URL
            logger.error("Ошибка при получении текущего URL", exc_info=ex)
            return False

        try:
             #  переход по url
            self.driver.get(url)
             # ожидание завершения загрузки страницы
            while self.ready_state != 'complete':
                ...

            if url != _previous_url:
                 #  сохранение предыдущего url
                self.previous_url = _previous_url
            #  сохранение куки
            self._save_cookies_localy()
            return True

        except WebDriverException as ex:
            #  логирование ошибки WebDriverException
            logger.error('WebDriverException', exc_info=ex)
            return False

        except InvalidArgumentException as ex:
             #  логирование ошибки InvalidArgumentException
            logger.error(f"InvalidArgumentException {url}", exc_info=ex)
            return False
        except Exception as ex:
             #  логирование ошибки при переходе по URL
            logger.error(f'Ошибка при переходе по URL: {url}\\n', exc_info=ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        """
        Открывает новую вкладку в текущем окне браузера и переключается на неё.

        :param url: URL для открытия в новой вкладке.
        :type url: Optional[str]
        """
        #  выполнение javascript для открытия новой вкладки
        self.execute_script('window.open();')
        #  переключение на новую вкладку
        self.switch_to.window(self.window_handles[-1])
        if url:
            # переход по url, если он передан
            self.get(url)

    def wait(self, delay: float = .3) -> None:
        """
        Ожидает указанное количество времени.

        :param delay: Время задержки в секундах.
        :type delay: float
        """
        #  ожидание delay секунд
        time.sleep(delay)

    def _save_cookies_localy(self) -> None:
        """
        Сохраняет текущие куки веб-драйвера в локальный файл.
        """
        try:
            # открытие файла для записи куки
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                #  сохранение куки
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            #  логирование ошибки при сохранении куки
            logger.error('Ошибка при сохранении куки:', exc_info=ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или веб-страницы.

        :param url: Путь к файлу или URL для извлечения HTML-контента.
        :type url: str
        :return: `True`, если контент успешно получен, иначе `False`.
        :rtype: Optional[bool]
        """
        if url.startswith('file://'):
             #  удаление префикса file:// из url
            cleaned_url = url.replace('file://', '')
            #  поиск пути файла
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                # создание объекта Path из пути файла
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        #  открытие и чтение html файла
                        with open(file_path, 'r', encoding='utf-8') as file:
                            #  сохранение html контента
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                         #  логирование ошибки при чтении файла
                        logger.error('Ошибка при чтении файла:', exc_info=ex)
                        return False
                else:
                     #  логирование ошибки если локальный файл не найден
                    logger.error('Локальный файл не найден:', file_path)
                    return False
            else:
                 #  логирование ошибки если некорректный путь файла
                logger.error('Некорректный путь к файлу:', cleaned_url)
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                #  получение html контента по url
                if self.get_url(url):
                     #  сохранение html контента
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                 #  логирование ошибки при получении html по url
                logger.error(f"Ошибка при получении {url}:", exc_info=ex)
                return False
        else:
             #  логирование ошибки если протокол не поддерживается
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False
```