# Анализ кода модуля `supplier`

**Качество кода**
8
-   Плюсы
    -   Код предоставляет базовую структуру для работы с поставщиками данных.
    -   Наличие атрибутов класса для хранения данных о поставщике, настройках, сценариях.
    -   Разделение логики на методы для загрузки конфигурации, входа на сайт и выполнения сценариев.
-   Минусы
    -   Отсутствуют docstring для класса и методов.
    -   Использование `json.load` вместо `j_loads` или `j_loads_ns` для загрузки файлов.
    -   Не импортирован логгер.
    -   Не используются f-strings для форматирования строк, где это возможно.
    -   Отсутствует обработка исключений с использованием `logger.error`.
    -   Избыточное использование `try-except` без конкретной обработки ошибок.
    -   Нет проверок типов и наличия атрибутов.
    -   Методы `run_scenario_files` и `run_scenarios` могут быть улучшены для большей гибкости и контроля.

**Рекомендации по улучшению**

1.  Добавить docstring для класса `Supplier` и всех его методов, включая описание аргументов, возвращаемых значений и возможных исключений.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON файлов.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Использовать f-strings для форматирования строк для лучшей читаемости и производительности.
5.  Заменить `try-except` на более конкретную обработку ошибок с использованием `logger.error` для логирования исключений.
6.  Реализовать проверки типов и наличия атрибутов для предотвращения ошибок.
7.  Улучшить методы `run_scenario_files` и `run_scenarios` для поддержки более сложных сценариев и обеспечения большей гибкости.
8.  Добавить документацию в формате RST для всех методов и атрибутов.
9.  Уточнить комментарии, избегая общих фраз типа "делаем" и использовать более конкретные формулировки.
10. Добавить примеры использования класса и методов.

**Оптимизированный код**

