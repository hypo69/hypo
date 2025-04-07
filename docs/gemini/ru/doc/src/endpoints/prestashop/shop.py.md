# Модуль `src.endpoints.prestashop.shop`

## Обзор

Модуль `src.endpoints.prestashop.shop` предоставляет класс `PrestaShopShop` для взаимодействия с магазинами PrestaShop. Он расширяет функциональность класса `PrestaShop` и предназначен для управления и выполнения операций в магазине PrestaShop через API.

## Подробнее

Этот модуль предназначен для упрощения работы с API PrestaShop, предоставляя удобный интерфейс для выполнения различных задач, таких как получение данных, создание, обновление и удаление ресурсов магазина. Он использует модуль `src.logger.logger` для ведения журнала операций и ошибок, а также модуль `src.utils.jjson` для обработки JSON-данных.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` предназначен для работы с магазинами PrestaShop через API. Он наследует функциональность от класса `PrestaShop`.

**Наследует**:

-   `PrestaShop`: Класс, предоставляющий базовую функциональность для взаимодействия с API PrestaShop.

**Атрибуты**:

-   Нет дополнительных атрибутов, кроме тех, что наследуются от `PrestaShop`.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `PrestaShopShop`.

### `__init__`

```python
def __init__(self, 
             credentials: Optional[dict | SimpleNamespace] = None, 
             api_domain: Optional[str] = None, 
             api_key: Optional[str] = None, 
             *args, **kwards) -> None:
    """
    Инициализация магазина PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.
    """
```

**Назначение**: Инициализирует новый экземпляр класса `PrestaShopShop`.

**Параметры**:

-   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
-   `api_domain` (Optional[str], optional): Домен API магазина PrestaShop. По умолчанию `None`.
-   `api_key` (Optional[str], optional): Ключ API для доступа к магазину PrestaShop. По умолчанию `None`.
-   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
-   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

**Возвращает**:

-   None

**Вызывает исключения**:

-   `ValueError`: Если `api_domain` или `api_key` не предоставлены ни в `credentials`, ни как отдельные аргументы.

**Как работает функция**:

1.  Проверяет, предоставлены ли учетные данные (`credentials`). Если да, пытается извлечь `api_domain` и `api_key` из них.
2.  Если `api_domain` или `api_key` не предоставлены (или равны `None`), вызывает исключение `ValueError`.
3.  Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами.

**Примеры**:

```python
# Пример 1: Инициализация с использованием отдельных параметров
shop = PrestaShopShop(api_domain='example.com', api_key='your_api_key')

# Пример 2: Инициализация с использованием словаря credentials
credentials = {'api_domain': 'example.com', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)
```
```
A: Проверка наличия credentials
|
B: Извлечение api_domain и api_key из credentials
|
C: Проверка наличия api_domain и api_key
|
D: Вызов конструктора родительского класса PrestaShop