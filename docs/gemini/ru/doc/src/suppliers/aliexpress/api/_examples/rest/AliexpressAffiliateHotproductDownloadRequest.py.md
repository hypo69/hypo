# Модуль `aliexpress.affiliate.hotproduct.download`

## Обзор

Модуль `AliexpressAffiliateHotproductDownloadRequest` представляет собой класс для работы с API AliExpress, позволяющий загружать горячие товары.

## Оглавление

- [Классы](#классы)
    - [`AliexpressAffiliateHotproductDownloadRequest`](#aliexpressaffiliatehotproductdownloadrequest)

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс для создания запроса на загрузку горячих товаров через API AliExpress.

**Методы**:

- `__init__`: Инициализирует объект `AliexpressAffiliateHotproductDownloadRequest` с заданным доменом и портом.
- `getapiname`: Возвращает имя API-метода.

#### `__init__`
```python
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
```

**Описание**: Конструктор класса `AliexpressAffiliateHotproductDownloadRequest`.

**Параметры**:
- `domain` (str, optional): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Метод не возвращает значения.

#### `getapiname`
```python
    def getapiname(self) -> str:
```

**Описание**: Возвращает имя API-метода для запроса горячих товаров.

**Параметры**:
- `None`: Метод не принимает параметров.

**Возвращает**:
- `str`: Строка, представляющая имя API-метода: `'aliexpress.affiliate.hotproduct.download'`.