# Модуль `supplier.py`

## Обзор

Модуль `supplier.py` содержит базовый класс `Supplier`, предназначенный для унификации взаимодействия с различными поставщиками. Он предоставляет абстракцию для запуска сценариев сбора данных, управления локаторами элементов страницы и взаимодействия с веб-драйвером. Модуль обеспечивает загрузку связанных модулей поставщика и управление сценариями.

## Подробнее

Этот модуль является ключевым компонентом системы, так как он определяет, как система взаимодействует с различными поставщиками данных. Класс `Supplier` предоставляет интерфейс для запуска сценариев сбора данных, управления локаторами элементов страницы и взаимодействия с веб-драйвером. Он также отвечает за загрузку связанных модулей поставщика и управление сценариями.

## Классы

### `Supplier`

**Описание**: Класс `Supplier` выполняет сценарии для различных поставщиков.

**Принцип работы**: Класс `Supplier` предназначен для управления процессом сбора данных от различных поставщиков. Он инициализируется с использованием параметров, специфичных для каждого поставщика, таких как идентификатор, префикс, локаль и правила расчета цен. Класс также загружает связанные модули поставщика и настраивает веб-драйвер для взаимодействия с веб-сайтом поставщика. Основная функциональность включает в себя выполнение сценариев сбора данных, вход на сайт поставщика и управление локаторами элементов страницы.

**Атрибуты**:

