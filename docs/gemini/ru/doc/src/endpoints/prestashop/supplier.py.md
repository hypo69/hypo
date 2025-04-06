# Модуль для работы с поставщиками PrestaShop

## Обзор

Модуль `supplier.py` предназначен для взаимодействия с API PrestaShop для управления поставщиками. Он содержит класс `PrestaSupplier`, который наследует функциональность от класса `PrestaShop` и предоставляет методы для работы с поставщиками в PrestaShop.

## Подробнее

Этот модуль является частью системы для интеграции с PrestaShop и позволяет автоматизировать процессы, связанные с управлением информацией о поставщиках. Он использует API PrestaShop для выполнения операций, таких как получение, добавление, обновление и удаление данных о поставщиках.

## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` предназначен для работы с поставщиками в PrestaShop. Он наследует функциональность от класса `PrestaShop` и расширяет её методами для управления поставщиками.

**Наследует**:

- `PrestaShop`: Класс `PrestaSupplier` наследует от класса `PrestaShop`, который предоставляет базовые методы для взаимодействия с API PrestaShop.

**Атрибуты**:

- Нет явных атрибутов, кроме тех, что наследуются от `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaSupplier`.

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

**Назначение**: Инициализирует экземпляр класса `PrestaSupplier`, устанавливая параметры для подключения к API PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API для доступа к PrestaShop. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

**Возвращает**:

- None

**Вызывает исключения**:

- `ValueError`: Если не указаны `api_domain` и `api_key`.

**Как работает функция**:

1. **Извлечение параметров из `credentials`**: Если передан аргумент `credentials`, функция пытается извлечь значения `api_domain` и `api_key` из него.
2. **Проверка наличия `api_domain` и `api_key`**: Проверяется, что оба параметра `api_domain` и `api_key` заданы. Если хотя бы один из них не задан, выбрасывается исключение `ValueError`.
3. **Инициализация родительского класса**: Вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

**ASCII flowchart**:

```
A[Получение api_domain и api_key из credentials]
|
B[Проверка наличия api_domain и api_key]
|
C[Вызов конструктора PrestaShop]
```

**Примеры**:

1. Инициализация с использованием отдельных параметров:

```python
supplier = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')
```

2. Инициализация с использованием объекта `SimpleNamespace`:

```python
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
supplier = PrestaSupplier(credentials=credentials)
```

3. Инициализация с использованием словаря:

```python
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
supplier = PrestaSupplier(credentials=credentials)