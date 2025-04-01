# Модуль: src.suppliers.aliexpress.api.api

## Обзор

Модуль предоставляет API для взаимодействия с AliExpress. Он включает в себя классы и методы для получения информации о продуктах, создания партнерских ссылок, поиска горячих предложений и получения категорий.

## Подробнее

Этот модуль является оберткой для AliExpress Open Platform API, упрощающей получение информации о товарах и создание партнерских ссылок с использованием официального API. Модуль позволяет взаимодействовать с API AliExpress для получения информации о продуктах, создания партнерских ссылок и поиска популярных товаров.

## Классы

### `AliexpressApi`

**Описание**: Класс предоставляет методы для получения информации из AliExpress с использованием учетных данных API.

**Принцип работы**:
1.  Инициализируется с использованием ключа API, секрета, языка, валюты и идентификатора отслеживания.
2.  Устанавливает параметры API по умолчанию.
3.  Предоставляет методы для получения информации о продуктах, создания партнерских ссылок и поиска популярных товаров.
4.  Кэширует категории для уменьшения количества запросов к API.

**Атрибуты**:

*   `_key` (str): Ключ API.
*   `_secret` (str): Секрет API.
*   `_tracking_id` (str | None): Идентификатор отслеживания для партнерских ссылок.
*   `_language` (str): Язык, используемый для запросов API.
*   `_currency` (str): Валюта, используемая для запросов API.
*   `_app_signature` (str | None): Подпись приложения.
*    `categories` (List[model_Category | model_ChildCategory] | None) : Список категорий, полученный из API AliExpress.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `AliexpressApi`.
*   `retrieve_product_details`: Получает информацию о продуктах.
*   `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
*   `get_hotproducts`: Поиск партнерских продуктов с высокой комиссией.
*   `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
*   `get_parent_categories`: Получает все доступные родительские категории.
*   `get_child_categories`: Получает все доступные дочерние категории для определенной родительской категории.

### `__init__`

```python
def __init__(self, key: str, secret: str, language: model_Language, currency: model_Currency, tracking_id: str = None, app_signature: str = None, **kwargs) -> None:
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

*   `key` (str): Ключ API.
*   `secret` (str): Секрет API.
*   `language` (model_Language): Язык, используемый для запросов API.
*   `currency` (model_Currency): Валюта, используемая для запросов API.
*   `tracking_id` (str, optional): Идентификатор отслеживания для партнерских ссылок. По умолчанию `None`.
*   `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.
*   `**kwargs`: Дополнительные параметры.

**Как работает функция**:

1.  Сохраняет переданные параметры в атрибуты экземпляра класса.
2.  Устанавливает ключ и секрет API по умолчанию, используя функцию `setDefaultAppInfo` из модуля `.skd`.

```
A[Сохранение параметров]
|
B[Установка параметров API по умолчанию]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)
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

**Назначение**: Получает информацию о продуктах.

**Параметры**:

*   `product_ids` (str | list): Один или несколько идентификаторов продуктов или ссылок.
*   `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None` (включает все поля).
*   `country` (str, optional): Страна, для которой необходимо отфильтровать продукты. По умолчанию `None` (без фильтрации по стране).
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `list[model_Product]`: Список объектов `model_Product`, содержащих информацию о продуктах.

**Вызывает исключения**:

*   `ProductsNotFoudException`: Если продукты не найдены.
*   `InvalidArgumentException`: Если переданы неверные аргументы.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Преобразует идентификаторы продуктов в строку, разделенную запятыми.
2.  Создает объект запроса `AliexpressAffiliateProductdetailGetRequest`.
3.  Устанавливает параметры запроса, такие как идентификаторы продуктов, поля, страна, валюта и язык.
4.  Выполняет запрос к API с помощью функции `api_request`.
5.  Обрабатывает ответ API, преобразует его в список объектов `model_Product` и возвращает его.

```
A[Преобразование product_ids в строку]
|
B[Создание объекта запроса AliexpressAffiliateProductdetailGetRequest]
|
C[Установка параметров запроса]
|
D[Выполнение запроса к API с помощью api_request]
|
E[Обработка ответа API]
|
F[Преобразование ответа в список объектов model_Product]
|
G[Возврат списка объектов model_Product]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

