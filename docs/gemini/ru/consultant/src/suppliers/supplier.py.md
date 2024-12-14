# Анализ кода модуля `supplier`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует классы для представления поставщиков.
    - Присутствует базовая документация в формате reStructuredText (RST) для модуля и классов.
    - Используется `pydantic` для валидации данных.
    - Применяется `logger` для логирования ошибок и информации.
    - Код соответствует PEP 8.

-  Минусы
    -  Не все функции и методы имеют docstring в формате reStructuredText (RST).
    -  В некоторых местах используются избыточные блоки `try-except`.
    -  В некоторых местах логирование ошибок не полное(не передаётся ex).
    - Отсутствуют комментарии для строк кода.
    - Присутствует импорт header, который не используется.
    - Не указаны типы для  параметров `scenario_files` в методе `run_scenario_files` и `scenarios` в методе `run_scenarios`

**Рекомендации по улучшению**
1.  Добавить подробные docstring в формате RST для всех функций и методов, включая параметры и возвращаемые значения.
2.  Улучшить обработку ошибок, используя `logger.error` с передачей объекта исключения для более детального логирования.
3.  Избегать избыточных блоков `try-except`, где это возможно, и применять логирование ошибок.
4.  Добавить комментарии к строкам кода для пояснения выполняемых действий.
5. Удалить неиспользуемый импорт `header`.
6.  Указать конкретные типы для параметров `scenario_files` в методе `run_scenario_files` и `scenarios` в методе `run_scenarios`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с поставщиками
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления
различными поставщиками, загрузки их настроек и выполнения сценариев.

Пример использования
--------------------

Пример использования класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix='example_supplier')
    supplier.run_scenario_files()
"""
MODE = 'dev'

import importlib
from typing import List, Optional, Dict, Any, Union
from types import ModuleType, SimpleNamespace

from pydantic import BaseModel, Field, validator

from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """
    Базовый класс для поставщиков.

    Предоставляет интерфейс для загрузки настроек поставщика,
    запуска сценариев и управления веб-драйвером.

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
        """Настройки модели."""
        arbitrary_types_allowed = True

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value: str) -> str:
        """
        Проверяет префикс поставщика.

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
        Инициализирует поставщика.

        Загружает конфигурацию поставщика и вызывает исключение `DefaultSettingsException`
        если конфигурация не загружена.

        :param data: Данные для инициализации поставщика.
        :type data: Dict[str, Any]
        :raises DefaultSettingsException: Если не удалось загрузить настройки поставщика.
        """
        super().__init__(**data)
        # Проверяет загрузку конфигурации поставщика
        if not self._payload():
            # Если загрузка не удалась вызывает исключение
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает параметры поставщика.

        Использует `j_loads_ns` для загрузки настроек из JSON-файла.
        Импортирует модуль, связанный с поставщиком.

        :return: `True`, если загрузка успешна, иначе `False`.
        :rtype: bool
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')

        # Пытается импортировать модуль, связанный с поставщиком
        try:
            # Формирует имя модуля для импорта
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            # Устанавливает модуль как атрибут экземпляра класса
            object.__setattr__(self, 'related_modules', related_module)
        except ModuleNotFoundError as ex:
            # Логирует ошибку, если модуль не найден
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False

        # Формирует путь к файлу настроек поставщика
        settings_path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'

        # Пытается загрузить настройки поставщика
        try:
            # Загружает настройки из файла с использованием j_loads_ns
            settings: SimpleNamespace = j_loads_ns(settings_path)
            # Проверяет, что настройки были загружены
            if not settings:
                # Логирует ошибку, если настройки не найдены
                logger.error(f'Настройки не найдены для поставщика: {self.supplier_prefix}')
                return False

            # Устанавливает значения атрибутов класса из загруженных настроек
            object.__setattr__(self, 'price_rule', getattr(settings, 'price_rule', 'default_rule'))
            object.__setattr__(self, 'locale', getattr(settings, 'locale', 'en'))
            object.__setattr__(self, 'scenario_files', getattr(settings, 'scenario_files', []))
            object.__setattr__(self, 'locators', getattr(settings, 'locators', {}))

            # Логирует успешную загрузку настроек
            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True

        except Exception as ex:
            # Логирует ошибку, если при загрузке произошла ошибка
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Вызывает метод `login` из модуля, связанного с поставщиком.

        :return: `True`, если вход выполнен успешно, иначе `False`.
        :rtype: bool
        """
        # Вызывает метод login из связанного модуля
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[Union[str, List[str]]] = None) -> bool:
        """
        Запускает выполнение одного или нескольких файлов сценариев.

        Если `scenario_files` не переданы, используются файлы из `self.scenario_files`.

        :param scenario_files: Список файлов сценариев.
        :type scenario_files: Optional[Union[str, List[str]]]
        :return: `True`, если все сценарии успешно выполнены, иначе `False`.
        :rtype: bool
        """
        # Определяет список файлов сценариев
        scenario_files = scenario_files if scenario_files else self.scenario_files
        # Вызывает функцию для выполнения файлов сценариев
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: Union[dict, List[dict]]) -> bool:
        """
        Запускает выполнение одного или списка сценариев.

        :param scenarios: Сценарий или список сценариев.
        :type scenarios: Union[dict, List[dict]]
        :return: `True`, если сценарий успешно выполнен, иначе `False`.
        :rtype: bool
        """
        # Вызывает функцию для выполнения сценариев
        return run_scenarios(self, scenarios)
```