# Класс `Supplier`

## Базовый класс для всех поставщиков

В контексте кода `Supplier` представляет собой поставщика информации. Поставщик может быть производителем товаров, данных или информации. Источники данных поставщика могут включать домашнюю страницу сайта, документ, базу данных или таблицу. Данный класс объединяет различных поставщиков под стандартным набором операций. Каждый поставщик имеет уникальный префикс (подробности о префиксах можно найти в файле [prefixes.md](prefixes.md)).

Класс `Supplier` служит основой для управления взаимодействиями с поставщиками. Он обрабатывает инициализацию, конфигурацию, аутентификацию и выполнение рабочих процессов для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиенты также могут определять дополнительных поставщиков.

---

## Список реализованных поставщиков:

- `[aliexpress](aliexpress)` — Реализован с двумя рабочими процессами: `webdriver` и `api`
- `[amazon](amazon)` — `webdriver`
- `[bangood](bangood)` — `webdriver`
- `[cdata](cdata)` — `webdriver`
- `[chat_gpt](chat_gpt)` — Взаимодействует с интерфейсом ChatGPT (НЕ с моделью!)
- `[ebay](ebay)` — `webdriver`
- `[etzmaleh](etzmaleh)` — `webdriver`
- `[gearbest](gearbest)` — `webdriver`
- `[grandadvance](grandadvance)` — `webdriver`
- `[hb](hb)` — `webdriver`
- `[ivory](ivory)` — `webdriver`
- `[ksp](ksp)` — `webdriver`
- `[kualastyle](kualastyle)` — `webdriver`
- `[morlevi](morlevi)` — `webdriver`
- `[visualdg](visualdg)` — `webdriver`
- `[wallashop](wallashop)` — `webdriver`
- `[wallmart](wallmart)` — `webdriver`

[Подробнее о WebDriver: класс `Driver`](../webdriver)
[Подробнее о рабочих процессах: класс `Scenario`](../scenarios)

---

## Атрибуты

- `supplier_id` (int): Уникальный идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика, например, `'amazon'`, `'aliexpress'`.
- `supplier_settings` (dict): Настройки поставщика, загруженные из файла JSON.
- `locale` (str): Код локализации (по умолчанию: `'en'`).
- `price_rule` (str): Правила расчета цены (например, правила НДС).
- `related_modules` (module): Вспомогательные модули для специфических операций с поставщиком.
- `scenario_files` (list): Список файлов сценариев, которые необходимо выполнить.
- `current_scenario` (dict): Сценарий, который выполняется в данный момент.
- `login_data` (dict): Данные для аутентификации.
- `locators` (dict): Словарь локаторов веб-элементов.
- `driver` (Driver): Экземпляр WebDriver для взаимодействия с веб-сайтом поставщика.
- `parsing_method` (str): Метод разбора данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).


---

## Методы

### `__init__`

Конструктор класса `Supplier`.

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Инициализирует экземпляр Supplier.

    Args:
        supplier_prefix (str): Префикс поставщика.
        locale (str, optional): Код локализации. По умолчанию 'en'.
        webdriver (str | Driver | bool, optional): Тип WebDriver. По умолчанию 'default'.

    Raises:
        DefaultSettingsException: Если настройки по умолчанию не правильно сконфигурированы.
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
        bool: Возвращает True, если загрузка прошла успешно.
    """
```

### `login`

Обрабатывает аутентификацию на веб-сайте поставщика.

```python
def login(self) -> bool:
    """Аутентифицирует пользователя на веб-сайте поставщика.

    Returns:
        bool: Возвращает True, если вход выполнен успешно.
    """
```

### `run_scenario_files`

Выполняет один или несколько файлов сценариев.

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Выполняет предоставленные файлы сценариев.

    Args:
        scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

    Returns:
        bool: Возвращает True, если сценарии были выполнены успешно.
    """
```

### `run_scenarios`

Выполняет указанные сценарии.

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Выполняет указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии, которые необходимо выполнить.

    Returns:
        bool: Возвращает True, если все сценарии были выполнены успешно.
    """
```

---

## Как это работает

1. **Инициализация**: Метод `__init__` устанавливает префикс поставщика, локализацию и WebDriver.
2. **Загрузка настроек**: `_payload` загружает конфигурацию, инициализирует локаторы и WebDriver.
3. **Аутентификация**: `login` выполняет вход на веб-сайте поставщика.
4. **Выполнение сценариев**: Выполнение файлов сценариев или отдельных сценариев.


**Примеры использования:**

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
supplier._payload(webdriver='firefox')
supplier.login()
supplier.run_scenario_files(['example_scenario.json'])
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```