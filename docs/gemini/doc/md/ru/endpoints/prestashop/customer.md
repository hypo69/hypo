```markdown
# Модуль `hypotez/src/endpoints/prestashop/customer.py`

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для работы с клиентами в системе управления интернет-магазином PrestaShop. Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.


## Оглавление

- [Классы](#классы)
    - [PrestaCustomer](#presta-customer)
        - [\_\_init\_\_](#init)

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop, наследуется от `PrestaShop`. Предоставляет методы для взаимодействия с API PrestaShop.

**Методы**:
- `__init__`: Инициализация клиента PrestaShop.

### `PrestaCustomer.__init__`

**Описание**: Метод инициализации класса `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- None

**Вызывает исключения**:
- `ValueError`: Если не заданы параметры `api_domain` и `api_key`.


```
