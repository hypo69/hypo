# Модуль `src.endpoints.prestashop.shop`

## Обзор

Модуль `src.endpoints.prestashop.shop` предоставляет класс `PrestaShopShop` для взаимодействия с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и позволяет инициализировать соединение с API PrestaShop, используя домен API и ключ API.

## Оглавление

1.  [Классы](#Классы)
    *   [`PrestaShopShop`](#PrestaShopShop)
        *   [`__init__`](#__init__)

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop.

**Методы**:

*   [`__init__`](#__init__): Инициализация магазина PrestaShop.

#### `__init__`

**Описание**: Инициализирует объект класса `PrestaShopShop`.

**Параметры**:

*   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
*   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
*   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:

*   `None`: Метод не возвращает значений.

**Вызывает исключения**:
* `ValueError`: Если не переданы `api_domain` или `api_key` в явном виде или через `credentials`.