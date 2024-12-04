# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Данный модуль предоставляет класс `PrestaSupplier` для работы с поставщиками в API платформы PrestaShop.  Он расширяет класс `PrestaShop`, добавляя специфические методы для работы с поставщиками.

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop. Он наследуется от класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект `PrestaSupplier`.


## Функции

Не содержит функций.


## Методы класса `PrestaSupplier`

### `__init__`

**Описание**: Инициализирует объект `PrestaSupplier`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
  
**Возвращает**:
  - Нет значения (None).

**Вызывает исключения**:

- `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.


**Детали реализации**:
Метод инициализирует атрибуты `api_domain` и `api_key` объекта, используя переданные параметры. Если `credentials` передан,  значения `api_domain` и `api_key` берутся из него. В случае, если ни `api_domain` ни `api_key` не указаны, генерируется исключение `ValueError`. Далее, вызывается метод `__init__` родительского класса `PrestaShop` с переданными параметрами.


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
        ValueError: Если не указаны оба параметра: api_domain и api_key.
    """
    
    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)
    
    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')
    
    super().__init__(api_domain, api_key, *args, **kwards)
```