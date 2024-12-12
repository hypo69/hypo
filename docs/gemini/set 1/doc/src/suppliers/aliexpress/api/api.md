# Модуль `hypotez/src/suppliers/aliexpress/api/api.py`

## Обзор

Модуль `hypotez/src/suppliers/aliexpress/api/api.py` предоставляет обертки для работы с API AliExpress Open Platform. Он упрощает получение информации о продуктах, аффилированных ссылках и категориях. Модуль использует типы данных из модулей `models`, `errors` и `helpers` для работы с данными и обработки ошибок.

## Классы

### `AliexpressApi`

**Описание**: Класс `AliexpressApi` предоставляет методы для работы с AliExpress API, используя предоставленные API-ключ и секрет.

**Методы**:

- `retrieve_product_details`
- `get_affiliate_links`
- `get_hotproducts`
- `get_categories`
- `get_parent_categories`
- `get_child_categories`

**Параметры конструктора**:

- `key` (str): API-ключ.
- `secret` (str): API-секрет.
- `language` (model_Language): Код языка. По умолчанию EN.
- `currency` (model_Currency): Код валюты. По умолчанию USD.
- `tracking_id` (str, optional): Идентификатор отслеживания для генерации ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.

### `retrieve_product_details`

**Описание**: Получает информацию о продуктах по заданным идентификаторам.

**Параметры**:

- `product_ids` (str | list[str]): Один или несколько идентификаторов продуктов или ссылок.
- `fields` (str | list[str], optional): Список полей для включения в результаты. По умолчанию все поля.
- `country` (str, optional): Страна для фильтрации продуктов по доставке.

**Возвращает**:

- list[model_Product]: Список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `InvalidArgumentException`
- `ApiRequestException`
- `ApiRequestResponseException`


### `get_affiliate_links`

**Описание**: Преобразует список ссылок в аффилированные ссылки.

**Параметры**:

- `links` (str | list[str]): Одна или несколько ссылок для преобразования.
- `link_type` (model_LinkType, optional): Тип ссылки (стандартная или горячая ссылка). По умолчанию `model_LinkType.NORMAL`.

**Возвращает**:

- list[model_AffiliateLink]: Список аффилированных ссылок.

**Вызывает исключения**:

- `InvalidArgumentException`
- `InvalidTrackingIdException`
- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


### `get_hotproducts`

**Описание**: Поиск аффилированных продуктов с высокой комиссией.

**Параметры**:

- `category_ids` (str | list[str], optional): Список категорий продуктов.
- `delivery_days` (int, optional): Ожидаемые дни доставки.
- `fields` (str | list[str], optional): Список полей для включения в результаты. По умолчанию все поля.
- ... (много параметров)

**Возвращает**:

- model_HotProductsResponse: Объект с информацией о результатах и списком продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


### `get_categories`

**Описание**: Получение всех доступных категорий (родительских и дочерних).

**Возвращает**:

- list[model_Category | model_ChildCategory]: Список категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


### `get_parent_categories`

**Описание**: Получение всех родительских категорий.

**Параметры**:

- `use_cache` (bool): Использовать кэшированные категории. По умолчанию `True`.

**Возвращает**:

- list[model_Category]: Список родительских категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


### `get_child_categories`

**Описание**: Получение дочерних категорий для указанной родительской категории.

**Параметры**:

- `parent_category_id` (int): Идентификатор родительской категории.
- `use_cache` (bool): Использовать кэшированные категории. По умолчанию `True`.

**Возвращает**:

- list[model_ChildCategory]: Список дочерних категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`
- `ApiRequestException`
- `ApiRequestResponseException`


## Функции

(Список функций, если они есть в файле, с подробными описаниями)

## Модули

(Список импортированных модулей)

## Исключения

(Список исключений, определённых в этом файле)