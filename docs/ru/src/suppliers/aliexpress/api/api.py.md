# Модуль `src.suppliers.aliexpress.api`

## Обзор

Модуль предоставляет обертку для API AliExpress для Python. Он упрощает получение информации о продуктах и партнерских ссылок с AliExpress, используя официальный API.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с API AliExpress. Он предоставляет удобные методы для получения информации о продуктах, создания партнерских ссылок и получения списка категорий. Модуль использует классы моделей данных для представления ответов API и обрабатывает ошибки, возвращая информативные исключения.

## Классы

### `AliexpressApi`

**Описание**:
Предоставляет методы для получения информации с AliExpress с использованием API credentials.

**Как работает класс**:
Класс `AliexpressApi` инициализируется с ключом API, секретом, языком и валютой. Он предоставляет методы для получения деталей продукта, создания партнерских ссылок и получения списка категорий. Класс также поддерживает кэширование категорий для уменьшения количества запросов к API.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliexpressApi` с ключом API, секретом, языком и валютой.
- `retrieve_product_details`: Получает информацию о продуктах.
- `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
- `get_hotproducts`: Поиск партнерских продуктов с высокой комиссией.
- `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
- `get_parent_categories`: Получает все доступные родительские категории.
- `get_child_categories`: Получает все доступные дочерние категории для определенной родительской категории.

**Параметры**:
- `key` (str): Ваш API key.
- `secret` (str): Ваш API secret.
- `language` (model_Language): Языковой код. По умолчанию EN.
- `currency` (model_Currency): Код валюты. По умолчанию USD.
- `tracking_id` (str, optional): The tracking id для link generator. По умолчанию None.
- `app_signature` (str, optional): Подпись приложения. По умолчанию None.

### `__init__`

```python
def __init__(
        self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs):
    """
    Args:
        key (str): Your API key.
        secret (str): Your API secret.
        language (str): Language code. Defaults to EN.
        currency (str): Currency code. Defaults to USD.
        tracking_id (str): The tracking id for link generator. Defaults to None.
    """
```

**Как работает функция**:

Метод инициализации класса `AliexpressApi`. Он принимает ключ API, секрет, язык, валюту, tracking ID и подпись приложения. Он сохраняет эти значения в атрибутах экземпляра класса и инициализирует API.

**Параметры**:
- `key` (str): API ключ для доступа к AliExpress API.
- `secret` (str): Секретный ключ для доступа к AliExpress API.
- `language` (model_Language): Язык, на котором будут возвращены результаты (например, 'EN' для английского).
- `currency` (model_Currency): Валюта, в которой будут отображаться цены (например, 'USD' для долларов США).
- `tracking_id` (str, optional): ID отслеживания для партнерских ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

**Примеры**:

```python
aliexpress_api = AliexpressApi(
    key='your_api_key',
    secret='your_api_secret',
    language=model_Language.EN,
    currency=model_Currency.USD,
    tracking_id='your_tracking_id'
)
```

### `retrieve_product_details`

```python
def retrieve_product_details(
        self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs) -> List[model_Product]:
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

**Как работает функция**:

Метод `retrieve_product_details` используется для получения информации о продуктах из AliExpress по их ID. Он принимает ID продуктов, список полей для включения в результаты и страну для фильтрации продуктов. Он возвращает список объектов `model_Product` с информацией о продуктах.  Функция сначала преобразует входные `product_ids` в строку, разделенную запятыми. Затем формируется запрос к API AliExpress для получения детальной информации о продуктах. Если продукты найдены, они парсятся и возвращаются в виде списка. Если продукты не найдены, в лог записывается предупреждение.

**Параметры**:
- `product_ids` (str | list): ID продукта или список ID продуктов для получения информации.
- `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None` (все поля).
- `country` (str, optional): Страна, в которую может быть отправлен продукт. Используется для получения цены с учетом налогов. По умолчанию `None`.

**Возвращает**:
- `list[model_Product]`: Список объектов `model_Product`, содержащих информацию о продуктах.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `InvalidArgumentException`: Если переданы неверные аргументы.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
product_ids = ['1234567890', '0987654321']
products = aliexpress_api.retrieve_product_details(product_ids=product_ids, fields=['product_title', 'product_price'], country='US')
if products:
    for product in products:
        print(f'Product Title: {product.product_title}, Price: {product.product_price}')
```

### `get_affiliate_links`

```python
def get_affiliate_links(
        self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs) -> List[model_AffiliateLink]:
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

**Как работает функция**:

Метод `get_affiliate_links` преобразует список ссылок в партнерские ссылки AliExpress. Он принимает список ссылок и тип ссылки (обычная или горячая) в качестве аргументов. Для работы этого метода требуется `tracking_id`. Если `tracking_id` не указан, будет зарегистрирована ошибка. Функция возвращает список объектов `model_AffiliateLink`, содержащих партнерские ссылки. Сначала проверяется наличие `tracking_id`. Если он отсутствует, функция завершается и возвращает `None`. Затем формируется запрос к API AliExpress для генерации партнерских ссылок. Если ссылки сгенерированы успешно, они возвращаются в виде списка. В противном случае в лог записывается предупреждение.

**Параметры**:
- `links` (str | list): Ссылка или список ссылок для конвертации в партнерские ссылки.
- `link_type` (model_LinkType, optional): Тип ссылки (обычная или горячая). По умолчанию `model_LinkType.NORMAL`.

**Возвращает**:
- `list[model_AffiliateLink]`: Список объектов `model_AffiliateLink`, содержащих партнерские ссылки.

