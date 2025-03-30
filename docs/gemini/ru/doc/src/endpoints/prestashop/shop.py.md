# Модуль `shop` для работы с магазинами PrestaShop

## Обзор

Модуль `shop` предоставляет класс `PrestaShopShop` для взаимодействия с магазинами PrestaShop через API. Он позволяет инициализировать магазин с использованием домена API и ключа API, а также выполняет основные операции, связанные с магазином PrestaShop.

## Подробней

Этот модуль предназначен для упрощения работы с API PrestaShop. Он использует класс `PrestaShop` из модуля `.api` для выполнения HTTP-запросов к API PrestaShop. Класс `PrestaShopShop` принимает параметры аутентификации (домен API и ключ API) и предоставляет методы для взаимодействия с различными ресурсами API PrestaShop. Модуль также обрабатывает ошибки, связанные с API PrestaShop, и логирует их с использованием модуля `logger` из `src.logger`.

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop. Наследуется от класса `PrestaShop`.

**Методы**:
- `__init__`: Инициализация магазина PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Примеры**:
```python
from types import SimpleNamespace

# Пример инициализации с использованием словаря
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)

# Пример инициализации с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)

# Пример инициализации с передачей параметров напрямую
shop = PrestaShopShop(api_domain='your_api_domain', api_key='your_api_key')
```

## Функции

### `__init__`

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

**Описание**: Инициализирует экземпляр класса `PrestaShopShop`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API магазина PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API для доступа к магазину PrestaShop. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример 1: Инициализация с использованием словаря
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)

# Пример 2: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)

# Пример 3: Инициализация с передачей параметров напрямую
shop = PrestaShopShop(api_domain='your_api_domain', api_key='your_api_key')

# Пример 4: Вызов исключения ValueError, если api_domain или api_key не предоставлены
try:
    shop = PrestaShopShop()
except ValueError as ex:
    print(f"Ошибка: {ex}")  # Вывод: Ошибка: Необходимы оба параметра: api_domain и api_key.