# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py

## Обзор

Модуль `AliexpressAffiliateProductSmartmatchRequest` предоставляет класс для работы с API AliExpress, позволяющий получать информацию о продуктах с помощью функции smartmatch.  Этот класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс для работы с API AliExpress, предоставляющий методы для запроса информации о продуктах с использованием smartmatch.

**Методы**:

- `__init__`


**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Описание метода `__init__`**:

Инициализирует экземпляр класса, вызывая конструктор родительского класса `RestApi` и инициализирует атрибуты:


- `app`:  (Не описано).
- `app_signature`: (Не описано).
- `country`: (Не описано).
- `device`: (Не описано).
- `device_id`: (Не описано).
- `fields`: (Не описано).
- `keywords`: (Не описано).
- `page_no`: (Не описано).
- `product_id`: (Не описано).
- `site`: (Не описано).
- `target_currency`: (Не описано).
- `target_language`: (Не описано).
- `tracking_id`: (Не описано).
- `user`: (Не описано).


**Возвращает**:
-  None


- `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- str: Название API-метода (`aliexpress.affiliate.product.smartmatch`).


## Функции


### Отсутствуют


## Исключение
Отсутствуют описания исключений.