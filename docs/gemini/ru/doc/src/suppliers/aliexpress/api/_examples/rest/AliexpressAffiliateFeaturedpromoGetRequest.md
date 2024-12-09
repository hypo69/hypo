# Модуль AliexpressAffiliateFeaturedpromoGetRequest

## Обзор

Модуль `AliexpressAffiliateFeaturedpromoGetRequest` предоставляет класс для взаимодействия с API AliExpress, позволяя получать данные о промоакциях.

## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс `AliexpressAffiliateFeaturedpromoGetRequest` наследуется от класса `RestApi` и предназначен для выполнения запроса к API AliExpress для получения информации о рекомендуемых промоакциях.

**Конструктор**:

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.

    Returns:
        None
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.fields = None
```

**Методы**:

- `getapiname()`: Возвращает имя API-метода.

```python
def getapiname(self):
    """
    Returns:
        str: Имя API-метода.
    """
    return 'aliexpress.affiliate.featuredpromo.get'
```

## Функции

(В данном модуле функций нет)

## Исключения

(В данном модуле исключений нет)

## Примеры использования

(Примеры использования отсутствуют)