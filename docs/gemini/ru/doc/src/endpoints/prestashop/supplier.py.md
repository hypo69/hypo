# Модуль `supplier.py`

## Обзор

Модуль `supplier.py` предназначен для работы с поставщиками в PrestaShop. Он содержит класс `PrestaSupplier`, который расширяет класс `PrestaShop` и предоставляет функциональность для взаимодействия с API PrestaShop для управления поставщиками.

## Подробней

Этот модуль является частью подсистемы `src.endpoints.prestashop` и предоставляет инструменты для автоматизации задач, связанных с поставщиками в PrestaShop. Он использует модуль `src.logger.logger` для логирования и `src.utils.jjson` для работы с JSON-данными.

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Наследует**:
- `PrestaShop`: Класс `PrestaSupplier` наследует от класса `PrestaShop`, что позволяет ему использовать общую функциональность для взаимодействия с API PrestaShop.

**Атрибуты**:
- Нет специфических атрибутов, определенных в классе, кроме тех, что наследуются от `PrestaShop`.

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

**Назначение**: Инициализация экземпляра класса `PrestaSupplier`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key` либо через `credentials`, либо по отдельности.

**Как работает функция**:

1. **Извлечение данных из `credentials`**:
   - Если параметр `credentials` передан (является словарем или объектом `SimpleNamespace`), функция пытается извлечь значения `api_domain` и `api_key` из него.
2. **Проверка наличия обязательных параметров**:
   - Проверяет, установлены ли значения `api_domain` и `api_key`. Если хотя бы один из них отсутствует, выбрасывается исключение `ValueError`.
3. **Инициализация родительского класса**:
   - Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами, необходимыми для работы с API PrestaShop.

**ASCII flowchart**:

```
A[Проверка credentials] --> B{credentials is not None?}
B -- Да --> C[Извлечение api_domain и api_key из credentials]
B -- Нет --> D[Проверка api_domain и api_key на None]
D -- api_domain или api_key is None --> E[Выброс ValueError]
D -- api_domain и api_key is not None --> F[Инициализация PrestaShop]
F --> Конец
E --> Конец
```

**Примеры**:

1. Инициализация с передачей `api_domain` и `api_key` напрямую:

```python
supplier = PrestaSupplier(api_domain='example.com', api_key='test_key')
```

2. Инициализация с передачей `credentials` в виде словаря:

```python
credentials = {'api_domain': 'example.com', 'api_key': 'test_key'}
supplier = PrestaSupplier(credentials=credentials)
```

3. Инициализация с передачей `credentials` в виде `SimpleNamespace`:

```python
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='test_key')
supplier = PrestaSupplier(credentials=credentials)