# Анализ кода модуля `supplier`

**Качество кода**
9
-  Плюсы
    -   Код хорошо структурирован и документирован.
    -   Используются статические типы, что повышает читаемость и надежность кода.
    -   Применяется `pydantic` для валидации данных.
    -   Код использует динамическую загрузку модулей.
    -   Используется логирование.
-  Минусы
    -  Не всегда используется `logger.error` для обработки ошибок.
    -  Избыточное использование try-except блоков.
    -  Файл `header` не определен.

**Рекомендации по улучшению**

1. **Обработка ошибок:**
   -  Заменить общие `except Exception as ex:` на более специфические исключения и использовать `logger.error` для логирования.
   -  Избегать избыточных блоков `try-except`.
2. **Импорты:**
   -  Добавить импорт `Path` из `pathlib`.
   -   Удалить неиспользуемый импорт `header`.
3. **Документация:**
    -  Добавить документацию в формате RST для функций, методов и класса `Supplier`, включая описания аргументов и возвращаемых значений.
    -  Добавить примеры использования в документацию.
4. **Валидация**:
   -  Рассмотреть добавление валидации для других полей модели, если это необходимо.
5.  **Логирование**:
    - Использовать f-strings для форматирования строк в `logger.debug`.
6.  **Именование переменных**:
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизиробанный код**

```python
"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления поставщиками,
загрузки их конфигураций, выполнения сценариев и входа на сайты поставщиков.

Пример использования
--------------------

Пример использования класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix='test_supplier')
    supplier.login()
    supplier.run_scenario_files()
"""
import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace
from pydantic import BaseModel, Field, validator
from pathlib import Path
# from header import header #  Удалить неиспользуемый импорт
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """
    Базовый класс для представления поставщиков.

    Управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

    Args:
        supplier_id (Optional[str]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика.
        locale (str): Код локали поставщика.
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Модуль, содержащий специфические функции для поставщика.
        scenario_files (Optional[List[str]]): Список файлов сценариев для поставщика.
        current_scenario (Optional[Dict[str, Any]]): Текущий исполняемый сценарий.
        locators (Optional[Dict[str, str]]): Локаторы для элементов страницы.
        driver (Optional[Driver]): Экземпляр веб-драйвера.

    Example:
        >>> supplier = Supplier(supplier_prefix="test_supplier")
        >>> supplier.login()
        >>> supplier.run_scenario_files()
    """
    supplier_id: Optional[str] = None
    supplier_prefix: str
    locale: str = 'en'
    price_rule: Optional[str] = None
    related_modules: Optional[ModuleType] = None
    scenario_files: Optional[List[str]] = None
    current_scenario: Optional[Dict[str, Any]] = None
    locators: Optional[Dict[str, str]] = None
    driver: Optional[Driver] = None

    class Config:
        """
        Настройки модели.

        `arbitrary_types_allowed = True` разрешает использовать произвольные типы данных.
        """
        arbitrary_types_allowed = True

    def __init__(self, **data):
        """
        Инициализирует объект поставщика.

        Args:
            **data: Произвольные данные для инициализации поставщика.
        """
        super().__init__(**data)
        #  Код инициализирует объект поставщика, загружает настройки через метод `_payload()`
        if not self._payload():
            #  Код выбрасывает исключение `DefaultSettingsException`, если загрузка настроек не удалась
            raise DefaultSettingsException(f'Ошибка загрузки настроек для поставщика {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает настройки поставщика из JSON-файла.

        Returns:
             bool: True в случае успеха, False в случае ошибки.
        """
        #  Код логирует начало загрузки настроек
        logger.debug(f'Загрузка настроек для поставщика {self.supplier_prefix}')
        try:
            #  Код формирует имя модуля поставщика
            module_name = f'src.suppliers.{self.supplier_prefix}'
            #  Код пытается динамически импортировать модуль поставщика
            try:
                related_module = importlib.import_module(module_name)
                self.related_modules = related_module
            except ModuleNotFoundError:
                # Код логирует ошибку, если модуль не найден
                logger.error(f'Модуль {module_name} не найден')
                return False
            #  Код формирует путь к файлу настроек поставщика
            settings_path = Path(gs.path.src) / 'suppliers' / f'{self.supplier_prefix}_settings.json'
            #  Код загружает настройки поставщика из JSON файла
            settings = j_loads_ns(settings_path)
            if not settings:
                # Код логирует ошибку, если файл настроек не найден или пуст
                logger.error(f'Файл настроек {settings_path} не найден или пуст')
                return False
            #  Код устанавливает значения атрибутов объекта Supplier из настроек
            self.price_rule = getattr(settings, 'price_rule', None) or self.price_rule
            self.locale = getattr(settings, 'locale', None) or self.locale
            self.scenario_files = getattr(settings, 'scenario_files', None) or self.scenario_files
            self.locators = getattr(settings, 'locators', None) or self.locators
            #  Код логирует успешную загрузку настроек
            logger.debug(f'Настройки для {self.supplier_prefix} успешно загружены')
            return True
        except Exception as ex:
             #  Код логирует ошибку, если происходит исключение
            logger.error(f'Ошибка при загрузке настроек {settings_path}', exc_info=ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        #  Код вызывает метод `login` из модуля поставщика
        try:
             # Проверка наличия модуля поставщика
            if not self.related_modules or not hasattr(self.related_modules, 'login'):
                logger.error(f'Модуль или метод login не найден для поставщика {self.supplier_prefix}')
                return False
            # Вызов функции login из модуля
            return self.related_modules.login(self)
        except Exception as ex:
            # Код логирует ошибку, если происходит исключение
            logger.error(f'Ошибка при выполнении login для поставщика {self.supplier_prefix}', exc_info=ex)
            return False

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет сценарии, указанные в файлах.

        Args:
            scenario_files (Optional[str | List[str]]): Список файлов сценариев или путь к одному файлу. Если не указан, использует self.scenario_files.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        #  Код выполняет сценарии, указанные в файлах
        if not scenario_files:
            scenario_files = self.scenario_files
        # Код вызывает функцию run_scenario_files из модуля src.scenario
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет сценарии, переданные как словарь или список словарей.

        Args:
            scenarios (dict | List[dict]): Сценарий или список сценариев для выполнения.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        #  Код выполняет сценарии, переданные как словарь или список словарей
        # Код вызывает функцию run_scenarios из модуля src.scenario
        return run_scenarios(self, scenarios)

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value: str) -> str:
        """
        Валидатор для проверки, что `supplier_prefix` не пустая строка.

        Args:
            value (str): Значение `supplier_prefix`.

        Returns:
            str: Значение `supplier_prefix`, если оно не пустое.

        Raises:
            ValueError: Если `supplier_prefix` является пустой строкой.
        """
        # Код проверяет, что `supplier_prefix` не пустая строка
        if not value:
            raise ValueError('supplier_prefix не может быть пустой строкой')
        return value
```