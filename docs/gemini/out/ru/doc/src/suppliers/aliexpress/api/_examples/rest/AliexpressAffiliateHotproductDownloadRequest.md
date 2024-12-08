# Модуль aliexpress/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductDownloadRequest.py

## Обзор

Этот модуль содержит класс `AliexpressAffiliateHotproductDownloadRequest`, представляющий запрос для скачивания горячих продуктов из AliExpress.  Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс представляет запрос для скачивания горячих продуктов из AliExpress.

**Атрибуты**:

- `app_signature`: Приложение подпись.
- `category_id`: Идентификатор категории.
- `country`: Страна.
- `fields`: Поля.
- `scenario_language_site`: Сценарий язык сайта.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.


**Методы**:

#### `__init__`

**Описание**: Инициализирует объект запроса.

**Параметры**:
- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Возвращает**:
- None

#### `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API  `aliexpress.affiliate.hotproduct.download`.