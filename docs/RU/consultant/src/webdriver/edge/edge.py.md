# Анализ кода модуля `edge`

**Качество кода**
7
-   Плюсы
    *   Код имеет базовую структуру, характерную для драйвера.
    *   Используется `fake_useragent` для генерации случайных `user-agent`.
    *   Настройки `webdriver` загружаются из файла `json`.
    *   Реализована обработка исключений при запуске `WebDriver`.
    *   Реализован механизм для добавления пользовательских опций и параметров запуска.
-   Минусы
    *   Не все функции имеют docstring.
    *   Используется неименованный импорт `from src import gs`.
    *   Используются стандартные `try-except` блоки.
    *   Отсутствует общая документация модуля.
    *   Не все методы класса документированы в формате reST.
    *   Метод `set_options` не используется внутри класса и не имеет описания в reST формате.
    *   В `_payload` методе не описан тип `ExecuteLocator`.

**Рекомендации по улучшению**

*   Добавить docstring для модуля.
*   Заменить импорт `from src import gs` на `from src.config import gs`.
*   Использовать `logger.error` вместо `try-except` блоков.
*   Добавить reST docstring для всех методов, включая `_payload` и `set_options`.
*   Удалить неиспользуемый метод `set_options`.
*   Сделать type hinting для `ExecuteLocator` в `_payload`.
*   Улучшить обработку ошибок и логирование, предоставляя больше контекста.
*   Привести код в соответствие с PEP8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для управления браузером Edge с использованием Selenium WebDriver.
======================================================================

Этот модуль предоставляет класс `Edge`, который расширяет возможности стандартного
WebDriver для Edge, добавляя поддержку кастомных `user-agent`, опций и параметров
запуска, сконфигурированных через JSON-файл.

Модуль также включает в себя функции для выполнения JavaScript кода на странице,
взаимодействия с элементами через локаторы и управления скриншотами элементов.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.edge.edge import Edge
    driver = Edge(options=['--headless', '--disable-gpu'])
    driver.get('https://www.example.com')
    driver.quit()

"""

import os
from pathlib import Path
from typing import Optional, List
from selenium.webdriver import Edge as WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException

# from src.webdriver.executor import ExecuteLocator #TODO Описать класс ExecuteLocator в reST документации
from src.webdriver.js import JavaScript
from fake_useragent import UserAgent
from src.config import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

class Edge(WebDriver):
    """
    Класс Edge для управления браузером Edge с использованием Selenium WebDriver.
    
    :param driver_name: Название драйвера. По умолчанию 'edge'.
    :type driver_name: str
    
    """
    driver_name: str = 'edge'

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Инициализирует драйвер Edge с заданным user-agent и опциями.

        :param user_agent: User-agent для браузера. Если не указан, будет сгенерирован случайный.
        :type user_agent: Optional[str]
        :param options: Список опций для запуска браузера.
        :type options: Optional[List[str]]
        :raises WebDriverException: Если не удается запустить WebDriver.
        :raises Exception: В случае возникновения общей ошибки.
        """
        # Инициализация user-agent
        self.user_agent = user_agent or UserAgent().random
        # Загрузка настроек из файла `edge.json`
        settings = j_loads_ns(Path(gs.path.src, 'webdriver', 'edge', 'edge.json'))

        # Инициализация опций Edge
        options_obj = EdgeOptions()
        options_obj.add_argument(f'user-agent={self.user_agent}')

        # Добавление пользовательских опций
        if options:
            for option in options:
                options_obj.add_argument(option)

        # Добавление опций из файла конфигурации
        if hasattr(settings, 'options') and settings.options:
            for option in settings.options:
                options_obj.add_argument(option)

        # Добавление заголовков из файла конфигурации
        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                options_obj.add_argument(f'--{key}={value}')
        try:
            logger.info('Starting Edge WebDriver')
            edgedriver_path = settings.executable_path.default
            service = EdgeService(executable_path=str(edgedriver_path))
            super().__init__(options=options_obj, service=service)
            self._payload()
        except WebDriverException as ex:
            # логирует ошибку запуска драйвера
            logger.error('Edge WebDriver failed to start:', exc_info=ex)
            return
        except Exception as ex:
            # Логирует ошибку общего характера
            logger.error('Edge WebDriver crashed. General error:', exc_info=ex)
            return

    def _payload(self) -> None:
        """
        Загружает исполнители для локаторов и JavaScript-сценариев.

        :return: None
        """
        # инициализация JavaScript executor
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        # Инициализация ExecuteLocator
        from src.webdriver.executor import ExecuteLocator
        execute_locator: ExecuteLocator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message

    # def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
    #     """
    #     Создаёт и конфигурирует параметры запуска для Edge WebDriver.
    #
    #     :param opts: Список опций для добавления в Edge WebDriver. По умолчанию None.
    #     :type opts: Optional[List[str]]
    #     :return: Объект EdgeOptions.
    #     :rtype: EdgeOptions
    #     """
    #     options = EdgeOptions()
    #     if opts:
    #         for opt in opts:
    #             options.add_argument(opt)
    #     return options

if __name__ == "__main__":
    driver = Edge(options=['--headless', '--disable-gpu'])
    driver.get('https://www.example.com')
    driver.quit()
```