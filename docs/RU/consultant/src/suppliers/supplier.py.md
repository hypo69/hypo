# Анализ кода модуля `supplier`

## Качество кода
**Соответствие требованиям по оформлению кода: 9/10**
- **Плюсы**
    - Код хорошо структурирован и использует `pydantic` для валидации данных.
    -  Используется `logger` для логирования.
    -  Присутствуют docstring для классов и методов.
    -  Используется `j_loads_ns` для загрузки данных из JSON.
    -  Конфигурация класса `Config` использует `arbitrary_types_allowed = True`.
- **Минусы**
    -  В коде используется `object.__setattr__` для установки атрибутов, что не рекомендуется.
    -  В функции `_payload`  обработка ошибок в блоке `try-except` не соответствует шаблону, где нужно использовать `logger.error` вместо `print`.
    - Не хватает подробных примеров использования в docstring.

## Рекомендации по улучшению
1. **Использование `setattr`:**
   - Вместо `object.__setattr__(self, 'attribute', value)` лучше использовать `setattr(self, 'attribute', value)` или прямое присваивание `self.attribute = value`.
2.  **Улучшение обработки ошибок:**
    - В методе `_payload` необходимо использовать `logger.error` для вывода ошибок и возвращать `False` при их возникновении.
3. **Документация:**
   - Добавить примеры использования класса и методов в docstring.
   - Расширить описания аргументов и возвращаемых значений в docstring.
4.  **Форматирование:**
    - Привести все строки к единому стилю с использованием одинарных кавычек, за исключением вывода в консоль.

## Оптимизированный код
```python
# -*- coding: utf-8 -*-
# file: src/suppliers/supplier.py
"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который является базовым классом
для работы с различными поставщиками. Он управляет загрузкой конфигурации,
аутентификацией и запуском сценариев.

Пример использования
--------------------

Пример использования класса `Supplier`:

.. code-block:: python

    from src.suppliers.supplier import Supplier
    from src.webdriver.driver import Driver
    
    # Пример инициализации поставщика
    supplier = Supplier(
        supplier_prefix='example_supplier', 
        driver=Driver()
    )

    # Запуск сценариев
    supplier.run_scenario_files()
"""

import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace

from pydantic import BaseModel, Field, validator
# from src import header #TODO: delete unused import
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """
    Базовый класс для поставщиков.

    Управляет настройками, аутентификацией и выполнением сценариев для конкретного поставщика.

    Args:
        supplier_id (Optional[int]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика, используется для загрузки настроек и модулей.
        locale (str): Код локали в формате ISO 639-1, по умолчанию `en`.
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Модуль, содержащий специфичные функции поставщика.
        scenario_files (List[str]): Список файлов сценариев для выполнения.
        current_scenario (Dict[str, Any]): Текущий исполняемый сценарий.
        locators (Dict[str, Any]): Локаторы для элементов страницы.
        driver (Optional[Driver]): Веб-драйвер.

    Attributes:
        supplier_id (Optional[int]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика.
        locale (str): Код локали в формате ISO 639-1.
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
        scenario_files (List[str]): Список файлов сценариев для выполнения.
        current_scenario (Dict[str, Any]): Текущий исполняемый сценарий.
        locators (Dict[str, Any]): Локаторы для элементов страницы.
        driver (Optional[Driver]): Веб-драйвер.
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
        Проверяет префикс поставщика на непустое значение.

        Args:
            value (str): Префикс поставщика.

        Returns:
            str: Префикс поставщика, если он не пустой.

        Raises:
            ValueError: Если префикс поставщика пустой.
        """
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

    def __init__(self, **data):
        """
        Инициализация поставщика, загрузка конфигурации.

        Args:
             **data:  Параметры для инициализации поставщика.
        Raises:
            DefaultSettingsException: Если загрузка настроек не удалась.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает параметры поставщика из JSON-файла и настраивает атрибуты.

        Returns:
            bool: `True`, если загрузка прошла успешно, иначе `False`.
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
        
        # Импорт модуля, связанного с поставщиком
        try:
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            setattr(self, 'related_modules', related_module) #  установка атрибута related_modules
        except ModuleNotFoundError as ex:
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False
        
        # Путь к файлу настроек поставщика
        settings_path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'
        
        # Загрузка настроек с использованием j_loads_ns
        try:
            settings: SimpleNamespace = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Настройки не найдены для поставщика: {self.supplier_prefix}')
                return False

            # Загрузка настроек в атрибуты класса
            setattr(self, 'price_rule', getattr(settings, 'price_rule', 'default_rule')) # установка атрибута price_rule
            setattr(self, 'locale', getattr(settings, 'locale', 'en')) # установка атрибута locale
            setattr(self, 'scenario_files', getattr(settings, 'scenario_files', [])) # установка атрибута scenario_files
            setattr(self, 'locators', getattr(settings, 'locators', {})) # установка атрибута locators

            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True
        
        except Exception as ex:
             # Вывод ошибки в лог
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Returns:
             bool: `True`, если вход выполнен успешно, иначе `False`.
        """
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Запускает один или несколько файлов сценариев.

        Args:
            scenario_files (Optional[str | List[str]]): Список файлов сценариев.
                Если не указан, берется из `self.scenario_files`.

        Returns:
            bool: `True`, если все сценарии успешно выполнены, иначе `False`.
        """
        scenario_files = scenario_files if scenario_files else self.scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Запускает один или несколько сценариев.

        Args:
            scenarios (dict | List[dict]): Сценарий или список сценариев для выполнения.

        Returns:
            bool: `True`, если сценарий успешно выполнен, иначе `False`.
        """
        return run_scenarios(self, scenarios)