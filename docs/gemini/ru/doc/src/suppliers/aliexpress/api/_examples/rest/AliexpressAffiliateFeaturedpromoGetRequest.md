# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, который представляет собой API-запрос для получения данных о выделенных промоакциях на AliExpress. Класс наследуется от `RestApi` и предоставляет методы для инициализации запроса и получения имени API.


## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**:  Класс `AliexpressAffiliateFeaturedpromoGetRequest` представляет API-запрос для получения данных о выделенных промоакциях на AliExpress.  Он реализует базовый функционал запросов REST API.

**Методы**:

- `__init__`


#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует экземпляр класса `AliexpressAffiliateFeaturedpromoGetRequest`.

**Параметры**:

- `domain` (str, опционально, по умолчанию `"api-sg.aliexpress.com"`): Доменное имя API.
- `port` (int, опционально, по умолчанию `80`): Порт API.

**Возвращает**:
-  Не имеет возвращаемого значения.

- `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- Не принимает параметров.

**Возвращает**:
- str: Имя API-метода (`aliexpress.affiliate.featuredpromo.get`).


## Функции

(В данном файле нет самостоятельных функций, только методы класса)


**ПРИМЕЧАНИЕ:**  В предоставленном коде не хватает важной информации:  документации к параметрам `app_signature` и `fields`. Без этой информации невозможно полностью описать функционал класса.  Также, не указано, что эти атрибуты представляют собой и в каком формате принимают входные данные.