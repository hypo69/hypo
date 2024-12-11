# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py`

## Обзор

Модуль `AliexpressAffiliateLinkGenerateRequest` предоставляет класс для генерации ссылок на партнерские программы AliExpress.  Он наследуется от базового класса `RestApi` и используется для взаимодействия с API AliExpress.

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**: Класс для генерации ссылок на партнерские программы AliExpress.  Обеспечивает взаимодействие с API AliExpress через REST-интерфейс.

**Методы**:

- `__init__`
- `getapiname`

**Параметры**:

- `__init__`
    - `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
    - `port` (int, optional): Порт API. По умолчанию 80.


**Атрибуты**:

- `app_signature`: Значение подписи приложения.
- `promotion_link_type`: Тип ссылки для продвижения.
- `source_values`: Дополнительные значения источника.
- `tracking_id`: Идентификатор отслеживания.


### `getapiname`

**Описание**: Возвращает имя API-метода для генерации ссылок.

**Возвращает**:

- str: Имя API-метода `aliexpress.affiliate.link.generate`.