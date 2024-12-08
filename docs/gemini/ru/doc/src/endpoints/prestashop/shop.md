# Модуль hypotez/src/endpoints/prestashop/shop.py

## Обзор

Модуль `shop.py` предоставляет класс `PrestaShopShop` для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.  Модуль использует библиотеку `header`, `gs`, `logger`, `jjson`, `PrestaShop` из других модулей проекта.

## Классы

### `PrestaShopShop`

**Описание**: Класс `PrestaShopShop` расширяет функциональность базового класса `PrestaShop` для работы со спецификой магазинов PrestaShop.

**Методы**:

- `__init__`: Инициализирует объект `PrestaShopShop`.

## Функции

(Нет функций в этом модуле)


## Методы класса `PrestaShopShop`

### `__init__`

**Описание**: Инициализирует магазин PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Возвращает ничего (None).

**Вызывает исключения**:

- `ValueError`: Если не заданы оба параметра `api_domain` и `api_key`.  Возникает, если `credentials` не содержит необходимых данных и `api_domain` или `api_key` не заданы явно.


```