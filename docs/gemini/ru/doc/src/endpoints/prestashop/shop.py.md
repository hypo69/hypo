# Модуль `hypotez/src/endpoints/prestashop/shop.py`

## Обзор

Модуль `shop.py` предоставляет класс `PrestaShopShop` для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и обеспечивает функциональность для взаимодействия с API PrestaShop.

## Содержание

- [Классы](#классы)
    - [`PrestaShopShop`](#prestashopshop)
- [Переменные](#переменные)
    - [`MODE`](#mode)

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop.

**Методы**:
- `__init__`: Инициализирует объект магазина PrestaShop.

#### `__init__`

**Описание**: Инициализация магазина PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если не переданы оба параметра `api_domain` и `api_key`

## Переменные

### `MODE`

**Описание**: Режим работы (по умолчанию 'dev').

**Тип**: str