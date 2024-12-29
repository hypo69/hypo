# Модуль `customer`

## Обзор

Модуль `customer` предоставляет класс `PrestaCustomer` для взаимодействия с API PrestaShop, позволяя выполнять операции с клиентами, такие как добавление, удаление, обновление и получение информации о клиентах.

## Содержание

1.  [Классы](#классы)
    *   [`PrestaCustomer`](#prestaCustomer)
2.  [Функции](#функции)
    *   [`__init__`](#__init__)

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop.

**Методы**:
- [`__init__`](#__init__): Инициализирует экземпляр класса PrestaCustomer.

## Функции

### `__init__`

**Описание**: Инициализация клиента PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Вызывает исключения**:
- `ValueError`: Если не переданы оба параметра: `api_domain` и `api_key`.