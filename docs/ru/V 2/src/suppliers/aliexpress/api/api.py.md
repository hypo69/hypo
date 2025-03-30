# Модуль `aliexpress.api`

## Обзор

Модуль `aliexpress.api` представляет собой Python-обёртку для API AliExpress. Он предоставляет удобный интерфейс для получения информации о товарах и генерации партнёрских ссылок, используя официальный API AliExpress.

## Оглавление

- [Класс `AliexpressApi`](#класс-aliexpressapi)
    - [Метод `__init__`](#__init__)
    - [Метод `retrieve_product_details`](#retrieve_product_details)
    - [Метод `get_affiliate_links`](#get_affiliate_links)
    - [Метод `get_hotproducts`](#get_hotproducts)
    - [Метод `get_categories`](#get_categories)
    - [Метод `get_parent_categories`](#get_parent_categories)
    - [Метод `get_child_categories`](#get_child_categories)

## Классы

### `AliexpressApi`

**Описание**: Предоставляет методы для получения информации из AliExpress с использованием ваших API-ключей.

**Параметры**:
- `key` (str): Ваш API ключ.
- `secret` (str): Ваш API секрет.
- `language` (`model_Language`): Языковой код. По умолчанию `EN`.
- `currency` (`model_Currency`): Код валюты. По умолчанию `USD`.
- `tracking_id` (str, optional): ID отслеживания для генерации ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Сигнатура приложения. По умолчанию `None`.

#### `__init__`

**Описание**: Инициализирует экземпляр класса `AliexpressApi`.

**Параметры**:
- `key` (str): Ваш API ключ.
- `secret` (str): Ваш API секрет.
- `language` (`model_Language`): Языковой код.
- `currency` (`model_Currency`): Код валюты.
- `tracking_id` (str, optional): ID отслеживания для генерации ссылок. По умолчанию `None`.
- `app_signature` (str, optional): Сигнатура приложения. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

#### `retrieve_product_details`

**Описание**: Получает информацию о товарах.

**Параметры**:
- `product_ids` (`str | list`): Один или несколько ID товаров или ссылок.
- `fields` (`str | list`, optional): Поля для включения в результаты. По умолчанию все.
- `country` (str, optional): Фильтр товаров, которые могут быть доставлены в указанную страну. Возвращает цену в соответствии с налоговой политикой страны.

**Возвращает**:
- `list[model_Product]`: Список товаров.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `InvalidArgumentException`: Если переданы некорректные аргументы.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.

#### `get_affiliate_links`

**Описание**: Преобразует список ссылок в партнёрские ссылки.

**Параметры**:
- `links` (`str | list`): Одна или несколько ссылок для преобразования.
- `link_type` (`model_LinkType`, optional): Тип ссылки: обычная или горячая. По умолчанию `NORMAL`.

**Возвращает**:
- `list[model_AffiliateLink]`: Список партнёрских ссылок.

**Вызывает исключения**:
- `InvalidArgumentException`: Если переданы некорректные аргументы.
- `InvalidTrackingIdException`: Если не указан tracking_id.
- `ProductsNotFoudException`: Если не удалось получить партнёрские ссылки.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.

#### `get_hotproducts`

**Описание**: Поиск партнёрских товаров с высокой комиссией.

**Параметры**:
- `category_ids` (`str | list`, optional): Один или несколько ID категорий.
- `delivery_days` (int, optional): Предполагаемое количество дней доставки.
- `fields` (`str | list`, optional): Поля для включения в результаты. По умолчанию все.
- `keywords` (str, optional): Ключевые слова для поиска товаров.
- `max_sale_price` (int, optional): Максимальная цена товара.
- `min_sale_price` (int, optional): Минимальная цена товара.
- `page_no` (int, optional): Номер страницы.
- `page_size` (int, optional): Количество товаров на странице.
- `platform_product_type` (`model_ProductType`, optional): Тип товара на платформе.
- `ship_to_country` (str, optional): Фильтр товаров, которые могут быть доставлены в указанную страну.
- `sort` (`model_SortBy`, optional): Метод сортировки.

**Возвращает**:
- `model_HotProductsResponse`: Ответ с информацией о горячих товарах и списком самих товаров.

**Вызывает исключения**:
- `ProductsNotFoudException`: Если товары не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.

#### `get_categories`

**Описание**: Получает все доступные категории, включая родительские и дочерние.

**Возвращает**:
- `list[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.

#### `get_parent_categories`

**Описание**: Получает все доступные родительские категории.

**Параметры**:
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `list[model_Category]`: Список родительских категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.

#### `get_child_categories`

**Описание**: Получает все доступные дочерние категории для указанной родительской категории.

**Параметры**:
- `parent_category_id` (int): ID родительской категории.
- `use_cache` (bool, optional): Использовать кэшированные категории для уменьшения количества запросов к API. По умолчанию `True`.

**Возвращает**:
- `list[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:
- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при запросе к API.
- `ApiRequestResponseException`: Если API вернул некорректный ответ.