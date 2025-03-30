# Модуль Supplier

## Обзор

Модуль `Supplier` представляет собой базовый класс для управления поставщиками данных в вашем приложении. Он предоставляет фреймворк для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другие. Этот класс обрабатывает инициализацию специфичных для поставщика настроек, управляет сценариями для сбора данных и предоставляет методы для входа в систему и выполнения сценариев.

## Подробнее

Класс `Supplier` служит основой для управления сбором данных от различных поставщиков. Он определяет общие методы и атрибуты, которые могут быть использованы или расширены конкретными реализациями для разных поставщиков. Класс централизует управление поставщиками, включая конфигурацию, вход в систему и выполнение сценариев.

## Классы

### `Supplier`

**Описание**:
Базовый класс для управления поставщиками данных.

**Методы**:
- `__init__`: Конструктор, который инициализирует атрибуты на основе префикса поставщика и других параметров.
- `_payload`: Загружает конфигурации, локаторы и инициализирует веб-драйвер.
- `login`: Обрабатывает процесс входа в систему для сайта поставщика, если требуется аутентификация.
- `run_scenario_files`: Выполняет один или несколько файлов сценариев.
- `run_scenarios`: Выполняет один или несколько сценариев.

**Параметры**:
- `supplier_prefix` (str): Уникальный префикс поставщика, например, `aliexpress` или `amazon`.
- `locale` (str, optional): Код локализации (например, `en` для английского, `ru` для русского). По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. По умолчанию `'default'`.

**Примеры**:

```python
# Создание объекта Supplier для 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполнение входа в систему на сайте поставщика
supplier.login()

# Выполнение файлов сценариев
supplier.run_scenario_files(['example_scenario.json'])

# Или выполнение конкретных сценариев
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Функции

### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """
    Args:
        supplier_prefix (str): Уникальный префикс поставщика, например, `aliexpress` или `amazon`.
        locale (str, optional): Код локализации (например, `en` для английского, `ru` для русского). По умолчанию `'en'`.
        webdriver (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. По умолчанию `'default'`.

    Returns:
        None

    Raises:
        None

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
    """
    # Инициализирует префикс поставщика, локаль и веб-драйвер
    ...
```

**Описание**:
Конструктор класса `Supplier`. Инициализирует атрибуты объекта на основе переданных параметров.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. По умолчанию `'default'`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
```

### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """
    Args:
        webdriver (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика.

    Returns:
        bool: Возвращает `True`, если загрузка конфигурации прошла успешно, иначе `False`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
        >>> supplier._payload(webdriver='chrome')
        True
    """
    # Загружает файлы конфигурации и инициализирует веб-драйвер
    ...
```

**Описание**:
Метод загружает конфигурацию поставщика, включая настройки и локаторы, и инициализирует веб-драйвер.

**Параметры**:
- `webdriver` (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика.

**Возвращает**:
- `bool`: Возвращает `True`, если загрузка конфигурации прошла успешно, иначе `False`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier._payload(webdriver='chrome')
```

### `login`

```python
def login(self) -> bool:
    """
    Args:
        None

    Returns:
        bool: Возвращает `True`, если вход в систему выполнен успешно, иначе `False`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
        >>> supplier.login()
        True
    """
    # Выполняет вход на сайт поставщика
    ...
```

**Описание**:
Метод обрабатывает процесс входа в систему на сайт поставщика, если требуется аутентификация.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `bool`: Возвращает `True`, если вход в систему выполнен успешно, иначе `False`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier.login()
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """
    Args:
        scenario_files (str | List[str], optional): Список файлов сценариев для выполнения. По умолчанию `None`.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно, иначе `False`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
        >>> supplier.run_scenario_files(['example_scenario.json'])
        True
    """
    # Выполняет файлы сценариев и возвращает True, если все сценарии успешно завершены
    ...
```

**Описание**:
Метод выполняет сценарии из списка файлов.

**Параметры**:
- `scenario_files` (str | List[str], optional): Список файлов сценариев для выполнения. По умолчанию `None`.

**Возвращает**:
- `bool`: Возвращает `True`, если все сценарии выполнены успешно, иначе `False`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier.run_scenario_files(['example_scenario.json'])
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """
    Args:
        scenarios (dict | list[dict]): Список сценариев для выполнения.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно, иначе `False`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
        >>> supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
        True
    """
    # Выполняет заданные сценарии и возвращает True, если все сценарии успешно завершены
    ...
```

**Описание**:
Метод выполняет сценарии из списка.

**Параметры**:
- `scenarios` (dict | list[dict]): Список сценариев для выполнения.

**Возвращает**:
- `bool`: Возвращает `True`, если все сценарии выполнены успешно, иначе `False`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```