- `supplier_id` (Optional[int]): Идентификатор поставщика. По умолчанию `None`.
- `supplier_prefix` (str): Префикс поставщика. Обязательный параметр.
- `locale` (str): Код локали в формате ISO 639-1. По умолчанию `'en'`.
- `price_rule` (Optional[str]): Правило расчета цен. По умолчанию `None`.
- `related_modules` (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения. По умолчанию пустой список.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий. По умолчанию пустой словарь.
- `locators` (Dict[str, Any]): Локаторы для элементов страницы. По умолчанию пустой словарь.
- `driver` (Optional[Driver]): Веб-драйвер.

**Методы**:

- `__init__(self, **data)`: Инициализация поставщика, загрузка конфигурации.
- `_payload(self) -> bool`: Загрузка параметров поставщика.
- `login(self) -> bool`: Выполняет вход на сайт поставщика.
- `run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool`: Выполнение одного или нескольких файлов сценариев.
- `run_scenarios(self, scenarios: dict | List[dict]) -> bool`: Выполнение списка или одного сценария.
- `check_supplier_prefix(cls, value: str) -> str`: Проверка префикса поставщика на пустое значение.

## Функции

### `check_supplier_prefix`

```python
@validator('supplier_prefix')
def check_supplier_prefix(cls, value: str) -> str:
    """Проверка префикса поставщика на пустое значение."""
    if not value:
        raise ValueError('supplier_prefix не может быть пустым')
    return value
```

**Назначение**: Проверяет, что префикс поставщика не является пустым значением.

**Параметры**:

- `cls`: Ссылка на класс. Используется декоратором `@validator`.
- `value` (str): Префикс поставщика, который необходимо проверить.

**Возвращает**:

- `str`: Префикс поставщика, если он не пустой.

**Вызывает исключения**:

- `ValueError`: Если `value` является пустой строкой.

**Как работает функция**:

1. Функция `check_supplier_prefix` проверяет, является ли переданный префикс поставщика (`value`) пустой строкой.
2. Если префикс поставщика пустой, возбуждается исключение `ValueError` с сообщением о том, что префикс не может быть пустым.
3. Если префикс поставщика не пустой, функция возвращает этот префикс.

**Примеры**:

```python
from pydantic import BaseModel, validator

class MyModel(BaseModel):
    supplier_prefix: str

    @validator('supplier_prefix')
    def check_supplier_prefix(cls, value: str) -> str:
        if not value:
            raise ValueError('supplier_prefix не может быть пустым')
        return value

# Пример успешной валидации
model = MyModel(supplier_prefix='valid_prefix')
print(model.supplier_prefix)  # Вывод: valid_prefix

# Пример неудачной валидации
try:
    model = MyModel(supplier_prefix='')
except ValueError as ex:
    print(ex)  # Вывод: supplier_prefix не может быть пустым
```

### `__init__`

```python
def __init__(self, **data):
    """Инициализация поставщика, загрузка конфигурации."""
    super().__init__(**data)
    if not self._payload():
        raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')
```

**Назначение**: Инициализирует экземпляр класса `Supplier`, выполняет базовую настройку и загружает конфигурацию поставщика.

**Параметры**:

- `**data`: Произвольные именованные аргументы, передаваемые для инициализации атрибутов класса.

**Возвращает**:

- None

**Вызывает исключения**:

- `DefaultSettingsException`: Если не удается загрузить конфигурацию поставщика с помощью метода `_payload()`.

**Как работает функция**:

1. **Вызов конструктора родительского класса**: Вызывает метод `__init__` родительского класса `BaseModel` для инициализации атрибутов класса на основе переданных данных `**data`.
2. **Загрузка конфигурации поставщика**: Вызывает метод `_payload()` для загрузки конфигурации поставщика.
3. **Проверка успешности загрузки**: Проверяет, успешно ли выполнена загрузка конфигурации с помощью `if not self._payload()`.
4. **Возбуждение исключения в случае ошибки**: Если загрузка конфигурации не удалась (метод `_payload()` вернул `False`), возбуждается исключение `DefaultSettingsException` с сообщением об ошибке, содержащим префикс поставщика (`self.supplier_prefix`).

**Примеры**:

```python
from typing import Optional
from pydantic import BaseModel
from src.logger.exceptions import DefaultSettingsException  # Предполагается, что исключение определено в этом модуле

class MockSupplier(BaseModel):
    supplier_prefix: str
    config_loaded: bool = False

    def __init__(self, **data):
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        # Имитация загрузки конфигурации, которая всегда успешна
        self.config_loaded = True
        return True

# Пример успешной инициализации
try:
    supplier = MockSupplier(supplier_prefix='test_supplier')
    print(f"Supplier {supplier.supplier_prefix} initialized successfully. Config loaded: {supplier.config_loaded}")
except DefaultSettingsException as ex:
    print(f"Error initializing supplier: {ex}")

class FailingSupplier(BaseModel):
    supplier_prefix: str

    def __init__(self, **data):
        super().__init__(**data)
        if not self._payload():
            raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')

    def _payload(self) -> bool:
        # Имитация загрузки конфигурации, которая всегда завершается неудачей
        return False

# Пример инициализации с ошибкой
try:
    supplier = FailingSupplier(supplier_prefix='failing_supplier')
    print(f"Supplier {supplier.supplier_prefix} initialized successfully.")
except DefaultSettingsException as ex:
    print(f"Error initializing supplier: {ex}")
```

### `_payload`

```python
def _payload(self) -> bool:
    """Загрузка параметров поставщика с использованием `j_loads_ns`.\n
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
```

**Назначение**: Загружает параметры поставщика, включая связанные модули, используя `importlib`.

**Параметры**:
- `self`: Ссылка на экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True`, если загрузка параметров и модулей выполнена успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `ModuleNotFoundError`: Если не удается импортировать модуль, связанный с поставщиком.

**Как работает функция**:

1. **Логирование начала загрузки**: Записывает информационное сообщение в лог о начале загрузки настроек для указанного поставщика.
2. **Импорт связанных модулей**:
   - Пытается динамически импортировать модуль, имя которого формируется на основе префикса поставщика (`src.suppliers.{self.supplier_prefix}`).
   - Использует `importlib.import_module` для выполнения импорта.
   - В случае успешного импорта, устанавливает импортированный модуль как атрибут `related_modules` текущего экземпляра класса `Supplier` с помощью `object.__setattr__`.
3. **Обработка ошибок импорта**:
   - Если модуль не найден (`ModuleNotFoundError`), функция перехватывает исключение.
   - Записывает сообщение об ошибке в лог с использованием `logger.error`, указывая на отсутствие модуля для данного поставщика.
   - Возвращает `False`, указывая на неудачную загрузку.
4. **Возврат успешного результата**: Если импорт модуля выполнен успешно, функция возвращает `True`.

**Примеры**:

```python
import importlib
from typing import Optional
from pydantic import BaseModel
from src.logger.logger import logger  # Предполагается, что logger настроен
from src.logger.exceptions import DefaultSettingsException  # Определение исключения
class MockSupplier(BaseModel):
    supplier_prefix: str
    related_modules: Optional[importlib.ModuleType] = None

    def _payload(self) -> bool:
        logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
        try:
            related_modules = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            object.__setattr__(self, 'related_modules', related_modules)
        except ModuleNotFoundError as ex:
            logger.error(f'Модуль не найден для поставщика {self.supplier_prefix}: ', ex)
            return False
        return True

# Пример успешной загрузки модуля
# Для этого примера необходимо создать пустой модуль src/suppliers/test_supplier.py
try:
    supplier = MockSupplier(supplier_prefix='test_supplier')
    if supplier._payload():
        print(f"Модуль для поставщика {supplier.supplier_prefix} успешно загружен.")
    else:
        print(f"Не удалось загрузить модуль для поставщика {supplier.supplier_prefix}.")
except Exception as ex:
    print(f"Произошла ошибка при инициализации поставщика: {ex}")

# Пример неудачной загрузки модуля
# Модуль src/suppliers/nonexistent_supplier.py отсутствует
try:
    supplier = MockSupplier(supplier_prefix='nonexistent_supplier')
    if supplier._payload():
        print(f"Модуль для поставщика {supplier.supplier_prefix} успешно загружен.")
    else:
        print(f"Не удалось загрузить модуль для поставщика {supplier.supplier_prefix}.")
except Exception as ex:
    print(f"Произошла ошибка при инициализации поставщика: {ex}")
```

### `login`

```python
def login(self) -> bool:
    """Выполняет вход на сайт поставщика.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `False`.
    """
    return self.related_modules.login(self)
```

**Назначение**: Выполняет вход на сайт поставщика, используя функцию `login` из связанного модуля поставщика.

**Параметры**:
- `self`: Ссылка на экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1. **Вызов функции входа**: Вызывает функцию `login` из модуля `related_modules`, передавая текущий экземпляр класса `Supplier` в качестве аргумента.
2. **Возврат результата**: Возвращает результат, полученный от функции `login`, который указывает на успешность выполнения входа.

**Примеры**:

```python
import importlib
from typing import Optional
from pydantic import BaseModel

# Создаем имитацию модуля поставщика
class MockRelatedModule:
    def login(self, supplier):
        # Здесь должна быть логика входа на сайт поставщика
        # В данном примере всегда возвращаем True
        return True

# Создаем имитацию класса Supplier
class MockSupplier(BaseModel):
    supplier_prefix: str
    related_modules: Optional[MockRelatedModule] = None

    def login(self) -> bool:
        """Выполняет вход на сайт поставщика.

        Returns:
            bool: `True`, если вход выполнен успешно, иначе `False`.
        """
        return self.related_modules.login(self)

# Пример использования
related_module = MockRelatedModule()
supplier = MockSupplier(supplier_prefix='test_supplier', related_modules=related_module)

# Вызываем метод login
success = supplier.login()
print(f"Вход выполнен успешно: {success}")
```

### `run_scenario_files`

```python
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
```

**Назначение**: Запускает выполнение сценариев, указанных в файлах. Если список файлов не предоставлен, использует список файлов, хранящийся в атрибуте `self.scenario_files`.

**Параметры**:

- `self`: Ссылка на экземпляр класса `Supplier`.
- `scenario_files` (Optional[str | List[str]]): Список файлов сценариев для выполнения. Может быть строкой, представляющей один файл, или списком строк. Если `None`, используются файлы из `self.scenario_files`.

**Возвращает**:

- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Как работает функция**:

1. **Определение списка файлов сценариев**:
   - Если `scenario_files` передан как аргумент, он используется как список файлов для выполнения.
   - Если `scenario_files` не передан (равен `None`), используется список файлов, хранящийся в атрибуте `self.scenario_files`.
2. **Запуск выполнения сценариев**:
   - Вызывает функцию `run_scenario_files` (из модуля `src.scenario`), передавая ей текущий экземпляр класса `Supplier` и список файлов сценариев.
3. **Возврат результата**:
   - Возвращает результат, полученный от функции `run_scenario_files`, который указывает на успешность выполнения всех сценариев.

**Примеры**:

```python
from typing import List, Optional
from pydantic import BaseModel

class MockSupplier(BaseModel):
    supplier_prefix: str
    scenario_files: List[str]

    def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
        scenario_files = scenario_files if scenario_files else self.scenario_files
        #  Здесь должна быть логика запуска файлов сценариев
        #  В этом примере всегда возвращаем True
        return True

# Пример использования с указанием файлов сценариев
supplier = MockSupplier(supplier_prefix='test_supplier', scenario_files=['scenario1.json', 'scenario2.json'])
success = supplier.run_scenario_files(scenario_files=['new_scenario.json'])
print(f"Сценарии выполнены успешно: {success}")

# Пример использования без указания файлов сценариев (используются файлы из self.scenario_files)
supplier = MockSupplier(supplier_prefix='test_supplier', scenario_files=['scenario1.json', 'scenario2.json'])
success = supplier.run_scenario_files()
print(f"Сценарии выполнены успешно: {success}")
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
    """Выполнение списка или одного сценария.

    Args:
        scenarios (dict | List[dict]): Сценарий или список сценариев для выполнения.

    Returns:
        bool: `True`, если сценарий успешно выполнен, иначе `False`.
    """
    return run_scenarios(self, scenarios)
```

**Назначение**: Запускает выполнение одного или нескольких сценариев, переданных в виде словаря или списка словарей.

**Параметры**:

- `self`: Ссылка на экземпляр класса `Supplier`.
- `scenarios` (dict | List[dict]): Сценарий или список сценариев для выполнения. Сценарий представляется в виде словаря.

**Возвращает**:

- `bool`: `True`, если сценарий успешно выполнен, иначе `False`.

**Как работает функция**:

1. **Запуск выполнения сценариев**:
   - Вызывает функцию `run_scenarios` (из модуля `src.scenario`), передавая ей текущий экземпляр класса `Supplier` и сценарии для выполнения.
2. **Возврат результата**:
   - Возвращает результат, полученный от функции `run_scenarios`, который указывает на успешность выполнения сценария.

```python
from typing import List, Dict, Any
from pydantic import BaseModel

class MockSupplier(BaseModel):
    supplier_prefix: str

    def run_scenarios(self, scenarios: Dict[str, Any] | List[Dict[str, Any]]) -> bool:
        #  Здесь должна быть логика запуска сценариев
        #  В этом примере всегда возвращаем True
        return True

# Пример использования с одним сценарием
supplier = MockSupplier(supplier_prefix='test_supplier')
scenario = {'name': 'test_scenario', 'steps': []}
success = supplier.run_scenarios(scenarios=scenario)
print(f"Сценарий выполнен успешно: {success}")

# Пример использования со списком сценариев
supplier = MockSupplier(supplier_prefix='test_supplier')
scenarios = [{'name': 'scenario1', 'steps': []}, {'name': 'scenario2', 'steps': []}]
success = supplier.run_scenarios(scenarios=scenarios)
print(f"Сценарии выполнены успешно: {success}")