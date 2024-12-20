# Модуль `src.scenario`

## Обзор

Модуль `src.scenario` предоставляет функции для выполнения сценариев для поставщиков. Он включает в себя функции `run_scenario_files`, `run_scenarios`, `execute_PrestaShop_insert` и `execute_PrestaShop_insert_async`, предназначенные для управления процессом выполнения сценариев из файлов или непосредственно из словарей. Модуль также поддерживает асинхронное выполнение операций.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Функции](#функции)
    - [`run_scenario`](#run_scenario)
    - [`run_scenarios`](#run_scenarios)
    - [`run_scenario_file`](#run_scenario_file)
    - [`run_scenario_files`](#run_scenario_files)
    - [`execute_PrestaShop_insert`](#execute_PrestaShop_insert)
    - [`execute_PrestaShop_insert_async`](#execute_PrestaShop_insert_async)
## Константы
### `MODE`
- **Описание**: Режим работы приложения (например, 'dev' для разработки).

## Функции

### `run_scenario`

**Описание**: Выполняет одиночный сценарий.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `scenario` (dict): Словарь, представляющий сценарий.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `dict | None`: Возвращает результат выполнения сценария или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: В случае возникновения общей ошибки во время выполнения сценария.

### `run_scenarios`

**Описание**: Выполняет несколько сценариев.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `scenarios` (list[dict] | dict): Список словарей-сценариев или один словарь-сценарий.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `list[dict] | dict | None`: Возвращает список результатов выполнения сценариев или результат выполнения одного сценария, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: В случае возникновения общей ошибки во время выполнения сценариев.

### `run_scenario_file`

**Описание**: Выполняет сценарий из файла.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `file_path` (str): Путь к файлу сценария.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `list[dict] | dict | None`: Возвращает результат выполнения сценария из файла или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл по указанному пути не найден.
- `Exception`: В случае возникновения общей ошибки во время выполнения сценария из файла.

### `run_scenario_files`

**Описание**: Выполняет сценарии из нескольких файлов.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `file_paths` (list[str] | str): Список путей к файлам сценариев или один путь к файлу сценария.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `list[list[dict] | dict] | list[dict] | dict | None`: Возвращает список результатов выполнения сценариев из файлов или результат выполнения сценария из одного файла, или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если один из файлов по указанному пути не найден.
- `Exception`: В случае возникновения общей ошибки во время выполнения сценариев из файлов.

### `execute_PrestaShop_insert`

**Описание**: Выполняет вставку данных в PrestaShop.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `data` (dict): Данные для вставки в PrestaShop.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `dict | None`: Возвращает результат вставки данных в PrestaShop или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: В случае возникновения общей ошибки во время вставки данных в PrestaShop.

### `execute_PrestaShop_insert_async`

**Описание**: Асинхронно выполняет вставку данных в PrestaShop.

**Параметры**:
- `supplier` (Supplier): Объект поставщика.
- `data` (dict): Данные для вставки в PrestaShop.
- `**kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `Awaitable[dict | None]`: Возвращает объект awaitable, который вернет результат вставки данных в PrestaShop или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: В случае возникновения общей ошибки во время асинхронной вставки данных в PrestaShop.