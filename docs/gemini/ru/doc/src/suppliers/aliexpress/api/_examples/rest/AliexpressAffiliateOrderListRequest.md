# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py`

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` предоставляет класс для работы с API AliExpress, позволяющий получать список заказов аффилированного партнера. Класс наследуется от `RestApi` и содержит методы для инициализации и получения имени API.

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс `AliexpressAffiliateOrderListRequest` реализует взаимодействие с API AliExpress для получения списка заказов аффилированного партнера.

**Методы**:

- `__init__`

**Описание**: Инициализирует объект `AliexpressAffiliateOrderListRequest`.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API AliExpress.
- `port` (int, опционально, по умолчанию 80): Порт API AliExpress.

**Атрибуты**:

- `app_signature`: Приложение подписи.
- `end_time`: Конечная дата.
- `fields`: Поля.
- `locale_site`: Локаль сайта.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `start_time`: Начальная дата.
- `status`: Статус.


- `getapiname`


**Описание**: Возвращает имя API.

**Возвращает**:
- str: Имя API, используемое для запроса.


## Функции


Нет функций в этом модуле.