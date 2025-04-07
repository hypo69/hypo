# Модуль тестирования AliPromoCampaign

## Обзор

Этот модуль содержит набор тестов для проверки функциональности класса `AliPromoCampaign`, который используется для управления рекламными кампаниями AliExpress. Он включает тесты для инициализации кампании, получения продуктов категории, создания пространства имен продуктов, подготовки продуктов и сохранения данных о продуктах.

## Подробнее

Модуль использует библиотеку `pytest` для организации и запуска тестов. Он также использует `mocker` для имитации внешних зависимостей и упрощения тестирования отдельных компонентов. Тесты охватывают различные сценарии, включая случаи, когда JSON-файлы отсутствуют или присутствуют, и проверяют правильность обработки данных и вызова методов.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламными кампаниями AliExpress.

**Принцип работы**:
Класс `AliPromoCampaign` предоставляет методы для инициализации кампании, получения продуктов из категорий, создания пространств имен для продуктов, категорий и кампаний, подготовки продуктов и сохранения данных о продуктах. Он использует различные утилиты, такие как `j_dumps`, `j_loads_ns`, `save_text_file` и `read_text_file`, для работы с данными и файлами.

## Функции

### `campaign`

```python
@pytest.fixture
def campaign():
    """Fixture for creating a campaign instance."""
    return AliPromoCampaign(campaign_name, category_name, language, currency)
```

**Назначение**: Фикстура для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `AliPromoCampaign`: Экземпляр класса `AliPromoCampaign`, инициализированный с тестовыми данными.

**Как работает функция**:

1. Создает экземпляр класса `AliPromoCampaign` с заданными параметрами: `campaign_name`, `category_name`, `language` и `currency`.
2. Возвращает созданный экземпляр.

```
Создание экземпляра AliPromoCampaign
│
└───> Возврат экземпляра
```

**Примеры**:

```python
# Фикстура campaign автоматически внедряется в тестовые функции
def test_example(campaign):
    assert isinstance(campaign, AliPromoCampaign)
```

### `test_initialize_campaign`

