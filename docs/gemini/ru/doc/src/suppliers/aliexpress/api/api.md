# Модуль `hypotez/src/suppliers/aliexpress/api/api.py`

## Обзор

Этот модуль предоставляет обертку для API AliExpress Open Platform. Он позволяет получать информацию о продуктах и аффилированные ссылки из AliExpress с помощью официального API более удобным способом.

## Классы

### `AliexpressApi`

**Описание**: Класс `AliexpressApi` предоставляет методы для получения информации с AliExpress Open Platform используя ваши API-ключи.

**Параметры конструктора**:

- `key` (str): Ваш API ключ.
- `secret` (str): Ваш API секрет.
- `language` (model_Language): Код языка. По умолчанию EN.
- `currency` (model_Currency): Код валюты. По умолчанию USD.
- `tracking_id` (str, optional): Идентификатор отслеживания для генерации ссылок. По умолчанию None.
- `app_signature` (str, optional): Подпись приложения.
- `**kwargs` (dict, optional): Дополнительные аргументы.


**Методы**:

#### `retrieve_product_details`

**Описание**: Получает информацию о продуктах по списку ID или ссылкам.

**Параметры**:

- `product_ids` (str | list[str]): Один или несколько ID или ссылок на продукты.
- `fields` (str | list[str], optional): Поля для включения в результаты. По умолчанию все поля.
- `country` (str, optional): Фильтрует продукты, которые могут быть отправлены в указанную страну. Возвращает цену в соответствии с политикой налогообложения страны.

**Возвращает**:

- list[model_Product]: Список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`: Если продукты не найдены.
- `InvalidArgumentException`: При некорректном формате входных данных.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.

#### `get_affiliate_links`

**Описание**: Преобразует список ссылок в аффилированные ссылки.

**Параметры**:

- `links` (str | list[str]): Один или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (обычная или горячая). По умолчанию NORMAL.

**Возвращает**:

- list[model_AffiliateLink]: Список аффилированных ссылок.

**Вызывает исключения**:

- `InvalidArgumentException`: При некорректном формате входных данных.
- `InvalidTrackingIdException`: Если идентификатор отслеживания не указан.
- `ProductsNotFoudException`: Если аффилированные ссылки недоступны.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.


#### `get_hotproducts`

**Описание**: Поиск аффилированных продуктов с высокой комиссией.

**Параметры**:
(см. исходный код для полного списка параметров)

**Возвращает**:

- model_HotProductsResponse: Содержит информацию о ответе и список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`: Если продукты не найдены.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.


#### `get_categories`

**Описание**: Получает все доступные категории (родительские и дочерние).

**Возвращает**:

- list[model_Category | model_ChildCategory]: Список категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.


#### `get_parent_categories`

**Описание**: Получает все доступные родительские категории.

**Параметры**:

- `use_cache` (bool, optional): Использовать кэшированные данные для ускорения. По умолчанию True.

**Возвращает**:

- list[model_Category]: Список родительских категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.


#### `get_child_categories`

**Описание**: Получает все дочерние категории для указанной родительской категории.

**Параметры**:

- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные данные для ускорения. По умолчанию True.

**Возвращает**:

- list[model_ChildCategory]: Список дочерних категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: При проблемах с выполнением запроса к API.
- `ApiRequestResponseException`: При проблемах с обработкой ответа API.