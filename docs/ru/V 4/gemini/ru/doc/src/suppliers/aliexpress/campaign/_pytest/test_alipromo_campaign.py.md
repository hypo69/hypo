# Модуль `test_alipromo_campaign`

## Обзор

Модуль `test_alipromo_campaign.py` содержит набор тестов для класса `AliPromoCampaign`, который используется для управления рекламными кампаниями в AliExpress. Тесты охватывают различные аспекты функциональности класса, такие как инициализация кампании, получение данных о продуктах, создание пространств имен и сохранение данных.
Расположение файла в проекте: `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py` указывает, что это модуль тестирования, специфичный для подсистемы управления рекламными кампаниями AliExpress. Тесты проверяют корректность работы класса `AliPromoCampaign` и связанных с ним функций.

## Подробней

Этот модуль содержит набор тестов, предназначенных для проверки функциональности класса `AliPromoCampaign`. Он использует библиотеку `pytest` для организации и выполнения тестов. Каждый тест проверяет определенный аспект работы класса, например, правильность инициализации кампании, обработку данных о продуктах, создание пространств имен и сохранение информации.

## Классы

### `campaign`

**Описание**: Fixture для создания экземпляра `AliPromoCampaign` для использования в тестах.

## Функции

### `test_initialize_campaign`

```python
def test_initialize_campaign(mocker, campaign):
    """Test the initialize_campaign method."""
    ...
```

**Описание**: Тестирует метод `initialize_campaign`.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_initialize_campaign` тестирует метод `initialize_campaign` класса `AliPromoCampaign`. Она использует `mocker` для подмены метода `j_loads_ns` и возвращает фиктивные данные JSON. Затем функция вызывает метод `initialize_campaign` и проверяет, что данные кампании инициализированы правильно.

### `test_get_category_products_no_json_files`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    ...
```

**Описание**: Тестирует метод `get_category_products` когда нет JSON файлов.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_get_category_products_no_json_files` тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда отсутствуют JSON-файлы. Она подменяет методы `get_filenames` и `fetch_product_data` с помощью `mocker` и проверяет, что метод возвращает пустой список.

### `test_get_category_products_with_json_files`

```python
def test_get_category_products_with_json_files(mocker, campaign):
    """Test get_category_products method when JSON files are present."""
    ...
```

**Описание**: Тестирует метод `get_category_products` когда есть JSON файлы.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_get_category_products_with_json_files` тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда JSON-файлы присутствуют. Она подменяет методы `get_filenames` и `j_loads_ns` с помощью `mocker` и проверяет, что метод возвращает список продуктов с ожидаемыми данными.

### `test_create_product_namespace`

```python
def test_create_product_namespace(campaign):
    """Test create_product_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_product_namespace`.

**Параметры**:
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_create_product_namespace` тестирует метод `create_product_namespace` класса `AliPromoCampaign`. Она создает фиктивные данные продукта и проверяет, что метод возвращает объект пространства имен с правильными данными.

### `test_create_category_namespace`

```python
def test_create_category_namespace(campaign):
    """Test create_category_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_category_namespace`.

**Параметры**:
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_create_category_namespace` тестирует метод `create_category_namespace` класса `AliPromoCampaign`. Она создает фиктивные данные категории и проверяет, что метод возвращает объект пространства имен с правильными данными.

### `test_create_campaign_namespace`

```python
def test_create_campaign_namespace(campaign):
    """Test create_campaign_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_campaign_namespace`.

**Параметры**:
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_create_campaign_namespace` тестирует метод `create_campaign_namespace` класса `AliPromoCampaign`. Она создает фиктивные данные кампании и проверяет, что метод возвращает объект пространства имен с правильными данными.

### `test_prepare_products`

```python
def test_prepare_products(mocker, campaign):
    """Test prepare_products method."""
    ...
```

**Описание**: Тестирует метод `prepare_products`.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_prepare_products` тестирует метод `prepare_products` класса `AliPromoCampaign`. Она подменяет методы `get_prepared_products`, `read_text_file`, `get_filenames` и `process_affiliate_products` с помощью `mocker` и проверяет, что метод `process_affiliate_products` вызывается один раз.

### `test_fetch_product_data`

```python
def test_fetch_product_data(mocker, campaign):
    """Test fetch_product_data method."""
    ...
```

**Описание**: Тестирует метод `fetch_product_data`.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_fetch_product_data` тестирует метод `fetch_product_data` класса `AliPromoCampaign`. Она подменяет метод `process_affiliate_products` с помощью `mocker` и проверяет, что метод возвращает список продуктов с ожидаемыми данными.

### `test_save_product`

```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
    ...
```

**Описание**: Тестирует метод `save_product`.

**Параметры**:
- `mocker`: Объект `mocker` для подмены (mocking) зависимостей.
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_save_product` тестирует метод `save_product` класса `AliPromoCampaign`. Она подменяет методы `j_dumps` и `Path.write_text` с помощью `mocker` и проверяет, что метод `Path.write_text` вызывается один раз с ожидаемыми аргументами.

### `test_list_campaign_products`

```python
def test_list_campaign_products(campaign):
    """Test list_campaign_products method."""
    ...
```

**Описание**: Тестирует метод `list_campaign_products`.

**Параметры**:
- `campaign`: Fixture `campaign` для получения экземпляра `AliPromoCampaign`.

**Как работает функция**:
Функция `test_list_campaign_products` тестирует метод `list_campaign_products` класса `AliPromoCampaign`. Она создает фиктивные продукты и добавляет их в категорию кампании. Затем функция вызывает метод `list_campaign_products` и проверяет, что метод возвращает список заголовков продуктов.