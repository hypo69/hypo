# Модуль `test_alipromo_campaign`

## Обзор

Модуль содержит набор тестов для проверки функциональности класса `AliPromoCampaign`, используемого для управления рекламными кампаниями на AliExpress. Тесты охватывают различные аспекты, включая инициализацию кампании, обработку продуктов, создание пространств имен и сохранение данных.

## Оглавление

1. [Фикстуры](#Фикстуры)
2. [Тесты](#Тесты)
    - [`test_initialize_campaign`](#test_initialize_campaign)
    - [`test_get_category_products_no_json_files`](#test_get_category_products_no_json_files)
    - [`test_get_category_products_with_json_files`](#test_get_category_products_with_json_files)
    - [`test_create_product_namespace`](#test_create_product_namespace)
    - [`test_create_category_namespace`](#test_create_category_namespace)
    - [`test_create_campaign_namespace`](#test_create_campaign_namespace)
    - [`test_prepare_products`](#test_prepare_products)
    - [`test_fetch_product_data`](#test_fetch_product_data)
    - [`test_save_product`](#test_save_product)
    - [`test_list_campaign_products`](#test_list_campaign_products)

## Фикстуры

### `campaign`

**Описание**: Фикстура для создания экземпляра `AliPromoCampaign` для использования в тестах.

## Тесты

### `test_initialize_campaign`

**Описание**: Проверяет, правильно ли метод `initialize_campaign` инициализирует данные кампании.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_get_category_products_no_json_files`

**Описание**: Проверяет метод `get_category_products`, когда отсутствуют JSON-файлы продуктов.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_get_category_products_with_json_files`

**Описание**: Проверяет метод `get_category_products`, когда JSON-файлы продуктов присутствуют.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_create_product_namespace`

**Описание**: Проверяет, правильно ли метод `create_product_namespace` создает пространство имен продукта.

**Параметры**:
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_create_category_namespace`

**Описание**: Проверяет, правильно ли метод `create_category_namespace` создает пространство имен категории.

**Параметры**:
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_create_campaign_namespace`

**Описание**: Проверяет, правильно ли метод `create_campaign_namespace` создает пространство имен кампании.

**Параметры**:
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_prepare_products`

**Описание**: Проверяет, вызывает ли метод `prepare_products` метод `process_affiliate_products`.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_fetch_product_data`

**Описание**: Проверяет, правильно ли метод `fetch_product_data` извлекает данные о продуктах.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_save_product`

**Описание**: Проверяет, правильно ли метод `save_product` сохраняет данные о продукте.

**Параметры**:
- `mocker`: Фикстура `mocker` для имитации вызовов функций.
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.

### `test_list_campaign_products`

**Описание**: Проверяет, правильно ли метод `list_campaign_products` составляет список названий продуктов кампании.

**Параметры**:
- `campaign`: Фикстура `campaign`, представляющая экземпляр `AliPromoCampaign`.