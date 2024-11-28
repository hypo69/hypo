# Модуль hypotez/src/endpoints/prestashop/shop.py

## Обзор

Модуль `shop.py` содержит класс `PrestaShopShop`, предназначенный для работы с магазинами PrestaShop.  Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

## Оглавление

* [Модуль `shop.py`](#модуль-shop-py)
* [Класс `PrestaShopShop`](#класс-prestashopshop)
    * [Метод `__init__`](#метод-init)

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop.  Наследуется от `PrestaShop`.

**Методы**:

#### `__init__`

**Описание**: Инициализация магазина PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не имеет значения, так как метод является конструктором.

**Вызывает исключения**:

- `ValueError`: Если не заданы оба параметра `api_domain` и `api_key`.
```
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
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)