# Анализ кода модуля `supplier`

**Качество кода**
7
- Плюсы
    - Код использует `pydantic` для валидации данных, что обеспечивает корректность работы с данными поставщиков.
    - Применяется статическая типизация, что улучшает читаемость и сопровождение кода.
    - Используется динамический импорт модулей для гибкости и расширяемости системы.
    - Код разделен на логические блоки, что улучшает его структуру и понимание.
    - Применяется `logger` для логирования событий и ошибок.
- Минусы
    - В коде присутствуют общие блоки `try-except` без конкретизации исключений, что может затруднить отладку.
    - Используется нестандартный импорт `header`, назначение которого неясно.
    -  Обработка ошибок в некоторых местах не детализирована, что может усложнить отладку.

**Рекомендации по улучшению**
1.  **Детализация обработки исключений:**
    -   Замените общие блоки `except Exception as ex:` на более конкретные исключения, такие как `FileNotFoundError`, `json.JSONDecodeError` и другие, чтобы более точно обрабатывать ошибки.
    -   Добавьте логирование с указанием конкретного типа исключения и места его возникновения.

2.  **Удаление/Замена `header`:**
    -   Уточните назначение модуля `header`. Если это локальный файл, то необходимо перенести общие константы или функции в более подходящий модуль, например, в `src.utils`. Если модуль не нужен, удалите импорт.
3. **Использование `logger.error` для обработки ошибок:**
   -   Избегайте использования `try-except` блоков для обработки ошибок, где это возможно, и используйте `logger.error` для логирования ошибок. Это упростит код и сделает его более читаемым.
4. **Улучшение документации:**
    -   Добавьте документацию в формате reStructuredText (RST) для всех классов, методов и переменных.
5. **Согласование импортов:**
    -   Убедитесь, что все импорты согласованы с другими модулями.

**Оптимизиробанный код**
```python
"""
Модуль для работы с поставщиками.
=========================================================================================

Этот модуль содержит класс :class:`Supplier`, который управляет загрузкой конфигурации,
выполнением сценариев и входом на сайты поставщиков.

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
# from header import MODE # TODO - Уточнить назначение модуля header или удалить
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

    :param supplier_id: Идентификатор поставщика (может быть None).
    :param supplier_prefix: Префикс поставщика (строка, обязательное поле).
    :param locale: Код локали поставщика (по умолчанию 'en').
    :param price_rule: Правило расчета цен (может быть None).
    :param related_modules: Модуль, содержащий специфические функции для поставщика (может быть None).
    :param scenario_files: Список файлов сценариев для поставщика.
    :param current_scenario: Текущий исполняемый сценарий (словарь).
    :param locators: Локаторы для элементов страницы.
    :param driver: Экземпляр веб-драйвера.

    :raises DefaultSettingsException: Если не удалось загрузить настройки поставщика.
    """
    supplier_id: Optional[int] = None
    supplier_prefix: str
    locale: str = 'en'
    price_rule: Optional[str] = None
    related_modules: Optional[ModuleType] = None
    scenario_files: List[str] = []
    current_scenario: Optional[dict] = None
    locators: Dict[str, Any] = {}
    driver: Optional[Driver] = None

    class Config:
        """
        Конфигурация модели pydantic.
        
        :param arbitrary_types_allowed: Разрешает произвольные типы данных.
        """
        arbitrary_types_allowed = True

    def __init__(self, **data):
        """
        Инициализирует объект поставщика.

        :param data: Словарь с данными для инициализации поставщика.
        :raises DefaultSettingsException: Если не удалось загрузить настройки поставщика.
        """
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Не удалось загрузить настройки для {self.supplier_prefix=}')

    def _payload(self) -> bool:
        """
        Загружает настройки поставщика из JSON-файла.

        :return: True в случае успеха, False в случае ошибки.
        """
        logger.info(f'Начало загрузки настроек для {self.supplier_prefix=}')
        try:
            # Код пытается динамически импортировать модуль поставщика.
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            self.related_modules = related_module
        except ImportError as ex:
            logger.error(f'Не удалось импортировать модуль поставщика {self.supplier_prefix=}', exc_info=ex)
            return False

        settings_path = f'{gs.path.src}/suppliers/{self.supplier_prefix}_settings.json'
        try:
            # Код пытается загрузить настройки из json файла.
            settings = j_loads_ns(settings_path)
            if not settings:
                logger.error(f'Файл настроек {settings_path} не найден или пуст')
                return False
        except FileNotFoundError as ex:
            logger.error(f'Файл настроек {settings_path} не найден', exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при загрузке файла настроек {settings_path}', exc_info=ex)
            return False
        
        # Код устанавливает атрибуты объекта Supplier на основе загруженных настроек.
        self.price_rule = getattr(settings, 'price_rule', self.price_rule)
        self.locale = getattr(settings, 'locale', self.locale)
        self.scenario_files = getattr(settings, 'scenario_files', self.scenario_files)
        self.locators = getattr(settings, 'locators', self.locators)
        
        logger.info(f'Настройки для {self.supplier_prefix=} успешно загружены')
        return True

    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика.

        :return: True в случае успеха, False в случае ошибки.
        """
        if not self.related_modules:
            logger.error(f'Модуль поставщика {self.supplier_prefix=} не загружен')
            return False
        try:
            # Код вызывает метод login из модуля поставщика.
            return self.related_modules.login(self)
        except Exception as ex:
             logger.error(f'Ошибка при выполнении входа в систему для {self.supplier_prefix=}', exc_info=ex)
             return False

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        """
        Выполняет сценарии, указанные в файлах.

        :param scenario_files: Список файлов сценариев или путь к одному файлу (необязательный).
        :return: True в случае успеха, False в случае ошибки.
        """
        # Код вызывает функцию run_scenario_files из модуля src.scenario.
        return run_scenario_files(self, scenario_files or self.scenario_files)

    def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
        """
        Выполняет сценарии, переданные как словарь или список словарей.

        :param scenarios: Словарь или список словарей, представляющих сценарии.
        :return: True в случае успеха, False в случае ошибки.
        """
        # Код вызывает функцию run_scenarios из модуля src.scenario.
        return run_scenarios(self, scenarios)

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value):
        """
        Валидатор для проверки, что `supplier_prefix` не пустая строка.

        :param value: Значение префикса поставщика.
        :return: Значение префикса поставщика, если оно не пустое.
        :raises ValueError: Если значение префикса поставщика пустое.
        """
        if not value:
            raise ValueError('Префикс поставщика не может быть пустым')
        return value
```