# Модуль для работы с магазином PrestaShop

## Обзор

Модуль `shop.py` предназначен для взаимодействия с магазинами, созданными на платформе PrestaShop. Он включает в себя класс `PrestaShopShop`, который наследуется от класса `PrestaShop` и предоставляет функциональность для работы с API PrestaShop. Модуль обеспечивает возможность инициализации магазина PrestaShop с использованием домена API и ключа API.

## Подробнее

Этот модуль обеспечивает удобный интерфейс для работы с магазинами PrestaShop, позволяя упростить процесс взаимодействия с API и выполнения различных операций, таких как получение данных о продуктах, категориях и т.д. Он использует модуль `src.logger` для логирования событий и ошибок, а также модуль `src.utils.jjson` для работы с JSON-данными.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` предназначен для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

**Наследует**:

- `PrestaShop`: Класс, предоставляющий базовую функциональность для работы с API PrestaShop.

**Атрибуты**:

- Отсутствуют специфичные атрибуты, кроме тех, что наследуются от `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaShopShop`.

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

- `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.

**Как работает функция**:

1. **Проверка наличия credentials**: Функция проверяет, передан ли параметр `credentials`. Если да, извлекает значения `api_domain` и `api_key` из него, перезаписывая значения, переданные напрямую, если они есть.
2. **Валидация параметров**: Проверяет, указаны ли `api_domain` и `api_key`. Если хотя бы один из них не указан, возбуждается исключение `ValueError`.
3. **Вызов конструктора родительского класса**: Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами.

```
A: Проверка credentials
|
-- B: Извлечение api_domain и api_key из credentials (если credentials переданы)
|
C: Валидация api_domain и api_key
|
-- D: Вызов конструктора родительского класса PrestaShop
```

**Примеры**:

```python
# Пример 1: Инициализация с использованием отдельных параметров
shop = PrestaShopShop(api_domain='https://example.com/api', api_key='your_api_key')

# Пример 2: Инициализация с использованием credentials в виде словаря
credentials = {'api_domain': 'https://example.com/api', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)

# Пример 3: Инициализация с использованием credentials в виде SimpleNamespace
credentials = SimpleNamespace(api_domain='https://example.com/api', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)