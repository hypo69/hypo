# Модуль executor

## Обзор

Этот модуль предоставляет функции для выполнения сценариев, обработки файлов сценариев, работы с продуктами и взаимодействия с API PrestaShop.  Примеры демонстрируют запуск списка файлов сценариев, одного файла сценария, одного сценария, работу со страницей продукта и добавление купонов.

## Оглавление

* [Функции](#функции)
    * [`run_scenario_files`](#run_scenario_files)
    * [`run_scenario_file`](#run_scenario_file)
    * [`run_scenario`](#run_scenario)
    * [`insert_grabbed_data`](#insert_grabbed_data)
    * [`execute_PrestaShop_insert`](#execute_prestashop_insert)
    * [`execute_PrestaShop_insert_async`](#execute_prestashop_insert_async)
    * [`add_coupon`](#add_coupon)

## Функции

### `run_scenario_files`

**Описание**: Запускает список файлов сценариев и выполняет их последовательно.

**Параметры**:
* `supplier` (объект): Экземпляр класса, предоставляющий данные о поставщике и сценариях.
* `scenario_files` (список): Список путей к файлам сценариев.

**Возвращает**:
* `bool`: `True`, если все сценарии были успешно выполнены, иначе `False`.

**Вызывает исключения**:
* `FileNotFoundError`: Если какой-либо из файлов сценариев не найден.
* `Exception`: В случае возникновения других ошибок во время выполнения сценариев.


### `run_scenario_file`

**Описание**: Запускает один файл сценария.

**Параметры**:
* `supplier` (объект): Экземпляр класса, предоставляющий данные о поставщике и сценариях.
* `scenario_file` (объект `Path`): Путь к файлу сценария.

**Возвращает**:
* `bool`: `True`, если сценарий был успешно выполнен, иначе `False`.

**Вызывает исключения**:
* `FileNotFoundError`: Если файл сценария не найден.
* `Exception`: В случае возникновения других ошибок во время выполнения сценария.


### `run_scenario`

**Описание**: Выполняет один сценарий.

**Параметры**:
* `supplier` (объект): Экземпляр класса, предоставляющий данные о поставщике и сценариях.
* `scenario` (словарь): Словарь, содержащий данные сценария.

**Возвращает**:
* `bool`: `True`, если сценарий был успешно выполнен, иначе `False`.

**Вызывает исключения**:
* `Exception`: В случае возникновения ошибок во время выполнения сценария.


### `insert_grabbed_data`

**Описание**: Вставляет данные о продукте в PrestaShop.

**Параметры**:
* `product_fields` (объект `ProductFields`): Объект, содержащий данные о продукте.

**Возвращает**:
* `None`

**Вызывает исключения**:
* `Exception`: В случае возникновения ошибок во время вставки данных.


### `execute_PrestaShop_insert`

**Описание**: Синхронно выполняет вставку данных о продукте в PrestaShop.

**Параметры**:
* `product_fields` (объект `ProductFields`): Объект, содержащий данные о продукте.

**Возвращает**:
* `bool`: `True`, если данные были успешно вставлены, иначе `False`.

**Вызывает исключения**:
* `Exception`: В случае возникновения ошибок во время вставки данных.


### `execute_PrestaShop_insert_async`

**Описание**: Асинхронно выполняет вставку данных о продукте в PrestaShop.

**Параметры**:
* `product_fields` (объект `ProductFields`): Объект, содержащий данные о продукте.

**Возвращает**:
* `None`

**Вызывает исключения**:
* `Exception`: В случае возникновения ошибок во время асинхронной вставки данных.


### `add_coupon`

**Описание**: Добавляет купон в базу данных PrestaShop.

**Параметры**:
* `credentials` (словарь): Данные для аутентификации API PrestaShop.
* `reference` (строка): Идентификатор продукта.
* `coupon_code` (строка): Код купона.
* `start_date` (строка): Дата начала действия купона (YYYY-MM-DD).
* `end_date` (строка): Дата окончания действия купона (YYYY-MM-DD).

**Возвращает**:
* `None`

**Вызывает исключения**:
* `Exception`: В случае возникновения ошибок во время добавления купона.