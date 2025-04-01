## \file /src/suppliers/supplier.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
```rst
.. :module:: src.suppliers.supplier 
```
Модуль описывает базовый класс поставщиков `Supplier`.
======================================================
Этот модуль является ключевым компонентом системы, обеспечивающим абстракцию и унификацию взаимодействия с различными поставщиками. 
Модуль включает функциональность для загрузки связанных модулей поставщика и управления сценариями.

Класс `Supplier` предназначен для:
 - Запуска сценариев сбора данных.
 - Управления локаторами элементов страницы.
 - Взаимодействия с веб-драйвером.

[Документция к модулю](https://github.com/hypo69/hypo/blob/master/docs/ru/src/suppliers/supplier.py.md)

[Докумeнтация по локаторам](https://github.com/hypo69/hypo/blob/master/docs/ru/src/webdriver/locator.ru.md)

Далее: класс [Graber](https://github.com/hypo69/hypo/blob/master/docs/ru/src/suppliers/graber.py.md)

Flowchart:


                   supplier_prefix
                         |
web <-> webdriver <-> SUPPLIER -> product
                         ^
                         |
                      scenario
"""



import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace

from pydantic import BaseModel, Field, validator
import header
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """Класс Supplier. Выполняет сценарии для различных поставщиков.
    
    Атрибуты:
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
        """Проверка префикса поставщика на пустое значение."""
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

    def __init__(self, **data):
        """Инициализация поставщика, загрузка конфигурации."""
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """Загрузка параметров поставщика с использованием `j_loads_ns`.

        Returns:
            bool: `True`, если загрузка успешна, иначе `False`.
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
        
        # Импорт модулей, связанных с конкртетным поставщиком
        try:
            related_modules = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            object.__setattr__(self, 'related_modules', related_modules)
        except ModuleNotFoundError as ex:
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False
   


    def login(self) -> bool:
        """Выполняет вход на сайт поставщика.

        Returns:
            bool: `True`, если вход выполнен успешно, иначе `False`.
        """
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """Выполнение одного или нескольких файлов сценариев.

        Args:
            scenario_files (Optional[str | List[str]]): Список файлов сценариев. 
                Если не указан, берется из `self.scenario_files`.

        Returns:
            bool: `True`, если все сценарии успешно выполнены, иначе `False`.
        """
        scenario_files = scenario_files  if scenario_files else self.scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """Выполнение списка или одного сценария.

        Args:
            scenarios (dict | List[dict]): Сценарий или список сценариев для выполнения.

        Returns:
            bool: `True`, если сценарий успешно выполнен, иначе `False`.
        """
        return run_scenarios(self, scenarios)
