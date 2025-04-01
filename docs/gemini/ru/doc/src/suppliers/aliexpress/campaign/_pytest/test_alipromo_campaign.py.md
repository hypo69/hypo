# Модуль для тестирования AliPromoCampaign
## Обзор

Модуль `test_alipromo_campaign.py` содержит набор тестов для проверки функциональности класса `AliPromoCampaign`, который предназначен для работы с рекламными кампаниями AliExpress. Тесты охватывают различные аспекты работы класса, включая инициализацию кампании, получение данных о продуктах, создание пространств имен и сохранение данных.
## Подробней

Модуль использует библиотеку `pytest` для организации и запуска тестов, а также библиотеки `pathlib`, `types` и модуль `src.utils.jjson` для работы с файлами и данными. Fixtures используются для создания экземпляров класса `AliPromoCampaign` и мокирования функций.
Тесты проверяют корректность работы методов класса `AliPromoCampaign` в различных сценариях, включая случаи, когда данные отсутствуют или содержат ошибки.

## Классы

### `campaign`

**Описание**: Fixture для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Принцип работы**:
Создает и возвращает экземпляр класса `AliPromoCampaign` с заданными параметрами: `campaign_name`, `category_name`, `language` и `currency`.

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
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если кампания не инициализируется правильно.

**Как работает функция**:
1. Создается мок данных JSON, представляющих структуру кампании.
2. Мокируется функция `src.utils.jjson.j_loads_ns`, которая должна возвращать мок данных JSON.
3. Вызывается метод `initialize_campaign` объекта `campaign`.
4. Проверяется, что атрибуты объекта `campaign.campaign` установлены правильно, сравнивая их со значениями из мок данных JSON.

**ASII flowchart**:
```
Создание мок данных JSON
↓
Мокирование j_loads_ns
↓
Вызов campaign.initialize_campaign()
↓
Проверка атрибутов campaign.campaign
```

**Примеры**:
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

### `test_get_category_products_no_json_files`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    ...
```

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда отсутствуют JSON-файлы.

**Параметры**:
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод возвращает непустой список продуктов.

**Как работает функция**:
1. Мокируется функция `src.utils.file.get_filenames`, чтобы она возвращала пустой список, имитируя отсутствие JSON-файлов.
2. Мокируется функция `src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data`, чтобы она возвращала пустой список.
3. Вызывается метод `get_category_products` объекта `campaign` с параметром `force=True`.
4. Проверяется, что метод возвращает пустой список.

**ASII flowchart**:
```
Мокирование get_filenames (возвращает [])
↓
Мокирование fetch_product_data (возвращает [])
↓
Вызов campaign.get_category_products(force=True)
↓
Проверка, что возвращен пустой список
```

**Примеры**:
```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
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

**Назначение**: Тестирует метод `get_category_products` класса `AliPromoCampaign` в ситуации, когда JSON-файлы присутствуют.

**Параметры**:
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод возвращает неверное количество продуктов или неверные данные о продуктах.

**Как работает функция**:
1. Создается мок данных продукта `SimpleNamespace`, представляющий данные, которые должны быть загружены из JSON-файла.
2. Мокируется функция `src.utils.file.get_filenames`, чтобы она возвращала список с именем файла продукта (`product_123.json`).
3. Мокируется функция `src.utils.jjson.j_loads_ns`, чтобы она возвращала мок данных продукта.
4. Вызывается метод `get_category_products` объекта `campaign`.
5. Проверяется, что метод возвращает список, содержащий один продукт, и что атрибуты этого продукта соответствуют мок данным продукта.

**ASII flowchart**:
```
Создание мок данных продукта
↓
Мокирование get_filenames (возвращает список с именем файла продукта)
↓
Мокирование j_loads_ns (возвращает мок данных продукта)
↓
Вызов campaign.get_category_products()
↓
Проверка, что возвращен список с одним продуктом и его атрибуты
```

**Примеры**:
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

### `test_create_product_namespace`

