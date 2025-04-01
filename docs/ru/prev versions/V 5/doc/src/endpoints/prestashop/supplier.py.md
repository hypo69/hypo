# Модуль для работы с поставщиками PrestaShop

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier`, предназначенный для взаимодействия с API PrestaShop для управления поставщиками. Он позволяет инициализировать поставщика с использованием домена API и ключа API, а также выполняет базовые операции, такие как аутентификация.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для упрощения интеграции с PrestaShop. Он обеспечивает удобный интерфейс для работы с поставщиками, абстрагируя детали реализации API PrestaShop. Класс `PrestaSupplier` наследуется от класса `PrestaShop`, который предоставляет общую функциональность для работы с API PrestaShop.

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Как работает класс**:
Класс `PrestaSupplier` предназначен для упрощения взаимодействия с API PrestaShop для управления поставщиками. При инициализации класса происходит проверка наличия необходимых параметров, таких как домен API и ключ API. Если параметры не предоставлены, выбрасывается исключение `ValueError`. Класс наследуется от класса `PrestaShop`, который предоставляет общую функциональность для работы с API PrestaShop.

**Методы**:
- `__init__`: Инициализация поставщика PrestaShop.

### `__init__`

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
```

**Описание**: Инициализирует экземпляр класса `PrestaSupplier`.

**Как работает функция**:
При инициализации проверяется, переданы ли параметры `api_domain` и `api_key` напрямую или через словарь `credentials`. Если параметры не переданы ни одним из способов, выбрасывается исключение `ValueError`. Затем вызывается конструктор родительского класса `PrestaShop` для инициализации общих параметров API.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key`.

**Примеры**:

```python
from types import SimpleNamespace
from src.endpoints.prestashop.supplier import PrestaSupplier

# Пример 1: Инициализация с использованием параметров
supplier = PrestaSupplier(api_domain='example.com', api_key='12345')

# Пример 2: Инициализация с использованием словаря credentials
credentials = {'api_domain': 'example.com', 'api_key': '12345'}
supplier = PrestaSupplier(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='12345')
supplier = PrestaSupplier(credentials=credentials)

# Пример 4: Ошибка инициализации
try:
    supplier = PrestaSupplier()
except ValueError as ex:
    print(f'Ошибка: {ex}')
```