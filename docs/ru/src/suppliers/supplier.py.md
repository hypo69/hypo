# Модуль `src.suppliers.supplier`

## Обзор

Модуль `src.suppliers.supplier` определяет базовый класс `Supplier`, который служит основой для создания классов, представляющих различных поставщиков. Он предоставляет функциональность для загрузки настроек поставщика, выполнения сценариев и управления веб-драйвером.

## Подробней

Этот модуль является ключевым компонентом системы, обеспечивающим абстракцию и унификацию взаимодействия с различными поставщиками. Он использует библиотеку `pydantic` для определения структуры данных поставщика и валидации входных данных. Модуль также включает функциональность для загрузки связанных модулей поставщика и управления сценариями.

## Классы

### `Supplier`

**Описание**: Базовый класс для представления поставщиков.

**Как работает класс**:

1.  Класс `Supplier` наследуется от `pydantic.BaseModel` и определяет набор атрибутов, общих для всех поставщиков, таких как `supplier_id`, `supplier_prefix`, `locale` и `scenario_files`.

2.  Метод `__init__` инициализирует экземпляр класса, вызывая метод `_payload` для загрузки конфигурации поставщика. Если загрузка конфигурации завершается неудачно, вызывается исключение `DefaultSettingsException`.

3.  Метод `_payload` загружает параметры поставщика из JSON-файла с использованием функции `j_loads_ns`. Он также загружает модуль, связанный с поставщиком, используя `importlib`.

4.  Методы `login`, `run_scenario_files` и `run_scenarios` предоставляют интерфейс для выполнения действий, связанных с поставщиком, таких как вход на сайт, запуск сценариев из файлов и запуск отдельных сценариев.

**Методы**:

*   `__init__(self, \*\*data)`: Инициализация поставщика, загрузка конфигурации.
*   `_payload(self) -> bool`: Загрузка параметров поставщика.
*   `login(self) -> bool`: Выполняет вход на сайт поставщика.
*   `run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool`: Выполнение одного или нескольких файлов сценариев.
*   `run_scenarios(self, scenarios: dict | List[dict]) -> bool`: Выполнение списка или одного сценария.
*   `check_supplier_prefix(cls, value: str) -> str`: Проверка префикса поставщика на пустое значение.

**Параметры**:

