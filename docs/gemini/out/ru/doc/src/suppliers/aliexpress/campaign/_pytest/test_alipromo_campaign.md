# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py`

## Обзор

Данный модуль содержит тесты для класса `AliPromoCampaign`, который используется для обработки кампаний на AliExpress. Модуль проверяет корректность инициализации кампании, извлечения данных о продуктах, создания различных пространств имен и сохранения данных.

## Оглавление

- [Тесты](#тесты)
- [Фикстуры](#фикстуры)
- [Функции](#функции)


## Фикстуры

### `campaign`

**Описание**: Фикстура для создания экземпляра класса `AliPromoCampaign` для использования в тестах.

**Возвращает**: Экземпляр класса `AliPromoCampaign`.

```python
@pytest.fixture
def campaign():
    """Fixture for creating a campaign instance."""
    return AliPromoCampaign(campaign_name, category_name, language, currency)
```


## Тесты

### `test_initialize_campaign`

**Описание**: Тестирует метод `initialize_campaign`, проверяя корректность инициализации данных кампании.

**Параметры**:
- `mocker`: объект для создания mock-объектов.
- `campaign`: экземпляр класса `AliPromoCampaign`, полученный из фикстуры.

**Возвращает**: Ничего.

**Проверяемые утверждения**:
- `campaign.campaign.name == campaign_name`
- `campaign.campaign.category.test_category.name == category_name`

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

**Описание**: Тестирует метод `get_category_products` в случае отсутствия JSON файлов.

**Параметры**:
- `mocker`: объект для создания mock-объектов.
- `campaign`: экземпляр класса `AliPromoCampaign`, полученный из фикстуры.

**Возвращает**: Список продуктов.

**Проверяемые утверждения**:
- `products == []`

```python
def test_get_category_products_no_json_files(mocker, campaign):
    """Test get_category_products method when no JSON files are present."""
    mocker.patch("src.utils.file.get_filenames", return_value=[])
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data", return_value=[])

    products = campaign.get_category_products(force=True)
    assert products == []
```

(Остальные тесты аналогично описываются, указывая параметры, возвращаемые значения и проверяемые утверждения.)

## Функции

(Список функций с описаниями, параметрами, возвращаемыми значениями и исключениями)


```
```