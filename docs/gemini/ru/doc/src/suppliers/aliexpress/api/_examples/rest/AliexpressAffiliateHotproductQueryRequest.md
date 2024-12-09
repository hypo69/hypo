# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py

## Обзор

Модуль `AliexpressAffiliateHotproductQueryRequest` предоставляет класс для отправки запросов к API AliExpress для получения горячих продуктов по партнерским программам.  Этот класс наследуется от базового класса `RestApi` и реализует метод для формирования имени API.

## Классы

### `AliexpressAffiliateHotproductQueryRequest`

**Описание**:  Класс для запроса горячих продуктов на AliExpress через API.  Он позволяет указать различные параметры для фильтрации результатов, такие как категории, цены, ключевые слова и т.д.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует экземпляр класса. Устанавливает значения параметров для подключения к API.
    **Параметры**:
        - `domain` (str, опционально): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
        - `port` (int, опционально): Порт API. По умолчанию 80.

- `getapiname(self)`:
    **Описание**: Возвращает имя API.
    **Возвращает**:
        - str: Имя API `aliexpress.affiliate.hotproduct.query`.