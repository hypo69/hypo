# Модуль `src.suppliers.aliexpress.api.api`

## Обзор

Модуль предоставляет обертку для работы с API AliExpress. Он упрощает получение информации о товарах и партнерских ссылок с использованием официального API AliExpress.

## Подробней

Этот модуль предоставляет класс `AliexpressApi`, который позволяет взаимодействовать с API AliExpress для получения информации о продуктах, создания партнерских ссылок и получения категорий товаров. Он использует ключи API, секреты и идентификаторы отслеживания для аутентификации и авторизации запросов к API AliExpress.

## Классы

### `AliexpressApi`

**Описание**: Предоставляет методы для получения информации с AliExpress, используя учетные данные API.

**Как работает класс**:
Класс `AliexpressApi` инициализируется с использованием ключа API, секрета, языка и валюты. Он предоставляет методы для получения деталей продукта, создания партнерских ссылок и запроса горячих продуктов. Класс также включает методы для получения категорий, родительских категорий и дочерних категорий.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliexpressApi` с предоставленными учетными данными API.
- `retrieve_product_details`: Получает информацию о продуктах.
- `get_affiliate_links`: Преобразует список ссылок в партнерские ссылки.
- `get_hotproducts`: Выполняет поиск партнерских продуктов с высокой комиссией.
- `get_categories`: Получает все доступные категории, как родительские, так и дочерние.
- `get_parent_categories`: Получает все доступные родительские категории.
- `get_child_categories`: Получает все доступные дочерние категории для указанной родительской категории.

```python
class AliexpressApi:
    """Provides methods to get information from AliExpress using your API credentials."""

    def __init__(self,
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
        self._key = key
        self._secret = secret
        self._tracking_id = tracking_id
        self._language = language
        self._currency = currency
        self._app_signature = app_signature
        self.categories = None
        setDefaultAppInfo(self._key, self._secret)
```

**Параметры**:
- `key` (str): Ваш ключ API.
- `secret` (str): Ваш секрет API.
- `language` (model_Language): Код языка. По умолчанию EN.
- `currency` (model_Currency): Код валюты. По умолчанию USD.
- `tracking_id` (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

```python
    def retrieve_product_details(self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs) -> List[model_Product]:
        """ Get products information.

        Args:
            product_ids (``str | list[str]``): One or more links or product IDs.
            fields (``str | list[str]``): The fields to include in the results. Defaults to all.
            country (``str``): Filter products that can be sent to that country. Returns the price
                according to the country\'s tax rate policy.

        Returns:
            ``list[model_Product]``: A list of products.

        Raises:
            ``ProductsNotFoudException``
            ``InvalidArgumentException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        product_ids = get_product_ids(product_ids)
        product_ids = get_list_as_string(product_ids)

        request = aliapi.rest.AliexpressAffiliateProductdetailGetRequest()
        request.app_signature = self._app_signature
        request.fields = get_list_as_string(fields)
        request.product_ids = product_ids
        request.country = country
        request.target_currency = self._currency.upper()
        request.target_language = self._language.upper()
        request.tracking_id = self._tracking_id

        response = api_request(request, 'aliexpress_affiliate_productdetail_get_response')
        try:
            if response.current_record_count > 0:
                response = parse_products(response.products.product)
                return response
            else:
                #raise ProductsNotFoudException('No products found with current parameters')
                logger.warning('No products found with current parameters')
                ...
                return
        except Exception as ex:
            logger.error(ex, exc_info=False)
            ...
            return
```

**Параметры**:
- `product_ids` (str | list): Одна или несколько ссылок или идентификаторов продуктов.
- `fields` (str | list, optional): Поля для включения в результаты. По умолчанию включает все поля.
- `country` (str, optional): Страна, в которую может быть отправлен продукт. Возвращает цену в соответствии с налоговой политикой страны.

**Возвращает**:
- `list[model_Product]`: Список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `InvalidArgumentException`: Если переданы неверные аргументы.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `retrieve_product_details` извлекает информацию о продуктах из API AliExpress.
2. Идентификаторы продуктов преобразуются в строку, разделенную запятыми.
3. Формируется запрос к API AliExpress для получения детальной информации о продуктах.
4. В запрос добавляются подпись приложения, список полей, идентификаторы продуктов, страна, валюта и язык.
5. Выполняется API-запрос и обрабатывается ответ.
6. Если продукты найдены, они преобразуются и возвращаются.
7. В случае отсутствия продуктов функция логирует предупреждение и возвращает `None`.
8. Если в процессе выполнения возникают исключения, они логируются и возвращается `None`.

```python
    def get_affiliate_links(self,
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
        if not self._tracking_id:
            #raise InvalidTrackingIdException('The tracking id is required for affiliate links')
            logger.error('The tracking id is required for affiliate links')
            return

        links = get_list_as_string(links)

        request = aliapi.rest.AliexpressAffiliateLinkGenerateRequest()
        request.app_signature = self._app_signature
        request.source_values = links
        request.promotion_link_type = link_type
        request.tracking_id = self._tracking_id
        ...
        response = api_request(request, 'aliexpress_affiliate_link_generate_response')
        if not response:
            return 
        if response.total_result_count > 0:
            return response.promotion_links.promotion_link
        else:
            #raise ProductsNotFoudException('Affiliate links not available')
            logger.warning('Affiliate links not available')
            return 
```

**Параметры**:
- `links` (str | list): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки: обычная или горячая. По умолчанию `NORMAL`.

**Возвращает**:
- `list[model_AffiliateLink]`: Список партнерских ссылок.

**Вызывает исключения**:
- `InvalidArgumentException`: Если передан неверный аргумент.
- `InvalidTrackingIdException`: Если отсутствует идентификатор отслеживания.
- `ProductsNotFoudException`: Если партнерские ссылки не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `get_affiliate_links` преобразует список обычных ссылок в партнерские ссылки AliExpress.
2. Проверяется наличие идентификатора отслеживания. Если он отсутствует, функция логирует ошибку и возвращает `None`.
3. Список ссылок преобразуется в строку, разделенную запятыми.
4. Формируется запрос к API AliExpress для генерации партнерских ссылок.
5. В запрос добавляются подпись приложения, список ссылок, тип ссылки и идентификатор отслеживания.
6. Выполняется API-запрос и обрабатывается ответ.
7. Если партнерские ссылки найдены, они возвращаются.
8. В случае отсутствия партнерских ссылок функция логирует предупреждение и возвращает `None`.

```python
    def get_hotproducts(self,
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
            page_no (``int``):
            page_size (``int``): Products on each page. Should be between 1 and 50.
            platform_product_type (``model_ProductType``): Specify platform product type.
            ship_to_country (``str``): Filter products that can be sent to that country.
                Returns the price according to the country\'s tax rate policy.
            sort (``model_SortBy``): Specifies the sort method.

        Returns:
            ``model_HotProductsResponse``: Contains response information and the list of products.

        Raises:
            ``ProductsNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        request = aliapi.rest.AliexpressAffiliateHotproductQueryRequest()
        request.app_signature = self._app_signature
        request.category_ids = get_list_as_string(category_ids)
        request.delivery_days = str(delivery_days)
        request.fields = get_list_as_string(fields)
        request.keywords = keywords
        request.max_sale_price = max_sale_price
        request.min_sale_price = min_sale_price
        request.page_no = page_no
        request.page_size = page_size
        request.platform_product_type = platform_product_type
        request.ship_to_country = ship_to_country
        request.sort = sort
        request.target_currency = self._currency
        request.target_language = self._language
        request.tracking_id = self._tracking_id

        response = api_request(request, 'aliexpress_affiliate_hotproduct_query_response')

        if response.current_record_count > 0:
            response.products = parse_products(response.products.product)
            return response
        else:
            raise ProductsNotFoudException('No products found with current parameters')
```

**Параметры**:
- `category_ids` (str | list, optional): Одна или несколько категорий ID.
- `delivery_days` (int, optional): Предполагаемое количество дней доставки.
- `fields` (str | list, optional): Поля для включения в результаты. По умолчанию включает все поля.
- `keywords` (str, optional): Ключевые слова для поиска продуктов.
- `max_sale_price` (int, optional): Максимальная цена продажи.
- `min_sale_price` (int, optional): Минимальная цена продажи.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Количество продуктов на странице. Должно быть между 1 и 50.
- `platform_product_type` (model_ProductType, optional): Тип продукта платформы.
- `ship_to_country` (str, optional): Страна доставки.
- `sort` (model_SortBy, optional): Метод сортировки.

**Возвращает**:
- `model_HotProductsResponse`: Ответ, содержащий информацию и список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `get_hotproducts` выполняет поиск партнерских продуктов с высокой комиссией на AliExpress.
2. Формируется запрос к API AliExpress для поиска популярных продуктов.
3. В запрос добавляются подпись приложения, категории ID, количество дней доставки, список полей, ключевые слова, максимальная и минимальная цены, номер страницы, размер страницы, тип продукта платформы, страна доставки и метод сортировки.
4. Выполняется API-запрос и обрабатывается ответ.
5. Если продукты найдены, они преобразуются и возвращаются в объекте `model_HotProductsResponse`.
6. В случае отсутствия продуктов выбрасывается исключение `ProductsNotFoudException`.

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
        request = aliapi.rest.AliexpressAffiliateCategoryGetRequest()
        request.app_signature = self._app_signature

        response = api_request(request, 'aliexpress_affiliate_category_get_response')

        if response.total_result_count > 0:
            self.categories = response.categories.category
            return self.categories
        else:
            raise CategoriesNotFoudException('No categories found')
```

**Возвращает**:
- `list[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `get_categories` получает все доступные категории (родительские и дочерние) из API AliExpress.
2. Формируется запрос к API AliExpress для получения категорий.
3. В запрос добавляется подпись приложения.
4. Выполняется API-запрос и обрабатывается ответ.
5. Если категории найдены, они сохраняются в атрибуте `categories` экземпляра класса и возвращаются.
6. В случае отсутствия категорий выбрасывается исключение `CategoriesNotFoudException`.

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
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_parent_categories(self.categories)
```

**Параметры**:
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `list[model_Category]`: Список родительских категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `get_parent_categories` получает все доступные родительские категории из API AliExpress.
2. Проверяется, нужно ли использовать кэшированные категории. Если кэш не используется или категории еще не были загружены, вызывается метод `get_categories` для получения категорий из API.
3. Вызывается функция `filter_parent_categories` для фильтрации родительских категорий из списка всех категорий.
4. Возвращается список родительских категорий.

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
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_child_categories(self.categories, parent_category_id)
```

**Параметры**:
- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `list[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если произошла ошибка в ответе от API.

**Как работает функция**:
1. Функция `get_child_categories` получает все доступные дочерние категории для указанной родительской категории из API AliExpress.
2. Проверяется, нужно ли использовать кэшированные категории. Если кэш не используется или категории еще не были загружены, вызывается метод `get_categories` для получения категорий из API.
3. Вызывается функция `filter_child_categories` для фильтрации дочерних категорий из списка всех категорий на основе идентификатора родительской категории.
4. Возвращается список дочерних категорий.