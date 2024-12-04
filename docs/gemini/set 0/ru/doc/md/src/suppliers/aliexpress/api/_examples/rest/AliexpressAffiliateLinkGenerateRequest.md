# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateLinkGenerateRequest`, который представляет собой запрос для генерации ссылки по партнерской программе AliExpress.  Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**: Класс для генерации партнерских ссылок на AliExpress.

**Атрибуты**:

- `app_signature`:  Значение, определяющее приложение.
- `promotion_link_type`: Тип промо-ссылки.
- `source_values`: Значения источника.
- `tracking_id`: Идентификатор отслеживания.

**Методы**:

#### `getapiname()`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- `str`: Строковое имя API-метода (`aliexpress.affiliate.link.generate`).

**Конструктор**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует экземпляр класса.

**Параметры**:

- `domain` (str, опционально): Домен API (по умолчанию `api-sg.aliexpress.com`).
- `port` (int, опционально): Порт API (по умолчанию `80`).

**Возвращает**:
- None


**Примечания**:  Этот класс предполагает использование базового класса `RestApi`, который не определен в этом фрагменте кода.  Для полной функциональности необходимо знать реализацию `RestApi`.