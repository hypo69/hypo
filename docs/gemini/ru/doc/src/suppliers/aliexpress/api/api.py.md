# Модуль для работы с API AliExpress
=================================================

Модуль предоставляет класс `AliexpressApi`, который используется для взаимодействия с API AliExpress.
Он позволяет получать информацию о продуктах, генерировать партнерские ссылки и получать категории.

## Обзор

Модуль предназначен для упрощения взаимодействия с AliExpress Open Platform API. Он предоставляет удобный интерфейс для получения информации о товарах и партнерских ссылках, используя официальный API AliExpress.

## Подробней

Модуль `api.py` содержит класс `AliexpressApi`, который инкапсулирует логику взаимодействия с API AliExpress. Класс предоставляет методы для получения информации о продуктах, генерации партнерских ссылок, получения списка горячих продуктов и категорий.

## Классы

### `AliexpressApi`

**Описание**: Класс для взаимодействия с API AliExpress.

**Принцип работы**: Класс инициализируется с API ключом, секретом, языком, валютой и идентификатором отслеживания. Он предоставляет методы для выполнения различных запросов к API AliExpress, таких как получение информации о продуктах, генерация партнерских ссылок и получение категорий.

**Аттрибуты**:
- `_key` (str): API ключ.
- `_secret` (str): API секрет.
- `_tracking_id` (str): Идентификатор отслеживания для партнерских ссылок.
- `_language` (model_Language): Код языка.
- `_currency` (model_Currency): Код валюты.
- `_app_signature` (str): Подпись приложения.
- `categories` (List[model_Category | model_ChildCategory] | None): Кэш категорий.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliexpressApi`.
- `retrieve_product_details`: Получает информацию о продуктах.
- `get_affiliate_links`: Генерирует партнерские ссылки.
- `get_hotproducts`: Получает список горячих продуктов.
- `get_categories`: Получает список категорий.
- `get_parent_categories`: Получает список родительских категорий.
- `get_child_categories`: Получает список дочерних категорий.

## Функции

### `__init__`

```python
def __init__(self, key: str, secret: str, language: model_Language, currency: model_Currency, tracking_id: str = None, app_signature: str = None, **kwargs):
    """
    Args:
        key (str): Your API key.
        secret (str): Your API secret.
        language (str): Language code. Defaults to EN.
        currency (str): Currency code. Defaults to USD.
        tracking_id (str): The tracking id for link generator. Defaults to None.
    """
