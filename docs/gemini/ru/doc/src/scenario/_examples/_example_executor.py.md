# Модуль `_example_executor.py`

## Обзор

Файл `_example_executor.py` содержит примеры использования функций из модуля `executor` (`src.scenario.executor`). Эти примеры демонстрируют, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с API PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [`MockSupplier`](#mocksupplier)
    - [`MockRelatedModules`](#mockrelatedmodules)
    - [`MockDriver`](#mockdriver)
- [Функции](#функции)
    - [`example_run_scenario_files`](#example_run_scenario_files)
    - [`example_run_scenario_file`](#example_run_scenario_file)
    - [`example_run_scenario`](#example_run_scenario)
    - [`example_insert_grabbed_data`](#example_insert_grabbed_data)
    - [`example_add_coupon`](#example_add_coupon)
    - [`example_execute_PrestaShop_insert_async`](#example_execute_prestashop_insert_async)
    - [`example_execute_PrestaShop_insert`](#example_execute_prestashop_insert)

## Классы

### `MockSupplier`

**Описание**:
Класс-заглушка для имитации поставщика. Содержит атрибуты, необходимые для запуска сценариев.

**Методы**:
- `__init__`: Инициализация объекта `MockSupplier` с атрибутами `supplier_abs_path`, `scenario_files`, `current_scenario`, `supplier_settings`, `related_modules` и `driver`.
    - `supplier_abs_path` (Path): Путь к каталогу со сценариями.
    - `scenario_files` (list): Список файлов сценариев.
    - `current_scenario` (None): Текущий выполняемый сценарий.
    - `supplier_settings` (dict): Настройки поставщика.
    - `related_modules` (MockRelatedModules): Модули, связанные с поставщиком.
    - `driver` (MockDriver): Драйвер для взаимодействия с веб-страницами.

### `MockRelatedModules`

**Описание**:
Класс-заглушка для имитации связанных модулей. Содержит методы для получения списка продуктов и извлечения данных со страниц.

**Методы**:
- `get_list_products_in_category(s: str) -> list`: Возвращает список URL продуктов в категории.
    - `s` (str): URL категории.
    - **Возвращает**: Список URL продуктов.
- `grab_product_page(s: str) -> ProductFields`: Возвращает данные продукта со страницы.
    - `s` (str): URL страницы продукта.
    - **Возвращает**: Объект `ProductFields`, содержащий данные о продукте.
- `grab_page(s: str) -> ProductFields`: Асинхронная версия метода `grab_product_page`.
     - `s` (str): URL страницы продукта.
     - **Возвращает**: Объект `ProductFields`, содержащий данные о продукте.

### `MockDriver`

**Описание**:
Класс-заглушка для имитации драйвера веб-браузера.

**Методы**:
- `get_url(url: str) -> bool`: Возвращает `True`, имитируя успешный переход по URL.
    - `url` (str): URL для перехода.
    - **Возвращает**: `True`, если переход успешен.

## Функции

### `example_run_scenario_files`

**Описание**:
Пример запуска списка файлов сценариев.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_run_scenario_file`

**Описание**:
Пример запуска отдельного файла сценария.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_run_scenario`

**Описание**:
Пример запуска единичного сценария.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_insert_grabbed_data`

**Описание**:
Пример вставки полученных данных продукта в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_add_coupon`

**Описание**:
Пример добавления купона с использованием API PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_execute_PrestaShop_insert_async`

**Описание**:
Пример асинхронной вставки данных продукта в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.

### `example_execute_PrestaShop_insert`

**Описание**:
Пример синхронной вставки данных продукта в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения, вывод в консоль.