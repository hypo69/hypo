# Модуль `supplier`

## Обзор

Модуль `supplier` содержит базовый класс `Supplier`, который представляет собой абстракцию поставщика данных. Он отвечает за загрузку настроек поставщика, выполнение сценариев и вход на сайты поставщиков. Этот модуль является основой для реализации конкретных поставщиков в проекте `hypotez`.

## Подробней

Модуль `supplier` предоставляет класс `Supplier`, который служит базовым классом для представления различных поставщиков. Основная задача этого класса - обеспечить унифицированный интерфейс для работы с поставщиками, включая загрузку конфигураций, выполнение сценариев и аутентификацию на сайтах поставщиков. Класс использует динамическую загрузку модулей для адаптации к специфическим требованиям каждого поставщика.

## TOC

- [Классы](#Классы)
  - [`Supplier`](#Supplier)
- [Функции](#Функции)
  - [`_payload`](#_payload)
  - [`login`](#login)
  - [`run_scenario_files`](#run_scenario_files)
  - [`run_scenarios`](#run_scenarios)

## Классы

### `Supplier`

**Описание**: Базовый класс для представления поставщиков. Этот класс управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

**Методы**:
- `__init__`: Инициализирует объект поставщика, загружает настройки через метод `_payload()`.
- `_payload`: Загружает настройки поставщика из JSON-файла, используя `j_loads_ns` и динамически импортирует модуль, связанный с поставщиком.
- `login`: Выполняет вход на сайт поставщика, вызывая метод `login` из модуля, связанного с поставщиком.
- `run_scenario_files`: Выполняет сценарии, указанные в файлах.
- `run_scenarios`: Выполняет сценарии, переданные как словарь или список словарей.
- `check_supplier_prefix`: Валидатор для проверки, что `supplier_prefix` не пустая строка.

**Параметры**:
- `supplier_id` (Optional[str]): Идентификатор поставщика (может быть `None`).
- `supplier_prefix` (str): Префикс поставщика (строка, обязательное поле).
- `locale` (str): Код локали поставщика (по умолчанию `'en'`).
- `price_rule` (Optional[str]): Правило расчета цен (может быть `None`).
- `related_modules` (Optional[ModuleType]): Модуль, содержащий специфические функции для поставщика (может быть `None`).
- `scenario_files` (List[str]): Список файлов сценариев для поставщика.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий (словарь).
- `locators` (Dict[str, str]): Локаторы для элементов страницы.
- `driver` (Driver): Экземпляр веб-драйвера.

**Примеры**
```python
from src.suppliers.supplier import Supplier

# Пример создания экземпляра класса Supplier
supplier = Supplier(supplier_prefix='test_supplier', locale='ru', scenario_files=['scenario1.json', 'scenario2.json'])

# Пример доступа к атрибутам
print(f'Supplier Prefix: {supplier.supplier_prefix}')
print(f'Locale: {supplier.locale}')
```

## Функции

### `_payload`

```python
def _payload(self):
    """ This if example function
    Args:
        self: экземпляр класса `Supplier`.
    Returns:
        bool: `True` в случае успеха, `False` в случае ошибки.

     Raises:
         DefaultSettingsException:  Если не удалось загрузить настройки.

     Example:
         Примеры вызовов
    """
   # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Метод загружает настройки поставщика из JSON-файла, используя `j_loads_ns`.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае ошибки.

**Вызывает исключения**:
- `DefaultSettingsException`: Если не удалось загрузить настройки.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='test_supplier')
success = supplier._payload()
if success:
    print('Настройки успешно загружены')
else:
    print('Ошибка при загрузке настроек')
```

### `login`

```python
def login(self):
    """ This if example function
    Args:
        self: экземпляр класса `Supplier`.
    Returns:
        bool: `True` в случае успеха, `False` в случае ошибки.

     Raises:
         Exception:  Если произошла ошибка при входе в систему.

     Example:
         Примеры вызовов
    """
   # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Метод выполняет вход на сайт поставщика.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при входе в систему.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='test_supplier')
if supplier.login():
    print('Вход выполнен успешно')
else:
    print('Ошибка при входе')
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: Optional[str | List[str]] = None):
    """ This if example function
    Args:
        self: экземпляр класса `Supplier`.
        scenario_files: Опциональный список файлов сценариев или путь к одному файлу. Если не указан, использует `self.scenario_files`.
    Returns:
        bool: `True` в случае успеха, `False` в случае ошибки.

     Raises:
         Exception: Если произошла ошибка при выполнении сценариев.

     Example:
         Примеры вызовов
    """
   # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Выполняет один или несколько файлов сценариев.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.
- `scenario_files` (Optional[str | List[str]]): Опциональный список файлов сценариев или путь к одному файлу. Если не указан, использует `self.scenario_files`.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при выполнении сценариев.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='test_supplier', scenario_files=['scenario1.json'])
if supplier.run_scenario_files():
    print('Сценарии из файлов выполнены успешно')
else:
    print('Ошибка при выполнении сценариев из файлов')

# Пример с указанием конкретных файлов сценариев
if supplier.run_scenario_files(scenario_files=['new_scenario.json']):
    print('Сценарии из указанных файлов выполнены успешно')
else:
    print('Ошибка при выполнении сценариев из указанных файлов')
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | List[dict]):
    """ This if example function
    Args:
        self: экземпляр класса `Supplier`.
        scenarios: Словарь или список словарей, представляющих сценарии.
    Returns:
        bool: `True` в случае успеха, `False` в случае ошибки.

     Raises:
         Exception: Если произошла ошибка при выполнении сценариев.

     Example:
         Примеры вызовов
    """
   # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Выполняет один или несколько сценариев.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.
- `scenarios` (dict | List[dict]): Словарь или список словарей, представляющих сценарии.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при выполнении сценариев.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='test_supplier')
scenario = {'step1': 'do_something', 'step2': 'do_another_thing'}
if supplier.run_scenarios(scenario):
    print('Сценарий выполнен успешно')
else:
    print('Ошибка при выполнении сценария')

# Пример с выполнением списка сценариев
scenarios = [{'step1': 'do_something'}, {'step2': 'do_another_thing'}]
if supplier.run_scenarios(scenarios):
    print('Сценарии выполнены успешно')
else:
    print('Ошибка при выполнении сценариев')
```