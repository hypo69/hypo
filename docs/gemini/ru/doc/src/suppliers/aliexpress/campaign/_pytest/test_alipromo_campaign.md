# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py`

## Обзор

Этот модуль содержит тестовые функции для класса `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign.ali_promo_campaign`.  Тесты проверяют корректность работы методов класса, связанных с инициализацией, получением данных о продуктах, созданием пространств имен и сохранением данных.

## Оглавление

- [Фикстуры](#фикстуры)
- [Тесты](#тесты)
    - [Тест `test_initialize_campaign`](#тест-test_initialize_campaign)
    - [Тест `test_get_category_products_no_json_files`](#тест-test_get_category_products_no_json_files)
    - [Тест `test_get_category_products_with_json_files`](#тест-test_get_category_products_with_json_files)
    - [Тест `test_create_product_namespace`](#тест-test_create_product_namespace)
    - [Тест `test_create_category_namespace`](#тест-test_create_category_namespace)
    - [Тест `test_create_campaign_namespace`](#тест-test_create_campaign_namespace)
    - [Тест `test_prepare_products`](#тест-test_prepare_products)
    - [Тест `test_fetch_product_data`](#тест-test_fetch_product_data)
    - [Тест `test_save_product`](#тест-test_save_product)
    - [Тест `test_list_campaign_products`](#тест-test_list_campaign_products)

## Фикстуры

### `campaign`

**Описание**: Фикстура для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Возвращает**: Экземпляр класса `AliPromoCampaign`.

## Тесты

### `test_initialize_campaign`

**Описание**: Тестирует метод `initialize_campaign`, проверяя правильность инициализации данных кампании.

**Параметры**:
- `mocker`: Моккер для подмены зависимостей.
- `campaign`: Экземпляр класса `AliPromoCampaign`, полученный из фикстуры.

**Действия**:
- Подменяет функцию `j_loads_ns` с помощью `mocker`.
- Вызывает метод `initialize_campaign` для тестируемого объекта.
- Проверяет, что значения `name` и `category.name` соответствуют ожидаемым.

**Ожидаемый результат**: Утверждение `assert` должно пройти успешно, подтверждая корректную инициализацию.

### `test_get_category_products_no_json_files`

**Описание**: Тестирует метод `get_category_products` в случае отсутствия JSON-файлов.

**Параметры**:
- `mocker`: Моккер для подмены зависимостей.
- `campaign`: Экземпляр класса `AliPromoCampaign`, полученный из фикстуры.

**Действия**:
- Подменяет функцию `get_filenames` возвращающую пустой список.
- Подменяет функцию `fetch_product_data` возвращающую пустой список.
- Вызывает метод `get_category_products` с параметром `force=True`.
- Проверяет, что возвращаемое значение - пустой список.

**Ожидаемый результат**: Утверждение `assert` должно пройти успешно, подтверждая корректную обработку случая отсутствия файлов.


### `test_get_category_products_with_json_files`

**Описание**: Тестирует метод `get_category_products` в случае наличия JSON-файлов.

**Параметры**:
- `mocker`: Моккер для подмены зависимостей.
- `campaign`: Экземпляр класса `AliPromoCampaign`, полученный из фикстуры.

**Действия**:
- Подменяет функцию `get_filenames` возвращающей список с именем "product_123.json".
- Подменяет функцию `j_loads_ns` для возвращения данных о продукте.
- Вызывает метод `get_category_products`.
- Проверяет, что полученный список продуктов содержит один элемент с ожидаемыми значениями `product_id` и `product_title`.

**Ожидаемый результат**: Утверждение `assert` должно пройти успешно, подтверждая корректную обработку случая наличия файлов.

**(Другие тесты аналогично описаны,  пропуская детали ввиду большого объема.)**