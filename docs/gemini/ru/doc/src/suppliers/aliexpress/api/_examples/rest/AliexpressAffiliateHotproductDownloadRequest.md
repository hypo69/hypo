# Модуль aliexpress/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductDownloadRequest.py

## Обзор

Модуль `AliexpressAffiliateHotproductDownloadRequest` предоставляет класс для работы с API AliExpress, позволяя загружать данные о горячих товарах. Класс наследуется от `RestApi`.

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс `AliexpressAffiliateHotproductDownloadRequest` представляет собой запрос для получения данных о горячих товарах на AliExpress. Он предоставляет методы для настройки параметров запроса и выполнения запроса к API.

**Методы**:

- `__init__`: 
    **Описание**: Конструктор класса. Инициализирует параметры запроса и устанавливает значения по умолчанию для домена и порта API AliExpress.
    **Параметры**:
        - `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API AliExpress.
        - `port` (int, опционально, по умолчанию 80): Порт API AliExpress.
    **Возвращает**:
        - Не имеет возвращаемого значения.

- `getapiname`:
    **Описание**: Возвращает имя API-метода для запроса.
    **Параметры**:
        - Не имеет параметров.
    **Возвращает**:
        - str: Имя API-метода ('aliexpress.affiliate.hotproduct.download').