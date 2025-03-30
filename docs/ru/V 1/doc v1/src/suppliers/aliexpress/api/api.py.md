# Модуль `src.suppliers.aliexpress.api.api`

## Обзор

Модуль предоставляет класс `AliexpressApi`, который является оберткой для API AliExpress Open Platform. Он упрощает получение информации о товарах и создание партнерских ссылок AliExpress с использованием официального API.

## Подробней

Этот модуль позволяет взаимодействовать с API AliExpress, используя ключи API для получения информации о продуктах, создания партнерских ссылок и получения категорий продуктов. Он включает в себя обработку ошибок и моделей данных для представления информации, полученной из API.

## Классы

### `AliexpressApi`

**Описание**:
Предоставляет методы для получения информации из AliExpress с использованием учетных данных API.

**Параметры**:
- `key` (str): Ваш ключ API.
- `secret` (str): Ваш секрет API.
- `language` (model_Language): Код языка. По умолчанию EN.
- `currency` (model_Currency): Код валюты. По умолчанию USD.
- `tracking_id` (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AliexpressApi`.
- `retrieve_product_details`: Получает информацию о товарах.
- `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
- `get_hotproducts`: Поиск партнерских продуктов с высокой комиссией.
- `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
- `get_parent_categories`: Получает все доступные родительские категории.
- `get_child_categories`: Получает все доступные дочерние категории для определенной родительской категории.

### `AliexpressApi.__init__`

```python
    def __init__(
        self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs
    ):
        """
        Args:
            key (str): Ваш ключ API.
            secret (str): Ваш секрет API.
            language (model_Language): Код языка. По умолчанию EN.
            currency (model_Currency): Код валюты. По умолчанию USD.
            tracking_id (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
            app_signature (str, optional): Подпись приложения. По умолчанию `None`.
        """
        ...
```

**Описание**: Инициализирует экземпляр класса `AliexpressApi`.

**Параметры**:
- `key` (str): Ключ API.
- `secret` (str): Секрет API.
- `language` (model_Language): Код языка.
- `currency` (model_Currency): Код валюты.
- `tracking_id` (str, optional): Идентификатор отслеживания. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

**Примеры**:
```python
api = AliexpressApi(
    key='your_api_key', 
    secret='your_api_secret', 
    language=model_Language.EN, 
    currency=model_Currency.USD, 
    tracking_id='your_tracking_id'
)
```

### `AliexpressApi.retrieve_product_details`

```python
    def retrieve_product_details(
        self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs
    ) -> List[model_Product]:
        """
        Args:
            product_ids (str | list): Один или несколько ID товаров или ссылок.
            fields (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию все поля.
            country (str, optional): Фильтр товаров, которые могут быть отправлены в данную страну. Возвращает цену в соответствии с налоговой политикой страны.

        Returns:
            List[model_Product]: Список товаров.

        Raises:
            ProductsNotFoudException: Если товары не найдены.
            InvalidArgumentException: Если передан неверный аргумент.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Получает информацию о товарах.

**Параметры**:
- `product_ids` (str | list): Один или несколько ID товаров или ссылок.
- `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None`, что означает все поля.
- `country` (str, optional): Фильтр товаров, которые могут быть отправлены в данную страну. Возвращает цену в соответствии с налоговой политикой страны. По умолчанию `None`.

**Возвращает**:
- `List[model_Product]`: Список товаров.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `InvalidArgumentException`: Если передан неверный аргумент.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
product_ids = ['1234567890', '0987654321']
products = api.retrieve_product_details(product_ids=product_ids, fields=['product_title', 'product_price'], country='US')
if products:
    for product in products:
        print(f'Product Title: {product.product_title}')
        print(f'Product Price: {product.product_price}')
```

### `AliexpressApi.get_affiliate_links`

```python
    def get_affiliate_links(
        self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs
    ) -> List[model_AffiliateLink]:
        """
        Args:
            links (str | list): Одна или несколько ссылок для преобразования.
            link_type (model_LinkType, optional): Тип ссылки. Может быть NORMAL (стандартная комиссия) или HOTLINK (высокая комиссия). По умолчанию NORMAL.

        Returns:
            List[model_AffiliateLink]: Список партнерских ссылок.

        Raises:
            InvalidArgumentException: Если передан неверный аргумент.
            InvalidTrackingIdException: Если не указан идентификатор отслеживания.
            ProductsNotFoudException: Если товары не найдены.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Преобразует список ссылок в партнерские ссылки.

**Параметры**:
- `links` (str | list): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки. Может быть `NORMAL` (стандартная комиссия) или `HOTLINK` (высокая комиссия). По умолчанию `NORMAL`.

**Возвращает**:
- `List[model_AffiliateLink]`: Список партнерских ссылок.

**Вызывает исключения**:
- `InvalidArgumentException`: Если передан неверный аргумент.
- `InvalidTrackingIdException`: Если не указан идентификатор отслеживания.
- `ProductsNotFoudException`: Если товары не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
links = ['https://www.aliexpress.com/item/1234567890.html', 'https://www.aliexpress.com/item/0987654321.html']
affiliate_links = api.get_affiliate_links(links=links, link_type=model_LinkType.HOTLINK)
if affiliate_links:
    for link in affiliate_links:
        print(f'Affiliate Link: {link}')
```

### `AliexpressApi.get_hotproducts`

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
        **kwargs
    ) -> model_HotProductsResponse:
        """
        Args:
            category_ids (str | list, optional): Один или несколько ID категорий. По умолчанию `None`.
            delivery_days (int, optional): Предполагаемое количество дней доставки. По умолчанию `None`.
            fields (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None`, что означает все поля.
            keywords (str, optional): Ключевые слова для поиска товаров. По умолчанию `None`.
            max_sale_price (int, optional): Фильтр товаров с ценой ниже указанного значения. Цены указываются в наименьшей валютной деноминации. Например, $31.41 следует указывать как 3141. По умолчанию `None`.
            min_sale_price (int, optional): Фильтр товаров с ценой выше указанного значения. Цены указываются в наименьшей валютной деноминации. Например, $31.41 следует указывать как 3141. По умолчанию `None`.
            page_no (int, optional): Номер страницы. По умолчанию `None`.
            page_size (int, optional): Количество товаров на странице. Должно быть между 1 и 50. По умолчанию `None`.
            platform_product_type (model_ProductType, optional): Тип товара на платформе. По умолчанию `None`.
            ship_to_country (str, optional): Фильтр товаров, которые могут быть отправлены в данную страну. Возвращает цену в соответствии с налоговой политикой страны. По умолчанию `None`.
            sort (model_SortBy, optional): Метод сортировки. По умолчанию `None`.

        Returns:
            model_HotProductsResponse: Объект, содержащий информацию об ответе и список товаров.

        Raises:
            ProductsNotFoudException: Если товары не найдены.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Поиск партнерских продуктов с высокой комиссией.

**Параметры**:
- `category_ids` (str | list, optional): Один или несколько ID категорий. По умолчанию `None`.
- `delivery_days` (int, optional): Предполагаемое количество дней доставки. По умолчанию `None`.
- `fields` (str | list, optional): Список полей, которые необходимо включить в результаты. По умолчанию `None`, что означает все поля.
- `keywords` (str, optional): Ключевые слова для поиска товаров. По умолчанию `None`.
- `max_sale_price` (int, optional): Фильтр товаров с ценой ниже указанного значения. Цены указываются в наименьшей валютной деноминации. Например, $31.41 следует указывать как 3141. По умолчанию `None`.
- `min_sale_price` (int, optional): Фильтр товаров с ценой выше указанного значения. Цены указываются в наименьшей валютной деноминации. Например, $31.41 следует указывать как 3141. По умолчанию `None`.
- `page_no` (int, optional): Номер страницы. По умолчанию `None`.
- `page_size` (int, optional): Количество товаров на странице. Должно быть между 1 и 50. По умолчанию `None`.
- `platform_product_type` (model_ProductType, optional): Тип товара на платформе. По умолчанию `None`.
- `ship_to_country` (str, optional): Фильтр товаров, которые могут быть отправлены в данную страну. Возвращает цену в соответствии с налоговой политикой страны. По умолчанию `None`.
- `sort` (model_SortBy, optional): Метод сортировки. По умолчанию `None`.

**Возвращает**:
- `model_HotProductsResponse`: Объект, содержащий информацию об ответе и список товаров.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
hot_products = api.get_hotproducts(category_ids=['123', '456'], keywords='example', min_sale_price=1000, max_sale_price=5000, ship_to_country='US')
if hot_products and hot_products.products:
    for product in hot_products.products:
        print(f'Product Title: {product.product_title}')
        print(f'Product Price: {product.product_price}')
```

### `AliexpressApi.get_categories`

```python
    def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
        """
        Returns:
            list[model_Category | model_ChildCategory]: Список категорий.

        Raises:
            CategoriesNotFoudException: Если категории не найдены.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Получает все доступные категории, как родительские, так и дочерние.

**Возвращает**:
- `List[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
categories = api.get_categories()
if categories:
    for category in categories:
        print(f'Category ID: {category.category_id}, Category Name: {category.category_name}')
```

### `AliexpressApi.get_parent_categories`

```python
    def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
        """
        Args:
            use_cache (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

        Returns:
            List[model_Category]: Список родительских категорий.

        Raises:
            CategoriesNotFoudException: Если категории не найдены.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Получает все доступные родительские категории.

**Параметры**:
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `List[model_Category]`: Список родительских категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
parent_categories = api.get_parent_categories(use_cache=True)
if parent_categories:
    for category in parent_categories:
        print(f'Parent Category ID: {category.category_id}, Category Name: {category.category_name}')
```

### `AliexpressApi.get_child_categories`

```python
    def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
        """
        Args:
            parent_category_id (int): ID родительской категории.
            use_cache (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

        Returns:
            List[model_ChildCategory]: Список дочерних категорий.

        Raises:
            CategoriesNotFoudException: Если категории не найдены.
            ApiRequestException: Если произошла ошибка при запросе к API.
            ApiRequestResponseException: Если произошла ошибка в ответе от API.
        """
        ...
```

**Описание**: Получает все доступные дочерние категории для определенной родительской категории.

**Параметры**:
- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `List[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Примеры**:

```python
child_categories = api.get_child_categories(parent_category_id=123, use_cache=True)
if child_categories:
    for category in child_categories:
        print(f'Child Category ID: {category.category_id}, Category Name: {category.category_name}')
```