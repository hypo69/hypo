# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py`

## Обзор

Данный модуль содержит тесты для функций модуля `prepare_campaigns`, отвечающего за подготовку кампаний на AliExpress. Тесты покрывают различные сценарии, включая успешное и неуспешное выполнение задач, а также обработку исключений.

## Оглавление

- [Функции](#функции)
    - [`test_update_category_success`](#test_update_category_success)
    - [`test_update_category_failure`](#test_update_category_failure)
    - [`test_process_campaign_category_success`](#test_process_campaign_category_success)
    - [`test_process_campaign_category_failure`](#test_process_campaign_category_failure)
    - [`test_process_campaign`](#test_process_campaign)
    - [`test_main`](#test_main)
- [Фикстуры](#фикстуры)
    - [`mock_j_loads`](#mock_j_loads)
    - [`mock_j_dumps`](#mock_j_dumps)
    - [`mock_logger`](#mock_logger)
    - [`mock_get_directory_names`](#mock_get_directory_names)
    - [`mock_ali_promo_campaign`](#mock_ali_promo_campaign)


## Функции

### `test_update_category_success`

**Описание**: Тестирует успешное обновление категории.

**Параметры**:
- `mock_j_loads`: Мок объекта `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок объекта `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.
- `mock_json_path` (Path): Путь к файлу JSON.
- `mock_category` (SimpleNamespace): Объект, представляющий категорию.

**Возвращает**:
- `True`: Возвращает `True`, если обновление прошло успешно.

**Вызывает исключения**:
-  Никаких исключений не ожидается.


### `test_update_category_failure`

**Описание**: Тестирует неуспешное обновление категории из-за ошибки.

**Параметры**:
- `mock_j_loads`: Мок объекта `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок объекта `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.
- `mock_json_path` (Path): Путь к файлу JSON.
- `mock_category` (SimpleNamespace): Объект, представляющий категорию.

**Возвращает**:
- `False`: Возвращает `False`, если обновление не удалось из-за исключения.

**Вызывает исключения**:
- `Exception("Error")`:  Мокирует исключение.


### `test_process_campaign_category_success`

**Описание**: Тестирует успешное выполнение `process_campaign_category`.

**Параметры**:
- `mock_ali_promo_campaign`: Фикстура для мокирования `AliPromoCampaign`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_category_name` (str): Название категории.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.

**Возвращает**:
- Не `None`: Функция возвращает значение, отличное от `None`, если выполнение прошло успешно.

**Вызывает исключения**:
-  Никаких исключений не ожидается.


### `test_process_campaign_category_failure`

**Описание**: Тестирует выполнение `process_campaign_category` при ошибке.

**Параметры**:
- `mock_ali_promo_campaign`: Фикстура для мокирования `AliPromoCampaign`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_category_name` (str): Название категории.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.

**Возвращает**:
- `None`: Возвращает `None`, если выполнение завершилось ошибкой.

**Вызывает исключения**:
- `Exception("Error")`: Мокирует исключение.


### `test_process_campaign`

**Описание**: Тестирует функцию `process_campaign`.

**Параметры**:
- `mock_get_directory_names`: Мок функции `get_directory_names`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_categories` (list): Список категорий.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.
- `mock_force` (bool): Флаг принудительного выполнения.


**Возвращает**:
- Список кортежей `(category_name, result)`: Функция возвращает список пар, где `category_name` - имя категории, `result` - результат обработки.

**Вызывает исключения**:
-  Никаких исключений не ожидается.



### `test_main`

**Описание**: Тестирует функцию `main`.

**Параметры**:
- `mock_get_directory_names`: Мок функции `get_directory_names`.
- `mock_campaign_name` (str): Название кампании.
- `mock_categories` (list): Список категорий.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.
- `mock_force` (bool): Флаг принудительного выполнения.


**Возвращает**:
-  Функция асинхронна и не возвращает явного значения.

**Вызывает исключения**:
-  Никаких исключений не ожидается.



## Фикстуры

### `mock_j_loads`

**Описание**: Фикстура для мокирования функции `j_loads` из `src.utils.jjson`.

### `mock_j_dumps`

**Описание**: Фикстура для мокирования функции `j_dumps` из `src.utils.jjson`.

### `mock_logger`

**Описание**: Фикстура для мокирования логгера из `src.logger`.

### `mock_get_directory_names`

**Описание**: Фикстура для мокирования функции `get_directory_names` из `src.utils`.

### `mock_ali_promo_campaign`

**Описание**: Фикстура для мокирования класса `AliPromoCampaign` из `src.suppliers.aliexpress.campaign`.