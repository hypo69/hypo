# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py`

## Обзор

Данный модуль содержит тесты для функций модуля `prepare_campaigns`, отвечающего за подготовку кампаний на AliExpress. Тесты покрывают различные сценарии, включая успешную и неуспешную обработку категорий и кампаний.

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

**Описание**: Тестирует функцию `update_category` при успешной обработке.

**Параметры**:
- `mock_j_loads`: Мок объекта `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок объекта `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`


### `test_update_category_failure`

**Описание**: Тестирует функцию `update_category` при возникновении ошибки.

**Параметры**:
- `mock_j_loads`: Мок объекта `j_loads` из модуля `src.utils.jjson`.
- `mock_j_dumps`: Мок объекта `j_dumps` из модуля `src.utils.jjson`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`


### `test_process_campaign_category_success`

**Описание**: Асинхронный тест для функции `process_campaign_category` при успешном выполнении.

**Параметры**:
- `mock_ali_promo_campaign`: Мок класса `AliPromoCampaign`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.


**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`


### `test_process_campaign_category_failure`

**Описание**: Асинхронный тест для функции `process_campaign_category` при возникновении ошибки.

**Параметры**:
- `mock_ali_promo_campaign`: Мок класса `AliPromoCampaign`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`


### `test_process_campaign`

**Описание**: Тестирует функцию `process_campaign`.

**Параметры**:
- `mock_get_directory_names`: Мок функции `get_directory_names` из модуля `src.utils`.
- `mock_logger`: Мок объекта `logger` из модуля `src.logger`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`



### `test_main`

**Описание**: Асинхронный тест для функции `main`.

**Параметры**:
- `mock_get_directory_names`: Мок функции `get_directory_names` из модуля `src.utils`.


**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`