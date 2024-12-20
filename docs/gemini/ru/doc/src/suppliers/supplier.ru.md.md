# Модуль `supplier`

## Обзор

Модуль `supplier` предоставляет класс `Supplier`, который является базовым классом для представления поставщиков. Он управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

## Оглавление

- [Классы](#классы)
  - [`Supplier`](#supplier)
- [Функции](#функции)
  - [`_payload`](#_payload)
  - [`login`](#login)
  - [`run_scenario_files`](#run_scenario_files)
  - [`run_scenarios`](#run_scenarios)

## Классы

### `Supplier`

**Описание**: Базовый класс для представления поставщиков. Управляет загрузкой конфигурации, выполнением сценариев и входом на сайты поставщиков.

**Методы**:

-   `__init__`: Инициализирует объект поставщика, загружает настройки через метод `_payload()`.
-   `_payload`: Загружает настройки поставщика из JSON-файла и динамически импортирует модуль, связанный с поставщиком.
-   `login`: Выполняет вход на сайт поставщика, вызывая метод `login` из модуля, связанного с поставщиком.
-   `run_scenario_files`: Выполняет сценарии, указанные в файлах.
-   `run_scenarios`: Выполняет сценарии, переданные как словарь или список словарей.

**Параметры**:

-   `supplier_id` (Optional[str]): Идентификатор поставщика. По умолчанию `None`.
-   `supplier_prefix` (str): Префикс поставщика. Обязательное поле.
-   `locale` (str): Код локали поставщика. По умолчанию `'en'`.
-   `price_rule` (Optional[str]): Правило расчета цен. По умолчанию `None`.
-   `related_modules` (Optional[ModuleType]): Модуль, содержащий специфические функции для поставщика. По умолчанию `None`.
-   `scenario_files` (List[str]): Список файлов сценариев для поставщика.
-   `current_scenario` (Optional[Dict]): Текущий исполняемый сценарий.
-   `locators` (Optional[Dict[str, str]]): Локаторы для элементов страницы.
-   `driver` (Optional[Driver]): Экземпляр веб-драйвера.

## Функции

### `_payload`

**Описание**: Загружает настройки поставщика из JSON-файла и динамически импортирует модуль, связанный с поставщиком.

**Параметры**:

-   `self` (Supplier): Экземпляр класса `Supplier`.

**Возвращает**:

-   `bool`: `True` в случае успеха, `False` в случае ошибки.

### `login`

**Описание**: Выполняет вход на сайт поставщика, вызывая метод `login` из модуля, связанного с поставщиком.

**Параметры**:

-   `self` (Supplier): Экземпляр класса `Supplier`.

**Возвращает**:

-   `bool`: `True` в случае успеха, `False` в случае ошибки.

### `run_scenario_files`

**Описание**: Выполняет сценарии, указанные в файлах.

**Параметры**:

-   `self` (Supplier): Экземпляр класса `Supplier`.
-   `scenario_files` (Optional[str | List[str]], optional): Список файлов сценариев или путь к одному файлу. Если не указан, использует `self.scenario_files`. По умолчанию `None`.

**Возвращает**:

-   `bool`: `True` в случае успеха, `False` в случае ошибки.

### `run_scenarios`

**Описание**: Выполняет сценарии, переданные как словарь или список словарей.

**Параметры**:

-   `self` (Supplier): Экземпляр класса `Supplier`.
-   `scenarios` (dict | List[dict]): Словарь или список словарей, представляющих сценарии.

**Возвращает**:

-   `bool`: `True` в случае успеха, `False` в случае ошибки.