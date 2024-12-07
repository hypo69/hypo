# Модуль hypotez/src/endpoints/prestashop/shop.py

## Обзор

Модуль `shop.py` предоставляет класс `PrestaShopShop` для работы с магазинами PrestaShop. Он наследуется от класса `PrestaShop` из модуля `api.py`, добавляя специфические методы для работы с магазинами.  Модуль использует аутентификацию и взаимодействует с API PrestaShop.


## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop.  Наследуется от `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект `PrestaShopShop`.


## Функции

Нет функций в этом модуле.


### `__init__`

**Описание**: Инициализирует объект `PrestaShopShop`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- Нет возвращаемых значений.

**Вызывает исключения**:

- `ValueError`: Если не заданы значения `api_domain` и `api_key`.  Возникает, если не заданы оба параметра.


**Подробное описание**:

Метод `__init__` инициализирует объект `PrestaShopShop`, принимая параметры для подключения к API PrestaShop.  Он проверяет наличие значений `api_domain` и `api_key`. Если они не заданы, генерируется исключение `ValueError`. Если `credentials` задан, значения из него переопределяют значения параметров `api_domain` и `api_key`.  Далее он вызывает конструктор базового класса `PrestaShop` для инициализации соединения с API.
```