# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateLinkGenerateRequest`, представляющий запрос к API AliExpress для генерации партнерской ссылки.  Класс наследуется от `RestApi` и предоставляет методы для инициализации, получения имени API и других параметров.


## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**:  Класс для генерации партнерских ссылок на AliExpress через API.

**Атрибуты**:

- `app_signature`:  (тип не указан)  Подпись приложения.
- `promotion_link_type`: (тип не указан)  Тип промо-ссылки.
- `source_values`: (тип не указан)  Значения источника.
- `tracking_id`: (тип не указан)  Идентификатор отслеживания.


**Методы**:

#### `getapiname()`

**Описание**: Возвращает имя API.

**Возвращает**:
- `str`: Название API - `aliexpress.affiliate.link.generate`.

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект класса.

**Параметры**:
- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Вызывает исключения**:
  Возможны исключения, порожденные родительским классом `RestApi`.


```