# Модуль `hypotez/src/endpoints/prestashop/supplier.py`

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier` для работы с поставщиками в платформе PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API.


## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` расширяет функциональность класса `PrestaShop`, предоставляя специфические методы для работы с поставщиками.

**Методы**:

- `__init__`: Инициализирует объект `PrestaSupplier`.


## Функции

Не содержит функций.


## Методы класса `PrestaSupplier`

### `__init__`

**Описание**: Инициализирует объект `PrestaSupplier`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- None.

**Вызывает исключения**:

- `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.


**Детали реализации**:
Метод `__init__` инициализирует атрибуты `api_domain` и `api_key` объекта `PrestaSupplier`. Принимает необязательный параметр `credentials`, позволяющий указать данные API в виде словаря или объекта `SimpleNamespace`. Если `credentials` задан, то значения `api_domain` и `api_key` берутся из него, в противном случае используются значения параметров `api_domain` и `api_key`. Если ни один из параметров `api_domain` и `api_key` не указан, то генерируется исключение `ValueError`. Затем вызывается метод `__init__` родительского класса `PrestaShop` с переданными значениями `api_domain`, `api_key`, `*args`, `**kwards`.