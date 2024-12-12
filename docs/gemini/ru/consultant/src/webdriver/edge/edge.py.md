# Анализ кода модуля `edge`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и использует классы для инкапсуляции логики.
    - Используются `EdgeOptions` для настройки браузера.
    - Логирование ошибок с помощью `logger`.
    - Использование `fake_useragent` для генерации случайного `user-agent`.
    - Применение `j_loads_ns` для загрузки JSON-конфигурации.
- Минусы
    - Отсутствуют подробные docstring для класса и методов.
    - Не все методы имеют аннотации типов.
    - Использование `...` в блоках `except` не является информативным.
    - Некоторые имена переменных не соответствуют стандарту (например, `j` в `_payload`).
    - Не хватает обработки `user_agent` в конструкторе.

**Рекомендации по улучшению**

1.  Добавить docstring к классам и методам в формате reStructuredText.
2.  Добавить аннотации типов для переменных и параметров функций.
3.  Заменить `...` на более конкретную логику логирования и обработки ошибок.
4.  Переименовать переменные для соответствия стандартам (например, `j` на `js_executor`).
5.  Уточнить обработку `user_agent` в конструкторе, чтобы использовать дефолтное значение, если передан `None`.
6.  Добавить проверку существования `edgedriver_path` перед созданием `EdgeService`.
7.  Добавить обработку случая, когда `edgedriver_path` не найден в JSON-файле.
8.  Использовать более информативные сообщения при логировании ошибок.
9.  Добавить проверки для входных параметров, где это необходимо.
10. Привести в соответствие имя метода `send_message = self.send_key_to_webelement = execute_locator.send_message`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления браузером Microsoft Edge.
=========================================================================================

Этот модуль предоставляет класс :class:`Edge`, который является расширением стандартного
WebDriver для Edge. Он упрощает настройку и использование WebDriver, включая
возможность использования случайного User-Agent.

Пример использования
--------------------

Пример использования класса `Edge`:

.. code-block:: python

    edge_driver = Edge()
    edge_driver.get("https://www.example.com")
    edge_driver.quit()
"""

MODE = 'dev'

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
    Расширенный класс WebDriver для Microsoft Edge.

    Предоставляет дополнительные возможности для управления браузером Edge,
    включая установку пользовательского User-Agent и упрощенную настройку.

    :param user_agent: Словарь для настройки User-Agent. Если `None`, User-Agent генерируется случайным образом.
    :type user_agent: Optional[dict]
    :ivar driver_name: Имя драйвера, по умолчанию 'edge'.
    :vartype driver_name: str
    """
    driver_name: str = 'edge'

    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """
        Инициализирует драйвер Edge с заданным User-Agent и опциями.

        :param user_agent: Словарь для настройки User-Agent. Если `None`, генерируется случайный User-Agent.
        :type user_agent: Optional[dict]
        :raises WebDriverException: Если не удается запустить WebDriver.
        :raises Exception: Если происходит общая ошибка при запуске WebDriver.
        """
        #  код инициализирует User-Agent, используя переданный параметр или генерируя случайный
        self.user_agent = user_agent if user_agent else UserAgent().random
        #  код загружает настройки драйвера из JSON файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'edge' / 'edge.json'))

        options = EdgeOptions()
        #  код добавляет User-Agent в опции запуска браузера
        options.add_argument(f'user-agent={self.user_agent}')

        try:
            logger.info('Запуск Edge WebDriver')
            #  код извлекает путь к исполняемому файлу драйвера из настроек
            edgedriver_path = settings.get('executable_path', {}).get('default')
            if not edgedriver_path:
                logger.error('Не найден путь к исполняемому файлу Edge WebDriver в конфигурации.')
                return
            #  код создает сервис драйвера, используя путь к исполняемому файлу
            service = EdgeService(executable_path=str(edgedriver_path))
            #  код инициализирует WebDriver с заданными опциями и сервисом
            super().__init__(options=options, service=service)
            self._payload()
        except WebDriverException as ex:
            logger.critical('Не удалось запустить Edge WebDriver:', exc_info=ex)
            return
        except Exception as ex:
            logger.critical('Edge WebDriver завершился с ошибкой:', exc_info=ex)
            return

    def _payload(self) -> None:
        """
        Загружает исполнители для локаторов и JavaScript-сценариев.

        Этот метод инициализирует и присваивает методы для взаимодействия с элементами
        страницы и выполнения JavaScript.
        """
        #  точка расширения функционала
        ...
        #  код создает экземпляр класса JavaScript для выполнения JS-кода
        js_executor = JavaScript(self)
        #  код устанавливает методы для получения языка страницы, готовности, реферера, скрытия элементов и фокуса окна
        self.get_page_lang = js_executor.get_page_lang
        self.ready_state = js_executor.ready_state
        self.get_referrer = js_executor.ready_state
        self.unhide_DOM_element = js_executor.unhide_DOM_element
        self.window_focus = js_executor.window_focus

        #  код создает экземпляр класса ExecuteLocator для выполнения поиска элементов
        execute_locator = ExecuteLocator(self)
        #  код устанавливает методы для выполнения поиска элементов, получения скриншотов, атрибутов и отправки сообщений
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message


    def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
        """
        Создает и настраивает параметры запуска для Edge WebDriver.

        :param opts: Список опций для добавления в Edge WebDriver. По умолчанию `None`.
        :type opts: Optional[List[str]]
        :return: Конфигурированный объект `EdgeOptions`.
        :rtype: EdgeOptions
        """
        #  код создает экземпляр класса EdgeOptions для настройки параметров браузера
        options = EdgeOptions()
        #  код добавляет переданные опции, если они есть
        if opts:
            for opt in opts:
                options.add_argument(opt)
        #  код возвращает объект EdgeOptions с добавленными опциями
        return options