*   `supplier_id` (Optional[int]): Идентификатор поставщика.
*   `supplier_prefix` (str): Префикс поставщика.
*   `locale` (str): Код локали в формате ISO 639-1.
*   `price_rule` (Optional[str]): Правило расчета цен.
*   `related_modules` (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
*   `scenario_files` (List[str]): Список файлов сценариев для выполнения.
*   `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий.
*   `locators` (Dict[str, Any]): Локаторы для элементов страницы.
*   `driver` (Optional[Driver]): Веб-драйвер.

**Примеры**:

```python
from src.suppliers.supplier import Supplier
from src.webdriver.driver import Driver
import asyncio

# Пример создания экземпляра класса Supplier
supplier = Supplier(
    supplier_prefix='test_supplier',
    locale='ru',
    scenario_files=['scenario1.json', 'scenario2.json'],
    driver=Driver()
)

# Вывод информации о созданном поставщике
print(f'Supplier prefix: {supplier.supplier_prefix}')
print(f'Locale: {supplier.locale}')
print(f'Scenario files: {supplier.scenario_files}')
print(f'Driver: {supplier.driver}')
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

**Как работает функция**:

Функция `check_supplier_prefix` является валидатором для поля `supplier_prefix` класса `Supplier`. Она проверяет, что переданное значение не является пустой строкой. Если значение пустое, вызывается исключение `ValueError`. В противном случае значение возвращается без изменений.

**Параметры**:

*   `cls` (class): Ссылка на класс, в котором определен валидатор.
*   `value` (str): Проверяемый префикс поставщика.

**Возвращает**:

*   `str`: Префикс поставщика, если он не пустой.

**Вызывает исключения**:

*   `ValueError`: Если `value` является пустой строкой.

**Примеры**:

```python
from src.suppliers.supplier import Supplier
from pydantic import ValidationError

# Пример успешной валидации префикса поставщика
valid_prefix = Supplier.check_supplier_prefix(Supplier, 'valid_prefix')
print(f'Valid prefix: {valid_prefix}')

# Пример неудачной валидации префикса поставщика (пустая строка)
try:
    invalid_prefix = Supplier.check_supplier_prefix(Supplier, '')
except ValueError as ex:
    print(f'Validation error: {ex}')
```

### `__init__`

```python
def __init__(self, **data):
    """Инициализация поставщика, загрузка конфигурации."""
    super().__init__(**data)
    if not self._payload():
        raise DefaultSettingsException(f'Ошибка запуска поставщика: {self.supplier_prefix}')
```

**Описание**: Инициализирует экземпляр класса `Supplier` и загружает конфигурацию поставщика.

**Как работает функция**:

1.  Вызывает конструктор базового класса (`pydantic.BaseModel`) для инициализации атрибутов объекта.

2.  Вызывает метод `_payload` для загрузки конфигурации поставщика.

3.  Если метод `_payload` возвращает `False` (что указывает на ошибку при загрузке конфигурации), вызывается исключение `DefaultSettingsException` с сообщением об ошибке, включающим префикс поставщика.

**Параметры**:

*   `**data`: Произвольные аргументы ключевого слова, передаваемые в конструктор базового класса.

**Вызывает исключения**:

*   `DefaultSettingsException`: Если не удается загрузить конфигурацию поставщика.

**Примеры**:

```python
from src.suppliers.supplier import Supplier
from src.logger.exceptions import DefaultSettingsException

# Пример успешной инициализации поставщика
try:
    supplier = Supplier(supplier_prefix='test_supplier')
    print(f'Supplier {supplier.supplier_prefix} initialized successfully')
except DefaultSettingsException as ex:
    print(f'Error initializing supplier: {ex}')

# Пример неудачной инициализации поставщика (предположим, что _payload возвращает False)
# В этом случае будет выброшено исключение DefaultSettingsException
```

### `_payload`

```python
def _payload(self) -> bool:
    """Загрузка параметров поставщика с использованием `j_loads_ns`.

    Returns:
        bool: `True`, если загрузка успешна, иначе `False`.
    """
    logger.info(f'Загрузка настроек для поставщика: {self.supplier_prefix}')
    
    # Импорт модуля, связанного с поставщиком
    try:
        related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
        object.__setattr__(self, 'related_modules', related_module)
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

        # Загрузка настроек в атрибуты класса
        object.__setattr__(self, 'price_rule', getattr(settings, 'price_rule', 'default_rule'))
        object.__setattr__(self, 'locale', getattr(settings, 'locale', 'en'))
        object.__setattr__(self, 'scenario_files', getattr(settings, 'scenario_files', []))
        object.__setattr__(self, 'locators', getattr(settings, 'locators', {}))

        logger.info(f'Настройки для поставщика {self.supplier_prefix} успешно загружены')
        return True
    
    except Exception as ex:
        logger.error(f'Ошибка при загрузке настроек для поставщика {self.supplier_prefix}: ', ex)
        return False
```

**Описание**: Загружает параметры поставщика из JSON-файла и устанавливает соответствующие атрибуты класса.

**Как работает функция**:

1.  Логирует начало процесса загрузки настроек для указанного поставщика.

2.  Пытается импортировать модуль, связанный с поставщиком, используя `importlib.import_module`. Если модуль не найден, логирует ошибку и возвращает `False`.

3.  Формирует путь к файлу настроек поставщика (`{supplier_prefix}_settings.json`) в каталоге `src/suppliers`.

4.  Загружает настройки из JSON-файла, используя функцию `j_loads_ns`. Если файл не найден или не может быть прочитан, логирует ошибку и возвращает `False`.

5.  Устанавливает атрибуты класса (`price_rule`, `locale`, `scenario_files`, `locators`) на основе загруженных настроек. Если атрибут не найден в файле настроек, используется значение по умолчанию.

6.  Логирует успешное завершение процесса загрузки настроек и возвращает `True`.

7.  Если в процессе загрузки или установки атрибутов возникает исключение, логирует ошибку и возвращает `False`.

**Возвращает**:

*   `bool`: `True`, если загрузка параметров прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Пример успешной загрузки параметров поставщика
supplier = Supplier(supplier_prefix='test_supplier')
if supplier._payload():
    print(f'Payload loaded successfully for {supplier.supplier_prefix}')
else:
    print(f'Failed to load payload for {supplier.supplier_prefix}')

# Пример неудачной загрузки параметров поставщика (например, файл настроек не найден)
# В этом случае _payload вернет False
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

**Описание**: Выполняет вход на сайт поставщика, используя функцию `login` из связанного модуля поставщика.

**Как работает функция**:

Функция вызывает метод `login` из модуля, связанного с текущим поставщиком (`self.related_modules`). Этот метод должен содержать логику для входа на сайт конкретного поставщика.

**Возвращает**:

*   `bool`: Возвращает `True`, если вход выполнен успешно, и `False` в противном случае.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Создаем экземпляр класса Supplier (предположим, что related_modules.login существует)
supplier = Supplier(supplier_prefix='test_supplier')

# Выполняем вход на сайт поставщика
if supplier.login():
    print(f'Login successful for {supplier.supplier_prefix}')
else:
    print(f'Login failed for {supplier.supplier_prefix}')
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

**Описание**: Выполняет сценарии, определенные в указанных файлах.

**Как работает функция**:

1.  Определяет список файлов сценариев для выполнения. Если аргумент `scenario_files` передан, используется он. В противном случае используется список файлов сценариев, хранящийся в атрибуте `self.scenario_files`.

2.  Вызывает функцию `run_scenario_files` из модуля `src.scenario` для выполнения сценариев.

3.  Возвращает `True`, если все сценарии успешно выполнены, и `False` в противном случае.

**Параметры**:

*   `scenario_files` (Optional[str | List[str]]): Список файлов сценариев для выполнения. Если не указан, используются файлы из `self.scenario_files`.

**Возвращает**:

*   `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Создаем экземпляр класса Supplier
supplier = Supplier(supplier_prefix='test_supplier', scenario_files=['scenario1.json', 'scenario2.json'])

# Выполняем сценарии из файлов
if supplier.run_scenario_files():
    print(f'Scenarios from files executed successfully for {supplier.supplier_prefix}')
else:
    print(f'Failed to execute scenarios from files for {supplier.supplier_prefix}')

# Выполняем сценарии из указанного файла
if supplier.run_scenario_files(scenario_files='scenario3.json'):
    print(f'Scenario from scenario3.json executed successfully for {supplier.supplier_prefix}')
else:
    print(f'Failed to execute scenario from scenario3.json for {supplier.supplier_prefix}')
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

**Описание**: Выполняет один или несколько сценариев, переданных в виде словаря или списка словарей.

**Как работает функция**:

1.  Вызывает функцию `run_scenarios` из модуля `src.scenario` для выполнения переданных сценариев.

2.  Возвращает `True`, если сценарий(и) выполнен(ы) успешно, и `False` в противном случае.

**Параметры**:

*   `scenarios` (dict | List[dict]): Сценарий или список сценариев для выполнения.

**Возвращает**:

*   `bool`: `True`, если сценарий(и) выполнен(ы) успешно, иначе `False`.

**Примеры**:

```python
from src.suppliers.supplier import Supplier

# Создаем экземпляр класса Supplier
supplier = Supplier(supplier_prefix='test_supplier')

# Определяем сценарий
scenario = {'name': 'test_scenario', 'steps': ['step1', 'step2']}

# Выполняем сценарий
if supplier.run_scenarios(scenarios=scenario):
    print(f'Scenario executed successfully for {supplier.supplier_prefix}')
else:
    print(f'Failed to execute scenario for {supplier.supplier_prefix}')

# Определяем список сценариев
scenarios = [{'name': 'test_scenario1', 'steps': ['step1', 'step2']}, {'name': 'test_scenario2', 'steps': ['step3', 'step4']}]

# Выполняем список сценариев
if supplier.run_scenarios(scenarios=scenarios):
    print(f'Scenarios executed successfully for {supplier.supplier_prefix}')
else:
    print(f'Failed to execute scenarios for {supplier.supplier_prefix}')