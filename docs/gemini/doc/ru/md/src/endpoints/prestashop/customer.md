# Модуль hypotez/src/endpoints/prestashop/customer.py

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для работы с клиентами в системе управления интернет-магазином PrestaShop.  Класс наследуется от `PrestaShop` и содержит методы для добавления, удаления, обновления и получения данных о клиентах.

## Классы

### `PrestaCustomer`

**Описание**:  Класс для работы с клиентами в PrestaShop.  Обеспечивает взаимодействие с API PrestaShop для управления клиентами.

**Методы**:

- `__init__`


### `__init__`

**Описание**: Инициализирует объект `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- Нет значения (None). Инициализирует объект `PrestaCustomer`.

**Вызывает исключения**:
- `ValueError`: Если оба параметра `api_domain` и `api_key` не заданы.

## Функции

(В данном файле нет других функций, кроме методов класса `PrestaCustomer`)