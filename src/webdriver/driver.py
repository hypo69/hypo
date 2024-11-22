## \file hypotez/src/webdriver/driver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.webdriver
   :platform: Windows, Unix
   :synopsis: Модуль для работы с веб-драйверами Selenium.
"""

MODE = 'development'

import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (InvalidArgumentException, 
                                        ElementClickInterceptedException, 
                                        ElementNotInteractableException, 
                                        ElementNotVisibleException )
import header
from src import gs
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException

class Driver:
    """
    Класс `Driver` для взаимодействия с веб-браузерами с помощью Selenium WebDriver.

    Этот класс обеспечивает унифицированный интерфейс для различных веб-драйверов, таких как Chrome, Firefox и Edge.
    Он включает методы для навигации по URL-адресам, прокрутки страниц, извлечения контента и обработки куки.

    Атрибуты:
        driver (selenium.webdriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        Инициализирует класс `Driver` с указанным веб-драйвером.

        Args:
            webdriver_cls (type): Класс WebDriver из `selenium.webdriver`, например `Chrome`, `Firefox` или `Edge`.
            *args: Дополнительные позиционные аргументы, передаваемые в конструктор WebDriver.
            **kwargs: Дополнительные ключевые аргументы, передаваемые в конструктор WebDriver.

        Возвращает:
            None

        Исключения:
            TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError("`webdriver_cls` должен быть допустимым классом WebDriver.")
        self.driver = webdriver_cls(*args, **kwargs)

    def __init_subclass__(cls, *, browser_name=None, **kwargs):
        """
        Определяет поведение для подклассов `Driver`.

        Args:
            browser_name (str): Имя браузера, для которого создается драйвер.
            **kwargs: Дополнительные аргументы для базового класса.
        """
        super().__init_subclass__(**kwargs)
        if browser_name is None:
            raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
        cls.browser_name = browser_name
     
    def __getattr__(self, item):
        """
        Прокси для доступа к аттрибутам WebDriver.

        Args:
            item (str): Имя атрибута для доступа.

        Возвращает:
            Any: Значение атрибута из экземпляра WebDriver.
        """
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """
        Прокручивает веб-страницу.

        Args:
            scrolls (int, optional): Количество прокруток. По умолчанию 1.
            frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 1800.
            direction (str, optional): Направление прокрутки. Возможные значения: 'both', 'down', 'up'. По умолчанию 'both'.
            delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.

        Возвращает:
            bool: `True`, если прокрутка выполнена успешно, `False` в противном случае.

        Исключения:
            Exception: Если произошла ошибка во время прокрутки.
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """
            Прокручивает экран вверх или вниз.

            Args:
                direction (str, optional): 'down', 'up', 'both'. По умолчанию 'both'.
                scrolls (int, optional): Количество прокруток. По умолчанию 5.
                frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 1800.
                delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 1.

            Возвращает:
                bool: `True`, если прокрутка выполнена успешно, `False` в противном случае.

            Исключения:
                Exception: Если произошла ошибка во время прокрутки.
            """
            try:
                for i in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error("Ошибка при прокрутке", exc_info=ex)
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                if not carousel('', scrolls, frame_size, delay) or not carousel('-', scrolls, frame_size, delay):
                    return False
                return True
        except Exception as ex:
            logger.error("Ошибка в функции прокрутки", ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """
        Попытка определить язык страницы.

        Возвращает:
            Optional[str]: Код языка, если он найден, `None` в противном случае.

        Исключения:
            Exception: Если произошла ошибка при определении языка.
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute("content")
        except Exception as ex:
            logger.debug("Не удалось определить язык сайта из META", ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug("Не удалось определить язык сайта из JavaScript", ex)
                return

    def get_url(self, url: str) -> bool:
        """
        Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

        Args:
            url (str): URL для перехода.

        Возвращает:
            bool: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

        Исключения:
            WebDriverException: Если возникает ошибка с WebDriver.
            InvalidArgumentException: Если URL некорректен.
            Exception: Для любых других ошибок при переходе.
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", ex)
            return False
        
        try:
            self.driver.get(url)
            
            while self.ready_state != 'complete':
                """ Ожидаем завершения загрузки страницы """

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True
            
        except WebDriverException as ex:
            logger.error('WebDriverException', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
            return False

    def fetch_html(self, url: str) -> Optional[bool]:
        """
        Извлекает HTML-контент из файла или URL и парсит его с помощью BeautifulSoup и XPath.

        Args:
            url (str): Путь к файлу или URL для извлечения HTML-контента.

        Возвращает:
            Optional[bool]: `True` при успешном получении контента, `None` в противном случае.

        Исключения:
            Exception: Если произошла ошибка при извлечении контента.
        """
        if url.startswith('file://'):
            cleaned_url = url.replace('file://', '')
        
            match = re.search(r'[a-zA-Z]:[\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Ошибка при чтении файла:', ex)
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path)
                    return False
            else:
                logger.error('Некорректный путь к файлу:', cleaned_url)
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при получении {url}:", ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False

    def _save_cookies_localy(self):
        """
        Сохраняет куки в локальный файл.

        Возвращает:
            None

        Исключения:
            Exception: Если произошла ошибка при сохранении куки.
        """
        try:
            with open(gs.cookies_filepath, 'wb') as cookiesfile:
                pickle.dump(self.driver.get_cookies(), cookiesfile)
        except Exception as ex:
            logger.error('Ошибка при сохранении куки:', ex)

    def wait(self, delay: float = .3) -> None:
        """
        Ждет указанное количество времени.

        Args:
            delay (float, optional): Время задержки в секундах. По умолчанию 0.3.

        Возвращает:
            None
        """
        time.sleep(delay)
