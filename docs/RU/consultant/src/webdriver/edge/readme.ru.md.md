# Анализ кода модуля src.webdriver.edge

**Качество кода: 8**

*   **Плюсы:**
    *   Хорошая структурированность и подробное описание модуля в формате reStructuredText (RST).
    *   Четко описаны ключевые особенности, требования, конфигурация и примеры использования.
    *   Используется формат JSON для конфигурационного файла, что облегчает настройку.
    *   Присутствует описание паттерна Singleton.
    *   Есть раздел о логировании и отладке.

*   **Минусы:**
    *   Не хватает примеров кода с использованием docstring для функций и методов.
    *   Необходимо добавить обработку ошибок с использованием `logger.error` в коде самого модуля.
    *   Необходимо добавить импорт необходимых библиотек.
    *   Необходимо реализовать чтение конфигурационного файла через `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  **Добавить docstring:** Необходимо добавить docstring в формате RST для всех функций и методов в коде модуля.
2.  **Использовать `j_loads` или `j_loads_ns`:** Для чтения конфигурационного файла `edge.json` следует использовать функции `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Использовать `logger.error`:** Необходимо использовать `logger.error` для логирования ошибок вместо стандартных блоков `try-except`, где это возможно.
4.  **Добавить импорты:** Добавить необходимые импорты в начале файла, такие как `os`, `json`, `webdriver`, `EdgeOptions` и `Service`.
5.  **Реализация Singleton:** Убедиться, что Singleton реализован корректно в коде, а не только описан в документации.
6.  **Улучшить описание параметров:** В описании полей конфигурации добавить более конкретные примеры и контекст использования каждого параметра.

**Оптимизированный код**

```python
"""
Модуль для управления Edge WebDriver с конфигурацией из JSON.
=========================================================================================

Этот модуль обеспечивает кастомную реализацию Edge WebDriver с использованием Selenium.
Он загружает конфигурацию из `edge.json` и интегрирует настройки, такие как user-agent
и параметры профиля браузера, для обеспечения гибкого и автоматизированного взаимодействия
с браузером Edge.

Пример использования
--------------------

Пример использования класса `Edge`:

.. code-block:: python

    from src.webdriver.edge import Edge

    # Инициализация Edge WebDriver с пользовательскими опциями и user-agent
    browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

    # Открытие веб-сайта
    browser.get("https://www.example.com")

    # Закрытие браузера
    browser.quit()
"""
import os
import json
from typing import List, Optional, Any
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

_instance = None


class Edge:
    """
    Класс для управления Edge WebDriver.

    Предоставляет Singleton реализацию Edge WebDriver с возможностью настройки через
    файл конфигурации `edge.json` и дополнительные параметры.
    """
    def __new__(cls, user_agent: Optional[str] = None, options: Optional[List[str]] = None, **kwargs):
        """
        Создает или возвращает существующий экземпляр Edge WebDriver.

        :param user_agent: Пользовательский user-agent для браузера.
        :param options: Список дополнительных опций для Edge WebDriver.
        :param kwargs: Дополнительные параметры.
        :return: Экземпляр класса Edge.
        """
        global _instance
        if not _instance:
            _instance = super(Edge, cls).__new__(cls)
            _instance.__init__(user_agent=user_agent, options=options, **kwargs)
        else:
            logger.debug('Используется существующий экземпляр Edge WebDriver')
            if _instance.driver:
                _instance.open_new_window()
        return _instance

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, **kwargs):
        """
        Инициализирует Edge WebDriver.

        Загружает конфигурацию из `edge.json`, настраивает опции и запускает WebDriver.

        :param user_agent: Пользовательский user-agent для браузера.
        :param options: Список дополнительных опций для Edge WebDriver.
        :param kwargs: Дополнительные параметры.
        """
        self.driver = None
        self.config = self._load_config()
        self.user_agent = user_agent or self.config.get('headers', {}).get('User-Agent')
        self.options = options or self.config.get('options', [])
        self.kwargs = kwargs
        self._init_driver()

    def _load_config(self) -> dict:
        """
        Загружает конфигурацию из файла `edge.json`.

        :return: Словарь с конфигурацией Edge WebDriver.
        """
        try:
            config_path = os.path.join(os.path.dirname(__file__), 'edge.json')
            # код исполняет чтение файла конфигурации
            config = j_loads(config_path)
            return config
        except Exception as ex:
            logger.error(f'Ошибка при загрузке файла конфигурации edge.json: {ex}')
            return {}

    def _init_driver(self):
        """
        Инициализирует и настраивает Edge WebDriver.

        Настраивает параметры браузера, такие как user-agent и профиль,
        и запускает WebDriver.
        """
        try:
            edge_options = EdgeOptions()

            if self.user_agent:
                edge_options.add_argument(f'user-agent={self.user_agent}')

            for option in self.options:
                edge_options.add_argument(option)

            if 'profiles' in self.config and 'internal' in self.config['profiles']:
                 profile_path = os.path.join(os.path.dirname(__file__), self.config['profiles']['internal'])
                 edge_options.add_argument(f'--user-data-dir={profile_path}')

            if 'executable_path' in self.config and 'default' in self.config['executable_path']:
                executable_path = self.config['executable_path']['default']
                service = Service(executable_path=executable_path)
            else:
                service = Service()

            self.driver = webdriver.Edge(service=service, options=edge_options, **self.kwargs)
            logger.info('Edge WebDriver успешно инициализирован')

        except Exception as ex:
            logger.error(f'Ошибка при инициализации Edge WebDriver: {ex}')

    def get(self, url: str):
        """
        Открывает URL в браузере.

        :param url: URL для открытия.
        """
        if not self.driver:
            logger.error('WebDriver не инициализирован')
            return
        self.driver.get(url)

    def quit(self):
        """
        Закрывает браузер и завершает сессию WebDriver.
        """
        if self.driver:
            self.driver.quit()
            self.driver = None
            global _instance
            _instance = None
            logger.info('Edge WebDriver закрыт')

    def open_new_window(self):
        """
        Открывает новое окно в браузере.
        """
        if self.driver:
            self.driver.execute_script("window.open();")
            logger.debug('Открыто новое окно Edge WebDriver')
```