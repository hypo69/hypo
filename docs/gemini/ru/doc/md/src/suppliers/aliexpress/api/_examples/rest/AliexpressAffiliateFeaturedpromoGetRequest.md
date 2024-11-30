# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, представляющий API-запрос для получения данных о специальных рекламных предложениях на AliExpress. Класс наследуется от `RestApi` и предоставляет методы для взаимодействия с API.

## Оглавление

- [Модуль `AliexpressAffiliateFeaturedpromoGetRequest`](#модуль-aliexpressaffiliatefeaturedpromogetrequest)
    - [Класс `AliexpressAffiliateFeaturedpromoGetRequest`](#класс-aliexpressaffiliatefeaturedpromogetrequest)
        - [Метод `__init__`](#метод-init)
        - [Метод `getapiname`](#метод-getapiname)


## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс представляет API-запрос для получения данных о специальных рекламных предложениях на AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

**Возвращает**:
- None

#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- None

**Возвращает**:
- str: Имя API-метода ("aliexpress.affiliate.featuredpromo.get").