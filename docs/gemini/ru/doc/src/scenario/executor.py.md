# Модуль `src.scenario.executor`

## Обзор

Модуль `src.scenario.executor` предназначен для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продуктах и их последующей вставки в PrestaShop.

## Содержание

- [Функции](#Функции)
  - [`dump_journal`](#dump_journal)
  - [`run_scenario_files`](#run_scenario_files)
  - [`run_scenario_file`](#run_scenario_file)
  - [`run_scenarios`](#run_scenarios)
  - [`run_scenario`](#run_scenario)
  - [`insert_grabbed_data`](#insert_grabbed_data)
  - [`execute_PrestaShop_insert_async`](#execute_PrestaShop_insert_async)
  - [`execute_PrestaShop_insert`](#execute_PrestaShop_insert)

<br>

## Функции

### `dump_journal`

**Описание**: Сохраняет данные журнала в JSON-файл.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика.
- `journal` (dict): Словарь, содержащий данные журнала.

**Возвращает**:
- `None`

<br>

### `run_scenario_files`

**Описание**: Выполняет список файлов сценариев.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика.
- `scenario_files_list` (List[Path] | Path): Список путей к файлам сценариев или путь к одному файлу.

**Возвращает**:
- `bool`: True, если все сценарии были выполнены успешно, False в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является списком или объектом `Path`.

<br>

### `run_scenario_file`

**Описание**: Загружает и выполняет сценарии из файла.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: True, если сценарий был выполнен успешно, False в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл сценария не найден.
- `json.JSONDecodeError`: Если не удалось декодировать JSON из файла сценария.

<br>

### `run_scenarios`

**Описание**: Выполняет список сценариев (НЕ ФАЙЛОВ).

**Параметры**:
- `s` (Supplier): Экземпляр поставщика.
- `scenarios` (List[dict] | dict, optional): Список сценариев или один сценарий в виде словаря. По умолчанию `None`.
- `_journal` (dict, optional): Журнал.

**Возвращает**:
- `List | dict | False`: Результат выполнения сценариев в виде списка или словаря, в зависимости от типа входных данных, или `False` в случае ошибки.

<br>

### `run_scenario`

**Описание**: Выполняет полученный сценарий.

**Параметры**:
- `supplier` (Supplier): Экземпляр поставщика.
- `scenario` (dict): Словарь, содержащий детали сценария.
- `scenario_name` (str): Название сценария.
- `_journal` (dict, optional): Журнал.

**Возвращает**:
- `List | dict | False`: Результат выполнения сценария.

<br>

### `insert_grabbed_data`

**Описание**: Вставляет полученные данные о продукте в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `None`

<br>

### `execute_PrestaShop_insert_async`

**Описание**: Асинхронно вставляет данные о продукте в PrestaShop.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (str, optional): Код купона. По умолчанию `None`.
- `start_date` (str, optional): Дата начала акции. По умолчанию `None`.
- `end_date` (str, optional): Дата окончания акции. По умолчанию `None`.

**Возвращает**:
- `None`

<br>

### `execute_PrestaShop_insert`

**Описание**: Вставляет данные о продукте в PrestaShop.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (str, optional): Код купона. По умолчанию `None`.
- `start_date` (str, optional): Дата начала акции. По умолчанию `None`.
- `end_date` (str, optional): Дата окончания акции. По умолчанию `None`.

**Возвращает**:
- `bool`: True, если вставка прошла успешно, False в противном случае.

**Вызывает исключения**:
- `Exception`: Если вставка данных в PrestaShop не удалась.