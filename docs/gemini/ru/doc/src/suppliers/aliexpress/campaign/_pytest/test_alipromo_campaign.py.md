# Модуль тестирования AliPromoCampaign

## Обзор

Этот модуль содержит набор тестов для класса `AliPromoCampaign`, который используется для управления рекламными кампаниями AliExpress. Тесты охватывают различные аспекты функциональности класса, такие как инициализация кампании, получение продуктов категории, создание пространства имен продуктов, подготовка продуктов, получение данных о продуктах и сохранение продуктов.

## Подробнее

Этот модуль использует библиотеку `pytest` для организации и выполнения тестов. Он также использует модуль `mocker` для имитации зависимостей и упрощения тестирования.

## Содержание

- [Классы](#классы)
  - [campaign](#campaign)
- [Функции](#функции)
  - [test_initialize_campaign](#test_initialize_campaign)
  - [test_get_category_products_no_json_files](#test_get_category_products_no_json_files)
  - [test_get_category_products_with_json_files](#test_get_category_products_with_json_files)
  - [test_create_product_namespace](#test_create_product_namespace)
  - [test_create_category_namespace](#test_create_category_namespace)
  - [test_create_campaign_namespace](#test_create_campaign_namespace)
  - [test_prepare_products](#test_prepare_products)
  - [test_fetch_product_data](#test_fetch_product_data)
  - [test_save_product](#test_save_product)
  - [test_list_campaign_products](#test_list_campaign_products)

## Классы

### `campaign`

**Описание**: Fixture для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Принцип работы**:
Создает экземпляр класса `AliPromoCampaign` с предопределенными параметрами `campaign_name`, `category_name`, `language` и `currency`. Этот экземпляр затем используется в различных тестах для проверки функциональности класса `AliPromoCampaign`.

**Методы**:
- Нет

**Параметры**:
- Нет

**Примеры**:
```python
@pytest.fixture
def campaign():
    """Fixture for creating a campaign instance."""
    return AliPromoCampaign(campaign_name, category_name, language, currency)
```

## Функции

### `test_initialize_campaign`

```python
def test_initialize_campaign(mocker, campaign):
    """Test the initialize_campaign method."""
    ...
```

**Назначение**: Тестирует метод `initialize_campaign` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция подготавливает моковые данные JSON, представляющие структуру данных кампании.
2. С помощью `mocker.patch` имитируется функция `j_loads_ns` из модуля `src.utils.jjson`, чтобы она возвращала моковые данные. Это необходимо для изоляции теста от реального чтения файлов и для контроля над входными данными.
3. Вызывается метод `initialize_campaign` объекта `campaign` (экземпляр класса `AliPromoCampaign`). Этот метод должен использовать моковые данные, чтобы инициализировать состояние кампании.
4. Проверяется, что атрибуты объекта `campaign.campaign` были правильно инициализированы на основе моковых данных.

**Примеры**:

Пример вызова функции:
```python
test_initialize_campaign(mocker, campaign)
```

### `test_get_category_products_no_json_files`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    ...
```

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда отсутствуют JSON-файлы.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция имитирует отсутствие JSON-файлов, используя `mocker.patch` для замены функции `get_filenames` из модуля `src.utils.file`. Мокированная функция возвращает пустой список, что означает отсутствие файлов.
2. Также имитируется функция `fetch_product_data` из класса `AliPromoCampaign`, чтобы избежать реального запроса данных. Мокированная функция также возвращает пустой список.
3. Вызывается метод `get_category_products` объекта `campaign` с параметром `force=True`. Это гарантирует, что метод попытается получить продукты, даже если нет файлов.
4. Проверяется, что метод `get_category_products` возвращает пустой список, что ожидаемо, так как отсутствуют JSON-файлы и мокированная функция `fetch_product_data` также возвращает пустой список.

**Примеры**:

Пример вызова функции:
```python
test_get_category_products_no_json_files(mocker, campaign)
```

### `test_get_category_products_with_json_files`

```python
def test_get_category_products_with_json_files(mocker, campaign):
    """Test get_category_products method when JSON files are present."""
    ...
```

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда JSON-файлы присутствуют.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция имитирует наличие JSON-файлов, используя `mocker.patch` для замены функции `get_filenames` из модуля `src.utils.file`. Мокированная функция возвращает список с именем файла `"product_123.json"`.
2. Также имитируется функция `j_loads_ns` из модуля `src.utils.jjson`, чтобы она возвращала моковые данные продукта.
3. Вызывается метод `get_category_products` объекта `campaign`.
4. Проверяется, что метод `get_category_products` возвращает список с одним элементом, и что этот элемент имеет атрибуты `product_id` и `product_title` с ожидаемыми значениями.

**Примеры**:

Пример вызова функции:
```python
test_get_category_products_with_json_files(mocker, campaign)
```

### `test_create_product_namespace`

```python
def test_create_product_namespace(campaign):
    """Test create_product_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_product_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция подготавливает словарь `product_data` с данными продукта.
2. Вызывается метод `create_product_namespace` объекта `campaign` с этими данными.
3. Проверяется, что метод возвращает объект с атрибутами `product_id` и `product_title` с ожидаемыми значениями.

**Примеры**:

Пример вызова функции:
```python
test_create_product_namespace(campaign)
```

### `test_create_category_namespace`

```python
def test_create_category_namespace(campaign):
    """Test create_category_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_category_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция подготавливает словарь `category_data` с данными категории.
2. Вызывается метод `create_category_namespace` объекта `campaign` с этими данными.
3. Проверяется, что метод возвращает объект с атрибутами `name` и `tags` с ожидаемыми значениями.

**Примеры**:

Пример вызова функции:
```python
test_create_category_namespace(campaign)
```

### `test_create_campaign_namespace`

```python
def test_create_campaign_namespace(campaign):
    """Test create_campaign_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_campaign_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция подготавливает словарь `campaign_data` с данными кампании.
2. Вызывается метод `create_campaign_namespace` объекта `campaign` с этими данными.
3. Проверяется, что метод возвращает объект с атрибутами `name` и `title` с ожидаемыми значениями.

**Примеры**:

Пример вызова функции:
```python
test_create_campaign_namespace(campaign)
```

### `test_prepare_products`

```python
def test_prepare_products(mocker, campaign):
    """Test prepare_products method."""
    ...
```

**Назначение**: Тестирует метод `prepare_products` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Имитируется метод `get_prepared_products`, чтобы вернуть пустой список.
2. Имитируется метод `read_text_file`, чтобы вернуть строку `"source_data"`.
3. Имитируется метод `get_filenames`, чтобы вернуть список с одним файлом `"source.html"`.
4. Имитируется метод `process_affiliate_products`.
5. Вызывается метод `prepare_products`.
6. Проверяется, что метод `process_affiliate_products` был вызван один раз.

**Примеры**:

Пример вызова функции:
```python
test_prepare_products(mocker, campaign)
```

### `test_fetch_product_data`

```python
def test_fetch_product_data(mocker, campaign):
    """Test fetch_product_data method."""
    ...
```

**Назначение**: Тестирует метод `fetch_product_data` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Определяется список `product_ids` с идентификаторами продуктов.
2. Создается список `mock_products` с моковыми объектами продуктов.
3. Имитируется метод `process_affiliate_products`, чтобы вернуть список `mock_products`.
4. Вызывается метод `fetch_product_data` с `product_ids`.
5. Проверяется, что возвращенный список содержит два элемента и что атрибуты `product_id` элементов соответствуют ожидаемым значениям.

**Примеры**:

Пример вызова функции:
```python
test_fetch_product_data(mocker, campaign)
```

### `test_save_product`

```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
    ...
```

**Назначение**: Тестирует метод `save_product` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Объект `mocker` для имитации зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Функция создает объект `SimpleNamespace` с данными продукта.
2. Мокирует функцию `j_dumps` из модуля `src.utils.jjson`, чтобы она возвращала строку `'{}'`. Это нужно для того, чтобы избежать реальной сериализации данных в JSON.
3. Мокирует метод `write_text` класса `pathlib.Path`. Это нужно для того, чтобы избежать реальной записи данных в файл.
4. Вызывает метод `save_product` объекта `campaign` с моковым продуктом.
5. Проверяет, что метод `write_text` был вызван один раз с ожидаемыми параметрами.

**Примеры**:

Пример вызова функции:
```python
test_save_product(mocker, campaign)
```

### `test_list_campaign_products`

```python
def test_list_campaign_products(campaign):
    """Test list_campaign_products method."""
    ...
```

**Назначение**: Тестирует метод `list_campaign_products` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Создаются два объекта `SimpleNamespace`, представляющие продукты.
2. Атрибуту `products` объекта `campaign.category` присваивается список, содержащий эти два продукта.
3. Вызывается метод `list_campaign_products`.
4. Проверяется, что возвращенный список содержит заголовки продуктов `"Product 1"` и `"Product 2"`.

**Примеры**:

Пример вызова функции:
```python
test_list_campaign_products(campaign)