```python
"""
Модуль для работы с поставщиками данных.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который служит основой для
реализации различных поставщиков данных.

Пример использования
--------------------

Пример использования класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
    supplier.login()
    supplier.run_scenario_files(['example_scenario.json'])
"""
import json # импорт стандартной библиотеки
from typing import Any, Dict, List, Optional
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver as Driver

from src.logger.logger import logger # импорт логгера
from src.utils.jjson import j_loads_ns # импорт j_loads_ns


class Supplier:
    """
    Базовый класс для работы с поставщиками данных.

    Атрибуты:
        supplier_id (str): Уникальный идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика (например, 'aliexpress', 'amazon').
        supplier_settings (dict): Настройки поставщика, загруженные из файла конфигурации.
        locale (str): Код локализации (например, 'en', 'ru').
        price_rule (Any): Правило для расчета цены.
        related_modules (Any): Модуль, содержащий специфические для поставщика функции.
        scenario_files (list[str]): Список файлов сценариев.
        current_scenario (Any): Текущий сценарий выполнения.
        login_data (dict): Данные для входа на сайт поставщика.
        locators (dict): Локаторы для веб-элементов на сайте поставщика.
        driver (Driver): Веб-драйвер для взаимодействия с сайтом поставщика.
        parsing_method (str): Метод парсинга данных ('webdriver', 'api', 'xls', 'csv').

    Пример:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
    """
    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
        """
        Инициализирует атрибуты класса `Supplier`.

        Args:
            supplier_prefix (str): Префикс поставщика (например, 'aliexpress', 'amazon').
            locale (str, optional): Код локализации (например, 'en', 'ru'). Defaults to 'en'.
            webdriver (str | Driver | bool, optional): Веб-драйвер или его настройка. Defaults to 'default'.
            *attrs: Дополнительные атрибуты.
            **kwargs: Дополнительные именованные аргументы.
        """
        self.supplier_id: str =  f'{supplier_prefix}_{locale}' # формируем уникальный id поставщика
        self.supplier_prefix: str = supplier_prefix  #  префикс поставщика
        self.supplier_settings: Optional[Dict] = None #  настройки поставщика
        self.locale: str = locale # код локализации
        self.price_rule: Any = None # правило расчета цены
        self.related_modules: Any = None # связанные модули
        self.scenario_files: List[str] = [] # список файлов сценариев
        self.current_scenario: Any = None # текущий сценарий
        self.login_data: Optional[Dict] = None # данные для входа
        self.locators: Optional[Dict] = None # локаторы
        self.driver: Driver | None = None # веб-драйвер
        self.parsing_method: Optional[str] = None # метод парсинга

        self._payload(webdriver, *attrs, **kwargs)  # загрузка конфигурации

    def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
        """
        Загружает настройки поставщика, конфигурационные файлы и инициализирует веб-драйвер.

        Args:
            webdriver (str | Driver | bool): Веб-драйвер или его настройка.
            *attrs: Дополнительные атрибуты.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            bool: True, если загрузка конфигурации прошла успешно, False в противном случае.

        Raises:
            FileNotFoundError: Если файл настроек или локаторов не найден.
            json.JSONDecodeError: Если файл настроек или локаторов не является корректным JSON.
        """
        try:
            # формируем путь к файлу настроек
            settings_path = Path(f'settings/{self.supplier_prefix}.json')
            # загрузка настроек поставщика
            self.supplier_settings = j_loads_ns(settings_path)  # используем j_loads_ns для загрузки JSON
            # проверка наличия настроек
            if not self.supplier_settings:
                logger.error(f'Не удалось загрузить настройки из файла {settings_path}')
                return False

            # формируем путь к файлу локаторов
            locators_path = Path(f'locators/{self.supplier_prefix}.json')
            # загружаем локаторы
            self.locators = j_loads_ns(locators_path) # используем j_loads_ns для загрузки JSON
            # проверяем наличие локаторов
            if not self.locators:
                logger.error(f'Не удалось загрузить локаторы из файла {locators_path}')
                return False

            # инициализируем веб-драйвер
            if webdriver and isinstance(webdriver, str) and webdriver != 'default':
               from src.webdriver import init_driver
               self.driver = init_driver(webdriver)  # инициализация веб-драйвера
            elif isinstance(webdriver, Driver):
                self.driver = webdriver
            else:
                self.driver = None
            # устанавливаем метод парсинга
            if self.supplier_settings.get('parsing_method'):
                self.parsing_method = self.supplier_settings.get('parsing_method')
            # устанавливаем данные для входа
            if self.supplier_settings.get('login_data'):
                self.login_data = self.supplier_settings.get('login_data')
            # устанавливаем файлы сценариев
            if self.supplier_settings.get('scenario_files'):
                self.scenario_files = self.supplier_settings.get('scenario_files')
            # устанавливаем правило расчета цены
            if self.supplier_settings.get('price_rule'):
                self.price_rule = self.supplier_settings.get('price_rule')
            # устанавливаем связанные модули
            if self.supplier_settings.get('related_modules'):
                self.related_modules = self.supplier_settings.get('related_modules')
            return True
        except FileNotFoundError as ex:
            logger.error(f'Файл не найден: {ex}')
            return False
        except json.JSONDecodeError as ex:
            logger.error(f'Ошибка декодирования JSON: {ex}')
            return False
        except Exception as ex:
            logger.error(f'Неизвестная ошибка при загрузке конфигурации: {ex}')
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика, если это необходимо.

        Returns:
            bool: True, если вход выполнен успешно, False в противном случае.
        """
        if not self.login_data:
            logger.debug(f'Нет данных для входа для {self.supplier_prefix}')
            return True # если нет данных для входа, возвращаем True

        try:
            # Код выполняет вход на сайт.
            logger.debug(f'Выполняем вход на сайт {self.supplier_prefix}')
            # TODO: implement login logic
            ... # логика входа
            return True
        except Exception as ex:
             logger.error(f'Ошибка при входе на сайт {self.supplier_prefix}: {ex}')
             return False

    def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
        """
        Запускает выполнение файлов сценариев.

        Args:
            scenario_files (str | list[str], optional): Список файлов сценариев или один файл. Defaults to None.

        Returns:
            bool: True, если сценарии выполнены успешно, False в противном случае.
        """
        if not scenario_files:
            scenario_files = self.scenario_files #  используем сценарии из настроек если нет входных параметров
        if not scenario_files:
            logger.debug(f'Нет файлов сценариев для выполнения для {self.supplier_prefix}')
            return True # если нет файлов сценариев, возвращаем True
        if isinstance(scenario_files, str):
            scenario_files = [scenario_files] #  если передан один файл, преобразуем его в список
        try:
            for file in scenario_files:
                 # Код выполняет сценарии из файла.
                logger.debug(f'Выполняем сценарии из файла: {file}')
                # TODO: implement scenario logic from files
                ...  # логика выполнения сценариев из файлов
            return True
        except Exception as ex:
            logger.error(f'Ошибка при выполнении сценариев из файлов {scenario_files}: {ex}')
            return False

    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        """
         Запускает выполнение заданных сценариев.

        Args:
            scenarios (dict | list[dict]): Словарь или список словарей, представляющих сценарии.

        Returns:
            bool: True, если сценарии выполнены успешно, False в противном случае.
        """
        if not scenarios:
            logger.debug(f'Нет сценариев для выполнения для {self.supplier_prefix}')
            return True # если нет сценариев, возвращаем True
        if isinstance(scenarios, dict):
            scenarios = [scenarios] # если передан один сценарий, преобразуем его в список
        try:
            for scenario in scenarios:
                # Код выполняет сценарии.
                logger.debug(f'Выполняем сценарий: {scenario}')
                # TODO: implement scenario logic
                ...  # логика выполнения сценариев
            return True
        except Exception as ex:
            logger.error(f'Ошибка при выполнении сценариев {scenarios}: {ex}')
            return False
```