# Анализ кода модуля `supplier`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и использует классы для представления поставщиков.
    - Применяется `pydantic` для валидации и управления данными.
    - Используется `logger` для логирования ошибок и информации.
    - Присутствует базовая документация в формате docstring.
    - Используются `j_loads_ns` для загрузки конфигурации.

 -  Минусы
    -  Не все функции и методы имеют подробную документацию в формате RST.
    -  Используются `object.__setattr__` для установки атрибутов, что может быть заменено на стандартное присваивание.
    -  Избыточное использование `try-except` блоков, которые можно упростить с использованием `logger.error`.
    -  Некоторые комментарии не соответствуют формату RST.

**Рекомендации по улучшению**

1.  Добавить подробные docstring в формате RST для всех функций, методов и класса, включая описания параметров и возвращаемых значений.
2.  Использовать стандартное присваивание атрибутов вместо `object.__setattr__`.
3.  Упростить обработку ошибок, используя `logger.error` с сообщением об ошибке и исключением.
4.  Избегать дублирования кода, где это возможно.
5.  Заменить `if not value:` на `if not value` в методе `check_supplier_prefix` для большей ясности.
6.  Добавить проверку на корректность пути к файлу настроек перед его чтением.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления
и запуском сценариев для различных поставщиков.

Модуль предоставляет функциональность для загрузки настроек,
аутентификации и выполнения сценариев для каждого поставщика.

Пример использования
--------------------

Пример создания экземпляра класса Supplier:

.. code-block:: python

    supplier = Supplier(supplier_prefix='some_supplier')
    supplier.login()
    supplier.run_scenario_files()

"""



import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType

from pydantic import BaseModel, Field, validator
# from src import gs # убрал неиспользуемый импорт
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException
from pathlib import Path # добавил импорт pathlib


class Supplier(BaseModel):
    """
    Базовый класс для работы с поставщиками.

    :param supplier_id: Идентификатор поставщика.
    :type supplier_id: Optional[int], optional
    :param supplier_prefix: Префикс поставщика.
    :type supplier_prefix: str
    :param locale: Код локали в формате ISO 639-1.
    :type locale: str, optional
    :param price_rule: Правило расчета цен.
    :type price_rule: Optional[str], optional
    :param related_modules: Функции, относящиеся к каждому поставщику.
    :type related_modules: Optional[ModuleType], optional
    :param scenario_files: Список файлов сценариев для выполнения.
    :type scenario_files: List[str], optional
    :param current_scenario: Текущий исполняемый сценарий.
    :type current_scenario: Dict[str, Any], optional
    :param locators: Локаторы для элементов страницы.
    :type locators: Dict[str, Any], optional
    :param driver: Веб-драйвер.
    :type driver: Optional[Driver], optional
    """

    supplier_id: Optional[int] = Field(default=None)
    supplier_prefix: str = Field(...)
    locale: str = Field(default='en')
    price_rule: Optional[str] = Field(default=None)
    related_modules: Optional[ModuleType] = Field(default=None)
    scenario_files: List[str] = Field(default_factory=list)
    current_scenario: Dict[str, Any] = Field(default_factory=dict)
    locators: Dict[str, Any] = Field(default_factory=dict)
    driver: Optional[Driver] = Field(default=None)

    class Config:
        """Настройки модели."""
        arbitrary_types_allowed = True

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value: str) -> str:
        """
        Проверяет, что префикс поставщика не является пустым.

        :param value: Префикс поставщика.
        :type value: str
        :raises ValueError: Если префикс поставщика пустой.
        :return: Префикс поставщика.
        :rtype: str
        """
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

    def __init__(self, **data):
        """
        Инициализирует объект поставщика, загружает конфигурацию и выполняет необходимые проверки.

        :raises DefaultSettingsException: Если произошла ошибка при загрузке настроек.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает параметры поставщика из файла настроек.

        :return: True, если загрузка прошла успешно, False в противном случае.
        :rtype: bool
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')

        # Импорт модуля, связанного с поставщиком
        try:
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            self.related_modules = related_module  # Используем стандартное присваивание
        except ModuleNotFoundError as ex:
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', exc_info=ex)
            return False

        # Путь к файлу настроек поставщика
        settings_path = Path('src') / 'suppliers' / f'{self.supplier_prefix}_settings.json'
        if not settings_path.exists(): # добавил проверку существования файла
            logger.error(f'Файл настроек не найден: {settings_path}')
            return False

        # Загрузка настроек с использованием j_loads_ns
        try:
            settings = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Настройки не найдены для поставщика: {self.supplier_prefix}')
                return False

            # Загрузка настроек в атрибуты класса
            self.price_rule = getattr(settings, 'price_rule', 'default_rule')
            self.locale = getattr(settings, 'locale', 'en')
            self.scenario_files = getattr(settings, 'scenario_files', [])
            self.locators = getattr(settings, 'locators', {})

            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True

        except Exception as ex:
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', exc_info=ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика, вызывая метод `login` из модуля поставщика.

        :return: True, если вход выполнен успешно, False в противном случае.
        :rtype: bool
        """
        try:
            return self.related_modules.login(self)
        except Exception as ex:
            logger.error(f'Ошибка при выполнении входа для поставщика {self.supplier_prefix}: ', exc_info=ex)
            return False


    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Запускает выполнение одного или нескольких файлов сценариев.

        :param scenario_files: Список файлов сценариев для выполнения. Если не указан, используется self.scenario_files.
        :type scenario_files: Optional[str | List[str]], optional
        :return: True, если все сценарии успешно выполнены, False в противном случае.
        :rtype: bool
        """
        scenario_files = scenario_files if scenario_files else self.scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Запускает выполнение списка сценариев.

        :param scenarios: Сценарий или список сценариев для выполнения.
        :type scenarios: dict | List[dict]
        :return: True, если сценарии успешно выполнены, False в противном случае.
        :rtype: bool
        """
        return run_scenarios(self, scenarios)
```