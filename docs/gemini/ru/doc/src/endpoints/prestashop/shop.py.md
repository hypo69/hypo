# Модуль `shop.py`

## Обзор

Модуль `shop.py` предназначен для работы с магазинами PrestaShop. Он содержит класс `PrestaShopShop`, который наследует функциональность от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для упрощения взаимодействия с API PrestaShop. Он позволяет инициализировать магазины PrestaShop, используя домен API и ключ API. Модуль также обрабатывает исключения, связанные с PrestaShop, и использует логирование для отслеживания ошибок.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` предназначен для работы с магазинами PrestaShop.

**Как работает класс**:
Класс `PrestaShopShop` наследуется от класса `PrestaShop` и расширяет его функциональность, предоставляя методы для взаимодействия с API PrestaShop. При инициализации класса требуется передать домен API и ключ API, которые используются для аутентификации при взаимодействии с API PrestaShop.

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

**Как работает функция**:
Функция `__init__` инициализирует экземпляр класса `PrestaShopShop`. Она принимает параметры `credentials`, `api_domain` и `api_key`, которые используются для аутентификации при взаимодействии с API PrestaShop. Если параметр `credentials` передан, он должен содержать параметры `api_domain` и `api_key`. Если параметры `api_domain` и `api_key` не переданы, функция вызывает исключение `ValueError`.

Внутри функции происходят следующие действия и преобразования:
A. Проверяется, передан ли параметр `credentials`.
|
B. Если параметр `credentials` передан, из него извлекаются значения `api_domain` и `api_key`.
|
C. Проверяется, установлены ли значения `api_domain` и `api_key`.
|
D. Если значения `api_domain` или `api_key` не установлены, вызывается исключение `ValueError`.
|
E. Вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- None

**Вызывает исключения**:
- `ValueError`: Если не переданы параметры `api_domain` и `api_key`.

**Примеры**:

```python
# Пример инициализации класса PrestaShopShop с использованием параметров api_domain и api_key
shop = PrestaShopShop(api_domain='https://example.com/api', api_key='YOUR_API_KEY')

# Пример инициализации класса PrestaShopShop с использованием параметра credentials
credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
shop = PrestaShopShop(credentials=credentials)
```