# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateCategoryGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateCategoryGetRequest`, представляющий API-запрос для получения категорий на AliExpress. Он наследуется от класса `RestApi`.

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**: Класс `AliexpressAffiliateCategoryGetRequest` реализует API-запрос для получения категорий партнёрской программы AliExpress.

**Методы**:

- `__init__`
- `getapiname`


#### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateCategoryGetRequest`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.


**Возвращает**:
- None


#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API-метода (`aliexpress.affiliate.category.get`).