# AliexpressAffiliateOrderListRequest

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` представляет собой класс для работы с API AliExpress, позволяющий получать список заказов аффилиата.

## Оглавление

1. [Классы](#классы)
    - [`AliexpressAffiliateOrderListRequest`](#aliexpressaffiliateorderlistrequest)

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс для отправки запроса на получение списка заказов аффилиата AliExpress.

**Методы**:
- `__init__`:  Инициализирует объект `AliexpressAffiliateOrderListRequest` с заданным доменом и портом, а также устанавливает начальные значения для параметров запроса.
- `getapiname`: Возвращает имя API метода, который будет вызван.

#### `__init__`
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80)
```
**Описание**: Конструктор класса `AliexpressAffiliateOrderListRequest`. Инициализирует объект с заданным доменом и портом, а также устанавливает начальные значения для параметров запроса.

**Параметры**:
- `domain` (str, optional): Доменное имя API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

#### `getapiname`
```python
def getapiname(self) -> str:
```
**Описание**: Возвращает имя API метода, который будет вызван.

**Возвращает**:
- `str`: Строка, представляющая имя API метода: `aliexpress.affiliate.order.list`.