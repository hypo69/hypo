# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductSmartmatchRequest`, который представляет собой запрос к API AliExpress для поиска продуктов по ключевым словам. Класс наследуется от класса `RestApi`.  Он позволяет настраивать различные параметры поиска, такие как ключевые слова, страницу, ID продукта и т.д.

## Оглавление

* [Модуль `AliexpressAffiliateProductSmartmatchRequest`](#модуль-aliexpressaffiliateproductsmartmatchrequest)
* [Класс `AliexpressAffiliateProductSmartmatchRequest`](#класс-aliexpressaffiliateproductsmartmatchrequest)


## Класс `AliexpressAffiliateProductSmartmatchRequest`

### Описание

Класс `AliexpressAffiliateProductSmartmatchRequest` предоставляет методы для формирования запроса к API AliExpress для поиска продуктов по ключевым словам.  Он инициализирует параметры запроса и возвращает имя API-метода.

### Методы

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Конструктор класса. Инициализирует атрибуты класса, принимая домен и порт в качестве параметров.

**Параметры**:

- `domain` (str, опционально "api-sg.aliexpress.com"): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, опционально 80): Порт API. По умолчанию 80.

**Возвращает**:
-  None


#### `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Параметры**:

- Нет

**Возвращает**:
- str: Имя API-метода ("aliexpress.affiliate.product.smartmatch").