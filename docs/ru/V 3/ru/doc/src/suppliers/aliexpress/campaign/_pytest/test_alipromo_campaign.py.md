# Модуль `test_alipromo_campaign.py`

## Обзор

Этот модуль содержит набор тестов для класса `AliPromoCampaign`, который используется для управления рекламными кампаниями AliExpress. Тесты охватывают различные аспекты функциональности класса, включая инициализацию кампании, получение продуктов категории, создание пространств имен, подготовку продуктов, получение данных о продуктах, сохранение продуктов и составление списка продуктов кампании.

## Подробней

Модуль использует библиотеку `pytest` для организации и запуска тестов. `AliPromoCampaign` — это класс, отвечающий за управление рекламными кампаниями AliExpress. Он предоставляет методы для инициализации кампании, получения продуктов из категорий, создания пространств имен для продуктов, категорий и кампаний, подготовки продуктов для кампании, получения данных о продуктах, сохранения информации о продуктах и получения списка продуктов, участвующих в кампании. Тесты проверяют корректность работы этих методов, используя фикстуры и моки для имитации различных сценариев и зависимостей.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламными кампаниями AliExpress.

**Методы**:
- `initialize_campaign`: Инициализирует данные кампании.
- `get_category_products`: Получает продукты из заданной категории.
- `create_product_namespace`: Создает пространство имен для продукта.
- `create_category_namespace`: Создает пространство имен для категории.
- `create_campaign_namespace`: Создает пространство имен для кампании.
- `prepare_products`: Подготавливает продукты для кампании.
- `fetch_product_data`: Получает данные о продукте.
- `save_product`: Сохраняет данные о продукте.
- `list_campaign_products`: Выводит список продуктов кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `category_name` (str): Имя категории.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**
```python
    from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
    campaign = AliPromoCampaign('test_campaign', 'test_category', 'EN', 'USD')
```

## Функции

### `campaign`

```python
@pytest.fixture
def campaign():
    """Fixture for creating a campaign instance."""
    return AliPromoCampaign(campaign_name, category_name, language, currency)
```

**Описание**: Фикстура `campaign` создает экземпляр класса `AliPromoCampaign` для использования в тестах.

**Параметры**:
- Нет

**Возвращает**:
- `AliPromoCampaign`: Экземпляр класса `AliPromoCampaign`.

**Вызывает исключения**:
- Нет

**Примеры**:
```python
    @pytest.fixture
    def campaign():
        return AliPromoCampaign('test_campaign', 'test_category', 'EN', 'USD')
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

**Описание**: Тест проверяет, что метод `initialize_campaign` корректно инициализирует данные кампании.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    mocker.patch("src.utils.file.get_filenames", return_value=[])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data", return_value=[])

    products = campaign.get_category_products(force=True)
    assert products == []
```

**Описание**: Тест проверяет метод `get_category_products`, когда отсутствуют JSON-файлы.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    mock_product_data = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.file.get_filenames", return_value=["product_123.json"])
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=mock_product_data)

    products = campaign.get_category_products()
    assert len(products) == 1
    assert products[0].product_id == "123"
    assert products[0].product_title == "Test Product"
```

**Описание**: Тест проверяет метод `get_category_products`, когда JSON-файлы присутствуют.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    product_data = {
        "product_id": "123",
        "product_title": "Test Product"
    }
    product = campaign.create_product_namespace(**product_data)
    assert product.product_id == "123"
    assert product.product_title == "Test Product"
```

**Описание**: Тест проверяет метод `create_product_namespace`.

**Параметры**:
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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

**Описание**: Тест проверяет метод `create_category_namespace`.

**Параметры**:
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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

**Описание**: Тест проверяет метод `create_campaign_namespace`.

**Параметры**:
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products", return_value=[])
    mocker.patch("src.utils.file.read_text_file", return_value="source_data")
    mocker.patch("src.utils.file.get_filenames", return_value=["source.html"])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products")

    campaign.prepare_products()
    campaign.process_affiliate_products.assert_called_once()
```

**Описание**: Тест проверяет метод `prepare_products`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    product_ids = ["123", "456"]
    mock_products = [SimpleNamespace(product_id="123"), SimpleNamespace(product_id="456")]
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products", return_value=mock_products)

    products = campaign.fetch_product_data(product_ids)
    assert len(products) == 2
    assert products[0].product_id == "123"
    assert products[1].product_id == "456"
```

**Описание**: Тест проверяет метод `fetch_product_data`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
    product = SimpleNamespace(product_id="123", product_title="Test Product")
    mocker.patch("src.utils.jjson.j_dumps", return_value="{}")
    mocker.patch("pathlib.Path.write_text")

    campaign.save_product(product)
    Path.write_text.assert_called_once_with("{}", encoding=\'utf-8\')
```

**Описание**: Тест проверяет метод `save_product`.

**Параметры**:
- `mocker`: Объект для создания моков.
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:
```python
    def test_save_product(mocker, campaign):
        product = SimpleNamespace(product_id="123", product_title="Test Product")
        mocker.patch("src.utils.jjson.j_dumps", return_value="{}")
        mocker.patch("pathlib.Path.write_text")

        campaign.save_product(product)
        Path.write_text.assert_called_once_with("{}", encoding=\'utf-8\')
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

**Описание**: Тест проверяет метод `list_campaign_products`.

**Параметры**:
- `campaign`: Фикстура кампании.

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:
```python
    def test_list_campaign_products(campaign):
        product1 = SimpleNamespace(product_title="Product 1")
        product2 = SimpleNamespace(product_title="Product 2")
        campaign.category.products = [product1, product2]

        product_titles = campaign.list_campaign_products()
        assert product_titles == ["Product 1", "Product 2"]