**Вызывает исключения**:
- `InvalidArgumentException`: Если переданы неверные аргументы.
- `InvalidTrackingIdException`: Если не указан `tracking_id`.
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
links = ['https://www.aliexpress.com/item/1234567890.html', 'https://www.aliexpress.com/item/0987654321.html']
affiliate_links = aliexpress_api.get_affiliate_links(links=links, link_type=model_LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(f'Affiliate Link: {link}')
```

### `get_hotproducts`

```python
def get_hotproducts(
        self,
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

**Как работает функция**:

Метод `get_hotproducts` выполняет поиск партнерских продуктов с высокой комиссией на AliExpress. Он принимает различные параметры фильтрации, такие как ID категории, количество дней доставки, ключевые слова, минимальная и максимальная цена, номер страницы, размер страницы, тип продукта платформы, страна доставки и метод сортировки. Метод возвращает объект `model_HotProductsResponse`, содержащий информацию об ответе и список продуктов. Формируется запрос к API AliExpress с указанными параметрами. Если продукты найдены, они парсятся и возвращаются в виде объекта `model_HotProductsResponse`. Если продукты не найдены, выбрасывается исключение `ProductsNotFoudException`.

**Параметры**:
- `category_ids` (str | list, optional): ID категории или список ID категорий для поиска. По умолчанию `None`.
- `delivery_days` (int, optional): Количество дней доставки. По умолчанию `None`.
- `fields` (str | list, optional): Список полей для включения в результаты. По умолчанию `None` (все поля).
- `keywords` (str, optional): Ключевые слова для поиска продуктов. По умолчанию `None`.
- `max_sale_price` (int, optional): Максимальная цена продукта. По умолчанию `None`.
- `min_sale_price` (int, optional): Минимальная цена продукта. По умолчанию `None`.
- `page_no` (int, optional): Номер страницы результатов. По умолчанию `None`.
- `page_size` (int, optional): Количество продуктов на странице (от 1 до 50). По умолчанию `None`.
- `platform_product_type` (model_ProductType, optional): Тип продукта платформы. По умолчанию `None`.
- `ship_to_country` (str, optional): Страна доставки. По умолчанию `None`.
- `sort` (model_SortBy, optional): Метод сортировки результатов. По умолчанию `None`.

**Возвращает**:
- `model_HotProductsResponse`: Объект `model_HotProductsResponse`, содержащий информацию об ответе и список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
hot_products = aliexpress_api.get_hotproducts(category_ids=['123', '456'], keywords='electronics', ship_to_country='US')
if hot_products:
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

**Как работает функция**:

Метод `get_categories` используется для получения списка всех доступных категорий, как родительских, так и дочерних, из API AliExpress. Он не принимает никаких аргументов, кроме `kwargs`. Функция возвращает список объектов `model_Category` и `model_ChildCategory`, представляющих категории. Формируется запрос к API AliExpress для получения списка категорий. Если категории найдены, они сохраняются в атрибуте `categories` экземпляра класса и возвращаются в виде списка. Если категории не найдены, выбрасывается исключение `CategoriesNotFoudException`.

**Возвращает**:
- `list[model_Category | model_ChildCategory]`: Список объектов `model_Category` и `model_ChildCategory`, представляющих категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
categories = aliexpress_api.get_categories()
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

**Как работает функция**:

Метод `get_parent_categories` используется для получения списка всех доступных родительских категорий из API AliExpress. Он принимает аргумент `use_cache`, который определяет, использовать ли кэшированные категории для уменьшения количества запросов к API. Функция возвращает список объектов `model_Category`, представляющих родительские категории. Сначала проверяется, нужно ли использовать кэшированные категории. Если `use_cache` равен `True` и категории уже загружены, используется кэшированный список. В противном случае вызывается метод `get_categories` для получения списка категорий из API. Затем вызывается функция `filter_parent_categories` для фильтрации списка категорий и возврата только родительских категорий.

**Параметры**:
- `use_cache` (bool, optional): Определяет, использовать ли кэшированные категории. По умолчанию `True`.

**Возвращает**:
- `list[model_Category]`: Список объектов `model_Category`, представляющих родительские категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
parent_categories = aliexpress_api.get_parent_categories(use_cache=True)
if parent_categories:
    for category in parent_categories:
        print(f'Category ID: {category.category_id}, Name: {category.category_name}')
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

**Как работает функция**:

Метод `get_child_categories` используется для получения списка всех доступных дочерних категорий для определенной родительской категории из API AliExpress. Он принимает ID родительской категории `parent_category_id` и аргумент `use_cache`, который определяет, использовать ли кэшированные категории для уменьшения количества запросов к API. Функция возвращает список объектов `model_ChildCategory`, представляющих дочерние категории. Сначала проверяется, нужно ли использовать кэшированные категории. Если `use_cache` равен `True` и категории уже загружены, используется кэшированный список. В противном случае вызывается метод `get_categories` для получения списка категорий из API. Затем вызывается функция `filter_child_categories` для фильтрации списка категорий и возврата только дочерних категорий для указанной родительской категории.

**Параметры**:
- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Определяет, использовать ли кэшированные категории. По умолчанию `True`.

**Возвращает**:
- `list[model_ChildCategory]`: Список объектов `model_ChildCategory`, представляющих дочерние категории.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

```python
child_categories = aliexpress_api.get_child_categories(parent_category_id=123456, use_cache=True)
if child_categories:
    for category in child_categories:
        print(f'Category ID: {category.category_id}, Name: {category.category_name}')
```