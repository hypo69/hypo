# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `supplier.py` содержит класс `PrestaSupplier`, предназначенный для работы с поставщиками в системе управления интернет-магазином PrestaShop.  Он расширяет класс `PrestaShop`, предоставляя методы для взаимодействия с API поставщиков.


## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` наследуется от `PrestaShop` и предоставляет методы для работы с поставщиками PrestaShop.

**Методы**:

- `__init__`: Инициализирует объект `PrestaSupplier`.


## Функции

(Нет функций в данном файле)


## Методы класса `PrestaSupplier`

### `__init__`

**Описание**: Метод инициализирует объект `PrestaSupplier`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
  
**Возвращает**:
    -  Не имеет значения возвращаемого типа.

**Вызывает исключения**:

- `ValueError`: Если оба параметра `api_domain` и `api_key` не заданы.