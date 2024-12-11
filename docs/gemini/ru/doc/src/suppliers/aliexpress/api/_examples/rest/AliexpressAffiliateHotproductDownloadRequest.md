# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductDownloadRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductDownloadRequest`, представляющий запрос для скачивания популярных товаров на AliExpress. Класс наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateHotproductDownloadRequest`](#модуль-aliexpressaffiliatehotproductdownloadrequest)
- [Класс `AliexpressAffiliateHotproductDownloadRequest`](#класс-aliexpressaffiliatehotproductdownloadrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateHotproductDownloadRequest`

**Описание**:  Класс представляет собой запрос для скачивания популярных товаров с AliExpress.  Он настраивает параметры запроса и предоставляет имя API.

### Метод `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Атрибуты**:

- `app_signature`: Не используется, но доступен для настройки.
- `category_id`: ID категории товаров.
- `country`: Страна.
- `fields`: Поля для возвращаемых данных.
- `scenario_language_site`: Язык и сайт.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: ID отслеживания.

**Возвращает**:

-  None


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API - `"aliexpress.affiliate.hotproduct.download"`.