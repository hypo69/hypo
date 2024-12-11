# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py`

## Обзор

Данный модуль содержит тесты для функций, связанных с подготовкой рекламных кампаний на AliExpress. Тесты покрывают функции `update_category`, `process_campaign_category`, `process_campaign` и `main`.

## Оглавление

- [Функции](#функции)
    - [`test_update_category_success`](#test_update_category_success)
    - [`test_update_category_failure`](#test_update_category_failure)
    - [`test_process_campaign_category_success`](#test_process_campaign_category_success)
    - [`test_process_campaign_category_failure`](#test_process_campaign_category_failure)
    - [`test_process_campaign`](#test_process_campaign)
    - [`test_main`](#test_main)


## Функции

### `test_update_category_success`

**Описание**: Тест проверяет успешное обновление категории.

**Параметры**:
- `mock_j_loads`: Мок для функции `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок для функции `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок для логгера.


**Возвращает**:
- `None`

**Вызывает исключения**:
-  Никаких исключений не ожидается.

### `test_update_category_failure`

**Описание**: Тест проверяет обработку ошибки при обновлении категории.

**Параметры**:
- `mock_j_loads`: Мок для функции `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок для функции `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок для логгера.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Ожидается обработка исключения `Exception`.


### `test_process_campaign_category_success`

**Описание**: Тест проверяет успешную обработку категории кампании.

**Параметры**:
- `mock_ali_promo_campaign`: Мок для класса `AliPromoCampaign`.
- `mock_logger`: Мок для логгера.


**Возвращает**:
- `None`

**Вызывает исключения**:
-  Никаких исключений не ожидается.


### `test_process_campaign_category_failure`

**Описание**: Тест проверяет обработку ошибки при обработке категории кампании.

**Параметры**:
- `mock_ali_promo_campaign`: Мок для класса `AliPromoCampaign`.
- `mock_logger`: Мок для логгера.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Ожидается обработка исключения `Exception`.


### `test_process_campaign`

**Описание**: Тест проверяет обработку кампании.

**Параметры**:
- `mock_get_directory_names`: Мок для функции `get_directory_names`.
- `mock_logger`: Мок для логгера.


**Возвращает**:
- `None`

**Вызывает исключения**:
- Никаких исключений не ожидается.


### `test_main`

**Описание**: Тест проверяет главную функцию для обработки кампаний.

**Параметры**:
- `mock_get_directory_names`: Мок для функции `get_directory_names`.


**Возвращает**:
- `None`

**Вызывает исключения**:
- Никаких исключений не ожидается.