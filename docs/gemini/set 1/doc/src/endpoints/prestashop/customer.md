# Модуль `hypotez/src/endpoints/prestashop/customer.py`

## Обзор

Данный модуль предоставляет класс `PrestaCustomer` для взаимодействия с клиентами в системе управления интернет-магазином PrestaShop.  Класс наследуется от класса `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

## Оглавление

- [Модуль `hypotez/src/endpoints/prestashop/customer.py`](#модуль-hypotezsrcendpointsprestashopcustomerpy)
- [Класс `PrestaCustomer`](#класс-prestacustomer)
  - [Метод `__init__`](#метод-init)


## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop. Предоставляет методы для взаимодействия с API PrestaShop.

**Методы**:

- `__init__`: Инициализирует объект `PrestaCustomer`.

### `__init__`

**Описание**: Инициализирует объект класса `PrestaCustomer`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  None

**Возможные исключения**:

- `ValueError`: Если не заданы значения `api_domain` и `api_key`.


**Детали**:

Метод `__init__` инициализирует объект `PrestaCustomer`, принимая на вход необязательные параметры `credentials`, `api_domain` и `api_key`.
Если `credentials` задан, значения `api_domain` и `api_key` извлекаются из него.
Если ни `api_domain`, ни `api_key` не указаны, генерируется исключение `ValueError`.  В противном случае, вызывается метод `__init__` родительского класса `PrestaShop`.
```
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
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)