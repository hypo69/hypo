# Модуль `Supplier`

## Обзор

Этот модуль содержит базовый класс `Supplier`, который служит основой для всех поставщиков данных. `Supplier` представляет собой поставщика информации и может быть источником товаров, данных или любой другой информации. Источниками поставщика могут быть веб-сайт, документ, база данных или таблица. Класс унифицирует разных поставщиков под стандартизированным набором операций. У каждого поставщика есть уникальный префикс.

## Оглавление

- [Класс `Supplier`](#класс-supplier)
    - [Атрибуты](#атрибуты)
    - [Методы](#методы)
        - [`__init__`](#__init__)
        - [`_payload`](#_payload)
        - [`login`](#login)
        - [`run_scenario_files`](#run_scenario_files)
        - [`run_scenarios`](#run_scenarios)
- [Как это работает](#как-это-работает)

## Класс `Supplier`

### Описание

Базовый класс для всех поставщиков. Этот класс управляет взаимодействием с поставщиками, включая инициализацию, конфигурацию, аутентификацию и выполнение рабочих процессов для различных источников данных.

### Атрибуты

- `supplier_id` (int): Уникальный идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
- `supplier_settings` (dict): Настройки поставщика, загруженные из JSON-файла.
- `locale` (str): Код локализации (по умолчанию: `'en'`).
- `price_rule` (str): Правила для расчета цен (например, правила НДС).
- `related_modules` (module): Вспомогательные модули для конкретных операций поставщика.
- `scenario_files` (list): Список файлов сценариев для выполнения.
- `current_scenario` (dict): Текущий выполняемый сценарий.
- `login_data` (dict): Данные для аутентификации.
- `locators` (dict): Словарь локаторов веб-элементов.
- `driver` (Driver): Экземпляр WebDriver для взаимодействия с веб-сайтом поставщика.
- `parsing_method` (str): Метод разбора данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

### Методы

#### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Initializes an instance of Supplier.

    Args:
        supplier_prefix (str): The supplier's prefix.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): Type of WebDriver. Defaults to 'default'.

    Raises:
        DefaultSettingsException: If default settings are not properly configured.
    """
```

**Описание**: Конструктор класса `Supplier`. Инициализирует экземпляр класса `Supplier` с указанным префиксом поставщика, локалью и типом WebDriver.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Тип WebDriver. По умолчанию `'default'`.

**Вызывает исключения**:
- `DefaultSettingsException`: Если настройки по умолчанию настроены некорректно.

---

#### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes the WebDriver.

    Args:
        webdriver (str | Driver | bool): Type of WebDriver.

    Returns:
        bool: Returns `True` if the loading was successful.
    """
```

**Описание**: Загружает настройки поставщика, локаторы и инициализирует WebDriver.

**Параметры**:
- `webdriver` (str | Driver | bool): Тип WebDriver.

**Возвращает**:
- `bool`: Возвращает `True`, если загрузка прошла успешно.

---

#### `login`

```python
def login(self) -> bool:
    """Authenticates the user on the supplier's website.

    Returns:
        bool: Returns `True` if login was successful.
    """
```

**Описание**: Выполняет аутентификацию пользователя на веб-сайте поставщика.

**Возвращает**:
- `bool`: Возвращает `True`, если вход в систему выполнен успешно.

---

#### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Runs the provided scenario files.

    Args:
        scenario_files (str | List[str], optional): List or path to scenario files.

    Returns:
        bool: Returns `True` if scenarios were executed successfully.
    """
```

**Описание**: Выполняет один или несколько файлов сценариев.

**Параметры**:
- `scenario_files` (str | List[str], optional): Список или путь к файлам сценариев.

**Возвращает**:
- `bool`: Возвращает `True`, если сценарии выполнены успешно.

---

#### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Executes specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to be executed.

    Returns:
        bool: Returns `True` if all scenarios were executed successfully.
    """
```

**Описание**: Выполняет указанные сценарии.

**Параметры**:
- `scenarios` (dict | list[dict]): Сценарии для выполнения.

**Возвращает**:
- `bool`: Возвращает `True`, если все сценарии выполнены успешно.

---

## Как это работает

1. **Инициализация**:
    - Метод `__init__` настраивает префикс поставщика, локализацию и WebDriver.
    - Пример:
      ```python
      supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
      ```

2. **Загрузка настроек**:
    - `_payload` загружает конфигурацию, инициализирует локаторы и WebDriver.
    - Пример:
      ```python
      supplier._payload(webdriver='firefox')
      ```

3. **Аутентификация**:
    - `login` выполняет вход пользователя на веб-сайт поставщика.
    - Пример:
      ```python
      supplier.login()
      ```

4. **Выполнение сценариев**:
    - **Запуск файлов сценариев**:
      ```python
      supplier.run_scenario_files(['example_scenario.json'])
      ```
    - **Запуск конкретных сценариев**:
      ```python
      supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
      ```