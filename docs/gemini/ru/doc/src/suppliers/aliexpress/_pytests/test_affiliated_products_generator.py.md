# Модуль `test_affiliated_products_generator.py`

## Обзор

Этот модуль содержит тесты для класса `AliAffiliatedProducts`, который отвечает за генерацию партнерских продуктов AliExpress. Модуль включает в себя фикстуры и тестовые функции, проверяющие корректность обработки и извлечения информации о партнерских продуктах.

## Подробнее

Модуль предназначен для тестирования функциональности, связанной с получением и обработкой данных о партнерских продуктах с AliExpress. Он использует `pytest` для организации тестов и `unittest.mock` для имитации внешних зависимостей.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `ali_affiliated_products`

```python
@pytest.fixture
def ali_affiliated_products():
    """
    Возвращает экземпляр класса AliAffiliatedProducts.

    Args:
        Нет аргументов.

    Returns:
        AliAffiliatedProducts: Объект класса AliAffiliatedProducts с предопределенными параметрами.

    Пример:
        >>> ali_affiliated_products()
        <src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts object at ...>
    """
    return AliAffiliatedProducts(campaign_name, category_name, language, currency)
```

**Назначение**: Фикстура `ali_affiliated_products` создает и возвращает экземпляр класса `AliAffiliatedProducts` с заранее определенными параметрами.

**Как работает функция**:

1.  Создается экземпляр класса `AliAffiliatedProducts` с использованием значений `campaign_name`, `category_name`, `language` и `currency`.
2.  Этот экземпляр возвращается для использования в тестах.

```
Создание экземпляра AliAffiliatedProducts
│
└───> Возврат экземпляра
```

**Примеры**:

```python
# Пример использования фикстуры в тесте
def test_something(ali_affiliated_products):
    assert isinstance(ali_affiliated_products, AliAffiliatedProducts)
```

### `test_check_and_process_affiliate_products`

```python
def test_check_and_process_affiliate_products(ali_affiliated_products):
    """
    Тестирует метод check_and_process_affiliate_products класса AliAffiliatedProducts.

    Args:
        ali_affiliated_products (AliAffiliatedProducts): Фикстура с экземпляром AliAffiliatedProducts.

    Returns:
        None

    Raises:
        AssertionError: Если метод process_affiliate_products не был вызван.
    """
    with patch.object(ali_affiliated_products, 'process_affiliate_products') as mock_process:
        ali_affiliated_products.check_and_process_affiliate_products(prod_urls)
        mock_process.assert_called_once_with(prod_urls)
```

**Назначение**: Тестирует метод `check_and_process_affiliate_products`, чтобы убедиться, что он вызывает метод `process_affiliate_products` с правильными аргументами.

**Параметры**:

*   `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Как работает функция**:

1.  Используется `patch.object` для замены метода `process_affiliate_products` мок-объектом.
2.  Вызывается метод `check_and_process_affiliate_products` с предопределенным списком URL-адресов продуктов (`prod_urls`).
3.  Проверяется, что мок-объект `process_affiliate_products` был вызван ровно один раз и с правильным аргументом (`prod_urls`).

```
Замена process_affiliate_products мок-объектом
│
└───> Вызов check_and_process_affiliate_products с prod_urls
│
└───> Проверка, что process_affiliate_products был вызван один раз с prod_urls
```

**Примеры**:

```python
# Пример вызова теста
test_check_and_process_affiliate_products(ali_affiliated_products())
```

### `test_process_affiliate_products`

```python
def test_process_affiliate_products(ali_affiliated_products):
    """
    Тестирует метод process_affiliate_products класса AliAffiliatedProducts.

    Args:
        ali_affiliated_products (AliAffiliatedProducts): Фикстура с экземпляром AliAffiliatedProducts.

    Returns:
        None

    Raises:
        AssertionError: Если обработанные продукты не соответствуют ожидаемым значениям.
    """
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

**Назначение**: Тестирует метод `process_affiliate_products`, чтобы убедиться, что он правильно обрабатывает продукты и возвращает ожидаемый результат.

**Параметры**:

*   `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, предоставляющая экземпляр класса `AliAffiliatedProducts`.

**Как работает функция**:

1.  Создается моковый объект `mock_product_details`, имитирующий детали продукта.
2.  Используются `patch.object` и `patch` для замены внешних зависимостей (таких как `retrieve_product_details`, `ensure_https`, `save_image_from_url`, `save_video_from_url` и `j_dumps`) мок-объектами.
3.  Вызывается метод `process_affiliate_products` с предопределенным списком URL-адресов продуктов (`prod_urls`).
4.  Проверяется, что возвращенный список обработанных продуктов содержит один элемент и что `product_id` этого элемента соответствует ожидаемому значению ("123").

```
Создание мокового объекта mock_product_details
│
└───> Замена внешних зависимостей мок-объектами
│
└───> Вызов process_affiliate_products с prod_urls
│
└───> Проверка, что возвращенный список содержит один элемент с product_id "123"
```

**Примеры**:

```python
# Пример вызова теста
test_process_affiliate_products(ali_affiliated_products())
```