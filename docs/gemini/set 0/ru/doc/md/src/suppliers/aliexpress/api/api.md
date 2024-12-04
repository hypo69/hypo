# Модуль `hypotez/src/suppliers/aliexpress/api/api.py`

## Обзор

Этот модуль предоставляет обертку для API AliExpress Open Platform на Python.  Он позволяет получать информацию о продуктах и аффилиатные ссылки с AliExpress, упрощая взаимодействие с официальным API.

## Классы

### `AliexpressApi`

**Описание**: Класс `AliexpressApi` предоставляет методы для получения информации с AliExpress, используя ваши API-ключи.

**Атрибуты**:

- `_key` (str): Ваш API ключ.
- `_secret` (str): Ваш API секрет.
- `_tracking_id` (str): ID отслеживания для генерации ссылок. По умолчанию `None`.
- `_language` (model_Language): Код языка. По умолчанию EN.
- `_currency` (model_Currency): Код валюты. По умолчанию USD.
- `_app_signature` (str): Подпись приложения.
- `categories` (list): Кэшированные категории.


**Методы**:

#### `retrieve_product_details`

**Описание**: Получение информации о продуктах по их ID или ссылкам.

**Параметры**:

- `product_ids` (str | list[str]): Один или несколько ID или ссылок на продукты.
- `fields` (str | list[str], optional): Поля, которые необходимо включить в результаты. По умолчанию все поля.
- `country` (str, optional): Страна доставки для фильтрации продуктов и отображения цен с учетом налогов.

**Возвращает**:

- list[model_Product]: Список объектов `model_Product` с информацией о продуктах.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `InvalidArgumentException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_affiliate_links`

**Описание**: Преобразование списка ссылок в аффилиатные ссылки.

**Параметры**:

- `links` (str | list[str]): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (обычная или горячая). По умолчанию `model_LinkType.NORMAL`.

**Возвращает**:

- list[model_AffiliateLink]: Список объектов `model_AffiliateLink` с аффилиатными ссылками.

**Вызывает исключения**:

- `InvalidArgumentException`
- `InvalidTrackingIdException`
- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_hotproducts`

**Описание**: Поиск горячих продуктов с высокой комиссией.

**Параметры**:

- `category_ids` (str | list[str], optional): ID категорий для фильтрации.
- `delivery_days` (int, optional): Ожидаемые дни доставки.
- `fields` (str | list[str], optional): Поля для включения в результат.
- `keywords` (str, optional): Ключевые слова для поиска.
- `max_sale_price` (int, optional): Максимальная цена.
- `min_sale_price` (int, optional): Минимальная цена.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Количество продуктов на странице.
- `platform_product_type` (model_ProductType, optional): Тип продукта.
- `ship_to_country` (str, optional): Страна доставки.
- `sort` (model_SortBy, optional): Способ сортировки.

**Возвращает**:

- model_HotProductsResponse: Объект содержащий информацию о результате и список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_categories`

**Описание**: Получение всех доступных категорий (родительских и дочерних).

**Возвращает**:

- list[model_Category | model_ChildCategory]: Список категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_parent_categories`

**Описание**: Получение всех родительских категорий.

**Параметры**:

- `use_cache` (bool, optional): Использует кэшированные категории для уменьшения запросов к API. По умолчанию `True`.

**Возвращает**:

- list[model_Category]: Список родительских категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


#### `get_child_categories`

**Описание**: Получение всех дочерних категорий для конкретной родительской категории.

**Параметры**:

- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Использует кэшированные категории для уменьшения запросов к API. По умолчанию `True`.

**Возвращает**:

- list[model_ChildCategory]: Список дочерних категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


## Функции

(Здесь будут описаны функции, если они есть в коде)