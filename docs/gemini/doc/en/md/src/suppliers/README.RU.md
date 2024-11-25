# Документация класса Supplier

## Обзор

Класс `Supplier` централизует управление поставщиками, включая настройки, аутентификацию и выполнение сценариев. Его можно расширять для новых поставщиков через наследование или добавление дополнительных модулей.

## Таблица содержания

* [Класс `Supplier`](#класс-supplier)
* [Атрибуты](#атрибуты)
* [Методы](#методы)
* [Как это работает](#как-это-работает)
* [Диаграмма класса](#диаграмма-класса)


## Класс `Supplier`

### Базовый класс для всех поставщиков

Класс `Supplier` служит основой для управления взаимодействиями с поставщиками. Он выполняет инициализацию, настройку, аутентификацию и запуск сценариев для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиент может определить дополнительные поставщики.


## Атрибуты

- `supplier_id` *(int)*: Уникальный идентификатор поставщика.
- `supplier_prefix` *(str)*: Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
- `supplier_settings` *(dict)*: Настройки поставщика, загружаемые из JSON-файла.
- `locale` *(str)*: Код локализации (по умолчанию: `'en'`).
- `price_rule` *(str)*: Правила расчета цен (например, правила НДС).
- `related_modules` *(module)*: Модули-помощники для работы с конкретным поставщиком.
- `scenario_files` *(list)*: Список файлов сценариев для выполнения.
- `current_scenario` *(dict)*: Выполняемый в текущий момент сценарий.
- `login_data` *(dict)*: Данные для аутентификации.
- `locators` *(dict)*: Словарь локаторов веб-элементов.
- `driver` *(Driver)*: Экземпляр WebDriver для взаимодействия с сайтом поставщика.
- `parsing_method` *(str)*: Метод парсинга данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).


## Методы

### `__init__`

**Конструктор класса `Supplier`.**

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
```

### `_payload`

**Загружает настройки поставщика и инициализирует WebDriver.**

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Загружает настройки, локаторы и инициализирует WebDriver.

    Args:
        webdriver (str | Driver | bool): Тип WebDriver.

    Returns:
        bool: Возвращает `True`, если загрузка выполнена успешно.
    """
```

### `login`

**Обрабатывает аутентификацию на сайте поставщика.**

```python
def login(self) -> bool:
    """Производит аутентификацию пользователя на сайте поставщика.

    Returns:
        bool: Возвращает `True`, если вход выполнен успешно.
    """
```

### `run_scenario_files`

**Выполняет один или несколько файлов сценариев.**

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Запускает предоставленные файлы сценариев.

    Args:
        scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

    Returns:
        bool: Возвращает `True`, если сценарии выполнены успешно.
    """
```

### `run_scenarios`

**Выполняет указанные сценарии.**

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Запускает указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии для выполнения.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно.
    """
```


## Как это работает

1. **Инициализация:** Метод `__init__` настраивает префикс поставщика, локализацию и WebDriver.
2. **Загрузка настроек:** `_payload` загружает конфигурацию, инициализирует локаторы и WebDriver.
3. **Аутентификация:** `login` выполняет вход пользователя на сайте поставщика.
4. **Выполнение сценариев:** `run_scenario_files` или `run_scenarios` запускают подготовленные сценарии.

## Диаграмма класса

```plantuml
@startuml
class Supplier {
    - supplier_id: int
    - supplier_prefix: str
    - supplier_settings: dict
    - locale: str
    - price_rule: str
    - related_modules: module
    - scenario_files: list
    - current_scenario: dict
    - login_data: dict
    - locators: dict
    - driver: Driver
    - parsing_method: str
    + __init__(supplier_prefix, locale = 'en', webdriver = 'default')
    + _payload(webdriver) : bool
    + login() : bool
    + run_scenario_files(scenario_files = null) : bool
    + run_scenarios(scenarios) : bool
}
@enduml
```
```