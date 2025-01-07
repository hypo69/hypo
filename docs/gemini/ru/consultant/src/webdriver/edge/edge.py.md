# Анализ кода модуля `edge`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, используется ООП подход.
    - Присутствует логирование ошибок и критических ситуаций.
    - Используется `fake_useragent` для генерации user-agent, что полезно для избежания блокировок.
    - Конфигурация Edge driver загружается из JSON файла, что обеспечивает гибкость.
    - Использование кастомного класса `Edge` для расширения возможностей `WebDriver`.
    - Присутствуют docstring для функций и классов, что делает код более понятным.
    - Применён reStructuredText в docstring.
- Минусы
    - Используется `j_loads_ns`, но не импортирован из `src.utils.jjson` - исправлено
    - В некоторых местах код использует `hasattr`, что может быть заменено на более явные проверки.
    -  Дублирование логики добавления параметров из конфигурационного файла в опции браузера.
    - Методы, которые выполняют схожие действия (например, `send_message` и `send_key_to_webelement`) имеют одинаковую реализацию.

**Рекомендации по улучшению**

1. **Импорты**: Добавить недостающие импорты.
2. **Обработка ошибок**:  Использовать `logger.error` вместо стандартного `try-except` в `__init__` для упрощения кода.
3. **Рефакторинг**:
   - Объединить логику добавления опций из `settings.options` и `options` в один цикл.
   - Повторное использование `EdgeOptions` можно вынести в отдельный метод.
   -  Сделать явным использование `vars(settings.headers)` для понимания, что используется атрибуты обьекта, а не просто словарь.
4. **Документация**:
   - Улучшить docstring для метода `set_options`.
   - Добавить комментарии в reStructuredText для переменных и методов.
5. **Унификация**:
    - `self.send_message = self.send_key_to_webelement = execute_locator.send_message` можно упростить, указав на один метод, то есть, `self.send_message = execute_locator.send_message`
    - Привести в соответсвие имена переменных, в соответсвии с предыдущими файлами.
6. **Проверка JSON**:
    - добавить проверку на существование и корректность данных в файле `edge.json`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.edge
   :platform: Windows, Unix
   :synopsis: Custom Edge WebDriver class with simplified configuration using fake_useragent.

"""

import os
from pathlib import Path
from typing import Optional, List, Any
from selenium.webdriver import Edge as WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from fake_useragent import UserAgent
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns




class Edge(WebDriver):
    """
    Custom Edge WebDriver class for enhanced functionality.

    :ivar driver_name: Name of the WebDriver used, defaults to 'edge'.
    :vartype driver_name: str
    """
    driver_name: str = 'edge'

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Edge WebDriver with the specified user agent and options.

        :param user_agent: The user-agent string to be used. If `None`, a random user agent is generated.
        :type user_agent: Optional[str]
        :param options: A list of Edge options to be passed during initialization.
        :type options: Optional[List[str]]
        """
        self.user_agent = user_agent or UserAgent().random
        # Загрузка настроек из JSON файла
        settings = j_loads_ns(Path(gs.path.src, 'webdriver', 'edge', 'edge.json'))

        # Инициализация объекта EdgeOptions
        options_obj = self._get_edge_options()

        # Добавление опций из параметров
        if options:
            for option in options:
                options_obj.add_argument(option)

        # Добавление опций из конфигурационного файла
        if hasattr(settings, 'options') and settings.options:
            for option in settings.options:
                options_obj.add_argument(option)

        # Добавление заголовков из конфигурационного файла
        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                 options_obj.add_argument(f'--{key}={value}')

        try:
            logger.info('Starting Edge WebDriver')
            # Получение пути к исполняемому файлу EdgeDriver из настроек
            edgedriver_path = settings.executable_path.default
            # Инициализация сервиса EdgeDriver
            service = EdgeService(executable_path=str(edgedriver_path))
            # Инициализация Edge WebDriver с заданными опциями и сервисом
            super().__init__(options=options_obj, service=service)
            self._payload()
        except WebDriverException as ex:
            # Обработка ошибки запуска WebDriver
            logger.error('Edge WebDriver failed to start:', ex)
            return
        except Exception as ex:
            # Обработка прочих ошибок
            logger.error('Edge WebDriver crashed. General error:', ex)
            return

    def _get_edge_options(self) -> EdgeOptions:
        """
        Create and configure launch options for the Edge WebDriver.
        """
        options_obj = EdgeOptions()
        options_obj.add_argument(f'user-agent={self.user_agent}')
        return options_obj

    def _payload(self) -> None:
        """
        Load executors for locators and JavaScript scenarios.
        """
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        executor = ExecuteLocator(self)
        self.execute_locator = executor.execute_locator
        self.get_webelement_as_screenshot = executor.get_webelement_as_screenshot
        self.get_webelement_by_locator = executor.get_webelement_by_locator
        self.get_attribute_by_locator = executor.get_attribute_by_locator
        self.send_message = executor.send_message
        self.send_key_to_webelement = executor.send_message


    def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
        """
        Create and configure launch options for the Edge WebDriver.

        :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.
        :type opts: Optional[List[str]]
        :return: Configured `EdgeOptions` object.
        :rtype: EdgeOptions
        """
        options = EdgeOptions()
        if opts:
            for opt in opts:
                options.add_argument(opt)
        return options


if __name__ == "__main__":
    driver = Edge(options=["--headless", "--disable-gpu"])
    driver.get("https://www.example.com")