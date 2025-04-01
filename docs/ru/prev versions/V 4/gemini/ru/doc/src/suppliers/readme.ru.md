# Модуль `suppliers`

## Обзор

Модуль `suppliers` предоставляет базовый класс `Supplier` для управления взаимодействиями с различными поставщиками данных, такими как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Класс `Supplier` служит основой для унификации работы с различными источниками данных, предоставляя общую структуру для инициализации, аутентификации и выполнения сценариев.

## Подробней

Основная цель модуля `suppliers` - предоставить абстракцию для работы с различными поставщиками данных, позволяя клиентам легко интегрировать и использовать данные из различных источников. Каждый поставщик имеет уникальный префикс, и модуль предоставляет механизмы для загрузки и управления настройками, локаторами и сценариями для каждого поставщика.

Модуль использует паттерн `Webdriver` для взаимодействия с сайтами поставщиков и предоставляет возможность выполнения сценариев, определяющих последовательность действий для получения данных. Клиент может определить дополнительных поставщиков, расширив функциональность модуля.

## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков данных.

**Атрибуты**:
- `supplier_id` (int): Уникальный идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
- `supplier_settings` (dict): Настройки поставщика, загружаемые из JSON-файла.
- `locale` (str): Код локализации (по умолчанию: `'en'`).
- `price_rule` (str): Правила расчета цен (например, правила НДС).
- `related_modules` (module): Модули-помощники для работы с конкретным поставщиком.
- `scenario_files` (list): Список файлов сценариев для выполнения.
- `current_scenario` (dict): Выполняемый в текущий момент сценарий.
- `login_data` (dict): Данные для аутентификации.
- `locators` (dict): Словарь локаторов веб-элементов.
- `driver` (Driver): Экземпляр WebDriver для взаимодействия с сайтом поставщика.
- `parsing_method` (str): Метод парсинга данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

**Методы**:
- `__init__`: Конструктор класса `Supplier`.
- `_payload`: Загружает настройки поставщика и инициализирует WebDriver.
- `login`: Выполняет аутентификацию на сайте поставщика.
- `run_scenario_files`: Выполняет один или несколько файлов сценариев.
- `run_scenarios`: Выполняет указанные сценарии.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier._payload(webdriver='firefox')
supplier.login()
supplier.run_scenario_files(['example_scenario.json'])
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Функции

### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Инициализация экземпляра Supplier.

    Args:
        supplier_prefix (str): Префикс поставщика.
        locale (str, optional): Код локализации. По умолчанию 'en'.
        webdriver (str | Driver | bool, optional): Тип WebDriver. По умолчанию 'default'.

    Raises:
        DefaultSettingsException: Если настройки по умолчанию не настроены корректно.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `Supplier` с заданным префиксом поставщика, локализацией и настройками WebDriver.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Тип WebDriver. По умолчанию `'default'`.

**Вызывает исключения**:
- `DefaultSettingsException`: Если настройки по умолчанию не настроены корректно.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
```

### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Загружает настройки, локаторы и инициализирует WebDriver.

    Args:
        webdriver (str | Driver | bool): Тип WebDriver.

    Returns:
        bool: Возвращает `True`, если загрузка выполнена успешно.
    """
    ...
```

**Описание**: Загружает настройки поставщика, инициализирует локаторы и WebDriver.

**Параметры**:
- `webdriver` (str | Driver | bool): Тип WebDriver.

**Возвращает**:
- `bool`: `True`, если загрузка выполнена успешно.

**Примеры**:
```python
supplier._payload(webdriver='firefox')
```

### `login`

```python
def login(self) -> bool:
    """Производит аутентификацию пользователя на сайте поставщика.

    Returns:
        bool: Возвращает `True`, если вход выполнен успешно.
    """
    ...
```

**Описание**: Выполняет аутентификацию пользователя на сайте поставщика.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно.

**Примеры**:
```python
supplier.login()
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Запускает предоставленные файлы сценариев.

    Args:
        scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

    Returns:
        bool: Возвращает `True`, если сценарии выполнены успешно.
    """
    ...
```

**Описание**: Запускает предоставленные файлы сценариев.

**Параметры**:
- `scenario_files` (str | List[str], optional): Список или путь к файлам сценариев.

**Возвращает**:
- `bool`: `True`, если сценарии выполнены успешно.

**Примеры**:
```python
supplier.run_scenario_files(['example_scenario.json'])
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Запускает указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии для выполнения.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно.
    """
    ...
```

**Описание**: Запускает указанные сценарии.

**Параметры**:
- `scenarios` (dict | list[dict]): Сценарии для выполнения.

**Возвращает**:
- `bool`: `True`, если все сценарии выполнены успешно.

**Примеры**:
```python
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```