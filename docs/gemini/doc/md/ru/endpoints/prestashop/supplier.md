```markdown
# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `supplier.py` содержит класс `PrestaSupplier`, предназначенный для работы с поставщиками в системе PrestaShop. Класс наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop, связанными с поставщиками.

## Оглавление

- [Модуль `supplier.py`](#модуль-supplierpy)
- [Класс `PrestaSupplier`](#класс-prestasupplier)
- [Метод `__init__`](#метод-init)


## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop, наследующий от класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект `PrestaSupplier`.


## Функции


## Методы

### `__init__`

**Описание**: Инициализирует объект `PrestaSupplier`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены значения для `api_domain` и `api_key`.


```
