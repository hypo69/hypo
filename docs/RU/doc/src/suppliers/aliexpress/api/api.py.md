# Модуль `aliexpress.api`

## Обзор

Модуль `aliexpress.api` предоставляет обертку для API AliExpress, упрощающую получение информации о товарах и партнерских ссылок. Он позволяет взаимодействовать с AliExpress API для получения данных о продуктах и генерации партнерских ссылок.

## Содержание

1.  [Класс `AliexpressApi`](#класс-aliexpressapi)
    *   [`__init__`](#__init__)
    *   [`retrieve_product_details`](#retrieve_product_details)
    *   [`get_affiliate_links`](#get_affiliate_links)
    *   [`get_hotproducts`](#get_hotproducts)
    *   [`get_categories`](#get_categories)
    *   [`get_parent_categories`](#get_parent_categories)
    *   [`get_child_categories`](#get_child_categories)

## Классы

### `AliexpressApi`

**Описание**:
Предоставляет методы для получения информации из AliExpress, используя учетные данные API.

**Параметры**:
- `key` (str): Ваш API ключ.
- `secret` (str): Ваш API секрет.
- `language` (str): Код языка. По умолчанию `EN`.
- `currency` (str): Код валюты. По умолчанию `USD`.
- `tracking_id` (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

#### `__init__`

**Описание**:
Инициализирует класс `AliexpressApi` с предоставленными ключом API, секретом, языком, валютой и идентификатором отслеживания.

**Параметры**:
- `key` (str): Ваш API ключ.
- `secret` (str): Ваш API секрет.
- `language` (model_Language): Код языка.
- `currency` (model_Currency): Код валюты.
- `tracking_id` (str, optional): Идентификатор отслеживания для генератора ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.
- `kwargs` (dict): Дополнительные параметры.

#### `retrieve_product_details`

**Описание**:
Получает информацию о продуктах.

**Параметры**:
- `product_ids` (str | list[str]): Одна или несколько ссылок или идентификаторов продуктов.
- `fields` (str | list[str], optional): Поля для включения в результаты. По умолчанию все.
- `country` (str, optional): Фильтрует продукты, которые могут быть отправлены в эту страну. Возвращает цену в соответствии с налоговой политикой страны.

**Возвращает**:
- `list[model_Product]`: Список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `InvalidArgumentException`: Если переданы неверные аргументы.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.

#### `get_affiliate_links`

**Описание**:
Конвертирует список ссылок в партнерские ссылки.

**Параметры**:
- `links` (str | list[str]): Одна или несколько ссылок для конвертации.
- `link_type` (model_LinkType, optional): Тип ссылки: нормальная или горячая. По умолчанию `NORMAL`.

**Возвращает**:
- `list[model_AffiliateLink]`: Список партнерских ссылок.

**Вызывает исключения**:
- `InvalidArgumentException`: Если переданы неверные аргументы.
- `InvalidTrackingIdException`: Если не указан `tracking_id`.
- `ProductsNotFoudException`: Если партнерские ссылки не найдены.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.

#### `get_hotproducts`

**Описание**:
Поиск партнерских продуктов с высокой комиссией.

**Параметры**:
- `category_ids` (str | list[str], optional): Один или несколько идентификаторов категорий.
- `delivery_days` (int, optional): Предполагаемые дни доставки.
- `fields` (str | list[str], optional): Поля для включения в список результатов. По умолчанию все.
- `keywords` (str, optional): Поиск продуктов по ключевым словам.
- `max_sale_price` (int, optional): Фильтрует продукты с ценой ниже указанного значения.
- `min_sale_price` (int, optional): Фильтрует продукты с ценой выше указанного значения.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Количество продуктов на каждой странице. Должно быть от 1 до 50.
- `platform_product_type` (model_ProductType, optional): Указать тип продукта платформы.
- `ship_to_country` (str, optional): Фильтровать продукты, которые можно отправить в эту страну.
- `sort` (model_SortBy, optional): Указывает метод сортировки.

**Возвращает**:
- `model_HotProductsResponse`: Содержит информацию об ответе и список продуктов.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.

#### `get_categories`

**Описание**:
Получает все доступные категории, как родительские, так и дочерние.

**Возвращает**:
- `list[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.

#### `get_parent_categories`

**Описание**:
Получает все доступные родительские категории.

**Параметры**:
- `use_cache` (bool, optional): Использует кэшированные категории, чтобы уменьшить количество запросов к API.

**Возвращает**:
- `list[model_Category]`: Список родительских категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.

#### `get_child_categories`

**Описание**:
Получает все доступные дочерние категории для определенной родительской категории.

**Параметры**:
- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool, optional): Использует кэшированные категории, чтобы уменьшить количество запросов к API.

**Возвращает**:
- `list[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если возникла ошибка при выполнении запроса API.
- `ApiRequestResponseException`: Если возникла ошибка в ответе от API.