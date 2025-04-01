# Модуль тестирования генератора партнерских продуктов AliExpress

## Обзор

Модуль `test_affiliated_products_generator.py` содержит набор тестов для проверки корректной работы класса `AliAffiliatedProducts`, который предназначен для генерации партнерских ссылок на товары AliExpress. Модуль включает в себя фикстуры и тесты, проверяющие основные методы класса, такие как `check_and_process_affiliate_products` и `process_affiliate_products`. Тесты имитируют внешние зависимости и проверяют соответствие выходных данных ожидаемым результатам.

## Подробнее

Этот файл содержит тесты, которые проверяют функциональность генерации партнерских продуктов AliExpress. Он использует библиотеку `pytest` для организации тестов и `unittest.mock` для имитации зависимостей. Тесты охватывают проверку правильности вызова методов и обработки данных.
В проекте `hypotez` этот модуль важен для обеспечения надежности и корректности работы с партнерскими продуктами AliExpress, гарантируя, что генерация ссылок и обработка данных происходят без ошибок.

## Фикстуры

### `ali_affiliated_products`

```python
@pytest.fixture
def ali_affiliated_products():
    """
    Возвращает экземпляр класса `AliAffiliatedProducts` с заданными параметрами.

    Returns:
        AliAffiliatedProducts: Экземпляр класса `AliAffiliatedProducts`.
    """
    ...
```

**Назначение**:
Фикстура `ali_affiliated_products` создает и возвращает экземпляр класса `AliAffiliatedProducts`. Это позволяет избежать повторного создания экземпляра класса в каждом тесте, упрощая код и повышая его читаемость.

**Возвращает**:
- `AliAffiliatedProducts`:  Возвращает экземпляр класса `AliAffiliatedProducts` с предопределенными значениями для параметров `campaign_name`, `category_name`, `language` и `currency`.

**Принцип работы**:
Фикстура создает экземпляр класса `AliAffiliatedProducts` с предопределенными значениями:
- `campaign_name = "sample_campaign"`
- `category_name = "sample_category"`
- `language = "EN"`
- `currency = "USD"`

**Примеры**:

```python
def test_example(ali_affiliated_products):
    assert isinstance(ali_affiliated_products, AliAffiliatedProducts)
```

## Функции

### `test_check_and_process_affiliate_products`

```python
def test_check_and_process_affiliate_products(ali_affiliated_products):
    """
    Тестирует метод `check_and_process_affiliate_products` класса `AliAffiliatedProducts`.

    Args:
        ali_affiliated_products: Фикстура `ali_affiliated_products`, предоставляющая экземпляр класса `AliAffiliatedProducts`.
    """
    ...
```

**Назначение**:
Тест `test_check_and_process_affiliate_products` проверяет, что метод `check_and_process_affiliate_products` вызывает метод `process_affiliate_products` с правильными аргументами.

**Параметры**:
- `ali_affiliated_products`: Фикстура `ali_affiliated_products`, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Как работает функция**:

1.  Патчим метод `process_affiliate_products` экземпляра `ali_affiliated_products` с помощью `unittest.mock.patch.object`.
2.  Вызываем метод `check_and_process_affiliate_products` с предопределенными URL-адресами продуктов `prod_urls`.
3.  Проверяем, что метод `process_affiliate_products` был вызван один раз с аргументом `prod_urls`.

**Примеры**:

```python
def test_check_and_process_affiliate_products(ali_affiliated_products):
    with patch.object(ali_affiliated_products, 'process_affiliate_products') as mock_process:
        ali_affiliated_products.check_and_process_affiliate_products(prod_urls)
        mock_process.assert_called_once_with(prod_urls)
```

### `test_process_affiliate_products`

```python
def test_process_affiliate_products(ali_affiliated_products):
    """
    Тестирует метод `process_affiliate_products` класса `AliAffiliatedProducts`.

    Args:
        ali_affiliated_products: Фикстура `ali_affiliated_products`, предоставляющая экземпляр класса `AliAffiliatedProducts`.
    """
    ...
```

**Назначение**:
Тест `test_process_affiliate_products` проверяет, что метод `process_affiliate_products` правильно обрабатывает список URL-адресов продуктов, извлекает детали продуктов и возвращает обработанные продукты.

**Параметры**:
-   `ali_affiliated_products`: Фикстура `ali_affiliated_products`, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Как работает функция**:

1.  Определяем моковые данные о продуктах `mock_product_details`, которые будут возвращаться при вызове `retrieve_product_details`.
2.  Имитируем вызовы нескольких функций и методов:
    *   `retrieve_product_details`: возвращает `mock_product_details`.
    *   `ensure_https`: возвращает `prod_urls`.
    *   `save_image_from_url`: ничего не делает.
    *   `save_video_from_url`: ничего не делает.
    *   `j_dumps`: возвращает `True`.
3.  Вызываем метод `process_affiliate_products` с `prod_urls`.
4.  Проверяем, что длина возвращенного списка `processed_products` равна 1.
5.  Проверяем, что `product_id` первого элемента в `processed_products` равен `"123"`.

**Примеры**:

```python
def test_process_affiliate_products(ali_affiliated_products):
    mock_product_details = [SimpleNamespace(product_id="123", promotion_link="promo_link", product_main_image_url="image_url", product_video_url="video_url")]
    
    with patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=mock_product_details) as mock_retrieve, \
         patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=prod_urls), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.save_image_from_url"), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url"), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps", return_value=True):
        
        processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)
        
        assert len(processed_products) == 1
        assert processed_products[0].product_id == "123"