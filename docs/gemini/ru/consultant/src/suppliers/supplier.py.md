# Анализ кода модуля `supplier`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует классы для представления поставщиков.
    - Используется `pydantic` для валидации данных и определения структуры класса.
    - Присутствует логирование ошибок и информационных сообщений.
    - Применяется `j_loads_ns` для загрузки настроек из JSON, что соответствует требованиям.
    - Есть разделение на методы `login`, `run_scenario_files`, `run_scenarios`.
-  Минусы
    -  Некоторые docstring не полностью соответствуют стандарту reStructuredText.
    -  В коде присутствуют множественные `object.__setattr__`, что может быть улучшено.
    -  Отсутствует обработка исключения `ModuleNotFoundError` в `run_scenario_files` и `run_scenarios`

**Рекомендации по улучшению**
1. **Документация**:
   - Улучшить docstring для соответствия reStructuredText, включая описание параметров и возвращаемых значений для всех методов.
   - Добавить описание исключений, которые могут быть вызваны методами.
2. **Использование `setattr`**:
   -  Заменить `object.__setattr__` на присваивание через `self`, где это возможно, для большей читаемости.
3. **Обработка ошибок**:
   - Добавить обработку исключения `ModuleNotFoundError` в `run_scenario_files` и `run_scenarios` для более корректной работы.
4. **Улучшение структуры**:
   - Рассмотреть возможность вынесения логики загрузки настроек в отдельный метод для улучшения читаемости.
5. **Импорты**:
    - Вынести импорты сторонних библиотек в начало модуля.
6. **Комментарии**:
   - Добавить больше комментариев в коде для пояснения логики работы.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль :mod:`src.suppliers.supplier`
====================================================

.. module:: src.suppliers.supplier
   :platform: Windows, Unix
   :synopsis: Базовый класс для поставщиков.

Этот модуль содержит класс :class:`Supplier`, который является базовым классом
для работы с различными поставщиками. Он управляет загрузкой настроек поставщика,
выполнением сценариев и другими операциями, связанными с поставщиками.
"""

MODE = 'dev'

import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace

from pydantic import BaseModel, Field, validator
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException
import header
from src import gs

class Supplier(BaseModel):
    """
    Базовый класс для поставщиков.

    :ivar supplier_id: Идентификатор поставщика.
    :vartype supplier_id: Optional[int]
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    :ivar locale: Код локали в формате ISO 639-1.
    :vartype locale: str
    :ivar price_rule: Правило расчета цен.
    :vartype price_rule: Optional[str]
    :ivar related_modules: Функции, относящиеся к каждому поставщику.
    :vartype related_modules: Optional[ModuleType]
    :ivar scenario_files: Список файлов сценариев для выполнения.
    :vartype scenario_files: List[str]
    :ivar current_scenario: Текущий исполняемый сценарий.
    :vartype current_scenario: Dict[str, Any]
    :ivar locators: Локаторы для элементов страницы.
    :vartype locators: Dict[str, Any]
    :ivar driver: Веб-драйвер.
    :vartype driver: Optional[Driver]
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
        Проверяет префикс поставщика на пустое значение.

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
        Инициализирует поставщика и загружает его конфигурацию.

        :raises DefaultSettingsException: Если не удалось загрузить настройки поставщика.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает параметры поставщика.

        Использует :func:`src.utils.jjson.j_loads_ns` для загрузки настроек из JSON файла.

        :return: `True`, если загрузка прошла успешно, `False` в противном случае.
        :rtype: bool
        """
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')

        # Импорт модуля, связанного с поставщиком
        try:
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            self.related_modules = related_module #  Присваивание модуля поставщика атрибуту `related_modules`
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

            #  Установка атрибутов класса из настроек
            self.price_rule = getattr(settings, 'price_rule', 'default_rule')
            self.locale = getattr(settings, 'locale', 'en')
            self.scenario_files = getattr(settings, 'scenario_files', [])
            self.locators = getattr(settings, 'locators', {})


            logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
            return True

        except Exception as ex:
            logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        :return: `True`, если вход выполнен успешно, `False` в противном случае.
        :rtype: bool
        """
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет один или несколько файлов сценариев.

        :param scenario_files: Список файлов сценариев. Если не указан, используется `self.scenario_files`.
        :type scenario_files: Optional[str | List[str]]
        :return: `True`, если все сценарии успешно выполнены, `False` в противном случае.
        :rtype: bool
        :raises ModuleNotFoundError: если не найден модуль сценариев
        """
        scenario_files = scenario_files if scenario_files else self.scenario_files
        try:
            return run_scenario_files(self, scenario_files) # Вызов функции для выполнения файлов сценариев
        except ModuleNotFoundError as ex:
            logger.error(f'Ошибка при выполнении файлов сценариев {scenario_files}: ', ex)
            return False


    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет список или один сценарий.

        :param scenarios: Сценарий или список сценариев для выполнения.
        :type scenarios: dict | List[dict]
        :return: `True`, если сценарий успешно выполнен, `False` в противном случае.
        :rtype: bool
        :raises ModuleNotFoundError: если не найден модуль сценариев
        """
        try:
            return run_scenarios(self, scenarios) # Вызов функции для выполнения сценариев
        except ModuleNotFoundError as ex:
            logger.error(f'Ошибка при выполнении сценариев: ', ex)
            return False
```