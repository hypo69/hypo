# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductSmartmatchRequest`, представляющий запрос к API AliExpress для поиска продуктов с использованием технологии `smartmatch`. Класс наследуется от базового класса `RestApi` и предоставляет методы для инициализации и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateProductSmartmatchRequest`](#модуль-aliexpressaffiliateproductsmartmatchrequest)
- [Класс `AliexpressAffiliateProductSmartmatchRequest`](#класс-aliexpressaffiliateproductsmartmatchrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)

## Класс `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс представляет запрос к API AliExpress для поиска продуктов с использованием технологии `smartmatch`.

### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateProductSmartmatchRequest`.

**Параметры**:
- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Доменное имя API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Возвращает**:
- None

**Вызывает исключения**:
-  Возможны исключения, связанные с базовым классом `RestApi`.


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Название API, в данном случае `aliexpress.affiliate.product.smartmatch`.