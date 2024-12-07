# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py

## Обзор

Модуль `AliexpressAffiliateOrderGetRequest` предоставляет класс для запроса информации об аффилированных заказах на AliExpress.  Он наследуется от базового класса `RestApi`.


## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс для взаимодействия с API AliExpress, позволяющий получать информацию об аффилированных заказах.

**Атрибуты**:

- `app_signature`: Значение подписи приложения.
- `fields`: Список полей для возврата.
- `order_ids`: Список идентификаторов заказов.

**Методы**:

#### `__init__`

**Описание**: Конструктор класса.

**Параметры**:
- `domain` (str, опционально): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, опционально): Порт API. По умолчанию `80`.

**Возвращает**:
- None


#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- str: Имя API-метода `aliexpress.affiliate.order.get`.