# Модуль `Supplier`

## Обзор

Данный модуль предоставляет базовый класс `Supplier` для взаимодействия с поставщиками данных. Класс отвечает за инициализацию, конфигурацию, аутентификацию и выполнение сценариев для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Дополнительные поставщики могут быть определены пользователем.

## Оглавление

* [Классы](#классы)
* [Атрибуты](#атрибуты)
* [Методы](#методы)
* [Как работает](#как-работает)
* [Диаграмма классов](#диаграмма-классов)


## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков данных. Обеспечивает обработку инициализации, конфигурации, аутентификации и выполнения сценариев для разных источников данных.

**Атрибуты**:

* `supplier_id` (int): Уникальный идентификатор поставщика.
* `supplier_prefix` (str): Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
* `supplier_settings` (dict): Настройки, специфичные для поставщика, загружаются из файла JSON.
* `locale` (str): Локализация (по умолчанию `'en'`).
* `price_rule` (str): Правила расчета цены (например, правила НДС).
* `related_modules` (module): Модули, специфичные для поставщика.
* `scenario_files` (list): Список сценариев для выполнения.
* `current_scenario` (dict): Текущий выполняемый сценарий.
* `login_data` (dict): Данные для аутентификации (логин и т.д.).
* `locators` (dict): Словарь локаторов для веб-элементов.
* `driver` (Driver): Экземпляр WebDriver для взаимодействия с сайтом поставщика.
* `parsing_method` (str): Метод парсинга данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

**Методы**:

* [`__init__`](#init)
* [`_payload`](#payload)
* [`login`](#login)
* [`run_scenario_files`](#run-scenario-files)
* [`run_scenarios`](#run-scenarios)


### `__init__`

**Описание**: Конструктор класса `Supplier`.

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Инициализирует экземпляр Supplier.

    Args:
        supplier_prefix (str): Префикс поставщика.
        locale (str, optional): Код локализации. По умолчанию 'en'.
        webdriver (str | Driver | bool, optional): Тип WebDriver. По умолчанию 'default'.

    Raises:
        DefaultSettingsException: Если настройки по умолчанию не настроены правильно.
    """
```


### `_payload`

**Описание**: Загружает настройки поставщика и инициализирует WebDriver.

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Загружает настройки, локаторы и инициализирует WebDriver.

    Args:
        webdriver (str | Driver | bool): Тип WebDriver.

    Returns:
        bool: Возвращает `True`, если загрузка успешна.
    """
```


### `login`

**Описание**: Обрабатывает аутентификацию на сайте поставщика.

```python
def login(self) -> bool:
    """Производит аутентификацию пользователя на сайте поставщика.

    Returns:
        bool: Возвращает `True`, если аутентификация успешна.
    """
```


### `run_scenario_files`

**Описание**: Выполняет один или несколько сценариев из файлов.

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Выполняет предоставленные сценарии из файлов.

    Args:
        scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно.
    """
```


### `run_scenarios`

**Описание**: Выполняет предоставленные сценарии.

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Выполняет указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии для выполнения.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно.
    """
```



## Атрибуты

(Описание атрибутов - повторяется из раздела "Классы")


## Как работает

(Описание работы - повторяется из раздела "Supplier Class Documentation")


## Диаграмма классов

(Диаграмма классов - повторяется из раздела "Supplier Class Documentation")
