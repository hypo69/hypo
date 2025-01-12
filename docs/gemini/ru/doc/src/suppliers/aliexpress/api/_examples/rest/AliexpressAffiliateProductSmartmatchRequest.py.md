# Модуль `AliexpressAffiliateProductSmartmatchRequest`

## Обзор

Модуль `AliexpressAffiliateProductSmartmatchRequest` предоставляет класс `AliexpressAffiliateProductSmartmatchRequest`, который является частью API для работы с AliExpress. Этот класс позволяет выполнять запросы для получения списка товаров, соответствующих заданным критериям поиска через API.

## Оглавление
- [Классы](#классы)
  - [`AliexpressAffiliateProductSmartmatchRequest`](#AliexpressAffiliateProductSmartmatchRequest)

## Классы

### `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс для выполнения запроса smartmatch продуктов через API AliExpress.

**Методы**:
- `__init__`: Инициализирует экземпляр класса с доменом и портом по умолчанию.
- `getapiname`: Возвращает имя API для запроса smartmatch продуктов.

#### `__init__`

**Описание**: Конструктор класса `AliexpressAffiliateProductSmartmatchRequest`.

**Параметры**:
- `domain` (str): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int): Порт API. По умолчанию 80.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `getapiname`

**Описание**: Возвращает имя API для запроса smartmatch продуктов.

**Параметры**:
- `None`: Метод не принимает параметров.

**Возвращает**:
- `str`: Строка, представляющая имя API, `'aliexpress.affiliate.product.smartmatch'`.