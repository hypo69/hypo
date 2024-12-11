# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductdetailGetRequest.py

## Обзор

Модуль `AliexpressAffiliateProductdetailGetRequest` предоставляет класс для выполнения запроса получения деталей товара на платформе AliExpress с использованием API. Класс наследуется от `RestApi`, обеспечивая базовые функциональности для работы с API.

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**: Класс представляет собой запрос к API AliExpress для получения деталей товара по партнерской программе. Он позволяет задать различные параметры для фильтрации и получения нужной информации.

**Методы**:

- `__init__`: Инициализирует объект запроса.
- `getapiname`: Возвращает имя API-метода.

**Атрибуты**:

- `app_signature`: Приложение подпись.
- `country`: Страна.
- `fields`: Поля.
- `product_ids`: Идентификаторы товаров.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.


### `__init__`

**Описание**: Конструктор класса. Инициализирует атрибуты объекта запроса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Не возвращает значение.


### `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- `str`: Имя API-метода (`aliexpress.affiliate.productdetail.get`).