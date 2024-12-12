# Анализ кода модуля `chrome`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует классы для инкапсуляции функциональности.
    - Применяются логирование для отслеживания ошибок и хода выполнения программы.
    - Используется `j_loads_ns` для загрузки JSON, что соответствует требованиям.
    - Присутствует обработка исключений для предотвращения сбоев программы.
    - Код достаточно хорошо документирован с использованием комментариев.
-  Минусы
    - Некоторые комментарии не соответствуют стандарту RST.
    - Не везде используется обработка ошибок через `logger.error`, вместо этого применяются стандартные блоки `try-except`.
    - В коде есть `...`, которые являются точками остановки и требуют дополнительной обработки.
    - В коде присутствуют todo.

**Рекомендации по улучшению**
- Необходимо переписать docstring в формате reStructuredText (RST).
- Заменить `try-except` на `logger.error` там, где это возможно.
- Заменить все `...` на корректный код.
- Удалить `WebDriverException` и обьединить с общим `Exception`.
- Все комментарии после `#` должны пояснять код, который следует за ними.
- Необходимо добавить обработку случая, когда не удалось выделить порт.

**Оптимизированный код**
```python
"""
Модуль для работы с веб-драйвером Chrome.
=========================================================================================

Этот модуль предоставляет класс :class:`Chrome`, который является подклассом
`selenium.webdriver.Chrome` и обеспечивает дополнительную функциональность для
настройки и управления веб-драйвером Chrome.

Пример использования
--------------------

Пример инициализации класса `Chrome`:

.. code-block:: python

    from src.webdriver.chrome.chrome import Chrome

    driver = Chrome()
    driver.get('https://www.example.com')
    driver.quit()
"""
import os
import socket
from pathlib import Path
from typing import List, Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent

from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Chrome(webdriver.Chrome):
    """
    Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительную функциональность.

    Этот класс расширяет возможности стандартного веб-драйвера Chrome,
    добавляя методы для настройки параметров запуска и управления портом.
    """

    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """
        Инициализирует веб-драйвер Chrome с заданными опциями и профилем.

        :param user_agent: Настройки User-Agent для веб-драйвера Chrome.
          Подробнее: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066
        :type user_agent: dict, optional
        :raises Exception: Если возникает ошибка при настройке или инициализации драйвера.
        """
        # устанавливаем user_agent или используем случайный из UserAgent()
        self.user_agent = user_agent if user_agent else UserAgent().random
        try:
            # загружает настройки chrome из файла chrome.json
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical("Ошибка в конфигурационном файле 'chrome.json'.")
                return

            # определяет директорию профиля пользователя
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')

            # формирует путь к драйверу chrome
            chromedriver_path_parts: list = settings['driver']['chromedriver']
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))

            # формирует путь к исполняемому файлу chrome
            binary_location_parts: list = settings['driver']['chrome_binary']
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))

            # устанавливаем опции chrome
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')
            
            # устанавливаем chrome service
            self.service = ChromeService(executable_path=binary_location)
            
            # задаём порт для webdriver
            free_port = gs.webdriver_current_port
            gs.webdriver_current_port += 1
            
            if free_port:
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт веб-драйвера: {free_port}')
            else:
                logger.critical("Нет свободных портов в диапазоне (9500, 9599)")
                return

        except Exception as e:
            logger.error('Ошибка при настройке веб-драйвера Chrome.', exc_info=True)
            return

        try:
            logger.info("Запуск веб-драйвера Chrome")
            super().__init__(options=self.options, service=self.service)

        except Exception as ex:
            logger.error("Веб-драйвер Chrome не запустился. Общая ошибка:", exc_info=True)
            return

    def find_free_port(self, start_port: int, end_port: int) -> int |  None:
        """
        Находит свободный порт в заданном диапазоне.

        :param start_port: Начальный порт диапазона.
        :type start_port: int
        :param end_port: Конечный порт диапазона.
        :type end_port: int
        :return: Свободный порт, если доступен, иначе None.
        :rtype: int | None
        """
        for port in range(start_port, end_port + 1):
            try:
                # пробуем забиндить порт для проверки свободен ли он
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError as ex:
                logger.debug(f"Порт {port} занят", exc_info=True)
        return None

    def set_options(self, settings: dict = None) -> ChromeOptions:
        """
        Устанавливает параметры запуска для веб-драйвера Chrome.

        :param settings: Конфигурационные настройки для опций Chrome.
        :type settings: dict, optional
        :return: Объект `ChromeOptions` с заданными параметрами запуска.
        :rtype: ChromeOptions
        """
        if not settings or ('options' not in settings and 'headers' not in settings):
            return ChromeOptions()

        options = ChromeOptions()

        if 'options' in settings:
            # конвертирует список формата [key=value, key2=value2, ...] в словарь
            options_dict = {}
            for item in settings['options']:
                key, value = item.split('=')
                options_dict[key.strip()] = value.strip()
        
            # устанавливает настройки из словаря в ChromeOptions
            [options.add_argument(f"--{key}={value}") for key, value in options_dict.items()]

        if 'headers' in settings and settings['headers']:
            [options.add_argument(f"--{key}={value}") for key, value in settings['headers'].items()]

        return options
```