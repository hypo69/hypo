# Модуль `hypotez/src/suppliers/aliexpress/api/api.py`

## Обзор

Данный модуль предоставляет обертку для API AliExpress Open Platform, позволяющую получать информацию о продуктах и аффилированных ссылках с использованием официального API. Модуль упрощает работу с API, предоставляя удобные методы для доступа к различным данным.

## Классы

### `AliexpressApi`

**Описание**: Класс `AliexpressApi` представляет собой обертку для API AliExpress, позволяющую получать информацию о продуктах, аффилированных ссылках и категориях.

**Методы**:

#### `retrieve_product_details`

**Описание**: Получает информацию о продуктах по заданным идентификаторам.

**Параметры**:

- `product_ids` (str | list[str]): Один или несколько идентификаторов продуктов или ссылок.
- `fields` (str | list[str], optional): Поля, которые нужно включить в результаты. По умолчанию - все поля.
- `country` (str, optional): Страна для фильтрации продуктов (возвращает цену с учетом налоговой политики страны).

**Возвращает**:

- list[model_Product]: Список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `InvalidArgumentException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_affiliate_links`

**Описание**: Преобразует список ссылок в аффилированные ссылки.

**Параметры**:

- `links` (str | list[str]): Один или несколько исходных URL-адресов.
- `link_type` (model_LinkType, optional): Тип ссылки (обычная или горячая, с повышенной комиссией). По умолчанию - `model_LinkType.NORMAL`.

**Возвращает**:

- list[model_AffiliateLink]: Список аффилированных ссылок.

**Вызывает исключения**:

- `InvalidArgumentException`
- `InvalidTrackingIdException`
- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_hotproducts`

**Описание**: Поиск аффилированных продуктов с высокой комиссией.

**Параметры**:

- `category_ids` (str | list[str], optional): Один или несколько идентификаторов категорий.
- `delivery_days` (int, optional): Ориентировочное количество дней доставки.
- `fields` (str | list[str], optional): Поля для включения в результаты. По умолчанию - все поля.
- `keywords` (str, optional): Поиск продуктов по ключевым словам.
- `max_sale_price` (int, optional): Фильтрация продуктов с ценой ниже указанной. Цена указывается в наименьшей денежной единице (например, $31.41 - это 3141).
- `min_sale_price` (int, optional): Фильтрация продуктов с ценой выше указанной. Цена указывается в наименьшей денежной единице.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Количество продуктов на странице (от 1 до 50).
- `platform_product_type` (model_ProductType, optional): Тип продукта платформы.
- `ship_to_country` (str, optional): Фильтрация продуктов, которые можно отправить в эту страну.
- `sort` (model_SortBy, optional): Способ сортировки.

**Возвращает**:

- model_HotProductsResponse: Содержит информацию о ответе и список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_categories`

**Описание**: Получает все доступные категории (родительские и дочерние).

**Возвращает**:

- list[model_Category | model_ChildCategory]: Список категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_parent_categories`

**Описание**: Получает все родительские категории.

**Параметры**:

- `use_cache` (bool, optional): Использовать кэш категорий для уменьшения запросов к API. По умолчанию - `True`.

**Возвращает**:

- list[model_Category]: Список родительских категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_child_categories`

**Описание**: Получает все дочерние категории для заданной родительской категории.

**Параметры**:

- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использовать кэш категорий для уменьшения запросов к API. По умолчанию - `True`.

**Возвращает**:

- list[model_ChildCategory]: Список дочерних категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


##  Функции

(Здесь перечисляются все функции модуля, если таковые есть)


## Модели

(Здесь перечисляются все модели, используемые в модуле, если таковые есть)