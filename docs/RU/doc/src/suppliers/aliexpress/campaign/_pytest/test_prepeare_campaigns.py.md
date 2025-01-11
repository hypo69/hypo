# Модуль `test_prepeare_campaigns.py`

## Обзор

Этот модуль содержит набор тестов для функций, связанных с подготовкой кампаний AliExpress, включая обновление категорий и обработку кампаний.

## Содержание

1.  [Фикстуры](#Фикстуры)
2.  [Функции](#Функции)
    *   [`test_update_category_success`](#test_update_category_success)
    *   [`test_update_category_failure`](#test_update_category_failure)
    *   [`test_process_campaign_category_success`](#test_process_campaign_category_success)
    *   [`test_process_campaign_category_failure`](#test_process_campaign_category_failure)
    *    [`test_process_campaign`](#test_process_campaign)
    *   [`test_main`](#test_main)

## Фикстуры

### `mock_j_loads`
  
**Описание**:  Фикстура, которая мокирует функцию `j_loads` из модуля `src.utils.jjson`.

### `mock_j_dumps`

**Описание**: Фикстура, которая мокирует функцию `j_dumps` из модуля `src.utils.jjson`.

### `mock_logger`

**Описание**: Фикстура, которая мокирует объект `logger` из модуля `src.logger`.

### `mock_get_directory_names`

**Описание**: Фикстура, которая мокирует функцию `get_directory_names` из модуля `src.utils`.

### `mock_ali_promo_campaign`

**Описание**: Фикстура, которая мокирует класс `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign`.

## Функции

### `test_update_category_success`

**Описание**: Тестирует успешное обновление категории.

**Параметры**:

*   `mock_j_loads` (MagicMock): Мок функции `j_loads`.
*   `mock_j_dumps` (MagicMock): Мок функции `j_dumps`.
*   `mock_logger` (MagicMock): Мок объекта `logger`.

**Возвращает**:
- `None`

### `test_update_category_failure`

**Описание**: Тестирует ситуацию, когда обновление категории завершается с ошибкой.

**Параметры**:

*   `mock_j_loads` (MagicMock): Мок функции `j_loads`.
*   `mock_j_dumps` (MagicMock): Мок функции `j_dumps`.
*   `mock_logger` (MagicMock): Мок объекта `logger`.

**Возвращает**:
- `None`

### `test_process_campaign_category_success`

**Описание**: Тестирует успешную обработку категории кампании.

**Параметры**:

*   `mock_ali_promo_campaign` (MagicMock): Мок класса `AliPromoCampaign`.
*   `mock_logger` (MagicMock): Мок объекта `logger`.

**Возвращает**:
- `None`

### `test_process_campaign_category_failure`

**Описание**: Тестирует ситуацию, когда обработка категории кампании завершается с ошибкой.

**Параметры**:

*   `mock_ali_promo_campaign` (MagicMock): Мок класса `AliPromoCampaign`.
*   `mock_logger` (MagicMock): Мок объекта `logger`.

**Возвращает**:
- `None`

### `test_process_campaign`

**Описание**: Тестирует функцию обработки кампании.

**Параметры**:

*   `mock_get_directory_names` (MagicMock): Мок функции `get_directory_names`.
*   `mock_logger` (MagicMock): Мок объекта `logger`.

**Возвращает**:
- `None`

### `test_main`

**Описание**: Тестирует функцию `main` .

**Параметры**:

*   `mock_get_directory_names` (MagicMock): Мок функции `get_directory_names`.

**Возвращает**:
- `None`