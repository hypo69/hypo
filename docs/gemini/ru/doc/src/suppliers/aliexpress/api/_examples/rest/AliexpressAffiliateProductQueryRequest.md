# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductQueryRequest`, представляющий запрос к API AliExpress для получения информации о продуктах. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**: Класс для создания запроса к API AliExpress для получения информации о продуктах.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект запроса.

**Параметры**:

- `domain` (str, опционально "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально 80): Порт API.

**Возвращает**:
-  `None`


#### `getapiname(self)`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.product.query`).