```

**Назначение**: Инициализирует экземпляр класса `AliexpressApi`.

**Параметры**:
- `key` (str): API ключ.
- `secret` (str): API секрет.
- `language` (model_Language): Код языка.
- `currency` (model_Currency): Код валюты.
- `tracking_id` (str, optional): Идентификатор отслеживания для партнерских ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

**Как работает функция**:

1.  Сохраняет переданные параметры в атрибуты экземпляра класса.
2.  Устанавливает параметры приложения по умолчанию, используя API ключ и секрет.

```
A[Сохранение параметров]
|
B[setDefaultAppInfo]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
```

### `retrieve_product_details`

```python
def retrieve_product_details(self, product_ids: str | list, fields: str | list = None, country: str = None, **kwargs) -> List[model_Product]:
    """ Get products information.

    Args:
        product_ids (``str | list[str]``): One or more links or product IDs.
        fields (``str | list[str]``): The fields to include in the results. Defaults to all.
        country (``str``): Filter products that can be sent to that country. Returns the price
            according to the country's tax rate policy.

    Returns:
        ``list[model_Product]``: A list of products.

    Raises:
        ``ProductsNotFoudException``
        ``InvalidArgumentException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Получает информацию о продуктах по их идентификаторам.

**Параметры**:
- `product_ids` (str | list): Идентификаторы продуктов. Может быть строкой или списком строк.
- `fields` (str | list, optional): Список полей, которые нужно включить в результаты. По умолчанию `None` (все поля).
- `country` (str, optional): Страна, для которой нужно отфильтровать продукты. По умолчанию `None`.

**Возвращает**:
- `List[model_Product]`: Список объектов `model_Product`, содержащих информацию о продуктах.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.

**Как работает функция**:

1.  Преобразует `product_ids` в список, если это строка.
2.  Преобразует список `product_ids` в строку, разделенную запятыми.
3.  Создает объект запроса `AliexpressAffiliateProductdetailGetRequest`.
4.  Устанавливает параметры запроса, такие как `app_signature`, `fields`, `product_ids`, `country`, `target_currency`, `target_language` и `tracking_id`.
5.  Выполняет API запрос с помощью функции `api_request`.
6.  Обрабатывает ответ:
    -   Если `current_record_count` больше 0, парсит продукты и возвращает список продуктов.
    -   Если `current_record_count` равен 0, логирует предупреждение и возвращает `None`.
    -   В случае ошибки, логирует ошибку и возвращает `None`.

```
A[Преобразование product_ids в список]
|
B[Преобразование списка product_ids в строку]
|
C[Создание объекта запроса AliexpressAffiliateProductdetailGetRequest]
|
D[Установка параметров запроса]
|
E[Выполнение API запроса api_request]
|
F[Обработка ответа]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
products = api.retrieve_product_details(product_ids=['123456789', '987654321'], fields=['product_title', 'product_price'], country='US')
if products:
    for product in products:
        print(product.product_title, product.product_price)
```

### `get_affiliate_links`

```python
def get_affiliate_links(self, links: str | list, link_type: model_LinkType = model_LinkType.NORMAL, **kwargs) -> List[model_AffiliateLink]:
    """ Converts a list of links in affiliate links.
    Args:
        links (``str | list[str]``): One or more links to convert.
        link_type (``model_LinkType``): Choose between normal link with standard commission
            or hot link with hot product commission. Defaults to NORMAL.
            @code
            link_type: model_LinkType = model_LinkType.HOTLINK
            @endcode

    Returns:
        ``list[model_AffiliateLink]``: A list containing the affiliate links.

    Raises:
        ``InvalidArgumentException``
        ``InvalidTrackingIdException``
        ``ProductsNotFoudException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Преобразует список ссылок в партнерские ссылки.

**Параметры**:
- `links` (str | list): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (NORMAL или HOTLINK). По умолчанию `model_LinkType.NORMAL`.

**Возвращает**:
- `List[model_AffiliateLink]`: Список объектов `model_AffiliateLink`, содержащих партнерские ссылки.

**Вызывает исключения**:
- `InvalidTrackingIdException`: Если не указан `tracking_id`.

**Как работает функция**:

1.  Проверяет, установлен ли `tracking_id`. Если нет, логирует ошибку и возвращает `None`.
2.  Преобразует `links` в список, если это строка.
3.  Преобразует список `links` в строку, разделенную запятыми.
4.  Создает объект запроса `AliexpressAffiliateLinkGenerateRequest`.
5.  Устанавливает параметры запроса, такие как `app_signature`, `source_values`, `promotion_link_type` и `tracking_id`.
6.  Выполняет API запрос с помощью функции `api_request`.
7.  Обрабатывает ответ:
    -   Если `total_result_count` больше 0, возвращает список партнерских ссылок.
    -   Если `total_result_count` равен 0, логирует предупреждение и возвращает `None`.

```
A[Проверка наличия tracking_id]
|
B[Преобразование links в список]
|
C[Преобразование списка links в строку]
|
D[Создание объекта запроса AliexpressAffiliateLinkGenerateRequest]
|
E[Установка параметров запроса]
|
F[Выполнение API запроса api_request]
|
G[Обработка ответа]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
affiliate_links = api.get_affiliate_links(links=['https://www.aliexpress.com/item/123456789.html', 'https://www.aliexpress.com/item/987654321.html'], link_type=model_LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(link)
```

