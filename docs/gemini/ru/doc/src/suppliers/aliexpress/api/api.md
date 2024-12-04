# Модуль `hypotez/src/suppliers/aliexpress/api/api.py`

## Обзор

Модуль `hypotez/src/suppliers/aliexpress/api/api.py` предоставляет обёртку для API AliExpress Open Platform на Python. Он позволяет получать информацию о продуктах и аффилированные ссылки с использованием официального API AliExpress в более удобном формате. Модуль включает методы для получения подробностей о продуктах, генерации аффилированных ссылок, поиска популярных продуктов и получения категорий продуктов.

## Классы

### `AliexpressApi`

**Описание**:  Класс `AliexpressApi` предоставляет методы для взаимодействия с API AliExpress.  Он хранит и использует API ключи, секреты и другие параметры для запросов.

**Методы**:

#### `retrieve_product_details`

**Описание**: Получает информацию о продуктах по заданным идентификаторам.

**Параметры**:
- `product_ids` (str | list[str]): Один или несколько идентификаторов продуктов или ссылок.
- `fields` (str | list[str], optional): Список полей, которые необходимо включить в результат. По умолчанию - все поля.
- `country` (str, optional): Страна доставки. Возвращает цену с учетом налогов и политики страны.

**Возвращает**:
- list[model_Product]: Список объектов `model_Product` с информацией о продуктах.

**Возможные исключения**:
- `ProductsNotFoudException`: Нет продуктов, соответствующих запросу.
- `InvalidArgumentException`: Некорректные параметры запроса.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.


#### `get_affiliate_links`

**Описание**: Преобразует список ссылок в аффилированные ссылки.

**Параметры**:
- `links` (str | list[str]): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (обычная или горячая). По умолчанию - обычная.

**Возвращает**:
- list[model_AffiliateLink]: Список объектов `model_AffiliateLink` с информацией об аффилированных ссылках.

**Возможные исключения**:
- `InvalidArgumentException`: Некорректные параметры запроса.
- `InvalidTrackingIdException`: Не задан идентификатор отслеживания.
- `ProductsNotFoudException`: Аффилированные ссылки недоступны.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.


#### `get_hotproducts`

**Описание**:  Ищет популярные продукты с высокой комиссией.

**Параметры**:
- `category_ids` (str | list[str], optional): Идентификаторы категорий.
- `delivery_days` (int, optional): Ожидаемое количество дней доставки.
- `fields` (str | list[str], optional): Список полей для включения в результат. По умолчанию - все поля.
- `keywords` (str, optional): Ключевые слова для поиска продуктов.
- `max_sale_price` (int, optional): Максимальная цена продукта.
- `min_sale_price` (int, optional): Минимальная цена продукта.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Размер страницы.
- `platform_product_type` (model_ProductType, optional): Тип продукта.
- `ship_to_country` (str, optional): Страна доставки.
- `sort` (model_SortBy, optional): Сортировка.

**Возвращает**:
- model_HotProductsResponse: Объект с информацией о популярных продуктах.

**Возможные исключения**:
- `ProductsNotFoudException`: Нет продуктов, соответствующих запросу.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.


#### `get_categories`

**Описание**: Получает список всех доступных категорий (родительских и дочерних).

**Возвращает**:
- list[model_Category | model_ChildCategory]: Список категорий.

**Возможные исключения**:
- `CategoriesNotFoudException`: Нет категорий, соответствующих запросу.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.


#### `get_parent_categories`

**Описание**: Получает список родительских категорий.

**Параметры**:
- `use_cache` (bool, optional): Использует кэшированные данные (по умолчанию True).

**Возвращает**:
- list[model_Category]: Список родительских категорий.

**Возможные исключения**:
- `CategoriesNotFoudException`: Нет категорий, соответствующих запросу.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.


#### `get_child_categories`

**Описание**: Получает список дочерних категорий для указанной родительской категории.

**Параметры**:
- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использует кэшированные данные (по умолчанию True).

**Возвращает**:
- list[model_ChildCategory]: Список дочерних категорий.

**Возможные исключения**:
- `CategoriesNotFoudException`: Нет категорий, соответствующих запросу.
- `ApiRequestException`: Ошибка при выполнении запроса к API.
- `ApiRequestResponseException`: Ошибка при обработке ответа API.