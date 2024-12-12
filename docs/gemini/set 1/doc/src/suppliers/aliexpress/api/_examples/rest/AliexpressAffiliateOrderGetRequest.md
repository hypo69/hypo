# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py

## Обзор

Модуль `AliexpressAffiliateOrderGetRequest` предоставляет класс для работы с API AliExpress, позволяющий получать информацию об аффилированных заказах. Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс для запроса информации об аффилированных заказах на AliExpress.

**Методы**:

- `__init__`: Инициализирует объект запроса.
- `getapiname`: Возвращает имя API-метода.

**Параметры конструктора `__init__`**:

- `domain` (str, опционально): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, опционально): Порт API. По умолчанию 80.


**Атрибуты класса**:

- `app_signature`: Значение приложения.
- `fields`: Поля для фильтрации.
- `order_ids`: Идентификаторы заказов.



## Методы

### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateOrderGetRequest`, настраивая соединение с API AliExpress.

**Параметры**:

- `domain` (str, опционально): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, опционально): Порт API. По умолчанию 80.

**Возвращает**:
- Не имеет возвращаемого значения.


### `getapiname`

**Описание**: Возвращает имя API-метода, используемого для получения информации об аффилированных заказах.

**Параметры**:
- Не имеет параметров.

**Возвращает**:
- str: Строковое имя API-метода ("aliexpress.affiliate.order.get").