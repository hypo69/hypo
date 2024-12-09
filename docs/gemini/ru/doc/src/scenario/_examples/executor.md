# Модуль `executor`

## Обзор

Данный модуль предоставляет функции для управления сценариями, работы с файлами сценариев, обработкой данных продуктов и взаимодействием с API PrestaShop.  Примеры демонстрируют использование функций для выполнения сценариев, обработки файлов сценариев, работы с данными продуктов и взаимодействия с API PrestaShop.

## Оглавление

* [Модуль `executor`](#модуль-executor)
* [Функции](#функции)
    * [`run_scenario_files`](#run_scenario_files)
    * [`run_scenario_file`](#run_scenario_file)
    * [`run_scenarios`](#run_scenarios)
    * [`run_scenario`](#run_scenario)
    * [`insert_grabbed_data`](#insert_grabbed_data)
    * [`execute_PrestaShop_insert`](#execute_prestashop_insert)
    * [`execute_PrestaShop_insert_async`](#execute_prestashop_insert_async)
    * [`add_coupon`](#add_coupon)
* [Примеры использования](#примеры-использования)
    * [Example 1: `run_scenario_files`](#example-1-run_scenario_files)
    * [Example 2: `run_scenario_file`](#example-2-run_scenario_file)
    * [Example 3: `run_scenario`](#example-3-run_scenario)
    * [Example 4: `insert_grabbed_data`](#example-4-insert_grabbed_data)
    * [Example 5: `add_coupon`](#example-5-add_coupon)
    * [Example 6: `execute_PrestaShop_insert_async`](#example-6-execute_prestashop_insert_async)
    * [Example 7: `execute_PrestaShop_insert`](#example-7-execute_prestashop_insert)


## Функции

### `run_scenario_files`

**Описание**: Выполняет список файлов сценариев.

**Параметры**:
- `supplier`: Экземпляр класса поставщика (например, `MockSupplier`). Необходим для доступа к файлам сценариев и другим ресурсам.
- `scenario_files` (list[Path]): Список путей к файлам сценариев.

**Возвращает**:
- `bool`: `True`, если все сценарии выполнены успешно, иначе `False`.

**Вызывает исключения**:
- Любые исключения, возникающие при работе с файлами сценариев или их выполнении.


### `run_scenario_file`

**Описание**: Выполняет один файл сценария.

**Параметры**:
- `supplier`: Экземпляр класса поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Вызывает исключения**:
- Любые исключения, возникающие при работе с файлом сценария или его выполнении.


### `run_scenarios`

**Описание**:  (Описание функции `run_scenarios` отсутствует в примере кода, поэтому его заполнить нечем).


### `run_scenario`

**Описание**: Выполняет один сценарий.

**Параметры**:
- `supplier`: Экземпляр класса поставщика.
- `scenario` (dict): Словарь, представляющий сценарий.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Вызывает исключения**:
- Любые исключения, возникающие при работе со сценарием или его выполнении.


### `insert_grabbed_data`

**Описание**: Вставляет данные о продукте в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Объект, содержащий данные о продукте.

**Возвращает**:
- Ничего не возвращает (None).

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с API PrestaShop.


### `execute_PrestaShop_insert`

**Описание**: Синхронно выполняет вставку данных продукта в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Объект, содержащий данные о продукте.

**Возвращает**:
- `bool`: `True`, если вставка выполнена успешно, иначе `False`.

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с PrestaShop API.


### `execute_PrestaShop_insert_async`

**Описание**: Асинхронно выполняет вставку данных продукта в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Объект, содержащий данные о продукте.

**Возвращает**:
- Ничего не возвращает (None).

**Вызывает исключения**:
- Любые исключения, возникающие при асинхронном взаимодействии с PrestaShop API.


### `add_coupon`

**Описание**: Добавляет купон в PrestaShop.

**Параметры**:
- `credentials` (dict): Словарь с данными для аутентификации.
- `reference` (str): Ссылка на продукт.
- `coupon_code` (str): Код купона.
- `start_date` (str): Дата начала действия купона (в формате YYYY-MM-DD).
- `end_date` (str): Дата окончания действия купона (в формате YYYY-MM-DD).

**Возвращает**:
- Ничего не возвращает (None).

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с PrestaShop API.


## Примеры использования

### Example 1: `run_scenario_files`

```
# Пример вызова run_scenario_files
supplier = MockSupplier()
scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
result = run_scenario_files(supplier, scenario_files)
if result:
    print("Все сценарии выполнены успешно.")
else:
    print("Некоторые сценарии не были выполнены.")
```

### Example 2: `run_scenario_file`

```
# Пример вызова run_scenario_file
supplier = MockSupplier()
scenario_file = Path('scenarios/scenario1.json')
result = run_scenario_file(supplier, scenario_file)
if result:
    print("Файл сценария выполнен успешно.")
else:
    print("Ошибка выполнения файла сценария.")
```

(Другие примеры аналогичным образом описываются, опираясь на информацию из примера Python)