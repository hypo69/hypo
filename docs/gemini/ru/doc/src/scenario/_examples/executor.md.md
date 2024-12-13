# Примеры использования модуля `executor`

## Обзор

Этот файл содержит примеры использования функций, предоставленных в модуле `executor`. Примеры показывают, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с API PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
  - [MockSupplier](#mocksupplier)
  - [MockRelatedModules](#mockrelatedmodules)
  - [MockDriver](#mockdriver)
- [Функции](#функции)
  - [example_run_scenario_files](#example_run_scenario_files)
  - [example_run_scenario_file](#example_run_scenario_file)
  - [example_run_scenario](#example_run_scenario)
  - [example_insert_grabbed_data](#example_insert_grabbed_data)
  - [example_add_coupon](#example_add_coupon)
  - [example_execute_PrestaShop_insert_async](#example_execute_prestashop_insert_async)
  - [example_execute_PrestaShop_insert](#example_execute_prestashop_insert)
- [Пояснение к примерам](#пояснение-к-примерам)
  
## Классы

### `MockSupplier`

**Описание**:
Мок-класс, имитирующий поставщика для тестирования функций модуля `executor`.

**Методы**:
- `__init__`: Инициализирует мок-объект поставщика с необходимыми атрибутами.

**Атрибуты**:
- `supplier_abs_path` (Path): Абсолютный путь к каталогу сценариев.
- `scenario_files` (List[Path]): Список файлов сценариев.
- `current_scenario` (Optional[dict]): Текущий сценарий (по умолчанию `None`).
- `supplier_settings` (dict): Настройки поставщика, включая список выполненных сценариев.
- `related_modules` (MockRelatedModules): Мок-объект связанных модулей.
- `driver` (MockDriver): Мок-объект драйвера.

### `MockRelatedModules`

**Описание**:
Мок-класс, имитирующий связанные модули для тестирования функций модуля `executor`.

**Методы**:
- `get_list_products_in_category(s)`: Возвращает список URL продуктов в заданной категории.
- `grab_product_page(s)`: Возвращает объект `ProductFields` с моковыми данными о продукте.
- `grab_page(s)`: Асинхронная версия `grab_product_page(s)`.

### `MockDriver`

**Описание**:
Мок-класс, имитирующий драйвер для тестирования функций модуля `executor`.

**Методы**:
- `get_url(url)`: Возвращает `True`, имитируя загрузку страницы по URL.

## Функции

### `example_run_scenario_files`

**Описание**:
Пример запуска списка файлов сценариев.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщения в консоль о результате выполнения.

### `example_run_scenario_file`

**Описание**:
Пример запуска одного файла сценария.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщения в консоль о результате выполнения.

### `example_run_scenario`

**Описание**:
Пример запуска одного сценария.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщения в консоль о результате выполнения.

### `example_insert_grabbed_data`

**Описание**:
Пример вставки данных о продукте в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщение в консоль о результате выполнения.

### `example_add_coupon`

**Описание**:
Пример добавления купона в базу данных PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщение в консоль о результате выполнения.

### `example_execute_PrestaShop_insert_async`

**Описание**:
Пример асинхронной вставки данных о продукте в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщение в консоль о результате выполнения.

### `example_execute_PrestaShop_insert`

**Описание**:
Пример синхронной вставки данных о продукте в PrestaShop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция выводит сообщение в консоль о результате выполнения.

## Пояснение к примерам

1. **Example 1: `run_scenario_files`**
   Запускает список файлов сценариев и выполняет их один за другим.

2. **Example 2: `run_scenario_file`**
   Запускает один файл сценария.

3. **Example 3: `run_scenario`**
   Выполняет один сценарий.

4. **Example 4: `insert_grabbed_data`**
   Вставляет данные о продукте в PrestaShop.

5. **Example 5: `add_coupon`**
   Добавляет купон в базу данных PrestaShop.

6. **Example 6: `execute_PrestaShop_insert_async`**
   Асинхронно выполняет вставку данных о продукте в PrestaShop.

7. **Example 7: `execute_PrestaShop_insert`**
   Синхронно выполняет вставку данных о продукте в PrestaShop.

Эти примеры помогут вам понять, как можно использовать функции модуля `executor` для различных задач в вашем проекте.