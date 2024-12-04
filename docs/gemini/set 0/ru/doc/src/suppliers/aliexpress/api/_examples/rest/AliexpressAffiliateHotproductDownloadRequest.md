# Модуль AliexpressAffiliateHotproductDownloadRequest

## Обзор

Модуль `AliexpressAffiliateHotproductDownloadRequest` предоставляет класс для работы с API AliExpress, позволяющий загрузить данные о популярных продуктах. Он наследуется от класса `RestApi`.

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс `AliexpressAffiliateHotproductDownloadRequest` представляет собой запрос для получения данных о популярных продуктах на AliExpress.  Он предоставляет методы для настройки параметров запроса и выполнения запроса к API.

**Атрибуты**:

- `app_signature`:  Ключевая подпись приложения.
- `category_id`:  Идентификатор категории.
- `country`:  Код страны.
- `fields`:  Список полей для возврата.
- `scenario_language_site`:  Настройки сценария, языка и сайта.
- `page_no`: Номер страницы (для пагинации).
- `page_size`: Размер страницы (для пагинации).
- `target_currency`:  Ценовая валюта.
- `target_language`:  Целевой язык.
- `tracking_id`: Идентификатор отслеживания.


**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует экземпляр класса `AliexpressAffiliateHotproductDownloadRequest`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`


#### `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Имя API-метода `aliexpress.affiliate.hotproduct.download`.


## Функции

(Нет функций в данном модуле)