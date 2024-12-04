# Модуль `hypotez/src/endpoints/prestashop/shop.py`

## Обзор

Этот модуль предоставляет класс `PrestaShopShop` для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop. Наследуется от `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект магазина PrestaShop.


## Функции

###  `__init__`

**Описание**: Инициализирует объект магазина PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:

-  None

**Вызывает исключения**:

- `ValueError`: Бросается, если не заданы `api_domain` и `api_key`.


```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
    """Инициализация магазина PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.

    Returns:
        None

    Raises:
        ValueError: Необходимы оба параметра: api_domain и api_key.
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)