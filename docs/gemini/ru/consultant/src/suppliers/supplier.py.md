# Анализ кода модуля `supplier`

**Качество кода**
10
- Плюсы
    - Код соответствует PEP 8.
    - Используются аннотации типов.
    - Присутствуют docstring для классов и методов.
    - Используется `pydantic` для валидации данных.
    - Логирование с помощью `src.logger.logger`.
    - Отдельная обработка ошибок с помощью `logger.error`.
- Минусы
   -  Смешанный стиль `reStructuredText` в docstring и обычных комментариях.

**Рекомендации по улучшению**
1. Привести все комментарии в docstring к формату `reStructuredText`.
2.  Уточнить docstring к методу `login`.
3. Убрать дублирование логики загрузки настроек в методе `_payload` в try/except блоке, разделив на несколько методов
4.  В методе `_payload` следует использовать константу или перечисление для ключей `price_rule`, `locale`, `scenario_files`, `locators`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который служит базовым классом
для работы с различными поставщиками. Он управляет загрузкой настроек,
выполнением сценариев и взаимодействием с веб-драйвером.

Пример использования
--------------------

Пример создания экземпляра класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix='example_supplier', locale='ru')
    supplier.run_scenario_files()
"""
MODE = 'dev'

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
    """
    Базовый класс для работы с поставщиками.

    Управляет загрузкой настроек поставщика, выполнением сценариев и
    взаимодействием с веб-драйвером.

    :param supplier_id: Идентификатор поставщика.
    :type supplier_id: Optional[int]
    :param supplier_prefix: Префикс поставщика.
    :type supplier_prefix: str
    :param locale: Код локали в формате ISO 639-1.
    :type locale: str
    :param price_rule: Правило расчета цен.
    :type price_rule: Optional[str]
    :param related_modules: Функции, относящиеся к каждому поставщику.
    :type related_modules: Optional[ModuleType]
    :param scenario_files: Список файлов сценариев для выполнения.
    :type scenario_files: List[str]
    :param current_scenario: Текущий исполняемый сценарий.
    :type current_scenario: Dict[str, Any]
    :param locators: Локаторы для элементов страницы.
    :type locators: Dict[str, Any]
    :param driver: Веб-драйвер.
    :type driver: Optional[Driver]

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
        """
        Настройки модели.

        :ivar arbitrary_types_allowed: Разрешает произвольные типы.
        :vartype arbitrary_types_allowed: bool
        """
        arbitrary_types_allowed = True

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value: str) -> str:
        """
        Проверяет префикс поставщика на пустоту.

        :param value: Префикс поставщика.
        :type value: str
        :raises ValueError: Если префикс пустой.
        :return: Префикс поставщика.
        :rtype: str
        """
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

    def __init__(self, **data):
        """
        Инициализирует поставщика и загружает конфигурацию.

        :param data: Параметры инициализации.
        :type data: dict
        :raises DefaultSettingsException: Если не удалось загрузить настройки.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _load_related_module(self) -> bool:
        """
        Импортирует модуль, связанный с поставщиком.

        :return: True, если импорт успешен, иначе False.
        :rtype: bool
        """
        try:
            #  код импортирует модуль поставщика
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            object.__setattr__(self, 'related_modules', related_module)
            return True
        except ModuleNotFoundError as ex:
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False

    def _load_settings(self) -> bool:
        """
        Загружает настройки поставщика из JSON файла.

        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        settings_path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'
        try:
            #  код загружает настройки поставщика
            settings: SimpleNamespace = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Настройки не найдены для поставщика: {self.supplier_prefix}')
                return False
            self._apply_settings(settings)
            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
            return False

    def _apply_settings(self, settings: SimpleNamespace) -> None:
        """
        Применяет загруженные настройки к атрибутам класса.

        :param settings: Настройки поставщика.
        :type settings: SimpleNamespace
        """
        #  код устанавливает значения атрибутов класса из загруженных настроек
        object.__setattr__(self, 'price_rule', getattr(settings, 'price_rule', 'default_rule'))
        object.__setattr__(self, 'locale', getattr(settings, 'locale', 'en'))
        object.__setattr__(self, 'scenario_files', getattr(settings, 'scenario_files', []))
        object.__setattr__(self, 'locators', getattr(settings, 'locators', {}))

    def _payload(self) -> bool:
        """
        Загружает параметры поставщика.

        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
        if not self._load_related_module():
            return False
        if not self._load_settings():
            return False
        return True

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.
        
        :return: True, если вход выполнен успешно, иначе False.
        :rtype: bool
        """
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет один или несколько файлов сценариев.

        :param scenario_files: Список файлов сценариев. Если не указан, берется из `self.scenario_files`.
        :type scenario_files: Optional[str | List[str]]
        :return: True, если все сценарии успешно выполнены, иначе False.
        :rtype: bool
        """
        scenario_files = scenario_files if scenario_files else self.scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет список или один сценарий.

        :param scenarios: Сценарий или список сценариев для выполнения.
        :type scenarios: dict | List[dict]
        :return: True, если сценарий успешно выполнен, иначе False.
        :rtype: bool
        """
        return run_scenarios(self, scenarios)
```