# Модуль `Supplier`

## Обзор

Модуль содержит базовый класс `Supplier`, предназначенный для управления поставщиками данных в приложении. Он предоставляет основу для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другие. Этот класс обрабатывает инициализацию специфических настроек поставщика, управляет сценариями для сбора данных и предоставляет методы для входа в систему и выполнения сценариев.

## Подробнее

Класс `Supplier` служит в качестве базового класса для управления поставщиками данных. Он предоставляет фреймворк для взаимодействия с различными источниками данных и обрабатывает инициализацию настроек поставщика, управляет сценариями сбора данных и предоставляет методы для входа в систему и выполнения сценариев.

## Классы

### `Supplier`

**Описание**: Базовый класс для управления поставщиками данных.

**Принцип работы**:
Класс `Supplier` действует как шаблон для управления сбором данных от различных поставщиков. Он определяет общие методы и атрибуты, которые могут быть использованы или расширены конкретными реализациями для различных поставщиков. Класс централизует управление поставщиками, включая конфигурацию, вход в систему и выполнение сценариев.

**Атрибуты**:
- `supplier_id` (str): Уникальный идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика, например, `aliexpress` или `amazon`.
- `supplier_settings` (dict): Настройки поставщика, загруженные из файла конфигурации.
- `locale` (str): Код локализации (например, `en` для английского, `ru` для русского).
- `price_rule` (str): Правило для расчета цен (например, добавление НДС или применение скидок).
- `related_modules` (module): Модуль, содержащий специфичные для поставщика функции.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения.
- `current_scenario` (dict): Текущий выполняемый сценарий.
- `login_data` (dict): Учетные данные для доступа к веб-сайту поставщика (если требуется).
- `locators` (dict): Локаторы для веб-элементов на сайте поставщика.
- `driver` (Driver): Веб-драйвер для взаимодействия с сайтом поставщика.
- `parsing_method` (str): Метод для разбора данных (например, `webdriver`, `api`, `xls`, `csv`).

**Методы**:
- `__init__`: Конструктор, который инициализирует атрибуты на основе префикса поставщика и других параметров.
- `_payload`: Загружает специфические для поставщика конфигурации, локаторы и инициализирует веб-драйвер.
- `login`: Обрабатывает процесс входа в систему для сайта поставщика, если требуется аутентификация.
- `run_scenario_files`: Выполняет один или несколько файлов сценариев.
- `run_scenarios`: Выполняет один или несколько сценариев.

## Функции

### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs) -> None:
    """
    Инициализирует экземпляр класса `Supplier`.

    Args:
        supplier_prefix (str): Префикс поставщика (например, 'aliexpress' или 'amazon').
        locale (str, optional): Локаль (например, 'en' для английского, 'ru' для русского). По умолчанию 'en'.
        webdriver (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой ('chrome', 'firefox'),
            экземпляром класса `Driver` или булевым значением ('default' для использования настроек по умолчанию, `False` для отключения). По умолчанию 'default'.
        *attrs: Дополнительные позиционные аргументы.
        **kwargs: Дополнительные именованные аргументы.

    Raises:
        ValueError: Если `supplier_prefix` не является строкой.
        TypeError: Если `webdriver` имеет недопустимый тип.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='firefox')
    """
    ...
```

**Назначение**: Инициализация объекта класса `Supplier` с заданными параметрами.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика (например, `aliexpress` или `amazon`).
- `locale` (str, optional): Локаль (например, `en` для английского, `ru` для русского). По умолчанию `en`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой (`chrome`, `firefox`), экземпляром класса `Driver` или булевым значением (`default` для использования настроек по умолчанию, `False` для отключения). По умолчанию `default`.
- `*attrs`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `supplier_prefix` не является строкой.
- `TypeError`: Если `webdriver` имеет недопустимый тип.

**Как работает функция**:
1. **Инициализация атрибутов**: Функция инициализирует основные атрибуты класса, такие как `supplier_prefix`, `locale` и `webdriver`.
2. **Валидация входных данных**: Проверяет, что `supplier_prefix` является строкой, а `webdriver` имеет допустимый тип.
3. **Загрузка настроек**: Вызывает метод `_payload` для загрузки специфических для поставщика конфигураций и инициализации веб-драйвера.

```
Инициализация атрибутов (supplier_prefix, locale, webdriver)
↓
Валидация входных данных (supplier_prefix, webdriver)
↓
Загрузка настроек (_payload)
```

**Примеры**:

```python
# Создание экземпляра класса Supplier для AliExpress с использованием Firefox в качестве веб-драйвера
supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='firefox')

# Создание экземпляра класса Supplier для Amazon с использованием настроек по умолчанию для веб-драйвера
supplier = Supplier(supplier_prefix='amazon', locale='en')

