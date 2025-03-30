# Модуль `supplier`

## Обзор

Модуль `supplier` содержит базовый класс `Supplier`, который используется для представления и управления поставщиками в системе. Он обеспечивает загрузку конфигурации поставщика, выполнение сценариев и взаимодействие с веб-драйвером.

## Подробней

Этот модуль является ключевым компонентом системы, поскольку он абстрагирует логику взаимодействия с различными поставщиками. Класс `Supplier` предоставляет интерфейс для выполнения сценариев, специфичных для каждого поставщика, и управляет их настройками. Расположение файла в структуре проекта указывает на его роль как центрального элемента в подсистеме управления поставщиками.

## Классы

### `Supplier`

**Описание**: Класс `Supplier` представляет поставщика и управляет его конфигурацией и сценариями.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `Supplier`, загружает конфигурацию поставщика.
- `_payload`: Загружает параметры поставщика из файла конфигурации.
- `login`: Выполняет вход на сайт поставщика.
- `run_scenario_files`: Выполняет один или несколько файлов сценариев.
- `run_scenarios`: Выполняет список или один сценарий.
- `check_supplier_prefix`: Проверяет префикс поставщика на пустое значение.

**Параметры**:

- `supplier_id` (Optional[int]): Идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str): Код локали в формате ISO 639-1.
- `price_rule` (Optional[str]): Правило расчета цен.
- `related_modules` (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий.
- `locators` (Dict[str, Any]): Локаторы для элементов страницы.
- `driver` (Optional[Driver]): Веб-драйвер.

**Примеры**

```python
from src.suppliers.supplier import Supplier
from src.webdriver.driver import Driver

# Пример создания экземпляра класса Supplier
supplier = Supplier(
    supplier_prefix='example',
    locale='ru',
    scenario_files=['scenario1.json', 'scenario2.json'],
    driver=Driver()
)

# Проверка значений атрибутов
print(f"Префикс поставщика: {supplier.supplier_prefix}")
print(f"Локаль: {supplier.locale}")
print(f"Файлы сценариев: {supplier.scenario_files}")
```

## Функции

### `check_supplier_prefix`

```python
def check_supplier_prefix(cls, value: str) -> str:
    """Проверка префикса поставщика на пустое значение."""
```

**Описание**: Проверяет, что префикс поставщика не является пустой строкой.

**Параметры**:

- `cls` (class): Ссылка на класс.
- `value` (str): Префикс поставщика.

**Возвращает**:

- `str`: Префикс поставщика, если он не пустой.

**Вызывает исключения**:

- `ValueError`: Если префикс поставщика является пустой строкой.

**Примеры**:

```python
from src.suppliers.supplier import Supplier
from pydantic import ValidationError

# Пример успешной валидации префикса поставщика
valid_prefix = Supplier.check_supplier_prefix(Supplier, "valid_prefix")
print(f"Валидный префикс: {valid_prefix}")

# Пример неудачной валидации префикса поставщика (пустая строка)
try:
    invalid_prefix = Supplier.check_supplier_prefix(Supplier, "")
except ValidationError as ex:
    print(f"Ошибка валидации: {ex}")
```

### `_payload`

```python
def _payload(self) -> bool:
    """Загрузка параметров поставщика с использованием `j_loads_ns`."""
```

**Описание**: Загружает параметры поставщика, такие как правило расчета цен, локаль и файлы сценариев, из файла конфигурации JSON с использованием функции `j_loads_ns`.

**Параметры**:

- `self` (Supplier): Экземпляр класса `Supplier`.

**Возвращает**:

- `bool`: `True`, если загрузка параметров прошла успешно, иначе `False`.

**Вызывает исключения**:

- `ModuleNotFoundError`: Если не найден модуль, связанный с поставщиком.
- `Exception`: Если произошла ошибка при загрузке параметров.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='example')

# Вызов метода _payload для загрузки параметров
result = supplier._payload()

if result:
    print("Параметры поставщика успешно загружены.")
    print(f"Правило расчета цен: {supplier.price_rule}")
    print(f"Локаль: {supplier.locale}")
    print(f"Файлы сценариев: {supplier.scenario_files}")
else:
    print("Не удалось загрузить параметры поставщика.")
```

### `login`

```python
def login(self) -> bool:
    """Выполняет вход на сайт поставщика."""
```

**Описание**: Выполняет вход на сайт поставщика, используя соответствующую функцию из связанного модуля поставщика.

**Параметры**:

- `self` (Supplier): Экземпляр класса `Supplier`.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='example')

# Вызов метода login для выполнения входа на сайт поставщика
result = supplier.login()

if result:
    print("Вход на сайт поставщика выполнен успешно.")
else:
    print("Не удалось выполнить вход на сайт поставщика.")
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool:
    """Выполнение одного или нескольких файлов сценариев."""
```

**Описание**: Выполняет сценарии, определенные в указанных файлах сценариев. Если файлы сценариев не указаны, используются файлы, определенные в атрибуте `scenario_files` экземпляра класса `Supplier`.

**Параметры**:

- `self` (Supplier): Экземпляр класса `Supplier`.
- `scenario_files` (Optional[str | List[str]]): Список файлов сценариев для выполнения. Если не указан, используются `self.scenario_files`.

**Возвращает**:

- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='example', scenario_files=['scenario1.json', 'scenario2.json'])

# Пример выполнения файлов сценариев, определенных в классе Supplier
result = supplier.run_scenario_files()

if result:
    print("Сценарии из файлов успешно выполнены.")
else:
    print("Не удалось выполнить сценарии из файлов.")

# Пример выполнения указанных файлов сценариев
result = supplier.run_scenario_files(scenario_files=['scenario3.json', 'scenario4.json'])

if result:
    print("Сценарии из указанных файлов успешно выполнены.")
else:
    print("Не удалось выполнить сценарии из указанных файлов.")
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | List[dict]) -> bool:
    """Выполнение списка или одного сценария."""
```

**Описание**: Выполняет один или несколько сценариев, переданных в виде словаря или списка словарей.

**Параметры**:

- `self` (Supplier): Экземпляр класса `Supplier`.
- `scenarios` (dict | List[dict]): Сценарий или список сценариев для выполнения.

**Возвращает**:

- `bool`: `True`, если сценарий успешно выполнен, иначе `False`.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='example')

# Пример выполнения одного сценария
scenario = {'name': 'test_scenario', 'steps': [{'action': 'navigate', 'url': 'https://example.com'}]}
result = supplier.run_scenarios(scenarios=scenario)

if result:
    print("Сценарий успешно выполнен.")
else:
    print("Не удалось выполнить сценарий.")

# Пример выполнения нескольких сценариев
scenarios = [
    {'name': 'test_scenario_1', 'steps': [{'action': 'navigate', 'url': 'https://example.com'}]},
    {'name': 'test_scenario_2', 'steps': [{'action': 'click', 'selector': '#button'}]}
]
result = supplier.run_scenarios(scenarios=scenarios)

if result:
    print("Сценарии успешно выполнены.")
else:
    print("Не удалось выполнить сценарии.")