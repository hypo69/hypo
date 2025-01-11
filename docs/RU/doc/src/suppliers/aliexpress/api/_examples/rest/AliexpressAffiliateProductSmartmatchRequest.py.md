# AliexpressAffiliateProductSmartmatchRequest

## Обзор

Модуль предоставляет класс `AliexpressAffiliateProductSmartmatchRequest` для выполнения запросов к API AliExpress для получения списка товаров по критериям.

## Оглавление

- [Классы](#классы)
    - [`AliexpressAffiliateProductSmartmatchRequest`](#aliexpressaffiliateproductsmartmatchrequest)
- [Функции](#функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс для создания запроса к API AliExpress для получения списка товаров на основе заданных параметров.

**Методы**:
- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API.

#### `__init__`

**Описание**: Конструктор класса `AliexpressAffiliateProductSmartmatchRequest`. Инициализирует объект с заданным доменом и портом, а также устанавливает атрибуты запроса в `None`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `None`: Функция не вызывает исключений.

#### `getapiname`

**Описание**: Возвращает имя API-метода, который будет использоваться для запроса.

**Параметры**:
- `None`: Функция не принимает параметров.

**Возвращает**:
- `str`: Возвращает строку `'aliexpress.affiliate.product.smartmatch'`.

**Вызывает исключения**:
- `None`: Функция не вызывает исключений.

## Функции

### `getapiname`

**Описание**: Возвращает имя API-метода, который будет использоваться для запроса.

**Параметры**:
- `None`: Функция не принимает параметров.

**Возвращает**:
- `str`: Возвращает строку `'aliexpress.affiliate.product.smartmatch'`.

**Вызывает исключения**:
- `None`: Функция не вызывает исключений.