### `get_hotproducts`

```python
def get_hotproducts(self, category_ids: str | list = None, delivery_days: int = None, fields: str | list = None, keywords: str = None, max_sale_price: int = None, min_sale_price: int = None, page_no: int = None, page_size: int = None, platform_product_type: model_ProductType = None, ship_to_country: str = None, sort: model_SortBy = None, **kwargs) -> model_HotProductsResponse:
    """Search for affiliated products with high commission.

    Args:
        category_ids (``str | list[str]``): One or more category IDs.
        delivery_days (``int``): Estimated delivery days.
        fields (``str | list[str]``): The fields to include in the results list. Defaults to all.
        keywords (``str``): Search products based on keywords.
        max_sale_price (``int``): Filters products with price below the specified value.
            Prices appear in lowest currency denomination. So $31.41 should be 3141.
        min_sale_price (``int``): Filters products with price above the specified value.
            Prices appear in lowest currency denomination. So $31.41 should be 3141.
        page_no (``int``):\
        page_size (``int``): Products on each page. Should be between 1 and 50.
        platform_product_type (``model_ProductType``): Specify platform product type.
        ship_to_country (``str``): Filter products that can be sent to that country.
            Returns the price according to the country's tax rate policy.
        sort (``model_SortBy``): Specifies the sort method.

    Returns:
        ``model_HotProductsResponse``: Contains response information and the list of products.

    Raises:
        ``ProductsNotFoudException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Ищет партнерские продукты с высокой комиссией.

**Параметры**:
- `category_ids` (str | list, optional): Идентификаторы категорий. По умолчанию `None`.
- `delivery_days` (int, optional): Оценочные дни доставки. По умолчанию `None`.
- `fields` (str | list, optional): Список полей, которые нужно включить в результаты. По умолчанию `None` (все поля).
- `keywords` (str, optional): Ключевые слова для поиска продуктов. По умолчанию `None`.
- `max_sale_price` (int, optional): Максимальная цена продажи. По умолчанию `None`.
- `min_sale_price` (int, optional): Минимальная цена продажи. По умолчанию `None`.
- `page_no` (int, optional): Номер страницы. По умолчанию `None`.
- `page_size` (int, optional): Количество продуктов на странице. По умолчанию `None`.
- `platform_product_type` (model_ProductType, optional): Тип продукта платформы. По умолчанию `None`.
- `ship_to_country` (str, optional): Страна доставки. По умолчанию `None`.
- `sort` (model_SortBy, optional): Метод сортировки. По умолчанию `None`.

**Возвращает**:
- `model_HotProductsResponse`: Объект `model_HotProductsResponse`, содержащий информацию об ответе и список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.

**Как работает функция**:

1.  Создает объект запроса `AliexpressAffiliateHotproductQueryRequest`.
2.  Устанавливает параметры запроса, такие как `app_signature`, `category_ids`, `delivery_days`, `fields`, `keywords`, `max_sale_price`, `min_sale_price`, `page_no`, `page_size`, `platform_product_type`, `ship_to_country`, `sort`, `target_currency`, `target_language` и `tracking_id`.
3.  Выполняет API запрос с помощью функции `api_request`.
4.  Обрабатывает ответ:
    -   Если `current_record_count` больше 0, парсит продукты и возвращает объект `model_HotProductsResponse`.
    -   Если `current_record_count` равен 0, вызывает исключение `ProductsNotFoudException`.

```
A[Создание объекта запроса AliexpressAffiliateHotproductQueryRequest]
|
B[Установка параметров запроса]
|
C[Выполнение API запроса api_request]
|
D[Обработка ответа]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
hot_products = api.get_hotproducts(category_ids=['123', '456'], keywords='smartphone', page_size=20)
if hot_products.products:
    for product in hot_products.products:
        print(product.product_title, product.product_price)