```python
def test_initialize_campaign(mocker, campaign):
    """Test the initialize_campaign method."""
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

**Назначение**: Тестирует метод `initialize_campaign` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет моковые данные JSON для имитации загрузки данных кампании.
2. Использует `mocker.patch` для имитации функции `j_loads_ns` и возвращает моковые данные.
3. Вызывает метод `initialize_campaign` на экземпляре `campaign`.
4. Проверяет, что данные кампании были правильно инициализированы, сравнивая значения атрибутов с ожидаемыми значениями.

```
Определение моковых данных
│
└───> Имитация функции j_loads_ns
│
└───> Вызов метода initialize_campaign
│
└───> Проверка инициализации данных кампании
```

**Примеры**:

```python
def test_initialize_campaign(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_get_category_products_no_json_files`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    mocker.patch("src.utils.file.get_filenames", return_value=[])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data", return_value=[])

    products = campaign.get_category_products(force=True)
    assert products == []
```

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в случае, когда отсутствуют JSON-файлы.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Использует `mocker.patch` для имитации функции `get_filenames` и возвращает пустой список, имитируя отсутствие JSON-файлов.
2. Использует `mocker.patch` для имитации метода `fetch_product_data` и возвращает пустой список.
3. Вызывает метод `get_category_products` на экземпляре `campaign` с параметром `force=True`.
4. Проверяет, что возвращаемый список продуктов пуст.

```
Имитация отсутствия JSON-файлов
│
└───> Имитация метода fetch_product_data
│
└───> Вызов метода get_category_products
│
└───> Проверка, что список продуктов пуст
```

**Примеры**:

```python
def test_get_category_products_no_json_files(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_get_category_products_with_json_files`

```python
def test_get_category_products_with_json_files(mocker, campaign):
    """Test get_category_products method when JSON files are present."""
    mock_product_data = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.file.get_filenames", return_value=["product_123.json"])
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=mock_product_data)

    products = campaign.get_category_products()
    assert len(products) == 1
    assert products[0].product_id == "123"
    assert products[0].product_title == "Test Product"
```

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в случае, когда JSON-файлы присутствуют.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет моковые данные продукта для имитации загрузки данных из JSON-файла.
2. Использует `mocker.patch` для имитации функции `get_filenames` и возвращает список с именем фиктивного JSON-файла.
3. Использует `mocker.patch` для имитации функции `j_loads_ns` и возвращает моковые данные продукта.
4. Вызывает метод `get_category_products` на экземпляре `campaign`.
5. Проверяет, что возвращаемый список продуктов содержит один элемент и что данные продукта соответствуют ожидаемым значениям.

```
Определение моковых данных продукта
│
└───> Имитация функции get_filenames
│
└───> Имитация функции j_loads_ns
│
└───> Вызов метода get_category_products
│
└───> Проверка возвращаемого списка продуктов и данных продукта
```

**Примеры**:

```python
def test_get_category_products_with_json_files(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_create_product_namespace`

```python
def test_create_product_namespace(campaign):
    """Test create_product_namespace method."""
    product_data = {
        "product_id": "123",
        "product_title": "Test Product"
    }
    product = campaign.create_product_namespace(**product_data)
    assert product.product_id == "123"
    assert product.product_title == "Test Product"
```

**Назначение**: Тестирует метод `create_product_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет словарь с данными продукта.
2. Вызывает метод `create_product_namespace` на экземпляре `campaign` с данными продукта.
3. Проверяет, что возвращаемый объект имеет атрибуты `product_id` и `product_title` с ожидаемыми значениями.

```
Определение данных продукта
│
└───> Вызов метода create_product_namespace
│
└───> Проверка атрибутов возвращаемого объекта
```

**Примеры**:

```python
def test_create_product_namespace(campaign):
    # (см. код выше)
    pass
```

### `test_create_category_namespace`

```python
def test_create_category_namespace(campaign):
    """Test create_category_namespace method."""
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

**Назначение**: Тестирует метод `create_category_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет словарь с данными категории.
2. Вызывает метод `create_category_namespace` на экземпляре `campaign` с данными категории.
3. Проверяет, что возвращаемый объект имеет атрибуты `name` и `tags` с ожидаемыми значениями.

```
Определение данных категории
│
└───> Вызов метода create_category_namespace
│
└───> Проверка атрибутов возвращаемого объекта
```

**Примеры**:

```python
def test_create_category_namespace(campaign):
    # (см. код выше)
    pass
```

### `test_create_campaign_namespace`

```python
def test_create_campaign_namespace(campaign):
    """Test create_campaign_namespace method."""
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

**Назначение**: Тестирует метод `create_campaign_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет словарь с данными кампании.
2. Вызывает метод `create_campaign_namespace` на экземпляре `campaign` с данными кампании.
3. Проверяет, что возвращаемый объект имеет атрибуты `name` и `title` с ожидаемыми значениями.

```
Определение данных кампании
│
└───> Вызов метода create_campaign_namespace
│
└───> Проверка атрибутов возвращаемого объекта
```

**Примеры**:

```python
def test_create_campaign_namespace(campaign):
    # (см. код выше)
    pass
```

### `test_prepare_products`

```python
def test_prepare_products(mocker, campaign):
    """Test prepare_products method."""
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products", return_value=[])
    mocker.patch("src.utils.file.read_text_file", return_value="source_data")
    mocker.patch("src.utils.file.get_filenames", return_value=["source.html"])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products")

    campaign.prepare_products()
    campaign.process_affiliate_products.assert_called_once()
```

**Назначение**: Тестирует метод `prepare_products` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Использует `mocker.patch` для имитации метода `get_prepared_products` и возвращает пустой список.
2. Использует `mocker.patch` для имитации функции `read_text_file` и возвращает фиктивные данные.
3. Использует `mocker.patch` для имитации функции `get_filenames` и возвращает список с именем фиктивного HTML-файла.
4. Использует `mocker.patch` для имитации метода `process_affiliate_products`.
5. Вызывает метод `prepare_products` на экземпляре `campaign`.
6. Проверяет, что метод `process_affiliate_products` был вызван один раз.

```
Имитация метода get_prepared_products
│
└───> Имитация функции read_text_file
│
└───> Имитация функции get_filenames
│
└───> Имитация метода process_affiliate_products
│
└───> Вызов метода prepare_products
│
└───> Проверка вызова метода process_affiliate_products
```

**Примеры**:

```python
def test_prepare_products(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_fetch_product_data`

```python
def test_fetch_product_data(mocker, campaign):
    """Test fetch_product_data method."""
    product_ids = ["123", "456"]
    mock_products = [SimpleNamespace(product_id="123"), SimpleNamespace(product_id="456")]
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products", return_value=mock_products)

    products = campaign.fetch_product_data(product_ids)
    assert len(products) == 2
    assert products[0].product_id == "123"
    assert products[1].product_id == "456"
```

**Назначение**: Тестирует метод `fetch_product_data` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет список идентификаторов продуктов.
2. Определяет список фиктивных продуктов с соответствующими идентификаторами.
3. Использует `mocker.patch` для имитации метода `process_affiliate_products` и возвращает список фиктивных продуктов.
4. Вызывает метод `fetch_product_data` на экземпляре `campaign` с списком идентификаторов продуктов.
5. Проверяет, что возвращаемый список продуктов содержит два элемента и что идентификаторы продуктов соответствуют ожидаемым значениям.

```
Определение списка идентификаторов продуктов
│
└───> Определение списка фиктивных продуктов
│
└───> Имитация метода process_affiliate_products
│
└───> Вызов метода fetch_product_data
│
└───> Проверка возвращаемого списка продуктов и идентификаторов продуктов
```

**Примеры**:

```python
def test_fetch_product_data(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_save_product`

```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
    product = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.jjson.j_dumps", return_value="{}")
    mocker.patch("pathlib.Path.write_text")

    campaign.save_product(product)
    Path.write_text.assert_called_once_with("{}", encoding='utf-8')
```

**Назначение**: Тестирует метод `save_product` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Фикстура `pytest-mock` для имитации объектов.
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Определяет фиктивный продукт с атрибутами `product_id` и `product_title`.
2. Использует `mocker.patch` для имитации функции `j_dumps` и возвращает пустую строку JSON.
3. Использует `mocker.patch` для имитации метода `write_text` класса `pathlib.Path`.
4. Вызывает метод `save_product` на экземпляре `campaign` с фиктивным продуктом.
5. Проверяет, что метод `write_text` был вызван один раз с ожидаемыми аргументами (пустая строка JSON и кодировка 'utf-8').

```
Определение фиктивного продукта
│
└───> Имитация функции j_dumps
│
└───> Имитация метода write_text
│
└───> Вызов метода save_product
│
└───> Проверка вызова метода write_text
```

**Примеры**:

```python
def test_save_product(mocker, campaign):
    # (см. код выше)
    pass
```

### `test_list_campaign_products`

```python
def test_list_campaign_products(campaign):
    """Test list_campaign_products method."""
    product1 = SimpleNamespace(product_title="Product 1")
    product2 = SimpleNamespace(product_title="Product 2")
    campaign.category.products = [product1, product2]

    product_titles = campaign.list_campaign_products()
    assert product_titles == ["Product 1", "Product 2"]
```

**Назначение**: Тестирует метод `list_campaign_products` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Фикстура `campaign`, создающая экземпляр `AliPromoCampaign`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1. Создает два фиктивных продукта с атрибутами `product_title`.
2. Присваивает список фиктивных продуктов атрибуту `products` объекта `campaign.category`.
3. Вызывает метод `list_campaign_products` на экземпляре `campaign`.
4. Проверяет, что возвращаемый список заголовков продуктов соответствует ожидаемому списку.

```
Создание фиктивных продуктов
│
└───> Присвоение списка продуктов атрибуту campaign.category.products
│
└───> Вызов метода list_campaign_products
│
└───> Проверка возвращаемого списка заголовков продуктов
```

**Примеры**:

```python
def test_list_campaign_products(campaign):
    # (см. код выше)
    pass