# Руководство по использованию класса `Supplier`

### Базовый класс для всех поставщиков данных

Этот класс предоставляет единый интерфейс для взаимодействия с различными поставщиками информации (например, производителями товаров, источниками данных).  Поставщики могут быть веб-сайтами, документами, базами данных и т.д.  Класс `Supplier` абстрагирует различия между поставщиками, позволяя использовать одинаковый алгоритм для работы с разными источниками. Каждый поставщик имеет уникальный префикс (см. [подробности о префиксах](prefixes.md)).

Класс `Supplier` служит основой для управления взаимодействием с поставщиками, выполняя инициализацию, настройку, аутентификацию и запуск сценариев для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`.  Вы можете определить дополнительных поставщиков.

---

## Список реализованных поставщиков:

* [aliexpress](aliexpress) – реализован в двух вариантах сценариев: `webriver` и `api`
* [amazon](amazon) – `webdriver`
* [bangood](bangood) – `webdriver`
* [cdata](cdata) – `webdriver`
* [chat_gpt](chat_gpt) – взаимодействие с чат-ботом chatgpt (НЕ с моделью!)
* [ebay](ebay) – `webdriver`
* [etzmaleh](etzmaleh) – `webdriver`
* [gearbest](gearbest) – `webdriver`
* [grandadvance](grandadvance) – `webdriver`
* [hb](hb) – `webdriver`
* [ivory](ivory) – `webdriver`
* [ksp](ksp) – `webdriver`
* [kualastyle](kualastyle) – `webdriver`
* [morlevi](morlevi) – `webdriver`
* [visualdg](visualdg) – `webdriver`
* [wallashop](wallashop) – `webdriver`
* [wallmart](wallmart) – `webdriver`

[Подробнее о веб-драйвере `Driver`](../webdriver)
[Подробнее о сценариях `Scenario`](../scenarios)

---

## Атрибуты

* **`supplier_id`** (int): Уникальный идентификатор поставщика.
* **`supplier_prefix`** (str): Префикс поставщика (например, `'amazon'`, `'aliexpress'`).
* **`supplier_settings`** (dict): Настройки поставщика, загружаемые из JSON-файла.
* **`locale`** (str): Код локализации (по умолчанию: `'en'`).
* **`price_rule`** (str): Правила расчета цен (например, правила НДС).
* **`related_modules`** (module): Модули-помощники для работы с конкретным поставщиком.
* **`scenario_files`** (list): Список файлов сценариев для выполнения.
* **`current_scenario`** (dict): Текущий сценарий, выполняемый в данный момент.
* **`login_data`** (dict): Данные для аутентификации.
* **`locators`** (dict): Словарь локаторов веб-элементов.
* **`driver`** (`Driver`): Экземпляр WebDriver для взаимодействия с сайтом поставщика.
* **`parsing_method`** (str): Метод парсинга данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

---

## Методы

### `__init__`

Конструктор класса `Supplier`.

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

Загружает настройки поставщика и инициализирует WebDriver.

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

Обрабатывает аутентификацию на сайте поставщика.

```python
def login(self) -> bool:
    """Производит аутентификацию пользователя на сайте поставщика.

    Returns:
        bool: Возвращает `True`, если вход выполнен успешно.
    """
```

### `run_scenario_files`

Выполняет один или несколько файлов сценариев.

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

Выполняет указанные сценарии.

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Запускает указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии для выполнения.

    Returns:
        bool: Возвращает `True`, если все сценарии выполнены успешно.
    """
```

---

## Как это работает

1. **Инициализация**: Метод `__init__` настраивает префикс, локаль и WebDriver.
2. **Загрузка настроек**: Метод `_payload` загружает конфигурацию и инициализирует WebDriver.
3. **Аутентификация**: Метод `login` выполняет вход на сайт поставщика.
4. **Выполнение сценариев**: Методы `run_scenario_files` и `run_scenarios` запускают заданные сценарии.  Примеры использования приведены в документации.
```