```python
def test_create_product_namespace(campaign):
    """Test create_product_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_product_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если атрибуты созданного пространства имен продукта не соответствуют заданным данным.

**Как работает функция**:
1. Определяются данные продукта в виде словаря.
2. Вызывается метод `create_product_namespace` объекта `campaign` с данными продукта.
3. Проверяется, что атрибуты созданного пространства имен продукта соответствуют значениям, указанным в словаре данных продукта.

**ASII flowchart**:
```
Определение данных продукта
↓
Вызов campaign.create_product_namespace(**product_data)
↓
Проверка атрибутов созданного пространства имен продукта
```

**Примеры**:
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

### `test_create_category_namespace`

```python
def test_create_category_namespace(campaign):
    """Test create_category_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_category_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если атрибуты созданного пространства имен категории не соответствуют заданным данным.

**Как работает функция**:
1. Определяются данные категории в виде словаря.
2. Вызывается метод `create_category_namespace` объекта `campaign` с данными категории.
3. Проверяется, что атрибуты созданного пространства имен категории соответствуют значениям, указанным в словаре данных категории.

**ASII flowchart**:
```
Определение данных категории
↓
Вызов campaign.create_category_namespace(**category_data)
↓
Проверка атрибутов созданного пространства имен категории
```

**Примеры**:
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

### `test_create_campaign_namespace`

```python
def test_create_campaign_namespace(campaign):
    """Test create_campaign_namespace method."""
    ...
```

**Назначение**: Тестирует метод `create_campaign_namespace` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если атрибуты созданного пространства имен кампании не соответствуют заданным данным.

**Как работает функция**:
1. Определяются данные кампании в виде словаря.
2. Вызывается метод `create_campaign_namespace` объекта `campaign` с данными кампании.
3. Проверяется, что атрибуты созданного пространства имен кампании соответствуют значениям, указанным в словаре данных кампании.

**ASII flowchart**:
```
Определение данных кампании
↓
Вызов campaign.create_campaign_namespace(**campaign_data)
↓
Проверка атрибутов созданного пространства имен кампании
```

**Примеры**:
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

### `test_prepare_products`

```python
def test_prepare_products(mocker, campaign):
    """Test prepare_products method."""
    ...
```

**Назначение**: Тестирует метод `prepare_products` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод `process_affiliate_products` не был вызван один раз.

**Как работает функция**:
1. Мокируется метод `get_prepared_products`, чтобы возвращать пустой список.
2. Мокируется функция `src.utils.file.read_text_file`, чтобы возвращать строку `source_data`.
3. Мокируется функция `src.utils.file.get_filenames`, чтобы возвращать список с именем файла `source.html`.
4. Мокируется метод `process_affiliate_products`.
5. Вызывается метод `prepare_products` объекта `campaign`.
6. Проверяется, что метод `process_affiliate_products` был вызван один раз.

**ASII flowchart**:
```
Мокирование get_prepared_products
↓
Мокирование read_text_file
↓
Мокирование get_filenames
↓
Мокирование process_affiliate_products
↓
Вызов campaign.prepare_products()
↓
Проверка вызова process_affiliate_products
```

**Примеры**:
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

### `test_fetch_product_data`

```python
def test_fetch_product_data(mocker, campaign):
    """Test fetch_product_data method."""
    ...
```

**Назначение**: Тестирует метод `fetch_product_data` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод возвращает неверное количество продуктов или неверные данные о продуктах.

**Как работает функция**:
1. Определяется список идентификаторов продуктов `product_ids`.
2. Создается мок списка продуктов `mock_products`.
3. Мокируется метод `process_affiliate_products`, чтобы он возвращал мок списка продуктов.
4. Вызывается метод `fetch_product_data` объекта `campaign` с списком идентификаторов продуктов.
5. Проверяется, что метод возвращает список с двумя продуктами и что атрибуты этих продуктов соответствуют мок данным.

**ASII flowchart**:
```
Определение списка идентификаторов продуктов
↓
Создание мок списка продуктов
↓
Мокирование process_affiliate_products
↓
Вызов campaign.fetch_product_data(product_ids)
↓
Проверка возвращенных продуктов
```

**Примеры**:
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

### `test_save_product`

```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
    ...
```

**Назначение**: Тестирует метод `save_product` класса `AliPromoCampaign`.

**Параметры**:
- `mocker`: Fixture из библиотеки `pytest-mock` для мокирования функций и методов.
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод `Path.write_text` не был вызван один раз с правильными аргументами.

**Как работает функция**:
1. Создается мок объекта продукта `SimpleNamespace`.
2. Мокируется функция `src.utils.jjson.j_dumps`, чтобы возвращать строку "{}".
3. Мокируется метод `pathlib.Path.write_text`.
4. Вызывается метод `save_product` объекта `campaign` с мок объектом продукта.
5. Проверяется, что метод `Path.write_text` был вызван один раз с аргументом "{}" и кодировкой 'utf-8'.

**ASII flowchart**:
```
Создание мок объекта продукта
↓
Мокирование j_dumps
↓
Мокирование Path.write_text
↓
Вызов campaign.save_product(product)
↓
Проверка вызова Path.write_text
```

**Примеры**:
```python
def test_save_product(mocker, campaign):
    """Test save_product method."""
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

**Назначение**: Тестирует метод `list_campaign_products` класса `AliPromoCampaign`.

**Параметры**:
- `campaign`: Fixture, создающая экземпляр класса `AliPromoCampaign`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если метод возвращает неверный список заголовков продуктов.

**Как работает функция**:
1. Создаются два мок объекта продукта `SimpleNamespace`.
2. Мок объектам продукта присваиваются значения `product_title`.
3. Мок объекты продукта добавляются в список `campaign.category.products`.
4. Вызывается метод `list_campaign_products` объекта `campaign`.
5. Проверяется, что метод возвращает список заголовков продуктов, соответствующий значениям `product_title` мок объектов продукта.

**ASII flowchart**:
```
Создание мок объектов продукта
↓
Присвоение значений product_title
↓
Добавление в campaign.category.products
↓
Вызов campaign.list_campaign_products()
↓
Проверка возвращенного списка
```

**Примеры**:
```python
def test_list_campaign_products(campaign):
    """Test list_campaign_products method."""
    product1 = SimpleNamespace(product_title="Product 1")
    product2 = SimpleNamespace(product_title="Product 2")
    campaign.category.products = [product1, product2]

    product_titles = campaign.list_campaign_products()
    assert product_titles == ["Product 1", "Product 2"]