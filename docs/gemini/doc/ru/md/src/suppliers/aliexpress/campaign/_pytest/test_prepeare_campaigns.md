# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py`

## Обзор

Этот модуль содержит тесты для функций, связанных с подготовкой кампаний на AliExpress.  Он использует фреймворк `pytest` для проверки корректности функций `update_category`, `process_campaign_category`, `process_campaign` и `main`.  Тесты покрывают успешные и неудачные сценарии, а также взаимодействие с внешними библиотеками и системами.


## Функции

### `test_update_category_success`

**Описание**: Тестирует функцию `update_category` в случае успешного обновления категории.

**Параметры**:

- `mock_j_loads`: Заглушка для `src.utils.jjson.j_loads`.
- `mock_j_dumps`: Заглушка для `src.utils.jjson.j_dumps`.
- `mock_logger`: Заглушка для `src.logger.logger`.
- `mock_json_path` (Path): Путь к файлу JSON с категорией.
- `mock_category` (SimpleNamespace): Объект с данными категории.


**Возвращает**:

- `True`: Если обновление прошло успешно.


**Вызывает исключения**:

- Не вызывает исключения в случае успеха.


### `test_update_category_failure`

**Описание**: Тестирует функцию `update_category` в случае ошибки при обновлении категории.

**Параметры**:

- `mock_j_loads`: Заглушка для `src.utils.jjson.j_loads`.
- `mock_j_dumps`: Заглушка для `src.utils.jjson.j_dumps`.
- `mock_logger`: Заглушка для `src.logger.logger`.
- `mock_json_path` (Path): Путь к файлу JSON с категорией.
- `mock_category` (SimpleNamespace): Объект с данными категории.


**Возвращает**:

- `False`: Если обновление не удалось.


**Вызывает исключения**:

- `Exception("Error")`: Исключение, симулирующее ошибку.


### `test_process_campaign_category_success`

**Описание**: Тестирует функцию `process_campaign_category` в случае успешной обработки категории кампании.

**Параметры**:

- `mock_ali_promo_campaign`: Заглушка для `src.suppliers.aliexpress.campaign.AliPromoCampaign`.
- `mock_logger`: Заглушка для `src.logger.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_category_name` (str): Название категории.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.


**Возвращает**:

- Не `None`: Успешное выполнение.


**Вызывает исключения**:

- Не вызывает исключения в случае успеха.


### `test_process_campaign_category_failure`

**Описание**: Тестирует функцию `process_campaign_category` в случае ошибки при обработке категории кампании.

**Параметры**:

- `mock_ali_promo_campaign`: Заглушка для `src.suppliers.aliexpress.campaign.AliPromoCampaign`.
- `mock_logger`: Заглушка для `src.logger.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_category_name` (str): Название категории.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.


**Возвращает**:

- `None`: Ошибка при выполнении.


**Вызывает исключения**:

- `Exception("Error")`: Исключение, симулирующее ошибку.


### `test_process_campaign`

**Описание**: Тестирует функцию `process_campaign`, проверяя обработку списка категорий.

**Параметры**:

- `mock_get_directory_names`: Заглушка для `src.utils.get_directory_names`.
- `mock_logger`: Заглушка для `src.logger.logger`.
- `mock_campaign_name` (str): Название кампании.
- `mock_categories` (list): Список категорий.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.
- `mock_force` (bool): Флаг принудительного выполнения.


**Возвращает**:

- Список кортежей (категория, результат): Успешные результаты обработки каждой категории.


**Вызывает исключения**:

- Не вызывает исключения в случае успеха.


### `test_main`

**Описание**: Тестирует функцию `main`, проверяя запуск обработки кампании.

**Параметры**:

- `mock_get_directory_names`: Заглушка для `src.utils.get_directory_names`.
- `mock_campaign_name` (str): Название кампании.
- `mock_categories` (list): Список категорий.
- `mock_language` (str): Язык.
- `mock_currency` (str): Валюта.
- `mock_force` (bool): Флаг принудительного выполнения.


**Возвращает**:

- Не возвращает значение.  Вызывает `process_campaign`.


**Вызывает исключения**:

- Не вызывает исключения в случае успеха.


## Фикстуры

Описание фикстур (заглушек) для тестирования.

### `mock_j_loads`, `mock_j_dumps`, `mock_logger`, `mock_get_directory_names`, `mock_ali_promo_campaign`


```