# Модуль `supplier.py`

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier` для работы с поставщиками в PrestaShop. Он включает методы для получения данных о поставщиках через API PrestaShop.

## Оглавление

1.  [Классы](#классы)
    *   [`PrestaSupplier`](#prestasuplier)
        *   [`__init__`](#__init__)

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop. Наследуется от класса `PrestaShop`.

#### `__init__`

**Описание**: Инициализация поставщика PrestaShop.

**Параметры**:

*   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
*   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
*   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:

*   `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.