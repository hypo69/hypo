# Модуль тестирования генератора партнерских продуктов AliExpress

## Обзор

Модуль содержит тесты для проверки функциональности класса `AliAffiliatedProducts`, который генерирует партнерские продукты для AliExpress. Он включает тесты для проверки методов `check_and_process_affiliate_products` и `process_affiliate_products`.

## Подробней

Этот модуль использует библиотеку `pytest` для организации и запуска тестов. В нем определены фикстуры и тестовые функции, которые проверяют правильность работы методов класса `AliAffiliatedProducts`. Модуль использует моки для изоляции тестируемого кода от внешних зависимостей и проверки правильности взаимодействия с ними.

## Классы

Здесь нет классов, описанных в явном виде, но есть фикстура `ali_affiliated_products`, которая возвращает экземпляр класса `AliAffiliatedProducts`.

## Функции

- `ali_affiliated_products`
- `test_check_and_process_affiliate_products`
- `test_process_affiliate_products`

### `ali_affiliated_products`

```python
@pytest.fixture
def ali_affiliated_products():
    return AliAffiliatedProducts(campaign_name, category_name, language, currency)
```

**Описание**: Фикстура `pytest`, которая создает и возвращает экземпляр класса `AliAffiliatedProducts` с заданными параметрами.

**Как работает функция**:
Функция создает экземпляр класса `AliAffiliatedProducts`, используя предопределенные значения переменных `campaign_name`, `category_name`, `language` и `currency`.

**Параметры**:
- Отсутствуют явные параметры, но используются переменные:
    - `campaign_name` (str): Название кампании.
    - `category_name` (str): Название категории.
    - `language` (str): Язык.
    - `currency` (str): Валюта.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`.

**Примеры**:
```python
    ali_affiliated_products = ali_affiliated_products()
    assert isinstance(ali_affiliated_products, AliAffiliatedProducts)
```

### `test_check_and_process_affiliate_products`

```python
def test_check_and_process_affiliate_products(ali_affiliated_products):
    with patch.object(ali_affiliated_products, 'process_affiliate_products') as mock_process:
        ali_affiliated_products.check_and_process_affiliate_products(prod_urls)
        mock_process.assert_called_once_with(prod_urls)
```

**Описание**: Тест проверяет, что метод `check_and_process_affiliate_products` вызывает метод `process_affiliate_products` с правильными аргументами.

**Как работает функция**:
1. Используется `patch.object` для замены метода `process_affiliate_products` мок-объектом.
2. Вызывается метод `check_and_process_affiliate_products` с предопределенным списком URL `prod_urls`.
3. Проверяется, что мок-объект `process_affiliate_products` был вызван ровно один раз и с правильными аргументами (`prod_urls`).

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:
```python
    ali_affiliated_products = ali_affiliated_products()
    test_check_and_process_affiliate_products(ali_affiliated_products)
```

### `test_process_affiliate_products`

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
```

**Описание**: Тест проверяет, что метод `process_affiliate_products` правильно обрабатывает продукты и возвращает ожидаемый результат.

**Как работает функция**:
1. Создается мок-объект `mock_product_details`, имитирующий детали продукта, возвращаемые методом `retrieve_product_details`.
2. Используется `patch.object` для замены метода `retrieve_product_details` мок-объектом, который возвращает `mock_product_details`.
3. Используются `patch` для замены функций `ensure_https`, `save_image_from_url`, `save_video_from_url` и `j_dumps` мок-объектами.
4. Вызывается метод `process_affiliate_products` с предопределенным списком URL `prod_urls`.
5. Проверяется, что длина списка обработанных продуктов равна 1 и что `product_id` первого продукта равен "123".

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:
```python
    ali_affiliated_products = ali_affiliated_products()
    test_process_affiliate_products(ali_affiliated_products)