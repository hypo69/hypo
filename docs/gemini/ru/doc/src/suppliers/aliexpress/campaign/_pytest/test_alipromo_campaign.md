# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py`

## Обзор

Данный модуль содержит тесты для класса `AliPromoCampaign`, отвечающего за обработку и подготовку данных для кампаний на AliExpress. Тесты покрывают различные сценарии работы класса, включая инициализацию, получение данных о продуктах, создание и сохранение данных, а также вывод списка продуктов кампании.

## Оглавление

- [Модуль `test_alipromo_campaign`](#модуль-test_alipromo_campaign)
- [Фикстуры](#фикстуры)
- [Тесты](#тесты)
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

**Описание**: Фикстура для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Возвращает**: Объект `AliPromoCampaign`.

## Тесты

### `test_initialize_campaign`

**Описание**: Тестирует метод `initialize_campaign`, проверяя корректность инициализации данных кампании.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `j_loads_ns`: Мок для загрузки данных из JSON.

**Ассерты**:
- Проверяет, что атрибуты `campaign.name` и `campaign.category.test_category.name` соответствуют ожидаемым значениям.

### `test_get_category_products_no_json_files`

**Описание**: Тестирует метод `get_category_products` в случае отсутствия JSON-файлов.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `get_filenames`: Мок для получения списка файлов. Возвращает пустой список.
- `AliPromoCampaign.fetch_product_data`: Мок для получения данных продуктов. Возвращает пустой список.

**Ассерты**:
- Проверяет, что возвращаемый список продуктов пуст.


### `test_get_category_products_with_json_files`

**Описание**: Тестирует метод `get_category_products` в случае наличия JSON-файлов.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `get_filenames`: Мок для получения списка файлов. Возвращает список `["product_123.json"]`.
- `j_loads_ns`: Мок для загрузки данных из JSON. Возвращает объект `SimpleNamespace` с данными о продукте.

**Ассерты**:
- Проверяет, что возвращаемый список продуктов содержит один элемент с корректными данными.


### `test_create_product_namespace`, `test_create_category_namespace`, `test_create_campaign_namespace`

**Описание**: Тесты для методов создания пространств имен для продуктов, категорий и кампаний. Проверяют корректность создания пространств имен с заданными данными.

**Параметры**:
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Ассерты**:
- Проверяют, что созданные пространства имен содержат ожидаемые значения.


### `test_prepare_products`

**Описание**: Тестирует метод `prepare_products`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `get_prepared_products`: Мок для получения подготовленных продуктов. Возвращает пустой список.
- `read_text_file`: Мок для чтения файла. Возвращает "source_data".
- `get_filenames`: Мок для получения списка файлов. Возвращает `["source.html"]`.
- `AliPromoCampaign.process_affiliate_products`: Мок для вызова метода обработки продуктов.

**Ассерты**:
- Проверяет, что метод `process_affiliate_products` был вызван один раз.


### `test_fetch_product_data`

**Описание**: Тестирует метод `fetch_product_data`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `AliPromoCampaign.process_affiliate_products`: Мок, возвращающий список продуктов.

**Ассерты**:
- Проверяет, что возвращаемый список продуктов содержит ожидаемые элементы.


### `test_save_product`

**Описание**: Тестирует метод `save_product`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Вызывает моки**:
- `j_dumps`: Мок для сериализации данных в JSON.
- `Path.write_text`: Мок для записи данных в файл.

**Ассерты**:
- Проверяет, что метод `Path.write_text` был вызван один раз с корректными аргументами.

### `test_list_campaign_products`

**Описание**: Тестирует метод `list_campaign_products`.

**Параметры**:
- `campaign`: Объект `AliPromoCampaign`, полученный из фикстуры.

**Ассерты**:
- Проверяет, что возвращаемый список названий продуктов соответствует ожидаемым значениям.