# Модуль API AliExpress

## Обзор

Модуль предоставляет обертку для API AliExpress Open Platform на языке Python. Он упрощает получение информации о товарах и партнерских ссылок с AliExpress с использованием официального API.

## Подробнее

Этот модуль предназначен для работы с API AliExpress. Он предоставляет классы и функции для выполнения различных операций, таких как получение информации о товарах, создание партнерских ссылок и получение категорий товаров. Модуль использует классы моделей данных для представления различных сущностей, таких как товары, категории и партнерские ссылки.

## Классы

### `AliexpressApi`

**Описание**: Предоставляет методы для получения информации с AliExpress с использованием ваших API-ключей.

**Принцип работы**:
Класс `AliexpressApi` инициализируется с использованием ключа API, секрета, языка, валюты и идентификатора отслеживания. Он предоставляет методы для получения информации о товарах, создания партнерских ссылок и получения категорий. Класс использует другие модули в пакете, такие как `skd` для установки информации о приложении по умолчанию, `helpers` для выполнения API-запросов и разбора ответов, а также `models` для представления данных.

**Аттрибуты**:
- `_key` (str): Ваш ключ API.
- `_secret` (str): Ваш секрет API.
- `_tracking_id` (str): Идентификатор отслеживания для генератора ссылок.
- `_language` (str): Код языка.
- `_currency` (str): Код валюты.
- `_app_signature` (str): Подпись приложения.
- `categories` (List[model_Category | model_ChildCategory] | None): Список категорий.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliexpressApi`.
- `retrieve_product_details`: Получает информацию о товарах.
- `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
- `get_hotproducts`: Поиск партнерских товаров с высокой комиссией.
- `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
- `get_parent_categories`: Получает все доступные родительские категории.
- `get_child_categories`: Получает все доступные дочерние категории для определенной родительской категории.

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
- `key` (str): Ваш ключ API.
- `secret` (str): Ваш секрет API.
- `language` (model_Language): Код языка.
- `currency` (model_Currency): Код валюты.
- `tracking_id` (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Функция инициализирует атрибуты экземпляра класса `AliexpressApi` с использованием предоставленных параметров.
2. Устанавливает информацию о приложении по умолчанию, используя функцию `setDefaultAppInfo` из модуля `skd`.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
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

**Назначение**: Получает информацию о товарах.

**Параметры**:
- `product_ids` (str | list): Один или несколько идентификаторов товаров или ссылок на товары.
- `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None` (все поля).
- `country` (str, optional): Страна, в которую может быть отправлен товар. Возвращает цену с учетом налоговой политики страны. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[model_Product]`: Список объектов `Product`, содержащих информацию о товарах.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `InvalidArgumentException`: Если предоставлены неверные аргументы.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Преобразует `product_ids` в список и затем в строку, разделенную запятыми.
2. Создает объект запроса `AliexpressAffiliateProductdetailGetRequest` из модуля `aliapi.rest`.
3. Устанавливает параметры запроса, такие как `app_signature`, `fields`, `product_ids`, `country`, `target_currency`, `target_language` и `tracking_id`.
4. Выполняет API-запрос с использованием функции `api_request` из модуля `helpers`.
5. Обрабатывает ответ от API:
   - Если `current_record_count` больше 0, разбирает товары с использованием функции `parse_products` и возвращает список объектов `Product`.
   - Если `current_record_count` равен 0, записывает предупреждение в лог и возвращает `None`.
   - Если возникает исключение, записывает ошибку в лог и возвращает `None`.

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
product_ids = ['1234567890', '0987654321']
products = api.retrieve_product_details(product_ids=product_ids, fields=['product_title', 'product_price'], country='US')
if products:
    for product in products:
        print(f'Product Title: {product.product_title}, Price: {product.product_price}')
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
- `link_type` (model_LinkType, optional): Тип ссылки: обычная (NORMAL) со стандартной комиссией или "горячая" (HOTLINK) с повышенной комиссией. По умолчанию `model_LinkType.NORMAL`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[model_AffiliateLink]`: Список объектов `AffiliateLink`, содержащих партнерские ссылки.

**Вызывает исключения**:
- `InvalidArgumentException`: Если предоставлены неверные аргументы.
- `InvalidTrackingIdException`: Если не указан идентификатор отслеживания.
- `ProductsNotFoudException`: Если товары не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Проверяет, установлен ли идентификатор отслеживания (`self._tracking_id`). Если он не установлен, записывает ошибку в лог и возвращает `None`.
2. Преобразует `links` в список и затем в строку, разделенную запятыми.
3. Создает объект запроса `AliexpressAffiliateLinkGenerateRequest` из модуля `aliapi.rest`.
4. Устанавливает параметры запроса, такие как `app_signature`, `source_values`, `promotion_link_type` и `tracking_id`.
5. Выполняет API-запрос с использованием функции `api_request` из модуля `helpers`.
6. Обрабатывает ответ от API:
   - Если `total_result_count` больше 0, возвращает список объектов `AffiliateLink` из `response.promotion_links.promotion_link`.
   - Если `total_result_count` равен 0, записывает предупреждение в лог и возвращает `None`.

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency, LinkType

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
links = ['https://www.aliexpress.com/item/1234567890.html', 'https://www.aliexpress.com/item/0987654321.html']
affiliate_links = api.get_affiliate_links(links=links, link_type=LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(f'Affiliate Link: {link}')
```

### `get_hotproducts`

