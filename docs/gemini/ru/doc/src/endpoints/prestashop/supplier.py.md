# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier` для взаимодействия с поставщиками в PrestaShop. Он наследует функциональность от базового класса `PrestaShop` и обеспечивает управление поставщиками через API PrestaShop.

## Оглавление

1.  [Классы](#классы)
    -   [`PrestaSupplier`](#prestasupplier)
2. [Функции](#функции)

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Методы**:

-   `__init__`: Инициализация экземпляра класса `PrestaSupplier`.

#### `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaSupplier`.

**Параметры**:

-   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
-   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
-   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
-   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор суперкласса.
-   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор суперкласса.

**Вызывает исключения**:

-   `ValueError`: Если не предоставлены параметры `api_domain` и `api_key`.

## Функции
    
На данный момент в файле нет отдельных функций.