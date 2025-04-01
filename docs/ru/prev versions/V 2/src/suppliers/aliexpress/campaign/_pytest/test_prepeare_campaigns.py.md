# Модуль `test_prepeare_campaigns`

## Обзор

Модуль содержит тесты для функций, связанных с подготовкой кампаний AliExpress, включая обновление категорий, обработку кампаний по категориям и общую обработку кампаний. Тесты используют `pytest` и `unittest.mock` для изоляции и проверки функций.

## Содержание

1. [Фикстуры](#Фикстуры)
2. [Тесты функций](#Тесты-функций)
   - [`test_update_category_success`](#test_update_category_success)
   - [`test_update_category_failure`](#test_update_category_failure)
   - [`test_process_campaign_category_success`](#test_process_campaign_category_success)
   - [`test_process_campaign_category_failure`](#test_process_campaign_category_failure)
   - [`test_process_campaign`](#test_process_campaign)
   - [`test_main`](#test_main)

## Фикстуры

### `mock_j_loads`

**Описание**: Фикстура, которая подменяет функцию `src.utils.jjson.j_loads` для мокирования загрузки JSON.

### `mock_j_dumps`

**Описание**: Фикстура, которая подменяет функцию `src.utils.jjson.j_dumps` для мокирования сохранения JSON.

### `mock_logger`

**Описание**: Фикстура, которая подменяет объект логгера `src.logger.logger` для проверки вызовов логирования.

### `mock_get_directory_names`

**Описание**: Фикстура, которая подменяет функцию `src.utils.get_directory_names` для мокирования получения имен директорий.

### `mock_ali_promo_campaign`

**Описание**: Фикстура, которая подменяет класс `src.suppliers.aliexpress.campaign.AliPromoCampaign` для мокирования его поведения.

## Тесты функций

### `test_update_category_success`

**Описание**: Тестирует успешное обновление категории.

**Параметры**:

- `mock_j_loads`: (MagicMock) Мокированная функция `j_loads`.
- `mock_j_dumps`: (MagicMock) Мокированная функция `j_dumps`.
- `mock_logger`: (MagicMock) Мокированный объект логгера.

**Проверяет**:

- Возвращает `True` при успешном обновлении.
- Функция `j_dumps` вызывается один раз с правильными аргументами.
- Функция логирования ошибок не вызывается.

### `test_update_category_failure`

**Описание**: Тестирует неудачное обновление категории из-за исключения при загрузке JSON.

**Параметры**:

- `mock_j_loads`: (MagicMock) Мокированная функция `j_loads`.
- `mock_j_dumps`: (MagicMock) Мокированная функция `j_dumps`.
- `mock_logger`: (MagicMock) Мокированный объект логгера.

**Проверяет**:

- Возвращает `False` при неудачном обновлении.
- Функция `j_dumps` не вызывается.
- Функция логирования ошибок вызывается один раз.

### `test_process_campaign_category_success`

**Описание**: Тестирует успешную обработку категории кампании.

**Параметры**:

- `mock_ali_promo_campaign`: (MagicMock) Мокированный класс `AliPromoCampaign`.
- `mock_logger`: (MagicMock) Мокированный объект логгера.

**Проверяет**:

- Возвращает не `None` при успешной обработке.
- Функция логирования ошибок не вызывается.

### `test_process_campaign_category_failure`

**Описание**: Тестирует неудачную обработку категории кампании из-за исключения.

**Параметры**:

- `mock_ali_promo_campaign`: (MagicMock) Мокированный класс `AliPromoCampaign`.
- `mock_logger`: (MagicMock) Мокированный объект логгера.

**Проверяет**:

- Возвращает `None` при неудачной обработке.
- Функция логирования ошибок вызывается один раз.

### `test_process_campaign`

**Описание**: Тестирует обработку кампании для нескольких категорий.

**Параметры**:

- `mock_get_directory_names`: (MagicMock) Мокированная функция `get_directory_names`.
- `mock_logger`: (MagicMock) Мокированный объект логгера.

**Проверяет**:

- Возвращает список кортежей, где каждый кортеж содержит имя категории и результат обработки.
- Количество результатов соответствует количеству категорий.
- Функция логирования предупреждений не вызывается.

### `test_main`

**Описание**: Тестирует основную функцию обработки кампании.

**Параметры**:

- `mock_get_directory_names`: (MagicMock) Мокированная функция `get_directory_names`.

**Проверяет**:

- Функция `get_directory_names` вызывается один раз.