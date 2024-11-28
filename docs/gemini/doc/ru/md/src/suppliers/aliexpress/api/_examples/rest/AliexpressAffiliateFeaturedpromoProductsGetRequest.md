# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Данный модуль предоставляет класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, который используется для взаимодействия с API AliExpress для получения данных о продуктах, участвующих в рекламных акциях. Класс наследуется от базового класса `RestApi`.

## Оглавление

- [Модуль `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#модуль-aliexpressaffiliatefeaturedpromo产品sgetrequest)
  - [Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#класс-aliexpressaffiliatefeaturedpromo产品sgetrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)


## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс для запроса данных о продуктах, участвующих в рекламных акциях на AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Атрибуты**:

- `app_signature`:  Значение для подписи приложения.
- `category_id`:  Идентификатор категории.
- `country`:  Код страны.
- `fields`:  Список полей для возвращаемых данных.
- `page_no`:  Номер страницы результатов.
- `page_size`:  Размер страницы результатов.
- `promotion_end_time`:  Время окончания рекламной акции.
- `promotion_name`:  Название рекламной акции.
- `promotion_start_time`:  Время начала рекламной акции.
- `sort`:  Параметр сортировки результатов.
- `target_currency`:  Целевая валюта.
- `target_language`:  Целевой язык.
- `tracking_id`:  Идентификатор отслеживания.


#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:

- str: Имя API-метода `"aliexpress.affiliate.featuredpromo.products.get"`.