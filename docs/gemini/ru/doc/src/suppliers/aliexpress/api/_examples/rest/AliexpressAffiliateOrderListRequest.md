# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py`

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` предоставляет класс для работы с API AliExpress, позволяя получать список заказов филиалов.

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс `AliexpressAffiliateOrderListRequest` наследуется от базового класса `RestApi` и предоставляет методы для взаимодействия с API AliExpress для получения списка заказов филиалов.

**Атрибуты**:

- `app_signature`: Приложение подпись.
- `end_time`: Конечная дата.
- `fields`: Поля.
- `locale_site`: Локаль сайта.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `start_time`: Начальная дата.
- `status`: Статус.

**Методы**:

#### `__init__`

**Описание**: Конструктор класса.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Возвращает**:
- None


#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- Нет

**Возвращает**:
- str: Название API-метода (`aliexpress.affiliate.order.list`).

## Функции

(В данном модуле функций нет)