# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `hypotez/src/endpoints/prestashop/supplier.py` предоставляет класс `PrestaSupplier` для взаимодействия с поставщиками на платформе PrestaShop. Класс наследуется от `PrestaShop`, обеспечивая базовые методы для работы с API. Он позволяет получать данные о поставщиках и взаимодействовать с ними.


## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop. Наследуется от `PrestaShop`.

**Методы**:

- `__init__`: Инициализация поставщика PrestaShop.


## Методы класса `PrestaSupplier`

### `__init__`

**Описание**: Инициализация поставщика PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- None

**Вызывает исключения**:
- `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.  Возникает в случае, когда `api_domain` и `api_key` не заданы ни явно, ни через параметр `credentials`.


```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
    """Инициализация поставщика PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.

    Raises:
        ValueError: Необходимы оба параметра: api_domain и api_key.
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)
```
```