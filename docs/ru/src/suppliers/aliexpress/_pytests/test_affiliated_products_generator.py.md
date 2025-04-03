# Модуль для тестирования генератора партнерских товаров AliExpress

## Обзор

Модуль содержит тесты для класса `AliAffiliatedProducts`, который генерирует партнерские ссылки для товаров AliExpress. Модуль использует библиотеку `pytest` для организации и запуска тестов, а также `unittest.mock` для создания заглушек (mock-объектов) и изоляции тестируемого кода от внешних зависимостей.

## Подробнее

Этот модуль предназначен для проверки корректности работы класса `AliAffiliatedProducts`. Он проверяет, что методы класса вызываются с правильными параметрами и возвращают ожидаемые результаты. В частности, модуль тестирует методы `check_and_process_affiliate_products` и `process_affiliate_products`.

## Классы

В этом модуле нет классов, он содержит только функции для тестирования.

## Функции

### `ali_affiliated_products`

```python
@pytest.fixture
def ali_affiliated_products():
    """
    Возвращает экземпляр класса `AliAffiliatedProducts`.
    
    Returns:
        AliAffiliatedProducts: Экземпляр класса `AliAffiliatedProducts`.
    """
    ...
```

**Назначение**: Фикстура `pytest`, которая создает и возвращает экземпляр класса `AliAffiliatedProducts`. Это позволяет использовать один и тот же экземпляр класса в нескольких тестах.

**Параметры**: Нет.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`, инициализированный с параметрами `campaign_name`, `category_name`, `language` и `currency`.

**Как работает фикстура**:

1. Фикстура создает экземпляр класса `AliAffiliatedProducts` с предопределенными значениями для имени кампании, категории, языка и валюты.
2. Этот экземпляр возвращается и может быть использован в тестах.

```
Создание экземпляра AliAffiliatedProducts
↓
Возврат экземпляра AliAffiliatedProducts
```

**Примеры**:

```python
def test_something(ali_affiliated_products):
    # Внутри теста можно использовать ali_affiliated_products
    # как экземпляр класса AliAffiliatedProducts
    ...
```

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

**Назначение**: Тестирует метод `check_and_process_affiliate_products` класса `AliAffiliatedProducts`, чтобы убедиться, что он вызывает метод `process_affiliate_products` с правильными аргументами.

**Параметры**:
- `ali_affiliated_products`: Фикстура `pytest`, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Возвращает**: Нет.

**Как работает функция**:

1.  Используется `patch.object` для замены метода `process_affiliate_products` экземпляра `ali_affiliated_products` на mock-объект (`mock_process`).
2.  Вызывается метод `check_and_process_affiliate_products` с тестовым списком URL-адресов продуктов (`prod_urls`).
3.  `mock_process.assert_called_once_with(prod_urls)` проверяет, что `process_affiliate_products` был вызван ровно один раз с правильным аргументом (`prod_urls`).

```
Замена process_affiliate_products на mock-объект
↓
Вызов check_and_process_affiliate_products(prod_urls)
↓
Проверка, что process_affiliate_products был вызван с prod_urls
```

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

**Назначение**: Тестирует метод `process_affiliate_products` класса `AliAffiliatedProducts`, чтобы убедиться, что он правильно обрабатывает список URL-адресов продуктов, извлекает детали продуктов и возвращает обработанный список продуктов.

**Параметры**:
- `ali_affiliated_products`: Фикстура `pytest`, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Возвращает**: Нет.

**Как работает функция**:

1.  Создается `mock_product_details` - список объектов `SimpleNamespace`, представляющих детали продукта, возвращаемые mock-объектом `retrieve_product_details`.
2.  Используются `patch.object` и `patch` для замены внешних зависимостей на mock-объекты.
    *   `ali_affiliated_products.retrieve_product_details` заменяется mock-объектом, который возвращает `mock_product_details`.
    *   `src.suppliers.aliexpress.affiliated_products_generator.ensure_https`, `src.suppliers.aliexpress.affiliated_products_generator.save_image_from_url`, `src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url` и `src.suppliers.aliexpress.affiliated_products_generator.j_dumps` также заменяются mock-объектами.
3.  Вызывается метод `process_affiliate_products` с тестовым списком URL-адресов продуктов (`prod_urls`).
4.  Проверяется, что возвращенный список `processed_products` содержит один элемент.
5.  Проверяется, что атрибут `product_id` первого элемента в `processed_products` равен `"123"`.

```
Создание mock-объекта деталей продукта
↓
Замена внешних зависимостей на mock-объекты
↓
Вызов process_affiliate_products(prod_urls)
↓
Проверка, что возвращенный список содержит один элемент
↓
Проверка, что product_id первого элемента равен "123"
```

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