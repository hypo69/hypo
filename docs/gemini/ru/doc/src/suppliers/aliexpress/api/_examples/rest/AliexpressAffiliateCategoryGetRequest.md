# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateCategoryGetRequest.py

## Обзор

Этот модуль содержит класс `AliexpressAffiliateCategoryGetRequest`, который представляет собой API-запрос для получения данных о категориях на AliExpress. Класс наследуется от базового класса `RestApi` и предоставляет методы для инициализации запроса и получения имени API.

## Оглавление

* [Модуль](#модуль)
* [Класс AliexpressAffiliateCategoryGetRequest](#класс-aliexpressaffiliatecategorygetrequest)
    * [Метод __init__](#метод-init)
    * [Метод getapiname](#метод-getapiname)


## Класс AliexpressAffiliateCategoryGetRequest

**Описание**: Класс `AliexpressAffiliateCategoryGetRequest` представляет собой API-запрос для получения данных о категориях на AliExpress. Он наследуется от базового класса `RestApi`, предоставляя общие методы для работы с API.

### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `AliexpressAffiliateCategoryGetRequest`.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Доменное имя API.
- `port` (int, опционально, по умолчанию 80): Порт API.


**Возвращает**:
- None

**Вызывает исключения**:
- Нет указанных исключений.


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:

- Нет параметров.

**Возвращает**:
- str: Имя API запроса.

**Вызывает исключения**:
- Нет указанных исключений.