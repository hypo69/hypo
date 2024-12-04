# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, предназначенный для работы с API AliExpress, позволяя получать список заказов филиала по индексу. Класс наследуется от базового класса `RestApi`. Он предоставляет методы для инициализации запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateOrderListbyindexRequest`](#модуль-aliexpressaffiliateorderlistbyindexrequest)
- [Класс `AliexpressAffiliateOrderListbyindexRequest`](#класс-aliexpressaffiliateorderlistbyindexrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс представляет собой запрос для получения списка заказов филиала по индексу в API AliExpress.

### Метод `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

**Возвращает**:

- None


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:

- Нет

**Возвращает**:

- str: Название API запроса.


**Атрибуты класса:**

- `app_signature`:  (Описание)
- `end_time`: (Описание)
- `fields`: (Описание)
- `page_size`: (Описание)
- `start_query_index_id`: (Описание)
- `start_time`: (Описание)
- `status`: (Описание)