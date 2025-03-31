# Модуль `shop.py`

## Обзор

Модуль `shop.py` предоставляет класс `PrestaShopShop`, предназначенный для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и обеспечивает функциональность для взаимодействия с API PrestaShop.

## Подробнее

Этот модуль содержит класс `PrestaShopShop`, который используется для инициализации и настройки подключения к магазину PrestaShop. Он требует наличия домена API и ключа API для установления соединения. Расположение файла в проекте указывает на то, что он является частью подсистемы, отвечающей за взаимодействие с PrestaShop, и, вероятно, используется для выполнения различных операций, связанных с магазином, таких как получение информации о товарах, категориях и т. д.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` предназначен для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет функциональность для взаимодействия с API PrestaShop.

**Как работает класс**:
Класс `PrestaShopShop` принимает учетные данные, такие как домен API и ключ API, для инициализации соединения с магазином PrestaShop. Он проверяет наличие необходимых параметров и вызывает конструктор родительского класса `PrestaShop` для установки соединения.

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
Функция `__init__` является конструктором класса `PrestaShopShop`. Она принимает учетные данные для подключения к магазину PrestaShop, проверяет их наличие и вызывает конструктор родительского класса `PrestaShop`.

Внутри функции происходят следующие действия и преобразования:
A. Проверяется, переданы ли учетные данные через аргумент `credentials`.
|
B. Если `credentials` переданы, извлекаются значения `api_domain` и `api_key` из `credentials`.
|
C. Проверяется наличие `api_domain` и `api_key`. Если хотя бы один из них отсутствует, вызывается исключение `ValueError`.
|
D. Вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API магазина PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API для доступа к магазину PrestaShop. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:

- `ValueError`: Если не переданы оба параметра `api_domain` и `api_key`.
```
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
```

**Примеры**:

```python
# Пример инициализации класса PrestaShopShop с использованием параметров api_domain и api_key
shop = PrestaShopShop(api_domain='your_api_domain', api_key='your_api_key')

# Пример инициализации класса PrestaShopShop с использованием credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)