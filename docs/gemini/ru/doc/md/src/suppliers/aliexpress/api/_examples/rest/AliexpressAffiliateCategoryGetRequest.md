# Модуль aliexpress.affiliate.category.get

## Обзор

Модуль `AliexpressAffiliateCategoryGetRequest` предоставляет класс для взаимодействия с API AliExpress, позволяющий получать данные о категориях аффилиатной программы.

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**: Класс `AliexpressAffiliateCategoryGetRequest` наследуется от `RestApi` и предоставляет методы для работы с API AliExpress, фокусируясь на получении данных о категориях аффилиатной программы.

**Методы**:

- `__init__`:
    ```python
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
    ```

    **Описание**: Инициализирует объект `AliexpressAffiliateCategoryGetRequest`.
    **Параметры**:
        - `domain` (str, опционально): Домен API AliExpress. По умолчанию `api-sg.aliexpress.com`.
        - `port` (int, опционально): Порт API AliExpress. По умолчанию `80`.
    **Возвращает**:
        - `None`

- `getapiname`:
    ```python
    def getapiname(self):
        return 'aliexpress.affiliate.category.get'
    ```

    **Описание**: Возвращает имя API.
    **Параметры**:
        -  Нет
    **Возвращает**:
        - `str`: Имя API `aliexpress.affiliate.category.get`.


## Функции

(Нет функций в данном модуле)


## Обработка исключений

(Нет обработчиков исключений в данном модуле)