product_ids = "1005000000000000,1005000000000001"
products = api.retrieve_product_details(product_ids=product_ids)
if products:
    for product in products:
        print(product.product_title)
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

*   `links` (str | list): Одна или несколько ссылок для преобразования.
*   `link_type` (model_LinkType, optional): Тип ссылки (NORMAL или HOTLINK). По умолчанию `model_LinkType.NORMAL`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `list[model_AffiliateLink]`: Список объектов `model_AffiliateLink`, содержащих партнерские ссылки.

**Вызывает исключения**:

*   `InvalidArgumentException`: Если переданы неверные аргументы.
*   `InvalidTrackingIdException`: Если не указан идентификатор отслеживания.
*   `ProductsNotFoudException`: Если продукты не найдены.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Проверяет, установлен ли идентификатор отслеживания.
2.  Преобразует список ссылок в строку, разделенную запятыми.
3.  Создает объект запроса `AliexpressAffiliateLinkGenerateRequest`.
4.  Устанавливает параметры запроса, такие как ссылки, тип ссылки и идентификатор отслеживания.
5.  Выполняет запрос к API с помощью функции `api_request`.
6.  Обрабатывает ответ API, преобразует его в список объектов `model_AffiliateLink` и возвращает его.

```
A[Проверка наличия tracking_id]
|
B[Преобразование links в строку]
|
C[Создание объекта запроса AliexpressAffiliateLinkGenerateRequest]
|
D[Установка параметров запроса]
|
E[Выполнение запроса к API с помощью api_request]
|
F[Обработка ответа API]
|
G[Преобразование ответа в список объектов model_AffiliateLink]
|
H[Возврат списка объектов model_AffiliateLink]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language, LinkType
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

links = "https://www.aliexpress.com/item/1005000000000000.html,https://www.aliexpress.com/item/1005000000000001.html"
affiliate_links = api.get_affiliate_links(links=links, link_type=LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(link)
```

### `get_hotproducts`

```python
def get_hotproducts(self, category_ids: str | list = None, delivery_days: int = None,\
                fields: str | list = None,\
                keywords: str = None,\
                max_sale_price: int = None,\
                min_sale_price: int = None,\
                page_no: int = None,\
                page_size: int = None,\
                platform_product_type: model_ProductType = None,\
                ship_to_country: str = None,\
                sort: model_SortBy = None,\
        **kwargs) -> model_HotProductsResponse:
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
        page_no (``int``):
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

**Назначение**: Выполняет поиск партнерских продуктов с высокой комиссией.

**Параметры**:

*   `category_ids` (str | list, optional): Один или несколько идентификаторов категорий. По умолчанию `None`.
*   `delivery_days` (int, optional): Ожидаемое количество дней доставки. По умолчанию `None`.
*   `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None` (включает все поля).
*   `keywords` (str, optional): Ключевые слова для поиска продуктов. По умолчанию `None`.
*   `max_sale_price` (int, optional): Максимальная цена продажи. По умолчанию `None`. Цены указываются в наименьшей валютной деноминации (например, $31.41 следует указывать как 3141).
*   `min_sale_price` (int, optional): Минимальная цена продажи. По умолчанию `None`. Цены указываются в наименьшей валютной деноминации (например, $31.41 следует указывать как 3141).
*   `page_no` (int, optional): Номер страницы. По умолчанию `None`.
*   `page_size` (int, optional): Количество продуктов на странице (от 1 до 50). По умолчанию `None`.
*   `platform_product_type` (model_ProductType, optional): Тип продукта платформы. По умолчанию `None`.
*   `ship_to_country` (str, optional): Страна доставки. По умолчанию `None`.
*   `sort` (model_SortBy, optional): Метод сортировки. По умолчанию `None`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `model_HotProductsResponse`: Объект `model_HotProductsResponse`, содержащий информацию об ответе и список продуктов.

**Вызывает исключения**:

*   `ProductsNotFoudException`: Если продукты не найдены.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Создает объект запроса `AliexpressAffiliateHotproductQueryRequest`.
2.  Устанавливает параметры запроса, такие как идентификаторы категорий, дни доставки, поля, ключевые слова, минимальная и максимальная цена, номер страницы, размер страницы, тип продукта платформы, страна доставки и метод сортировки.
3.  Выполняет запрос к API с помощью функции `api_request`.
4.  Обрабатывает ответ API, преобразует его в список объектов `model_Product` и возвращает его в объекте `model_HotProductsResponse`.

```
A[Создание объекта запроса AliexpressAffiliateHotproductQueryRequest]
|
B[Установка параметров запроса]
|
C[Выполнение запроса к API с помощью api_request]
|
D[Обработка ответа API]
|
E[Преобразование ответа в список объектов model_Product]
|
F[Возврат объекта model_HotProductsResponse]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language, SortBy
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