```python
def get_hotproducts(self, category_ids: str | list = None, delivery_days: int = None,
                        fields: str | list = None,
                        keywords: str = None,
                        max_sale_price: int = None,
                        min_sale_price: int = None,
                        page_no: int = None,
                        page_size: int = None,
                        platform_product_type: model_ProductType = None,
                        ship_to_country: str = None,
                        sort: model_SortBy = None,
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

**Назначение**: Поиск партнерских товаров с высокой комиссией.

**Параметры**:
- `category_ids` (str | list, optional): Один или несколько идентификаторов категорий. По умолчанию `None`.
- `delivery_days` (int, optional): Предполагаемое количество дней доставки. По умолчанию `None`.
- `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None` (все поля).
- `keywords` (str, optional): Ключевые слова для поиска товаров. По умолчанию `None`.
- `max_sale_price` (int, optional): Максимальная цена товара. Цены указываются в наименьшей валютной деноминации (например, 3141 для $31.41). По умолчанию `None`.
- `min_sale_price` (int, optional): Минимальная цена товара. Цены указываются в наименьшей валютной деноминации (например, 3141 для $31.41). По умолчанию `None`.
- `page_no` (int, optional): Номер страницы. По умолчанию `None`.
- `page_size` (int, optional): Количество товаров на странице (от 1 до 50). По умолчанию `None`.
- `platform_product_type` (model_ProductType, optional): Тип товара на платформе. По умолчанию `None`.
- `ship_to_country` (str, optional): Страна доставки товара. Возвращает цену с учетом налоговой политики страны. По умолчанию `None`.
- `sort` (model_SortBy, optional): Метод сортировки. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `model_HotProductsResponse`: Объект `HotProductsResponse`, содержащий информацию об ответе и список товаров.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Создает объект запроса `AliexpressAffiliateHotproductQueryRequest` из модуля `aliapi.rest`.
2. Устанавливает параметры запроса, такие как `app_signature`, `category_ids`, `delivery_days`, `fields`, `keywords`, `max_sale_price`, `min_sale_price`, `page_no`, `page_size`, `platform_product_type`, `ship_to_country`, `sort`, `target_currency` и `tracking_id`.
3. Выполняет API-запрос с использованием функции `api_request` из модуля `helpers`.
4. Обрабатывает ответ от API:
   - Если `current_record_count` больше 0, разбирает товары с использованием функции `parse_products` и возвращает объект `HotProductsResponse`.
   - Если `current_record_count` равен 0, вызывает исключение `ProductsNotFoudException`.

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency, SortBy

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
hot_products = api.get_hotproducts(category_ids=['123', '456'], keywords='shoes', sort=SortBy.PRICE_ASC)
if hot_products.products:
    for product in hot_products.products:
        print(f'Product Title: {product.product_title}, Price: {product.product_price}')
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
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[model_Category | model_ChildCategory]`: Список объектов `Category` и `ChildCategory`, представляющих категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Создает объект запроса `AliexpressAffiliateCategoryGetRequest` из модуля `aliapi.rest`.
2. Устанавливает параметр `app_signature`.
3. Выполняет API-запрос с использованием функции `api_request` из модуля `helpers`.
4. Обрабатывает ответ от API:
   - Если `total_result_count` больше 0, сохраняет категории в атрибут `self.categories` и возвращает их.
   - Если `total_result_count` равен 0, вызывает исключение `CategoriesNotFoudException`.

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
categories = api.get_categories()
if categories:
    for category in categories:
        print(f'Category ID: {category.category_id}, Name: {category.category_name}')
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
- `use_cache` (bool, optional): Использовать ли кэшированные категории для уменьшения количества API-запросов. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[model_Category]`: Список объектов `Category`, представляющих родительские категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Проверяет, следует ли использовать кэшированные категории (`use_cache`) и существуют ли они (`self.categories`). Если `use_cache` равно `False` или `self.categories` равны `None`, вызывает метод `self.get_categories()` для получения категорий.
2. Фильтрует родительские категории из списка всех категорий с использованием функции `filter_parent_categories` из модуля `helpers.categories`.

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
parent_categories = api.get_parent_categories()
if parent_categories:
    for category in parent_categories:
        print(f'Parent Category ID: {category.category_id}, Name: {category.category_name}')
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
- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использовать ли кэшированные категории для уменьшения количества API-запросов. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[model_ChildCategory]`: Список объектов `ChildCategory`, представляющих дочерние категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении API-запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Как работает функция**:
1. Проверяет, следует ли использовать кэшированные категории (`use_cache`) и существуют ли они (`self.categories`). Если `use_cache` равно `False` или `self.categories` равны `None`, вызывает метод `self.get_categories()` для получения категорий.
2. Фильтрует дочерние категории из списка всех категорий с использованием функции `filter_child_categories` из модуля `helpers.categories`, передавая идентификатор родительской категории (`parent_category_id`).

**Внутренние функции**: Отсутствуют.

**Примеры**:
```python
from src.suppliers.aliexpress.api.api import AliexpressApi
from src.suppliers.aliexpress.api.models import Language, Currency

api = AliexpressApi(key='your_api_key', secret='your_api_secret', language=Language.EN, currency=Currency.USD, tracking_id='your_tracking_id')
child_categories = api.get_child_categories(parent_category_id=123)
if child_categories:
    for category in child_categories:
        print(f'Child Category ID: {category.category_id}, Name: {category.category_name}')
```