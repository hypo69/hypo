# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, представляющий запрос для получения списка заказов филиала AliExpress по индексу. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

* [Модуль](#модуль)
* [Класс AliexpressAffiliateOrderListbyindexRequest](#класс-aliexpressaffiliateorderlistbyindexrequest)
    * [Метод __init__](#метод-init)
    * [Метод getapiname](#метод-getapiname)


## Класс `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс представляет собой запрос для получения списка заказов филиала AliExpress по индексу. Он наследуется от `RestApi` и предоставляет методы для настройки параметров запроса.

### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateOrderListbyindexRequest`.

**Параметры**:

* `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Доменное имя API.
* `port` (int, опционально, по умолчанию 80): Порт API.

**Возвращает**:

* `None`


### Метод `getapiname`

**Описание**: Возвращает имя API для запроса.

**Параметры**:

* Нет

**Возвращает**:

* `str`: Имя API (`aliexpress.affiliate.order.listbyindex`).

**Примечание**:
Этот метод используется для определения имени API для отправки запроса к сервису.