# Модуль тестирования AliPromoCampaign

## Обзор

Модуль `test_alipromo_campaign.py` содержит набор тестов для класса `AliPromoCampaign`, который используется для управления рекламными кампаниями на платформе AliExpress. Тесты охватывают различные аспекты функциональности класса, включая инициализацию кампании, получение данных о продуктах, создание пространств имен и сохранение данных.

## Подробней

Этот модуль использует библиотеку `pytest` для организации и выполнения тестов. Он проверяет правильность работы методов класса `AliPromoCampaign` в различных сценариях, включая случаи с наличием и отсутствием данных, а также с использованием мокированных объектов для изоляции тестируемого кода.

## Оглавление

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

**Как работает класс**:
Fixture `campaign` инициализирует объект `AliPromoCampaign` с предопределенными значениями для имени кампании, имени категории, языка и валюты. Этот объект затем используется в различных тестах для проверки функциональности класса `AliPromoCampaign`.

**Параметры**:
- Нет параметров.

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

**Описание**: Тестирует метод `initialize_campaign`.

**Как работает функция**:
Функция `test_initialize_campaign` проверяет, правильно ли метод `initialize_campaign` инициализирует данные кампании. Она мокирует функцию `j_loads_ns`, чтобы вернуть предопределенные данные JSON, а затем вызывает метод `initialize_campaign` объекта `campaign`. После этого функция проверяет, соответствуют ли атрибуты объекта `campaign` ожидаемым значениям.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_initialize_campaign(mocker, campaign):
    mock_json_data = {
        "name": campaign_name,
        "title": "Test Campaign",
        "language": language,
        "currency": currency,
        "category": {
            category_name: {
                "name": category_name,
                "tags": "tag1, tag2",
                "products": [],
                "products_count": 0
            }
        }
    }
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=SimpleNamespace(**mock_json_data))

    campaign.initialize_campaign()
    assert campaign.campaign.name == campaign_name
    assert campaign.campaign.category.test_category.name == category_name
```

### `test_get_category_products_no_json_files`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    ...
```

**Описание**: Тестирует метод `get_category_products`, когда нет JSON-файлов.

**Как работает функция**:
Функция `test_get_category_products_no_json_files` проверяет, как метод `get_category_products` обрабатывает ситуацию, когда отсутствуют JSON-файлы с данными о продуктах. Она мокирует функции `get_filenames` и `fetch_product_data`, чтобы вернуть пустой список, а затем вызывает метод `get_category_products` объекта `campaign`. После этого функция проверяет, что возвращаемый список продуктов пуст.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_get_category_products_no_json_files(mocker, campaign):
    mocker.patch("src.utils.file.get_filenames", return_value=[])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data", return_value=[])

    products = campaign.get_category_products(force=True)
    assert products == []
```

### `test_get_category_products_with_json_files`

```python
def test_get_category_products_with_json_files(mocker, campaign):
    """Test get_category_products method when JSON files are present."""
    ...
```

**Описание**: Тестирует метод `get_category_products`, когда JSON-файлы присутствуют.

**Как работает функция**:
Функция `test_get_category_products_with_json_files` проверяет, как метод `get_category_products` обрабатывает ситуацию, когда JSON-файлы с данными о продуктах присутствуют. Она мокирует функции `get_filenames` и `j_loads_ns`, чтобы вернуть предопределенные данные о продуктах, а затем вызывает метод `get_category_products` объекта `campaign`. После этого функция проверяет, что возвращаемый список продуктов содержит ожидаемые данные.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_get_category_products_with_json_files(mocker, campaign):
    mock_product_data = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.file.get_filenames", return_value=["product_123.json"])
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=mock_product_data)

    products = campaign.get_category_products()
    assert len(products) == 1
    assert products[0].product_id == "123"
    assert products[0].product_title == "Test Product"
```

### `test_create_product_namespace`

```python
def test_create_product_namespace(campaign):
    """Test create_product_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_product_namespace`.

**Как работает функция**:
Функция `test_create_product_namespace` проверяет, правильно ли метод `create_product_namespace` создает пространство имен продукта. Она вызывает метод `create_product_namespace` объекта `campaign` с предопределенными данными о продукте, а затем проверяет, соответствуют ли атрибуты возвращаемого объекта ожидаемым значениям.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_create_product_namespace(campaign):
    product_data = {
        "product_id": "123",
        "product_title": "Test Product"
    }
    product = campaign.create_product_namespace(**product_data)
    assert product.product_id == "123"
    assert product.product_title == "Test Product"
