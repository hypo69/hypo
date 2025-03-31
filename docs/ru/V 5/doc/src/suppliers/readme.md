# Документация для модуля `Supplier`

## Обзор

Этот документ предоставляет подробное описание класса `Supplier`, базового класса для всех поставщиков в проекте `hypotez`. `Supplier` представляет собой поставщика информации, такого как производитель товаров, данных или информации. Источники поставщика могут включать целевую страницу веб-сайта, документ, базу данных или таблицу. Этот класс объединяет различных поставщиков под стандартизированным набором операций.

## Содержание

- [Обзор](#обзор)
- [Атрибуты](#атрибуты)
- [Методы](#методы)
    - [`__init__`](#__init__)
    - [`_payload`](#_payload)
    - [`login`](#login)
    - [`run_scenario_files`](#run_scenario_files)
    - [`run_scenarios`](#run_scenarios)
- [Как это работает](#как-это-работает)

## Подробней

Класс `Supplier` служит основой для управления взаимодействием с поставщиками. Он обрабатывает инициализацию, конфигурацию, аутентификацию и выполнение рабочих процессов для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиенты также могут определять дополнительных поставщиков.

Каждый поставщик имеет уникальный префикс.

## Атрибуты

- **`supplier_id`** *(int)*: Уникальный идентификатор поставщика.
- **`supplier_prefix`** *(str)*: Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
- **`supplier_settings`** *(dict)*: Настройки поставщика, загруженные из JSON-файла.
- **`locale`** *(str)*: Код локализации (по умолчанию: `'en'`).
- **`price_rule`** *(str)*: Правила для расчета цены (например, правила НДС).
- **`related_modules`** *(module)*: Вспомогательные модули для конкретных операций поставщика.
- **`scenario_files`** *(list)*: Список файлов сценариев для выполнения.
- **`current_scenario`** *(dict)*: Сценарий, выполняемый в данный момент.
- **`login_data`** *(dict)*: Данные для аутентификации.
- **`locators`** *(dict)*: Словарь локаторов веб-элементов.
- **`driver`** *(Driver)*: Экземпляр WebDriver для взаимодействия с веб-сайтом поставщика.
- **`parsing_method`** *(str)*: Метод анализа данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

## Методы

### `__init__`

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

**Описание**: Конструктор класса `Supplier`.

**Как работает функция**:

- Инициализирует экземпляр класса `Supplier` с заданным префиксом поставщика, локалью и типом WebDriver.
- Принимает префикс поставщика (`supplier_prefix`), который является уникальным идентификатором поставщика.
- Устанавливает локаль (`locale`) для определения языковых настроек (по умолчанию используется английский язык).
- Определяет тип WebDriver (`webdriver`), который может быть строкой, экземпляром `Driver` или булевым значением (по умолчанию `'default'`).
- Вызывает исключение `DefaultSettingsException`, если настройки по умолчанию не сконфигурированы должным образом.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Тип WebDriver. По умолчанию `'default'`.

**Вызывает исключения**:
- `DefaultSettingsException`: Если настройки по умолчанию не настроены правильно.

**Примеры**:
```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
```

### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Loads settings, locators, and initializes the WebDriver.

    Args:
        webdriver (str | Driver | bool): Type of WebDriver.

    Returns:
        bool: Returns `True` if the loading was successful.
    """
```

**Описание**: Загружает настройки поставщика, инициализирует локаторы и WebDriver.

**Как работает функция**:
- Загружает настройки поставщика, включая параметры конфигурации и локаторы веб-элементов.
- Инициализирует WebDriver для взаимодействия с веб-сайтом поставщика.
- Возвращает `True`, если загрузка настроек и инициализация WebDriver прошли успешно.

**Параметры**:
- `webdriver` (str | Driver | bool): Тип WebDriver.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно.

**Примеры**:
```python
supplier._payload(webdriver='firefox')
```

### `login`

```python
def login(self) -> bool:
    """Authenticates the user on the supplier's website.

    Returns:
        bool: Returns `True` if login was successful.
    """
```

**Описание**: Выполняет аутентификацию пользователя на веб-сайте поставщика.

**Как работает функция**:
- Использует данные для входа, хранящиеся в атрибуте `login_data`, для аутентификации на веб-сайте поставщика.
- Возвращает `True`, если вход в систему выполнен успешно.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно.

**Примеры**:
```python
supplier.login()
```

### `run_scenario_files`

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

**Как работает функция**:
- Принимает список или путь к файлам сценариев (`scenario_files`).
- Выполняет сценарии, определенные в указанных файлах.
- Возвращает `True`, если сценарии выполнены успешно.

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
    """Executes specified scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to be executed.

    Returns:
        bool: Returns `True` if all scenarios were executed successfully.
    """
```

**Описание**: Выполняет указанные сценарии.

**Как работает функция**:
- Принимает словарь или список словарей, представляющих сценарии для выполнения (`scenarios`).
- Выполняет каждый сценарий в списке.
- Возвращает `True`, если все сценарии выполнены успешно.

**Параметры**:
- `scenarios` (dict | list[dict]): Сценарии для выполнения.

**Возвращает**:
- `bool`: `True`, если все сценарии выполнены успешно.

**Примеры**:
```python
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Как это работает

1. **Инициализация**:
   - Метод `__init__` настраивает префикс поставщика, локализацию и WebDriver.
     Пример:
     ```python
     supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
     ```

2. **Загрузка настроек**:
   - `_payload` загружает конфигурацию, инициализирует локаторы и WebDriver.
     Пример:
     ```python
     supplier._payload(webdriver='firefox')
     ```

3. **Аутентификация**:
   - `login` выполняет вход пользователя на веб-сайт поставщика.
     Пример:
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