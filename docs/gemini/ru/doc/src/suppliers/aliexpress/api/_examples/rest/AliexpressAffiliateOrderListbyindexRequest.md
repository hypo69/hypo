# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, представляющий запрос к API AliExpress для получения списка заказов партнера по индексу.  Класс наследуется от `RestApi` и предоставляет методы для инициализации запроса и получения имени API.

## Оглавление

* [Модуль `AliexpressAffiliateOrderListbyindexRequest`](#модуль-aliexpressaffiliateorderlistbyindexrequest)
* [Класс `AliexpressAffiliateOrderListbyindexRequest`](#класс-aliexpressaffiliateorderlistbyindexrequest)
    * [Метод `__init__`](#метод-init)
    * [Метод `getapiname`](#метод-getapiname)

## Класс `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс для формирования запроса к API AliExpress для получения списка заказов партнера по индексу.

**Наследуется от**: `RestApi`

### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateOrderListbyindexRequest`.

**Параметры**:

* `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
* `port` (int, опционально, по умолчанию 80): Порт API.

**Атрибуты**:

* `app_signature`:  Значение для подписи приложения.
* `end_time`: Конечная дата для фильтрации заказов.
* `fields`: Список необходимых полей для возвращаемых данных.
* `page_size`: Размер страницы результатов.
* `start_query_index_id`: Начальный индекс запроса.
* `start_time`: Начальная дата для фильтрации заказов.
* `status`: Статус заказа.


**Возвращает**:
*  None.

**Прим.** Вызывает конструктор родительского класса `RestApi`.


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Возвращает**:
* str: Имя API запроса `aliexpress.affiliate.order.listbyindex`.