category_ids = "200000000"
hot_products = api.get_hotproducts(category_ids=category_ids, sort=SortBy.COMMISSION_RATE_UP)
if hot_products and hot_products.products:
    for product in hot_products.products:
        print(product.product_title)
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

**Параметры**:

*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `list[model_Category | model_ChildCategory]`: Список объектов `model_Category` и `model_ChildCategory`, содержащих информацию о категориях.

**Вызывает исключения**:

*   `CategoriesNotFoudException`: Если категории не найдены.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Создает объект запроса `AliexpressAffiliateCategoryGetRequest`.
2.  Выполняет запрос к API с помощью функции `api_request`.
3.  Обрабатывает ответ API, преобразует его в список объектов `model_Category` и `model_ChildCategory` и сохраняет его в атрибуте `categories` экземпляра класса.
4.  Возвращает список категорий.

```
A[Создание объекта запроса AliexpressAffiliateCategoryGetRequest]
|
B[Выполнение запроса к API с помощью api_request]
|
C[Обработка ответа API]
|
D[Сохранение категорий в атрибуте categories]
|
E[Возврат списка категорий]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

categories = api.get_categories()
if categories:
    for category in categories:
        print(category.category_name)
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

*   `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `list[model_Category]`: Список объектов `model_Category`, содержащих информацию о родительских категориях.

**Вызывает исключения**:

*   `CategoriesNotFoudException`: Если категории не найдены.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Проверяет, нужно ли использовать кэшированные категории и есть ли они в атрибуте `categories` экземпляра класса.
2.  Если кэш не используется или категории отсутствуют, вызывает метод `get_categories` для получения категорий из API.
3.  Фильтрует список категорий, чтобы получить только родительские категории, используя функцию `filter_parent_categories` из модуля `.helpers.categories`.
4.  Возвращает список родительских категорий.

```
A[Проверка использования кэша и наличия категорий]
|
B[Вызов get_categories, если кэш не используется или категории отсутствуют]
|
C[Фильтрация категорий для получения родительских категорий]
|
D[Возврат списка родительских категорий]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

parent_categories = api.get_parent_categories()
if parent_categories:
    for category in parent_categories:
        print(category.category_name)
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

**Назначение**: Получает все доступные дочерние категории для определенной родительской категории.

**Параметры**:

*   `parent_category_id` (int): Идентификатор родительской категории.
*   `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `list[model_ChildCategory]`: Список объектов `model_ChildCategory`, содержащих информацию о дочерних категориях.

**Вызывает исключения**:

*   `CategoriesNotFoudException`: Если категории не найдены.
*   `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
*   `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:

1.  Проверяет, нужно ли использовать кэшированные категории и есть ли они в атрибуте `categories` экземпляра класса.
2.  Если кэш не используется или категории отсутствуют, вызывает метод `get_categories` для получения категорий из API.
3.  Фильтрует список категорий, чтобы получить только дочерние категории для указанной родительской категории, используя функцию `filter_child_categories` из модуля `.helpers.categories`.
4.  Возвращает список дочерних категорий.

```
A[Проверка использования кэша и наличия категорий]
|
B[Вызов get_categories, если кэш не используется или категории отсутствуют]
|
C[Фильтрация категорий для получения дочерних категорий]
|
D[Возврат списка дочерних категорий]
```

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Currency, Language
from src.suppliers.aliexpress.api.api import AliexpressApi

key = "your_api_key"
secret = "your_api_secret"
language = Language.RU
currency = Currency.RUB
tracking_id = "your_tracking_id"

api = AliexpressApi(key=key, secret=secret, language=language, currency=currency, tracking_id=tracking_id)

parent_category_id = 200000000
child_categories = api.get_child_categories(parent_category_id=parent_category_id)
if child_categories:
    for category in child_categories:
        print(category.category_name)