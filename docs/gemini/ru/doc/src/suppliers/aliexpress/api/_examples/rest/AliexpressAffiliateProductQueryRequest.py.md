# Модуль `AliexpressAffiliateProductQueryRequest`

## Обзор

Модуль `AliexpressAffiliateProductQueryRequest` представляет собой класс для создания запросов к API AliExpress для получения информации о товарах по партнерской программе. Он позволяет фильтровать товары по различным параметрам, таким как категории, ключевые слова, ценовой диапазон и т.д.

## Оглавление

1. [Классы](#классы)
    - [`AliexpressAffiliateProductQueryRequest`](#aliexpressaffiliateproductqueryrequest)
2. [Функции](#функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**:
Класс для формирования запроса на получение списка товаров AliExpress по партнерской программе.

**Методы**:
- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API метода.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Атрибуты**:

- `app_signature` (str, optional): Подпись приложения.
- `category_ids` (str, optional): Идентификаторы категорий товаров.
- `delivery_days` (int, optional): Количество дней доставки.
- `fields` (str, optional): Список полей, которые нужно включить в ответ.
- `keywords` (str, optional): Ключевые слова для поиска товаров.
- `max_sale_price` (float, optional): Максимальная цена товара.
- `min_sale_price` (float, optional): Минимальная цена товара.
- `page_no` (int, optional): Номер страницы результатов.
- `page_size` (int, optional): Размер страницы результатов.
- `platform_product_type` (str, optional): Тип товара на платформе.
- `ship_to_country` (str, optional): Код страны доставки.
- `sort` (str, optional): Параметры сортировки.
- `target_currency` (str, optional): Целевая валюта.
- `target_language` (str, optional): Целевой язык.
- `tracking_id` (str, optional): Идентификатор отслеживания.

## Функции

### `getapiname`

**Описание**:
Возвращает имя API метода.

**Параметры**:
-  Нет.

**Возвращает**:
- `str`: Строка `'aliexpress.affiliate.product.query'`, представляющая имя API метода.