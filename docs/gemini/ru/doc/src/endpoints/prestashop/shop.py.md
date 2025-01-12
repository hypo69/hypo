# Модуль `src.endpoints.prestashop.shop`

## Обзор

Модуль `src.endpoints.prestashop.shop` предоставляет класс `PrestaShopShop` для взаимодействия с магазинами PrestaShop. Этот класс расширяет функциональность базового класса `PrestaShop` и позволяет настраивать соединение с магазином, используя домен API и ключ API.

## Содержание

- [Классы](#классы)
    - [PrestaShopShop](#prestashopshop)

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
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены оба параметра `api_domain` и `api_key`.