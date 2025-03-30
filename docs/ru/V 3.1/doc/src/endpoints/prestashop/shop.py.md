# Модуль `shop.py`

## Обзор

Модуль `shop.py` предоставляет класс `PrestaShopShop` для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предназначен для инициализации и настройки соединения с API PrestaShop. Класс позволяет передавать учетные данные как напрямую, так и через объект `SimpleNamespace` или словарь.

## Подробней

Этот модуль является частью подсистемы взаимодействия с PrestaShop и обеспечивает удобный интерфейс для выполнения запросов к API магазина. Он использует классы `PrestaShop` для выполнения фактических запросов и `logger` для логирования ошибок и отладочной информации.

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop. Наследуется от класса `PrestaShop`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShopShop`.

#### `__init__`

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
    ...
```

**Описание**: Инициализирует экземпляр класса `PrestaShopShop`, устанавливая параметры соединения с API PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не переданы `api_domain` и `api_key` ни через `credentials`, ни отдельными параметрами.

**Примеры**:

```python
# Пример 1: Инициализация с использованием параметров api_domain и api_key
shop = PrestaShopShop(api_domain='your_domain', api_key='your_api_key')

# Пример 2: Инициализация с использованием объекта SimpleNamespace
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_domain', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)

# Пример 3: Инициализация с использованием словаря
credentials = {'api_domain': 'your_domain', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)

# Пример 4: Вызов исключения ValueError
try:
    shop = PrestaShopShop()
except ValueError as ex:
    print(f"Ошибка: {ex}")  # Вывод: Ошибка: Необходимы оба параметра: api_domain и api_key.