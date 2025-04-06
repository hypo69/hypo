# Модуль для работы с магазинами PrestaShop

## Обзор

Модуль предоставляет класс `PrestaShopShop`, который используется для взаимодействия с API PrestaShop для управления магазином. Он позволяет инициализировать магазин PrestaShop с использованием учетных данных, а также выполняет операции, связанные с магазином.

## Подробнее

Модуль содержит класс `PrestaShopShop`, который наследуется от класса `PrestaShop` и предназначен для работы с магазинами PrestaShop. Класс `PrestaShopShop` инициализируется с использованием учетных данных, таких как домен API и ключ API, и предоставляет методы для взаимодействия с API PrestaShop.

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop.

**Наследует**:

- `PrestaShop`: Класс, предоставляющий базовую функциональность для взаимодействия с API PrestaShop.

**Атрибуты**:

- Отсутствуют, так как используются атрибуты родительского класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaShopShop`.

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

**Назначение**: Инициализация экземпляра класса `PrestaShopShop`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:

- None

**Вызывает исключения**:

- `ValueError`: Если не предоставлены оба параметра: `api_domain` и `api_key`.

**Как работает функция**:

1.  Функция `__init__` инициализирует объект класса `PrestaShopShop`.
2.  Она проверяет, переданы ли учетные данные через аргумент `credentials`.
3.  Если `credentials` переданы, то извлекает значения `api_domain` и `api_key` из `credentials`.
4.  Если `api_domain` или `api_key` не предоставлены ни через `credentials`, ни отдельными аргументами, вызывается исключение `ValueError`.
5.  В конце вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

```
A: Проверка наличия credentials
|
B: Извлечение api_domain и api_key из credentials (если credentials есть)
|
C: Проверка наличия api_domain и api_key
|
D: Вызов исключения ValueError (если api_domain или api_key отсутствуют)
|
E: Вызов конструктора родительского класса PrestaShop
```

**Примеры**:

```python
# Пример 1: Инициализация с использованием credentials
credentials = {'api_domain': 'example.com', 'api_key': '12345'}
shop = PrestaShopShop(credentials=credentials)

# Пример 2: Инициализация с использованием отдельных параметров
shop = PrestaShopShop(api_domain='example.com', api_key='12345')

# Пример 3: Вызов исключения ValueError
try:
    shop = PrestaShopShop()
except ValueError as ex:
    print(f"Ошибка: {ex}")