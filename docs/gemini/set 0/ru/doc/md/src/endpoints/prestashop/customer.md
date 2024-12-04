# Модуль `hypotez/src/endpoints/prestashop/customer.py`

## Обзор

Модуль `hypotez/src/endpoints/prestashop/customer.py` предоставляет класс `PrestaCustomer` для работы с клиентами в системе PrestaShop. Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

## Оглавление

* [Классы](#классы)
    * [PrestaCustomer](#presta-customer)

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в системе PrestaShop.  Предоставляет методы для взаимодействия с API PrestaShop.

**Методы**:

* [`__init__`](#__init__)


### `__init__`

**Описание**: Инициализирует клиента PrestaShop.

**Параметры**:

* `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
* `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
* `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
  -  None.

**Вызывает исключения**:

* `ValueError`: Если не заданы значения `api_domain` и `api_key`.


```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
    """Инициализация клиента PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.

    Raises:
        ValueError: Если не заданы значения `api_domain` и `api_key`.
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)
```