# Модуль aliexpress/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductDownloadRequest.py

## Обзор

Этот модуль предоставляет класс `AliexpressAffiliateHotproductDownloadRequest`, который реализует запрос для скачивания горячих продуктов из программы аффилированного маркетинга AliExpress. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс `AliexpressAffiliateHotproductDownloadRequest` предназначен для формирования запросов к API AliExpress для загрузки горячих продуктов. Он предоставляет возможность настройки различных параметров, необходимых для формирования запроса, таких как `app_signature`, `category_id`, `country` и другие.

**Атрибуты**:

- `app_signature`: Строковое значение, представляющее подпись приложения.
- `category_id`: Целое число, идентификатор категории.
- `country`: Строка, представляющая страну.
- `fields`:  Значение, определяющее поля для возврата.
- `scenario_language_site`: Значение, определяющее язык и регион.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.


**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект класса.

**Параметры**:
- `domain` (str, опционально): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, опционально): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname(self)`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Имя API `aliexpress.affiliate.hotproduct.download`.