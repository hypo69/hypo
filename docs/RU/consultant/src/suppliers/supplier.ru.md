# Анализ кода модуля `supplier.py`

**Качество кода**
9
 -  Плюсы
    -   Код хорошо структурирован, используются классы и функции для разделения логики.
    -   Применяется статическая типизация, что улучшает читаемость и предотвращает ошибки.
    -   Используются `pydantic` для валидации данных.
    -   Присутствует базовая обработка исключений.
    -   Динамическая загрузка модулей позволяет легко добавлять новых поставщиков.
    -   Логирование событий и ошибок помогает отслеживать работу кода.
 -  Минусы
    -   Обработка исключений может быть более детальной, с логированием типа ошибки.
    -   Не хватает документации в формате RST для класса, методов и переменных.
    -   Не все переменные имеют описания.
    -  Импорт `header` не определен и не используется в коде, его нужно удалить.
    -  `settings_path` и `settings` используются только в методе `_payload` и могут быть объявлены как локальные переменные этого метода.

**Рекомендации по улучшению**

1.  **Добавить документацию RST:**
    -   Добавить документацию для модуля, класса, методов и переменных, используя формат RST.
2.  **Улучшить обработку ошибок:**
    -   Логировать конкретный тип исключения, а не просто общее сообщение.
    -   Избегать `try-except Exception` блоков, если можно обработать конкретное исключение.
3.  **Удалить неиспользуемые импорты:**
    -   Удалить импорт `header`.
4.  **Уточнить переменные:**
    -   Добавить описания для переменных `settings_path`, `settings`, `ex`.
5.  **Улучшить валидацию:**
    -   Можно добавить дополнительные валидаторы для других полей, если необходимо.
6.  **Использовать f-строки для логирования:**
    -   Использовать f-строки вместо конкатенации строк.

**Оптимизированный код**

```python
"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который используется для управления
загрузкой конфигурации поставщика, выполнением сценариев и входом на сайты поставщиков.

Пример использования
--------------------

Пример создания экземпляра класса `Supplier`:

.. code-block:: python

    supplier = Supplier(supplier_prefix='test_supplier')
    supplier.login()
    supplier.run_scenario_files()
"""
import importlib
from typing import List, Optional, Dict, Any
from types import ModuleType, SimpleNamespace
from pydantic import BaseModel, Field, validator
# from header import * # Удален неиспользуемый импорт
from src import gs
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.scenario import run_scenarios, run_scenario_files
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException


class Supplier(BaseModel):
    """
    Базовый класс для представления поставщиков.

    Этот класс управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

    Args:
        supplier_id (Optional[str]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика (обязательное поле).
        locale (str): Код локали поставщика (по умолчанию 'en').
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Модуль, содержащий специфические функции для поставщика.
        scenario_files (List[str]): Список файлов сценариев для поставщика.
        current_scenario (Optional[Dict]): Текущий исполняемый сценарий.
        locators (Optional[Dict]): Локаторы для элементов страницы.
        driver (Optional[Driver]): Экземпляр веб-драйвера.

    Attributes:
        supplier_id (Optional[str]): Идентификатор поставщика.
        supplier_prefix (str): Префикс поставщика.
        locale (str): Код локали поставщика.
        price_rule (Optional[str]): Правило расчета цен.
        related_modules (Optional[ModuleType]): Модуль, содержащий специфические функции для поставщика.
        scenario_files (List[str]): Список файлов сценариев для поставщика.
        current_scenario (Optional[Dict]): Текущий исполняемый сценарий.
        locators (Optional[Dict]): Локаторы для элементов страницы.
        driver (Optional[Driver]): Экземпляр веб-драйвера.


    Example:
        >>> supplier = Supplier(supplier_prefix='test_supplier')
        >>> print(supplier.supplier_prefix)
        test_supplier
    """
    supplier_id: Optional[str] = None
    supplier_prefix: str
    locale: str = 'en'
    price_rule: Optional[str] = None
    related_modules: Optional[ModuleType] = None
    scenario_files: List[str] = []
    current_scenario: Optional[Dict] = None
    locators: Optional[Dict] = None
    driver: Optional[Driver] = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        """
        Инициализирует объект поставщика.

        Args:
            **data: Произвольные данные для инициализации.

        Raises:
            DefaultSettingsException: Если не удалось загрузить настройки поставщика.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Не удалось загрузить настройки для {self.supplier_prefix}')

    def _payload(self) -> bool:
        """
        Загружает настройки поставщика из JSON-файла.

        Загружает конфигурационные данные поставщика (правила цен, локаль, файлы сценариев, локаторы)
        и сохраняет их в атрибуты объекта поставщика.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        logger.info(f'Загрузка настроек для {self.supplier_prefix}')
        try:
            #  Код динамически импортирует модуль поставщика
            related_module_name = f'src.suppliers.{self.supplier_prefix}'
            try:
                related_module = importlib.import_module(related_module_name)
                self.related_modules = related_module
            except ModuleNotFoundError as ex:
                logger.error(f'Не найден модуль {related_module_name}', exc_info=ex)
                return False
            #  Формирование пути к файлу настроек
            settings_path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'
            #  Загрузка настроек из JSON файла
            settings = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Не удалось загрузить настройки из файла {settings_path}')
                return False

            self.price_rule = getattr(settings, 'price_rule', self.price_rule)
            self.locale = getattr(settings, 'locale', self.locale)
            self.scenario_files = getattr(settings, 'scenario_files', self.scenario_files)
            self.locators = getattr(settings, 'locators', self.locators)

            logger.info(f'Настройки для {self.supplier_prefix} успешно загружены')
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки настроек для {self.supplier_prefix}', exc_info=ex)
            return False

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        Вызывает метод `login` из динамически загруженного модуля поставщика.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        #  Код выполняет вход на сайт поставщика, вызывая метод login из модуля поставщика
        if self.related_modules and hasattr(self.related_modules, 'login'):
            return self.related_modules.login(self)
        logger.error(f'Модуль {self.supplier_prefix} не имеет метода login')
        return False

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет один или несколько файлов сценариев.

        Args:
            scenario_files (Optional[str | List[str]]): Список файлов сценариев или путь к одному файлу.
                Если не указан, использует `self.scenario_files`.

        Returns:
            bool: True в случае успеха, False в случае ошибки.
        """
        #  Код вызывает функцию run_scenario_files из модуля src.scenario
        scenario_files = scenario_files or self.scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет один или несколько сценариев.

        Args:
             scenarios (dict | List[dict]): Словарь или список словарей, представляющих сценарии.

        Returns:
             bool: True в случае успеха, False в случае ошибки.
        """
        #  Код вызывает функцию run_scenarios из модуля src.scenario
        return run_scenarios(self, scenarios)

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value):
        """
        Проверяет, что `supplier_prefix` не пустая строка.

        Args:
            value (str): Значение `supplier_prefix`.

        Returns:
            str: Значение `supplier_prefix`, если проверка прошла успешно.

        Raises:
            ValueError: Если `supplier_prefix` является пустой строкой.
        """
        #  Код проверяет, что supplier_prefix не пустая строка
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value
```