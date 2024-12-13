# Модуль `aliexpress.affiliate.product.query`

## Обзор

Модуль содержит пример запроса к API AliExpress для получения списка товаров.

## Оглавление

1.  [Классы](#классы)
    -   [`AliexpressAffiliateProductQueryRequest`](#aliexpressaffiliateproductqueryrequest)
2.  [Функции](#функции)
    -   [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**: Класс для формирования запроса на получение списка товаров через API AliExpress. Наследуется от `RestApi`.

**Методы**:
- `__init__`: Инициализирует объект запроса.
- `getapiname`: Возвращает имя API метода.

**Параметры** конструктора `__init__`:
-   `domain` (str): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
-   `port` (int): Порт API. По умолчанию `80`.

**Атрибуты**:
-   `app_signature` (str, Optional): Подпись приложения. По умолчанию `None`.
-   `category_ids` (str, Optional): Идентификаторы категорий. По умолчанию `None`.
-   `delivery_days` (int, Optional): Количество дней доставки. По умолчанию `None`.
-  `fields` (str, Optional): Набор полей для выдачи. По умолчанию `None`.
-   `keywords` (str, Optional): Ключевые слова для поиска. По умолчанию `None`.
-   `max_sale_price` (float, Optional): Максимальная цена товара. По умолчанию `None`.
-   `min_sale_price` (float, Optional): Минимальная цена товара. По умолчанию `None`.
-   `page_no` (int, Optional): Номер страницы. По умолчанию `None`.
-   `page_size` (int, Optional): Размер страницы. По умолчанию `None`.
-   `platform_product_type` (str, Optional): Тип продукта. По умолчанию `None`.
-   `ship_to_country` (str, Optional): Страна доставки. По умолчанию `None`.
-   `sort` (str, Optional): Параметры сортировки. По умолчанию `None`.
-   `target_currency` (str, Optional): Валюта. По умолчанию `None`.
-   `target_language` (str, Optional): Язык. По умолчанию `None`.
-   `tracking_id` (str, Optional): Трекинговый ID. По умолчанию `None`.

## Функции

### `getapiname`

**Описание**: Возвращает имя API метода.

**Возвращает**:
-   `str`: Строка `'aliexpress.affiliate.product.query'`, представляющая имя API метода.