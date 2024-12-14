# Анализ кода модуля `supplier.py`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и разбит на классы и функции.
    -   Используется `pydantic` для валидации данных.
    -   Применяется динамический импорт модулей через `importlib`.
    -   Используется логирование для отслеживания ошибок.
    -   Код использует статическую типизацию через `typing`.
    -   Используется `SimpleNamespace` для удобного доступа к настройкам.
-   Минусы
    -   Некоторые комментарии не соответствуют стандарту reStructuredText (RST).
    -   Обработка ошибок в некоторых местах может быть улучшена.
    -   Зависимость от модуля `header` не ясна.
    -   Используются стандартные блоки `try-except` в некоторых случаях, хотя можно использовать `logger.error`.
    -   Отсутствует документация в формате RST для функций и класса.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить документацию в формате RST для всех функций, методов и класса.
    -   Использовать docstring для описания параметров, возвращаемых значений и назначения функций и методов.
2.  **Обработка ошибок**:
    -   Вместо общих `except Exception as ex:` использовать более конкретные исключения и логировать их с помощью `logger.error`.
    -   Избегать лишних блоков `try-except`, если это не требуется.
3.  **Зависимости**:
    -   Уточнить назначение модуля `header`. Если он содержит константы, их лучше вынести в отдельный файл конфигурации или использовать `src.gs`.
4.  **Валидация**:
    -   Рассмотреть возможность добавления дополнительных валидаторов для других полей модели.
5.  **Комментарии**:
    -   Переписать все комментарии в формате reStructuredText (RST).
    -   Комментарии после `#` должны содержать подробное объяснение следующего за ними блока кода.
6.  **Именование**:
    -   Привести в соответствие имена переменных, функций и импортов с ранее обработанными файлами.
7.  **Логирование**:
    -   Использовать `logger.error` для обработки ошибок вместо стандартных `try-except`, когда это возможно.

**Оптимизиробанный код**

```python
"""
Модуль для управления поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления поставщиками, 
загрузки их конфигураций, выполнения сценариев и входа на сайты.

Пример использования
--------------------

Пример создания экземпляра класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix="test_supplier")
    supplier.login()
    supplier.run_scenario_files()
"""
import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace
from pydantic import BaseModel, Field, validator
# import header # TODO: Уточнить назначение header
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


MODE = 'dev'


class Supplier(BaseModel):
    """
    Базовый класс для представления поставщиков.

    :ivar supplier_id: Идентификатор поставщика (может быть None).
    :vartype supplier_id: Optional[int]
    :ivar supplier_prefix: Префикс поставщика (обязательное поле).
    :vartype supplier_prefix: str
    :ivar locale: Код локали поставщика (по умолчанию 'en').
    :vartype locale: str
    :ivar price_rule: Правило расчета цен (может быть None).
    :vartype price_rule: Optional[str]
    :ivar related_modules: Модуль, содержащий специфические функции для поставщика (может быть None).
    :vartype related_modules: Optional[ModuleType]
    :ivar scenario_files: Список файлов сценариев для поставщика.
    :vartype scenario_files: List[str]
    :ivar current_scenario: Текущий исполняемый сценарий (словарь).
    :vartype current_scenario: Optional[dict]
    :ivar locators: Локаторы для элементов страницы.
    :vartype locators: Optional[dict]
    :ivar driver: Экземпляр веб-драйвера.
    :vartype driver: Optional[Driver]

    :raises DefaultSettingsException: Если не удалось загрузить настройки поставщика.
    """
    supplier_id: Optional[int] = None
    supplier_prefix: str
    locale: str = 'en'
    price_rule: Optional[str] = None
    related_modules: Optional[ModuleType] = None
    scenario_files: List[str] = []
    current_scenario: Optional[dict] = None
    locators: Optional[dict] = None
    driver: Optional[Driver] = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        """
        Инициализирует объект поставщика.

        Загружает настройки через метод `_payload()`.

        :param data: Данные для инициализации поставщика.
        :type data: dict
        :raises DefaultSettingsException: Если не удалось загрузить настройки.
        """
        super().__init__(**data)
        if not self._payload():
            logger.error(f"Не удалось загрузить настройки для поставщика {self.supplier_prefix}")
            raise DefaultSettingsException(f"Не удалось загрузить настройки для поставщика {self.supplier_prefix}")

    def _payload(self) -> bool:
        """
        Загружает настройки поставщика из JSON-файла.

        Использует `j_loads_ns` для загрузки данных и динамически импортирует модуль, связанный с поставщиком.

        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        logger.info(f'Загрузка настроек для поставщика {self.supplier_prefix}')
        try:
            #  Код выполняет динамический импорт модуля поставщика
            related_module_name = f'src.suppliers.{self.supplier_prefix}'
            try:
                related_module = importlib.import_module(related_module_name)
                self.related_modules = related_module
            except ModuleNotFoundError as ex:
                logger.error(f'Не найден модуль {related_module_name}', exc_info=ex)
                return False
            # Код формирует путь к файлу настроек поставщика
            settings_path = f'{gs.path.src}/suppliers/{self.supplier_prefix}_settings.json'
            # Код загружает настройки из JSON файла
            settings = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Не удалось загрузить настройки из файла {settings_path}')
                return False
            # Код устанавливает значения атрибутов объекта Supplier
            self.price_rule = getattr(settings, 'price_rule', None)
            self.locale = getattr(settings, 'locale', 'en')
            self.scenario_files = getattr(settings, 'scenario_files', [])
            self.locators = getattr(settings, 'locators', {})
            logger.info(f'Настройки для {self.supplier_prefix} успешно загружены')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке настроек поставщика {self.supplier_prefix}', exc_info=ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Вызывает метод `login` из модуля, связанного с поставщиком.

        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        # Код выполняет вызов метода login из модуля поставщика
        if self.related_modules and hasattr(self.related_modules, 'login'):
            return self.related_modules.login(self)
        logger.error(f'Метод login не найден в модуле {self.supplier_prefix}')
        return False

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет сценарии, указанные в файлах.

        :param scenario_files: Список файлов сценариев или путь к одному файлу.
            Если не указан, используется `self.scenario_files`.
        :type scenario_files: Optional[str | List[str]]
        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        # Код вызывает функцию run_scenario_files из модуля src.scenario
        files = scenario_files or self.scenario_files
        return run_scenario_files(self, files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет сценарии, переданные как словарь или список словарей.

        :param scenarios: Словарь или список словарей, представляющих сценарии.
        :type scenarios: dict | List[dict]
        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        # Код вызывает функцию run_scenarios из модуля src.scenario
        return run_scenarios(self, scenarios)

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value):
        """
        Валидатор для проверки, что `supplier_prefix` не пустая строка.

        :param value: Значение префикса поставщика.
        :type value: str
        :raises ValueError: Если префикс поставщика пустой.
        :return: Значение префикса поставщика.
        :rtype: str
        """
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value
```