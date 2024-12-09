# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateCategoryGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateCategoryGetRequest`, представляющий собой API-запрос для получения категории на AliExpress.

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**: Класс, представляющий API-запрос для получения категории на AliExpress. Наследуется от класса `RestApi`.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Конструктор класса. Инициализирует базовый класс `RestApi` с заданными параметрами `domain` и `port`.  Устанавливает значение `app_signature` в `None`.

**Параметры**:

- `domain` (str, опционально "api-sg.aliexpress.com"): Доменное имя API.
- `port` (int, опционально 80): Порт API.


#### `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Возвращает**:

- str: Имя API-метода (`aliexpress.affiliate.category.get`).