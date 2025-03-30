# Модуль `src.endpoints.prestashop.supplier`

## Обзор

Модуль `src.endpoints.prestashop.supplier` предоставляет класс `PrestaSupplier` для работы с поставщиками в PrestaShop. Он расширяет базовый класс `PrestaShop` и обеспечивает функциональность для взаимодействия с API PrestaShop для управления поставщиками.

## Содержание

1.  [Классы](#классы)
    *   [`PrestaSupplier`](#prestasupplier)

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Методы**:

*   `__init__`: Инициализация поставщика PrestaShop.

#### `__init__`

**Описание**: Инициализация поставщика PrestaShop.

**Параметры**:

*   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
*   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
*   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы, передаваемые в родительский класс `PrestaShop`.
*   `**kwards`: Произвольные именованные аргументы, передаваемые в родительский класс `PrestaShop`.

**Вызывает исключения**:

*   `ValueError`: Если не предоставлены `api_domain` и `api_key`.