# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateLinkGenerateRequest`, представляющий запрос для генерации аффилиатной ссылки AliExpress.  Класс наследуется от `RestApi`. Он предоставляет методы для инициализации запроса, получения имени API и управления параметрами запроса.

## Оглавление

* [Модуль `AliexpressAffiliateLinkGenerateRequest`](#модуль-aliexpressaffiliatelinkgeneraterequest)
* [Класс `AliexpressAffiliateLinkGenerateRequest`](#класс-aliexpressaffiliatelinkgeneraterequest)
    * [Метод `__init__`](#метод-init)
    * [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateLinkGenerateRequest`

**Описание**: Класс `AliexpressAffiliateLinkGenerateRequest` представляет запрос для генерации аффилиатной ссылки на AliExpress. Он инициализирует параметры запроса и предоставляет метод для получения имени API.

### Метод `__init__`

**Описание**: Инициализирует объект `AliexpressAffiliateLinkGenerateRequest`.

**Параметры**:
- `domain` (str, опционально): Домен API (по умолчанию "api-sg.aliexpress.com").
- `port` (int, опционально): Порт API (по умолчанию 80).

**Возвращает**:
- None

**Вызывает исключения**:
-  Не описаны исключения, которые могут быть вызваны в данном методе.


### Метод `getapiname`

**Описание**: Возвращает имя API для данного запроса.

**Параметры**:
- Нет

**Возвращает**:
- str: Строковое имя API (`aliexpress.affiliate.link.generate`).

**Вызывает исключения**:
- Не описаны исключения, которые могут быть вызваны в данном методе.