# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py`

## Обзор

Этот модуль предоставляет класс `AliexpressAffiliateLinkGenerateRequest`, который реализует запрос API для генерации аффилиатной ссылки на AliExpress.

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**:  Класс, представляющий запрос для генерации аффилиатной ссылки на AliExpress. Наследует от базового класса `RestApi`.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса.

**Параметры**:

- `domain` (str, опционально, по умолчанию `"api-sg.aliexpress.com"`): Домен API.
- `port` (int, опционально, по умолчанию `80`): Порт API.


**Вызывает исключения**:
- Возможны исключения, генерируемые базовым классом `RestApi`.


#### `getapiname`

**Описание**: Возвращает имя API метода.

**Возвращает**:
- str: Название API метода (`aliexpress.affiliate.link.generate`).