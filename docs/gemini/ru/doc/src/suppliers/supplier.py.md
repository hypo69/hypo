# Модуль `supplier`

## Обзор

Модуль `supplier` содержит базовый класс `Supplier`, предназначенный для управления и выполнения сценариев для различных поставщиков. Он обеспечивает загрузку конфигураций, выполнение входа в систему поставщика и запуск сценариев.

## Подробней

Этот модуль является основой для взаимодействия с различными поставщиками в проекте `hypotez`. Он определяет структуру и основные методы, необходимые для работы с каждым поставщиком, такие как загрузка настроек, вход в систему и выполнение сценариев. Класс `Supplier` использует библиотеку `pydantic` для валидации данных и `importlib` для динамической загрузки модулей, специфичных для каждого поставщика.

## Классы

### `Supplier`

**Описание**: Класс `Supplier` представляет собой базовый класс для всех поставщиков. Он содержит основную логику для загрузки конфигурации, выполнения входа в систему и запуска сценариев.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Supplier` и загружает конфигурацию поставщика.
- `_payload`: Загружает параметры поставщика из JSON-файла с использованием `j_loads_ns`.
- `login`: Выполняет вход на сайт поставщика.
- `run_scenario_files`: Выполняет один или несколько файлов сценариев.
- `run_scenarios`: Выполняет список или один сценарий.

**Параметры**:
- `supplier_id` (Optional[int]): Идентификатор поставщика. По умолчанию `None`.
- `supplier_prefix` (str): Префикс поставщика (обязательный параметр).
- `locale` (str): Код локали в формате ISO 639-1. По умолчанию `'en'`.
- `price_rule` (Optional[str]): Правило расчета цен. По умолчанию `None`.
- `related_modules` (Optional[ModuleType]): Функции, относящиеся к каждому поставщику. По умолчанию `None`.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения. По умолчанию пустой список.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий. По умолчанию пустой словарь.
- `locators` (Dict[str, Any]): Локаторы для элементов страницы. По умолчанию пустой словарь.
- `driver` (Optional[Driver]): Веб-драйвер. По умолчанию `None`.

**Примеры**
```python
from src.suppliers.supplier import Supplier
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='test_supplier', locale='ru', scenario_files=['scenario1.json', 'scenario2.json'])

print(f"Supplier prefix: {supplier.supplier_prefix}")
print(f"Locale: {supplier.locale}")
print(f"Scenario files: {supplier.scenario_files}")
```

## Функции

### `check_supplier_prefix`

```python
def check_supplier_prefix(cls, value: str) -> str:
    """Проверка префикса поставщика на пустое значение."""
    if not value:
        raise ValueError('supplier_prefix не может быть пустым')
    return value
```

**Описание**: Проверяет, что префикс поставщика не является пустым.

**Параметры**:
- `cls`: Класс, к которому принадлежит метод.
- `value` (str): Префикс поставщика.

**Возвращает**:
- `str`: Префикс поставщика, если он не пустой.

**Вызывает исключения**:
- `ValueError`: Если префикс поставщика пустой.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from pydantic import ValidationError

# Пример успешной валидации префикса поставщика
valid_prefix = Supplier.check_supplier_prefix(Supplier, 'valid_prefix')
print(f"Valid prefix: {valid_prefix}")

# Пример неудачной валидации префикса поставщика
try:
    invalid_prefix = Supplier.check_supplier_prefix(Supplier, '')
except ValidationError as ex:
    print(f"Validation Error: {ex}")
```

### `__init__`

```python
def __init__(self, **data):
    """Инициализация поставщика, загрузка конфигурации."""
    super().__init__(**data)
    if not self._payload():
        raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')
```

**Описание**: Инициализирует поставщика и загружает его конфигурацию.

**Параметры**:
- `**data`: Произвольные аргументы, передаваемые в конструктор класса.

**Вызывает исключения**:
- `DefaultSettingsException`: Если не удается загрузить конфигурацию поставщика.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from src.logger.exceptions import DefaultSettingsException
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено
# Пример успешной инициализации поставщика
try:
    supplier = Supplier(supplier_prefix='test_supplier')
    print(f"Supplier {supplier.supplier_prefix} initialized successfully.")
except DefaultSettingsException as ex:
    print(f"Error initializing supplier: {ex}")
```

### `_payload`

```python
def _payload(self) -> bool:
    """Загрузка параметров поставщика с использованием `j_loads_ns`.

    Returns:
        bool: `True`, если загрузка успешна, иначе `False`.
    """
```

**Описание**: Загружает параметры поставщика из JSON-файла с использованием `j_loads_ns`.

**Возвращает**:
- `bool`: `True`, если загрузка успешна, иначе `False`.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено

# Пример загрузки параметров поставщика
supplier = Supplier(supplier_prefix='test_supplier')
is_loaded = supplier._payload()
print(f"Supplier settings loaded: {is_loaded}")
```

### `login`

```python
def login(self) -> bool:
    """Выполняет вход на сайт поставщика.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `False`.
    """
```

**Описание**: Выполняет вход на сайт поставщика, используя модуль, связанный с этим поставщиком.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено

# Пример выполнения входа на сайт поставщика
supplier = Supplier(supplier_prefix='test_supplier')
is_logged_in = supplier.login()
print(f"Supplier logged in: {is_logged_in}")
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
```

**Описание**: Выполняет один или несколько файлов сценариев для поставщика.

**Параметры**:
- `scenario_files` (Optional[str | List[str]]): Список файлов сценариев для выполнения. Если не указан, используются сценарии из `self.scenario_files`.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено

# Пример запуска файлов сценариев
supplier = Supplier(supplier_prefix='test_supplier', scenario_files=['scenario1.json', 'scenario2.json'])
are_scenarios_run = supplier.run_scenario_files()
print(f"Scenarios run: {are_scenarios_run}")
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
```

**Описание**: Выполняет один или несколько сценариев для поставщика.

**Параметры**:
- `scenarios` (dict | List[dict]): Сценарий или список сценариев для выполнения.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Примеры**:
```python
from src.suppliers.supplier import Supplier
from pathlib import Path
from src import gs

gs.path.src = Path('./src') # необходимо для работы примера. В production среде это определено
# Пример запуска сценариев
supplier = Supplier(supplier_prefix='test_supplier')
scenarios = [{'name': 'scenario1'}, {'name': 'scenario2'}]
are_scenarios_run = supplier.run_scenarios(scenarios)
print(f"Scenarios run: {are_scenarios_run}")