```

### `test_create_category_namespace`

```python
def test_create_category_namespace(campaign):
    """Test create_category_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_category_namespace`.

**Как работает функция**:
Функция `test_create_category_namespace` проверяет, правильно ли метод `create_category_namespace` создает пространство имен категории. Она вызывает метод `create_category_namespace` объекта `campaign` с предопределенными данными о категории, а затем проверяет, соответствуют ли атрибуты возвращаемого объекта ожидаемым значениям.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_create_category_namespace(campaign):
    category_data = {
        "name": category_name,
        "tags": "tag1, tag2",
        "products": [],
        "products_count": 0
    }
    category = campaign.create_category_namespace(**category_data)
    assert category.name == category_name
    assert category.tags == "tag1, tag2"
```

### `test_create_campaign_namespace`

```python
def test_create_campaign_namespace(campaign):
    """Test create_campaign_namespace method."""
    ...
```

**Описание**: Тестирует метод `create_campaign_namespace`.

**Как работает функция**:
Функция `test_create_campaign_namespace` проверяет, правильно ли метод `create_campaign_namespace` создает пространство имен кампании. Она вызывает метод `create_campaign_namespace` объекта `campaign` с предопределенными данными о кампании, а затем проверяет, соответствуют ли атрибуты возвращаемого объекта ожидаемым значениям.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_create_campaign_namespace(campaign):
    campaign_data = {
        "name": campaign_name,
        "title": "Test Campaign",
        "language": language,
        "currency": currency,
        "category": SimpleNamespace()
    }
    camp = campaign.create_campaign_namespace(**campaign_data)
    assert camp.name == campaign_name
    assert camp.title == "Test Campaign"
```

### `test_prepare_products`

```python
def test_prepare_products(mocker, campaign):
    """Test prepare_products method."""
    ...
```

**Описание**: Тестирует метод `prepare_products`.

**Как работает функция**:
Функция `test_prepare_products` проверяет, вызывает ли метод `prepare_products` метод `process_affiliate_products`. Она мокирует функции `get_prepared_products`, `read_text_file`, `get_filenames` и `process_affiliate_products`, а затем вызывает метод `prepare_products` объекта `campaign`. После этого функция проверяет, был ли вызван метод `process_affiliate_products` один раз.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_prepare_products(mocker, campaign):
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products", return_value=[])
    mocker.patch("src.utils.file.read_text_file", return_value="source_data")
    mocker.patch("src.utils.file.get_filenames", return_value=["source.html"])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products")

    campaign.prepare_products()
    campaign.process_affiliate_products.assert_called_once()
```

### `test_fetch_product_data`

```python
def test_fetch_product_data(mocker, campaign):
    """Test fetch_product_data method."""
    ...
```

**Описание**: Тестирует метод `fetch_product_data`.

**Как работает функция**:
Функция `test_fetch_product_data` проверяет, правильно ли метод `fetch_product_data` получает данные о продуктах. Она мокирует функцию `process_affiliate_products`, чтобы вернуть предопределенный список продуктов, а затем вызывает метод `fetch_product_data` объекта `campaign`. После этого функция проверяет, что возвращаемый список продуктов содержит ожидаемые данные.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_fetch_product_data(mocker, campaign):
    product_ids = ["123", "456"]
    mock_products = [SimpleNamespace(product_id="123"), SimpleNamespace(product_id="456")]
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products", return_value=mock_products)

    products = campaign.fetch_product_data(product_ids)
    assert len(products) == 2
    assert products[0].product_id == "123"
    assert products[1].product_id == "456"
```

### `test_save_product`

```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
    ...
```

**Описание**: Тестирует метод `save_product`.

**Как работает функция**:
Функция `test_save_product` проверяет, правильно ли метод `save_product` сохраняет данные о продукте. Она мокирует функции `j_dumps` и `Path.write_text`, а затем вызывает метод `save_product` объекта `campaign`. После этого функция проверяет, был ли вызван метод `Path.write_text` с ожидаемыми аргументами.

**Параметры**:
- `mocker`: Объект `pytest-mock` для мокирования зависимостей.
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_save_product(mocker, campaign):
    product = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.jjson.j_dumps", return_value="{}")
    mocker.patch("pathlib.Path.write_text")

    campaign.save_product(product)
    Path.write_text.assert_called_once_with("{}", encoding='utf-8')
```

### `test_list_campaign_products`

```python
def test_list_campaign_products(campaign):
    """Test list_campaign_products method."""
    ...
```

**Описание**: Тестирует метод `list_campaign_products`.

**Как работает функция**:
Функция `test_list_campaign_products` проверяет, правильно ли метод `list_campaign_products` составляет список названий продуктов кампании. Она создает два объекта `SimpleNamespace`, представляющих продукты, добавляет их в атрибут `products` объекта `campaign.category`, а затем вызывает метод `list_campaign_products` объекта `campaign`. После этого функция проверяет, что возвращаемый список названий продуктов соответствует ожидаемому.

**Параметры**:
- `campaign`: Fixture `campaign`, представляющая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:

```python
def test_list_campaign_products(campaign):
    product1 = SimpleNamespace(product_title="Product 1")
    product2 = SimpleNamespace(product_title="Product 2")
    campaign.category.products = [product1, product2]

    product_titles = campaign.list_campaign_products()
    assert product_titles == ["Product 1", "Product 2"]