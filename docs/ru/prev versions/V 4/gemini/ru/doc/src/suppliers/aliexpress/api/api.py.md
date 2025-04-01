# Модуль: src.suppliers.aliexpress.api

## Обзор

Модуль предоставляет API для взаимодействия с AliExpress. Он позволяет получать информацию о продуктах и создавать партнерские ссылки, используя официальный API AliExpress.

## Подробней

Этот модуль упрощает взаимодействие с API AliExpress, предоставляя удобные методы для получения информации о продуктах, создания партнерских ссылок и работы с категориями. Он включает в себя обработку ошибок, логирование и использование моделей данных для представления информации. Модуль предназначен для использования в проектах, где требуется интеграция с AliExpress для получения данных о продуктах и создания партнерских программ.

## Классы

### `AliexpressApi`

**Описание**:
Предоставляет методы для получения информации с AliExpress, используя API credentials.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliexpressApi`.
- `retrieve_product_details`: Получает информацию о продуктах.
- `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
- `get_hotproducts`: Поиск партнерских продуктов с высокой комиссией.
- `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
- `get_parent_categories`: Получает все доступные родительские категории.
- `get_child_categories`: Получает все доступные дочерние категории для указанной родительской категории.

**Параметры**:
- `key` (str): Your API key.
- `secret` (str): Your API secret.
- `language` (str): Language code. Defaults to EN.
- `currency` (str): Currency code. Defaults to USD.
- `tracking_id` (str): The tracking id for link generator. Defaults to None.

**Примеры**
```python
api = AliexpressApi(
    key='your_key',
    secret='your_secret',
    language=model_Language.RU,
    currency=model_Currency.RUB,
    tracking_id='your_tracking_id'
)
```

## Функции

### `retrieve_product_details`

```python
def retrieve_product_details(
    product_ids: str | list,
    fields: str | list = None,
    country: str = None,
    **kwargs
) -> List[model_Product]:
    """
    Args:
        product_ids (str | list): One or more links or product IDs.
        fields (str | list): The fields to include in the results. Defaults to all.
        country (str): Filter products that can be sent to that country. Returns the price
            according to the country's tax rate policy.

    Returns:
        List[model_Product]: A list of products.

    Raises:
        ProductsNotFoudException
        InvalidArgumentException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Получает информацию о продуктах.

**Параметры**:
- `product_ids` (str | list): Один или несколько линков или ID продуктов.
- `fields` (str | list, optional): Поля для включения в результаты. По умолчанию `None` (все поля).
- `country` (str, optional): Страна, для которой фильтруются продукты. Возвращает цену с учетом налоговой политики страны. По умолчанию `None`.

**Возвращает**:
- `List[model_Product]`: Список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `InvalidArgumentException`: Если переданы некорректные аргументы.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
products = api.retrieve_product_details(product_ids=['1234567890', '0987654321'], fields=['product_title', 'product_price'], country='RU')
if products:
    for product in products:
        print(product.product_title, product.product_price)
```

### `get_affiliate_links`

```python
def get_affiliate_links(
    links: str | list,
    link_type: model_LinkType = model_LinkType.NORMAL,
    **kwargs
) -> List[model_AffiliateLink]:
    """
    Args:
        links (str | list): One or more links to convert.
        link_type (model_LinkType): Choose between normal link with standard commission
            or hot link with hot product commission. Defaults to NORMAL.
            @code
            link_type: model_LinkType = model_LinkType.HOTLINK
            @endcode

    Returns:
        List[model_AffiliateLink]: A list containing the affiliate links.

    Raises:
        InvalidArgumentException
        InvalidTrackingIdException
        ProductsNotFoudException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Преобразует список ссылок в партнерские ссылки.

**Параметры**:
- `links` (str | list): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (NORMAL или HOTLINK). По умолчанию `model_LinkType.NORMAL`.

**Возвращает**:
- `List[model_AffiliateLink]`: Список партнерских ссылок.

