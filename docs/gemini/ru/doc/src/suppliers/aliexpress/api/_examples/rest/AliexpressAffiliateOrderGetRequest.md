# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderGetRequest`, представляющий собой API-запрос для получения информации об аффилиатных заказах на AliExpress. Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс представляет API-запрос для получения данных об аффилиатных заказах на AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateOrderGetRequest`.

**Параметры**:

- `domain` (str, опционально): Доменное имя API (по умолчанию "api-sg.aliexpress.com").
- `port` (int, опционально): Порт API (по умолчанию 80).

**Возвращает**:
- None

#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- str: Имя API-метода ("aliexpress.affiliate.order.get").