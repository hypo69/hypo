# Модуль для работы с магазинами PrestaShop

## Обзор

Модуль `src.endpoints.prestashop.shop` предоставляет класс `PrestaShopShop` для взаимодействия с магазинами PrestaShop через API. Он позволяет инициализировать подключение к магазину, используя домен API и ключ API, а также предоставляет методы для выполнения различных операций, таких как получение данных о продуктах, категориях и т.д.

## Подробней

Этот модуль является частью системы `hypotez` и предназначен для интеграции с платформой электронной коммерции PrestaShop. Класс `PrestaShopShop` наследуется от класса `PrestaShop` и предоставляет удобный интерфейс для работы с API PrestaShop. Он позволяет автоматизировать задачи, такие как синхронизация данных о продуктах, управление заказами и т.д.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` предназначен для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

**Как работает класс**:

1.  При инициализации класса `PrestaShopShop` происходит проверка наличия `api_domain` и `api_key`. Эти параметры необходимы для аутентификации при запросах к API PrestaShop.
2.  Если параметры переданы в `credentials`, они извлекаются из словаря или объекта `SimpleNamespace`.
3.  В случае отсутствия `api_domain` или `api_key` вызывается исключение `ValueError`.
4.  После успешной проверки вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `PrestaShopShop`.

**Параметры**:

-   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
-   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
-   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Примеры**:

```python
from types import SimpleNamespace

# Инициализация с использованием словаря
shop = PrestaShopShop(credentials={'api_domain': 'your_domain', 'api_key': 'your_key'})

# Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_domain', api_key='your_key')
shop = PrestaShopShop(credentials=credentials)

# Инициализация с прямым указанием параметров
shop = PrestaShopShop(api_domain='your_domain', api_key='your_key')
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
```

**Описание**: Инициализирует экземпляр класса `PrestaShopShop`.

**Как работает функция**:

1.  Проверяет, переданы ли параметры `api_domain` и `api_key` через аргумент `credentials` (словарь или `SimpleNamespace`).
2.  Если `credentials` переданы, пытается извлечь значения `api_domain` и `api_key` из `credentials`.
3.  Если `api_domain` или `api_key` не переданы ни через `credentials`, ни отдельными аргументами, вызывает исключение `ValueError`.
4.  Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами.

**Параметры**:

-   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
-   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
-   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
-   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
-   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:

-   `ValueError`: Если не переданы `api_domain` и `api_key`.

**Примеры**:

```python
from types import SimpleNamespace

# Инициализация с использованием словаря
shop = PrestaShopShop(credentials={'api_domain': 'your_domain', 'api_key': 'your_key'})

# Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_domain', api_key='your_key')
shop = PrestaShopShop(credentials=credentials)

# Инициализация с прямым указанием параметров
shop = PrestaShopShop(api_domain='your_domain', api_key='your_key')
```