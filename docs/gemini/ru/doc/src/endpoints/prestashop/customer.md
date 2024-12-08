# Модуль hypotez/src/endpoints/prestashop/customer.py

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для взаимодействия с клиентами в системе управления интернет-магазином PrestaShop.  Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop.  Он предоставляет методы для взаимодействия с API PrestaShop.

**Методы**:

- `__init__`

#### `__init__`

**Описание**: Инициализирует объект `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Если не заданы `api_domain` и `api_key`.



**Примечание**:  Документация для методов `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop`, `get_customer_details_PrestaShop`  (которые, похоже, являются методами наследуемого класса) не была предоставлена в исходном коде и должна быть дополнена.  Для обеспечения полной документации, необходимо предоставить соответствующие комментарии с использованием указанного в инструкции формата.