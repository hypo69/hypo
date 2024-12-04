# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, предназначенный для взаимодействия с API AliExpress для получения информации о рекламных акциях.  Этот класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс для запроса информации о рекламных акциях на AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, опционально): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, опционально): Порт API. По умолчанию `80`.


**Возвращает**:
- Не имеет возвращаемого значения.

#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:

- Нет.

**Возвращает**:
- str: Строка 'aliexpress.affiliate.featuredpromo.get'.