**Вызывает исключения**:
- `InvalidArgumentException`: Если переданы некорректные аргументы.
- `InvalidTrackingIdException`: Если не указан tracking_id.
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
affiliate_links = api.get_affiliate_links(links=['https://aliexpress.com/item/1234567890.html'], link_type=model_LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(link)
```

### `get_hotproducts`

```python
def get_hotproducts(
    category_ids: str | list = None,
    delivery_days: int = None,
    fields: str | list = None,
    keywords: str = None,
    max_sale_price: int = None,
    min_sale_price: int = None,
    page_no: int = None,
    page_size: int = None,
    platform_product_type: model_ProductType = None,
    ship_to_country: str = None,
    sort: model_SortBy = None,
    **kwargs
) -> model_HotProductsResponse:
    """
    Args:
        category_ids (str | list): One or more category IDs.
        delivery_days (int): Estimated delivery days.
        fields (str | list): The fields to include in the results list. Defaults to all.
        keywords (str): Search products based on keywords.
        max_sale_price (int): Filters products with price below the specified value.
            Prices appear in lowest currency denomination. So $31.41 should be 3141.
        min_sale_price (int): Filters products with price above the specified value.
            Prices appear in lowest currency denomination. So $31.41 should be 3141.
        page_no (int):
        page_size (int): Products on each page. Should be between 1 and 50.
        platform_product_type (model_ProductType): Specify platform product type.
        ship_to_country (str): Filter products that can be sent to that country.
            Returns the price according to the country's tax rate policy.
        sort (model_SortBy): Specifies the sort method.

    Returns:
        model_HotProductsResponse: Contains response information and the list of products.

    Raises:
        ProductsNotFoudException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Поиск партнерских продуктов с высокой комиссией.

**Параметры**:
- `category_ids` (str | list, optional): Один или несколько ID категорий. По умолчанию `None`.
- `delivery_days` (int, optional): Предполагаемое количество дней доставки. По умолчанию `None`.
- `fields` (str | list, optional): Поля для включения в результаты. По умолчанию `None` (все поля).
- `keywords` (str, optional): Ключевые слова для поиска продуктов. По умолчанию `None`.
- `max_sale_price` (int, optional): Максимальная цена продукта. По умолчанию `None`.
- `min_sale_price` (int, optional): Минимальная цена продукта. По умолчанию `None`.
- `page_no` (int, optional): Номер страницы. По умолчанию `None`.
- `page_size` (int, optional): Количество продуктов на странице (1-50). По умолчанию `None`.
- `platform_product_type` (model_ProductType, optional): Тип платформы продукта. По умолчанию `None`.
- `ship_to_country` (str, optional): Страна доставки. По умолчанию `None`.
- `sort` (model_SortBy, optional): Метод сортировки. По умолчанию `None`.

**Возвращает**:
- `model_HotProductsResponse`: Объект, содержащий информацию об ответе и список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
hot_products = api.get_hotproducts(category_ids=['123', '456'], keywords='модный', ship_to_country='RU')
if hot_products:
    for product in hot_products.products:
        print(product.product_title, product.product_price)
```

### `get_categories`

```python
def get_categories(**kwargs) -> List[model_Category | model_ChildCategory]:
    """
    Returns:
        list[model_Category | model_ChildCategory]: A list of categories.

    Raises:
        CategoriesNotFoudException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Получает все доступные категории, как родительские, так и дочерние.

**Возвращает**:
- `List[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
categories = api.get_categories()
if categories:
    for category in categories:
        print(category.category_name)
```

### `get_parent_categories`

```python
def get_parent_categories(use_cache=True, **kwargs) -> List[model_Category]:
    """
    Args:
        use_cache (bool): Uses cached categories to reduce API requests.

    Returns:
        list[model_Category]: A list of parent categories.

    Raises:
        CategoriesNotFoudException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Получает все доступные родительские категории.

**Параметры**:
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `List[model_Category]`: Список родительских категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
parent_categories = api.get_parent_categories()
if parent_categories:
    for category in parent_categories:
        print(category.category_name)
```

### `get_child_categories`

```python
def get_child_categories(parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
    """
    Args:
        parent_category_id (int): The parent category id.
        use_cache (bool): Uses cached categories to reduce API requests.

    Returns:
        list[model_ChildCategory]: A list of child categories.

    Raises:
        CategoriesNotFoudException
        ApiRequestException
        ApiRequestResponseException
    """
```

**Описание**:
Получает все доступные дочерние категории для указанной родительской категории.

**Параметры**:
- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `List[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:
```python
child_categories = api.get_child_categories(parent_category_id=123456)
if child_categories:
    for category in child_categories:
        print(category.category_name)