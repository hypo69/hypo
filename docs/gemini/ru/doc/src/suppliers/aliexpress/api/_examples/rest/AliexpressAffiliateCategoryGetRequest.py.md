# Модуль `AliexpressAffiliateCategoryGetRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateCategoryGetRequest`, который представляет собой запрос для получения списка категорий товаров через AliExpress API. Он наследуется от базового класса `RestApi` и предназначен для использования в контексте аффилиатной программы AliExpress.

## Оглавление

- [Классы](#классы)
    - [`AliexpressAffiliateCategoryGetRequest`](#aliexpressaffiliatecategorygetrequest)

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**: Класс, представляющий запрос на получение категорий товаров AliExpress.

**Методы**:

- `__init__`: Инициализирует экземпляр класса.
- `getapiname`: Возвращает имя API метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80)
```

**Описание**: Конструктор класса `AliexpressAffiliateCategoryGetRequest`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:

- `None`: Метод не возвращает значения.

#### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Возвращает имя API метода, используемого для получения категорий товаров.

**Параметры**:

- `self`: Экземпляр класса.

**Возвращает**:

- `str`: Строка, представляющая имя API метода `"aliexpress.affiliate.category.get"`.