# Создание экземпляра класса Supplier без использования веб-драйвера
supplier = Supplier(supplier_prefix='walmart', locale='en', webdriver=False)
```

### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """
    Загружает специфические для поставщика конфигурации, локаторы и инициализирует веб-драйвер.

    Args:
        webdriver (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой ('chrome', 'firefox'),
            экземпляром класса `Driver` или булевым значением ('default' для использования настроек по умолчанию, `False` для отключения).
        *attrs: Дополнительные позиционные аргументы.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        bool: `True`, если конфигурация успешно загружена и веб-драйвер инициализирован, иначе `False`.

    Raises:
        FileNotFoundError: Если не найден файл конфигурации для данного поставщика.
        ValueError: Если возникла ошибка при инициализации веб-драйвера.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='ru')
        >>> result = supplier._payload(webdriver='chrome')
        >>> print(result)
        True
    """
    ...
```

**Назначение**: Загрузка конфигураций, локаторов и инициализация веб-драйвера для поставщика.

**Параметры**:
- `webdriver` (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой (`chrome`, `firefox`), экземпляром класса `Driver` или булевым значением (`default` для использования настроек по умолчанию, `False` для отключения).
- `*attrs`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `bool`: `True`, если конфигурация успешно загружена и веб-драйвер инициализирован, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если не найден файл конфигурации для данного поставщика.
- `ValueError`: Если возникла ошибка при инициализации веб-драйвера.

**Как работает функция**:
1. **Загрузка конфигурации**: Функция загружает специфические для поставщика конфигурации из файла конфигурации.
2. **Инициализация веб-драйвера**: Инициализирует веб-драйвер на основе переданного параметра `webdriver`.
3. **Обработка ошибок**: Возвращает `True`, если конфигурация успешно загружена и веб-драйвер инициализирован, иначе `False`.

```
Загрузка конфигурации (supplier_settings, locators)
↓
Инициализация веб-драйвера (webdriver)
↓
Обработка ошибок (FileNotFoundError, ValueError)
```

**Примеры**:

```python
# Создание экземпляра класса Supplier и загрузка конфигурации с использованием Chrome в качестве веб-драйвера
supplier = Supplier(supplier_prefix='aliexpress', locale='ru')
result = supplier._payload(webdriver='chrome')
print(result)

# Создание экземпляра класса Supplier и загрузка конфигурации с использованием Firefox в качестве веб-драйвера
supplier = Supplier(supplier_prefix='amazon', locale='en')
result = supplier._payload(webdriver='firefox')
print(result)

# Создание экземпляра класса Supplier и загрузка конфигурации без использования веб-драйвера
supplier = Supplier(supplier_prefix='walmart', locale='en')
result = supplier._payload(webdriver=False)
print(result)
```

### `login`

```python
def login(self) -> bool:
    """
    Выполняет вход на сайт поставщика, если требуется аутентификация.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `False`.

    Raises:
        AuthenticationError: Если произошла ошибка аутентификации.
        WebDriverException: Если возникла проблема с веб-драйвером.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
        >>> supplier._payload(webdriver='chrome')
        True
        >>> result = supplier.login()
        >>> print(result)
        True
    """
    ...
```

**Назначение**: Выполнение входа на сайт поставщика, если это необходимо.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Вызывает исключения**:
- `AuthenticationError`: Если произошла ошибка аутентификации.
- `WebDriverException`: Если возникла проблема с веб-драйвером.

**Как работает функция**:
1. **Проверка необходимости входа**: Функция проверяет, требуется ли вход на сайт поставщика.
2. **Выполнение входа**: Если вход требуется, функция выполняет процесс входа с использованием учетных данных, сохраненных в `login_data`.
3. **Обработка ошибок**: Возвращает `True`, если вход выполнен успешно, иначе `False`.

```
Проверка необходимости входа
↓
Выполнение входа (использование login_data)
↓
Обработка ошибок (AuthenticationError, WebDriverException)
```

**Примеры**:

```python
# Создание экземпляра класса Supplier и выполнение входа на сайт AliExpress
supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
supplier._payload(webdriver='chrome')
result = supplier.login()
print(result)

# Создание экземпляра класса Supplier и выполнение входа на сайт Amazon
supplier = Supplier(supplier_prefix='amazon', locale='en', webdriver='firefox')
supplier._payload(webdriver='firefox')
result = supplier.login()
print(result)

# Создание экземпляра класса Supplier, для которого не требуется вход на сайт
supplier = Supplier(supplier_prefix='walmart', locale='en', webdriver=False)
supplier._payload(webdriver=False)
result = supplier.login()
print(result)
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """
    Выполняет один или несколько файлов сценариев.

    Args:
        scenario_files (str | List[str], optional): Список файлов сценариев для выполнения.
            Если указана строка, она будет преобразована в список из одного элемента.
            Если `None`, используются файлы сценариев по умолчанию из `self.scenario_files`. По умолчанию `None`.

    Returns:
        bool: `True`, если все сценарии успешно выполнены, иначе `False`.

    Raises:
        FileNotFoundError: Если не найден файл сценария.
        ScenarioError: Если произошла ошибка во время выполнения сценария.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
        >>> supplier._payload(webdriver='chrome')
        True
        >>> result = supplier.run_scenario_files(['scenario1.json', 'scenario2.json'])
        >>> print(result)
        True
    """
    ...
```

**Назначение**: Выполнение одного или нескольких файлов сценариев.

**Параметры**:
- `scenario_files` (str | List[str], optional): Список файлов сценариев для выполнения. Если указана строка, она будет преобразована в список из одного элемента. Если `None`, используются файлы сценариев по умолчанию из `self.scenario_files`. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если не найден файл сценария.
- `ScenarioError`: Если произошла ошибка во время выполнения сценария.

**Как работает функция**:
1. **Определение файлов сценариев**: Функция определяет, какие файлы сценариев следует выполнить. Если `scenario_files` не указан, используются файлы сценариев по умолчанию из `self.scenario_files`.
2. **Выполнение сценариев**: Выполняет каждый файл сценария.
3. **Обработка ошибок**: Возвращает `True`, если все сценарии успешно выполнены, иначе `False`.

```
Определение файлов сценариев (scenario_files, self.scenario_files)
↓
Выполнение сценариев
↓
Обработка ошибок (FileNotFoundError, ScenarioError)
```

**Примеры**:

```python
# Создание экземпляра класса Supplier и выполнение файлов сценариев
supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
supplier._payload(webdriver='chrome')
result = supplier.run_scenario_files(['scenario1.json', 'scenario2.json'])
print(result)

# Создание экземпляра класса Supplier и выполнение файлов сценариев по умолчанию
supplier = Supplier(supplier_prefix='amazon', locale='en', webdriver='firefox')
supplier._payload(webdriver='firefox')
supplier.scenario_files = ['default_scenario.json']
result = supplier.run_scenario_files()
print(result)

# Создание экземпляра класса Supplier и выполнение одного файла сценария
supplier = Supplier(supplier_prefix='walmart', locale='en', webdriver=False)
supplier._payload(webdriver=False)
result = supplier.run_scenario_files('single_scenario.json')
print(result)
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """
    Выполняет один или несколько сценариев.

    Args:
        scenarios (dict | list[dict]): Список сценариев для выполнения.
            Если указан словарь, он будет преобразован в список из одного элемента.

    Returns:
        bool: `True`, если все сценарии успешно выполнены, иначе `False`.

    Raises:
        ScenarioError: Если произошла ошибка во время выполнения сценария.

    Example:
        >>> supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
        >>> supplier._payload(webdriver='chrome')
        True
        >>> result = supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
        >>> print(result)
        True
    """
    ...
```

**Назначение**: Выполнение одного или нескольких сценариев.

**Параметры**:
- `scenarios` (dict | list[dict]): Список сценариев для выполнения. Если указан словарь, он будет преобразован в список из одного элемента.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, иначе `False`.

**Вызывает исключения**:
- `ScenarioError`: Если произошла ошибка во время выполнения сценария.

**Как работает функция**:
1. **Определение сценариев**: Функция определяет, какие сценарии следует выполнить. Если `scenarios` является словарем, он преобразуется в список из одного элемента.
2. **Выполнение сценариев**: Выполняет каждый сценарий.
3. **Обработка ошибок**: Возвращает `True`, если все сценарии успешно выполнены, иначе `False`.

```
Определение сценариев (scenarios)
↓
Выполнение сценариев
↓
Обработка ошибок (ScenarioError)
```

**Примеры**:

```python
# Создание экземпляра класса Supplier и выполнение сценариев
supplier = Supplier(supplier_prefix='aliexpress', locale='ru', webdriver='chrome')
supplier._payload(webdriver='chrome')
result = supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
print(result)

# Создание экземпляра класса Supplier и выполнение одного сценария
supplier = Supplier(supplier_prefix='amazon', locale='en', webdriver='firefox')
supplier._payload(webdriver='firefox')
result = supplier.run_scenarios({'action': 'check_price', 'target': 'product_page'})
print(result)

# Создание экземпляра класса Supplier и выполнение нескольких сценариев
supplier = Supplier(supplier_prefix='walmart', locale='en', webdriver=False)
supplier._payload(webdriver=False)
scenarios = [
    {'action': 'scrape', 'target': 'product_list'},
    {'action': 'check_stock', 'target': 'product_page'}
]
result = supplier.run_scenarios(scenarios)
print(result)
```

## Пример использования

```python
# Создание объекта Supplier для 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполнение входа на сайт поставщика
supplier.login()

# Выполнение файлов сценариев
supplier.run_scenario_files(['example_scenario.json'])

# Или выполнение конкретных сценариев
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Заключение

Класс `Supplier` предоставляет структурированный способ взаимодействия с поставщиками данных, управляя конфигурациями, выполняя входы в систему и выполняя сценарии сбора данных. Он служит в качестве основного компонента, который может быть расширен для конкретных поставщиков путем наследования от этого базового класса и добавления или переопределения функциональности по мере необходимости.