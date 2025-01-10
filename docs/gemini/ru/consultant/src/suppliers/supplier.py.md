## Анализ кода модуля `supplier`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, используются классы и функции для разделения логики.
    - Применяется `pydantic` для валидации данных и определения структуры модели.
    - Используется `j_loads_ns` для загрузки JSON-конфигураций.
    - Присутствует базовая обработка ошибок с использованием `logger.error`.
    - Есть документация к классу и функциям.
    - Использование `from src.logger.logger import logger`
- Минусы
    - Некоторые комментарии не соответствуют формату RST.
    - Отсутствует подробная документация для некоторых переменных и методов.
    - Не везде используется `logger.error` для обработки ошибок, есть `try-except` блоки.
    - Есть импорт `header` без использования, можно удалить.

**Рекомендации по улучшению**

1.  Дополнить документацию в формате RST для всех классов, методов и переменных, включая описание атрибутов класса.
2.  Удалить неиспользуемый импорт `header`.
3.  Заменить блоки `try-except` в методе `_payload` на более конкретную обработку ошибок с помощью `logger.error`.
4.  Добавить более подробные комментарии для сложных блоков кода, объясняющие их назначение.
5.  Использовать `isinstance(scenario_files, str)` для проверки типа `scenario_files`, вместо `scenario_files if scenario_files else self.scenario_files` в `run_scenario_files`.
6.  Пересмотреть использование `object.__setattr__` и по возможности заменить на более явные присваивания.
7.  Добавить проверку типа для `scenarios` в `run_scenarios`, и выводить ошибку если тип неверный.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиками
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления и выполнения сценариев для различных поставщиков.
Он отвечает за загрузку конфигураций поставщиков, выполнение входа в систему и запуск сценариев.

Пример использования
--------------------

Пример создания и использования класса `Supplier`:

.. code-block:: python

    from src.suppliers.supplier import Supplier
    
    supplier = Supplier(supplier_prefix='example_supplier')
    if supplier.login():
        supplier.run_scenario_files()
    

"""
import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace
from pathlib import Path

from pydantic import BaseModel, Field, validator
# удален неиспользуемый импорт
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """
    Базовый класс для поставщиков.

    Args:
        supplier_id (Optional[int]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика.
        locale (str): Код локали в формате ISO 639-1.
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
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
        Проверка префикса поставщика на пустое значение.
        
        Args:
            value (str): Префикс поставщика.

        Returns:
            str: Префикс поставщика.

        Raises:
             ValueError: если `value` пустая строка.
        """
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

    def __init__(self, **data):
        """
        Инициализация поставщика, загрузка конфигурации.
        
        Args:
           **data:  Произвольные ключевые аргументы для инициализации.
        
        Raises:
            DefaultSettingsException: если загрузка настроек не удалась.
        """
        super().__init__(**data)
        if not self._payload():
            # если загрузка настроек не удалась, вызывается исключение
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загрузка параметров поставщика из JSON файла с использованием `j_loads_ns`.

        Returns:
            bool: `True`, если загрузка успешна, иначе `False`.
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
        
        #  блок кода исполняет импорт модуля, связанного с поставщиком
        try:
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            #  устанавливает атрибут related_modules
            setattr(self, 'related_modules', related_module)
        except ModuleNotFoundError as ex:
             # логирование ошибки, если модуль не найден
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False
        
        # формируется путь к файлу настроек поставщика
        settings_path: Path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'
        
        # блок кода исполняет загрузку настроек
        try:
            settings: SimpleNamespace = j_loads_ns(settings_path)
            if not settings:
                 # если настройки не найдены, логируется ошибка
                logger.error(f'Настройки не найдены для поставщика: {self.supplier_prefix}')
                return False

            #  установка атрибутов класса
            self.price_rule = getattr(settings, 'price_rule', 'default_rule')
            self.locale = getattr(settings, 'locale', 'en')
            self.scenario_files = getattr(settings, 'scenario_files', [])
            self.locators = getattr(settings, 'locators', {})

            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True
        
        except Exception as ex:
            # логирование ошибки при загрузке настроек
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Returns:
            bool: `True`, если вход выполнен успешно, иначе `False`.
        """
        # код исполняет вызов функции login из связанного модуля поставщика
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполнение одного или нескольких файлов сценариев.

        Args:
            scenario_files (Optional[str | List[str]]): Список файлов сценариев.
                Если не указан, берется из `self.scenario_files`.

        Returns:
            bool: `True`, если все сценарии успешно выполнены, иначе `False`.
        """
        #  проверка типа scenario_files
        if isinstance(scenario_files, str):
            scenario_files = [scenario_files]
        # если scenario_files None, используем  self.scenario_files
        scenario_files = scenario_files or self.scenario_files

        # код исполняет запуск сценариев из файлов
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
         Выполнение списка или одного сценария.
        
        Args:
            scenarios (dict | List[dict]): Сценарий или список сценариев для выполнения.

        Returns:
            bool: `True`, если сценарий успешно выполнен, иначе `False`.
        
        Raises:
            TypeError: если тип `scenarios` не `dict` или `list`.
        """
        # проверка типа `scenarios`
        if not isinstance(scenarios, (dict, list)):
            logger.error(f'Неверный тип для scenarios: {type(scenarios)}, ожидается dict или list')
            return False
        # код исполняет запуск сценариев
        return run_scenarios(self, scenarios)