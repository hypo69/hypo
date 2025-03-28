# Модуль `supplier`

## Обзор

Модуль `supplier` содержит класс `Supplier`, который является базовым классом для представления поставщиков. Он управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

## Оглавление

- [Классы](#классы)
    - [`Supplier`](#supplier)
- [Функции](#функции)
    - [`_payload`](#_payload)
    - [`login`](#login)
    - [`run_scenario_files`](#run_scenario_files)
    - [`run_scenarios`](#run_scenarios)
- [Переменные](#переменные)
- [Потенциальные ошибки и области для улучшения](#потенциальные-ошибки-и-области-для-улучшения)
- [Цепочка взаимосвязей с другими частями проекта](#цепочка-взаимосвязей-с-другими-частями-проекта)

## Классы

### `Supplier`

**Описание**: Базовый класс для представления поставщиков. Управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

**Методы**:
- `__init__(self, **data)`: Инициализирует объект поставщика, загружает настройки через метод `_payload()`.
- `_payload(self)`: Загружает настройки поставщика из JSON-файла.
- `login(self)`: Выполняет вход на сайт поставщика.
- `run_scenario_files(self, scenario_files: Optional[str | List[str]] = None)`: Выполняет сценарии, указанные в файлах.
- `run_scenarios(self, scenarios: dict | List[dict])`: Выполняет сценарии, переданные как словарь или список словарей.
- `check_supplier_prefix(cls, value)`: Валидатор для проверки, что `supplier_prefix` не пустая строка.

**Параметры**:
- `supplier_id` (Optional[str]): Идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локали поставщика. По умолчанию `en`.
- `price_rule` (Optional[str], optional): Правило расчета цен. По умолчанию `None`.
- `related_modules` (Optional[ModuleType], optional): Модуль, содержащий специфические функции для поставщика. По умолчанию `None`.
- `scenario_files` (Optional[List[str]], optional): Список файлов сценариев для поставщика. По умолчанию `None`.
- `current_scenario` (Optional[Dict], optional): Текущий исполняемый сценарий. По умолчанию `None`.
- `locators` (Optional[Dict], optional): Локаторы для элементов страницы. По умолчанию `None`.
- `driver` (Optional[Driver], optional): Экземпляр веб-драйвера. По умолчанию `None`.

**Пример**
```python
supplier = Supplier(supplier_prefix="test_supplier")
```
## Функции

### `_payload`

**Описание**: Загружает настройки поставщика из JSON-файла и динамически импортирует модуль поставщика.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True`, если настройки загружены успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `DefaultSettingsException`: Если загрузка настроек не удалась.

### `login`

**Описание**: Выполняет вход на сайт поставщика, вызывая метод `login` из модуля, связанного с поставщиком.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, `False` в случае ошибки.

### `run_scenario_files`

**Описание**: Выполняет сценарии, указанные в файлах.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.
- `scenario_files` (Optional[str | List[str]], optional): Список файлов сценариев или путь к одному файлу. Если не указан, использует `self.scenario_files`. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, `False` в случае ошибки.

### `run_scenarios`

**Описание**: Выполняет сценарии, переданные как словарь или список словарей.

**Параметры**:
- `self`: Экземпляр класса `Supplier`.
- `scenarios` (dict | List[dict]): Словарь или список словарей, представляющих сценарии.

**Возвращает**:
- `bool`: `True`, если все сценарии успешно выполнены, `False` в случае ошибки.

## Переменные

-  `settings_path`: Путь к файлу настроек поставщика.
-  `settings`: Настройки поставщика, загруженные из JSON-файла.
-  `ex`: Переменная для хранения информации об исключениях.
-  `value`: Переменная для хранения значения `supplier_prefix` в валидаторе.
- `related_module`:  Динамически загруженный модуль поставщика.
-  `scenario_files`: Список файлов сценариев.

## Потенциальные ошибки и области для улучшения

1.  **Обработка ошибок**:
    *   Используются `try-except` блоки, но обработка ошибок может быть более детальной.
    *   В блоке `except Exception as ex:` логируется общее исключение, но было бы полезно логировать конкретный тип ошибки для более легкой отладки.

2.  **Зависимости**:
    *   Файл `header` не определен, поэтому его назначение неясно.
    *   В зависимости от сложности проекта может потребоваться более гибкое управление зависимостями.

3.  **Улучшение валидации:**
    *   Можно добавить дополнительные валидаторы для других полей.

## Цепочка взаимосвязей с другими частями проекта

1.  **`src.suppliers.*`**: Данный файл служит базой для всех поставщиков (например, `src.suppliers.test_supplier`). Каждый конкретный поставщик может реализовывать методы `login`, специфичные для этого поставщика.
2.  **`src.scenario`**: Класс `Supplier` использует `run_scenarios` и `run_scenario_files` для выполнения сценариев, что обеспечивает единый механизм выполнения сценариев для всех поставщиков.
3.  **`src.webdriver.driver`**:  Класс `Supplier` может использовать `Driver` для управления веб-драйвером.
4.  **`src.utils.jjson`**: `j_loads_ns` используется для загрузки настроек поставщика, обеспечивая единый механизм работы с JSON-конфигурациями.
5.  **`src.logger`**: Используется для логирования событий, позволяя отслеживать состояние и работу `Supplier` и связанных процессов.
6.  **`src.gs`**: `gs.path` используется для построения путей к конфигурационным файлам, обеспечивая доступ к глобальным параметрам проекта.
7.  **`header`**:  Ожидается, что данный модуль используется для общих настроек или конфигурации, но это неявно.
8.  **`pydantic`**: Используется для валидации данных, обеспечивая корректность работы класса `Supplier`.
9.  **`types`**: Используется для работы с типами, что делает код более читаемым и понятным.
10. **`importlib`**: Используется для динамического импорта модулей, что обеспечивает гибкость и расширяемость системы.