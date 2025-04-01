# Модуль `supplier`

## Обзор

Модуль `supplier` предназначен для работы с поставщиками в PrestaShop. Он содержит класс `PrestaSupplier`, который наследуется от класса `PrestaShop` и предоставляет функциональность для взаимодействия с API PrestaShop для управления поставщиками.

## Подробней

Этот модуль позволяет инициализировать поставщика PrestaShop с использованием домена API и ключа API, которые могут быть переданы как отдельные параметры или как часть словаря учетных данных. Он обеспечивает абстракцию для работы с API PrestaShop, упрощая выполнение операций, связанных с поставщиками. Модуль использует `logger` для логирования ошибок и отладочной информации.

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Методы**:
- `__init__`: Инициализация поставщика PrestaShop.

#### `__init__`

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
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `PrestaSupplier`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, которые передаются в конструктор родительского класса `PrestaShop`.
- `**kwards`: Произвольные именованные аргументы, которые передаются в конструктор родительского класса `PrestaShop`.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены оба параметра `api_domain` и `api_key`.

**Примеры**:
```python
from types import SimpleNamespace

# Пример 1: Инициализация с использованием отдельных параметров
supplier = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')

# Пример 2: Инициализация с использованием словаря credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
supplier = PrestaSupplier(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
supplier = PrestaSupplier(credentials=credentials)