```

### `get_categories`

```python
def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
    """Get all available categories, both parent and child.

    Returns:
        ``list[model_Category | model_ChildCategory]``: A list of categories.

    Raises:
        ``CategoriesNotFoudException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Получает все доступные категории, как родительские, так и дочерние.

**Возвращает**:
- `List[model_Category | model_ChildCategory]`: Список объектов `model_Category` и `model_ChildCategory`, содержащий все категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.

**Как работает функция**:

1.  Создает объект запроса `AliexpressAffiliateCategoryGetRequest`.
2.  Устанавливает параметр запроса `app_signature`.
3.  Выполняет API запрос с помощью функции `api_request`.
4.  Обрабатывает ответ:
    -   Если `total_result_count` больше 0, сохраняет категории в атрибут `categories` и возвращает список категорий.
    -   Если `total_result_count` равен 0, вызывает исключение `CategoriesNotFoudException`.

```
A[Создание объекта запроса AliexpressAffiliateCategoryGetRequest]
|
B[Установка параметров запроса]
|
C[Выполнение API запроса api_request]
|
D[Обработка ответа]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
categories = api.get_categories()
if categories:
    for category in categories:
        print(category.category_name, category.category_id)
```

### `get_parent_categories`

```python
def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
    """Get all available parent categories.

    Args:
        use_cache (``bool``): Uses cached categories to reduce API requests.

    Returns:
        ``list[model_Category]``: A list of parent categories.

    Raises:
        ``CategoriesNotFoudException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Получает все доступные родительские категории.

**Параметры**:
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества API запросов. По умолчанию `True`.

**Возвращает**:
- `List[model_Category]`: Список объектов `model_Category`, содержащий родительские категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.

**Как работает функция**:

1.  Проверяет, нужно ли использовать кэш или категории не были загружены. Если кэш не используется или категории не загружены, вызывает метод `get_categories` для получения категорий.
2.  Вызывает функцию `filter_parent_categories` для фильтрации родительских категорий из списка всех категорий.
3.  Возвращает список родительских категорий.

```
A[Проверка использования кэша или наличия категорий]
|
B[Вызов get_categories, если необходимо]
|
C[Фильтрация родительских категорий filter_parent_categories]
|
D[Возврат списка родительских категорий]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
parent_categories = api.get_parent_categories()
if parent_categories:
    for category in parent_categories:
        print(category.category_name, category.category_id)
```

### `get_child_categories`

```python
def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
    """Get all available child categories for a specific parent category.

    Args:
        parent_category_id (``int``): The parent category id.
        use_cache (``bool``): Uses cached categories to reduce API requests.

    Returns:
        ``list[model_ChildCategory]``: A list of child categories.

    Raises:
        ``CategoriesNotFoudException``
        ``ApiRequestException``
        ``ApiRequestResponseException``
    """
```

**Назначение**: Получает все доступные дочерние категории для указанной родительской категории.

**Параметры**:
- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества API запросов. По умолчанию `True`.

**Возвращает**:
- `List[model_ChildCategory]`: Список объектов `model_ChildCategory`, содержащий дочерние категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.

**Как работает функция**:

1.  Проверяет, нужно ли использовать кэш или категории не были загружены. Если кэш не используется или категории не загружены, вызывает метод `get_categories` для получения категорий.
2.  Вызывает функцию `filter_child_categories` для фильтрации дочерних категорий из списка всех категорий на основе `parent_category_id`.
3.  Возвращает список дочерних категорий.

```
A[Проверка использования кэша или наличия категорий]
|
B[Вызов get_categories, если необходимо]
|
C[Фильтрация дочерних категорий filter_child_categories]
|
D[Возврат списка дочерних категорий]
```

**Примеры**:

```python
api = AliexpressApi(key='your_api_key', secret='your_api_secret', language='EN', currency='USD', tracking_id='your_tracking_id')
child_categories = api.get_child_categories(parent_category_id=123456)
if child_categories:
    for category in child_categories:
        print(category.category_name, category.category_id)