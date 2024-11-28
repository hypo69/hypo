# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderGetRequest`, представляющий собой API-запрос для получения данных об аффилированных заказах на AliExpress.  Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс `AliexpressAffiliateOrderGetRequest` предназначен для выполнения запроса к API AliExpress для получения данных об аффилированных заказах.

**Атрибуты**:

- `app_signature`:  Значение подписи приложения.
- `fields`:  Список полей для возврата.
- `order_ids`: Список идентификаторов заказов.


**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, опционально): Домен API (по умолчанию `api-sg.aliexpress.com`).
- `port` (int, опционально): Порт API (по умолчанию `80`).

**Возвращает**:
- None


#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:

- Нет

**Возвращает**:
- str: Имя API-метода (`aliexpress.affiliate.order.get`).