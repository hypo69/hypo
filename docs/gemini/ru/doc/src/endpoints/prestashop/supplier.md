# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier` для взаимодействия с API поставщиков PrestaShop.  Он наследуется от класса `PrestaShop` и добавляет необходимые методы для работы с поставщиками.

## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` предназначен для работы с поставщиками в системе PrestaShop.  Он расширяет функциональность базового класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaSupplier`.


## Функции

Нет функций в этом модуле.


## Методы класса `PrestaSupplier`

### `__init__`

**Описание**: Метод `__init__` инициализирует экземпляр класса `PrestaSupplier`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Дополнительные позиционные аргументы, передаваемые в конструктор базового класса.
- `**kwards`: Дополнительные именованные аргументы, передаваемые в конструктор базового класса.


**Возвращает**:

- Нет значения возвращается.


**Вызывает исключения**:

- `ValueError`: Бросается, если не заданы `api_domain` и `api_key`.


```