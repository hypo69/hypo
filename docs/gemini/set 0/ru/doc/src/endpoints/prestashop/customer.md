# Модуль `hypotez/src/endpoints/prestashop/customer.py`

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для работы с клиентами в системе управления интернет-магазином PrestaShop.  Он использует базовый класс `PrestaShop` для взаимодействия с API.  Модуль обеспечивает функции добавления, удаления, обновления и получения информации о клиентах.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` наследуется от класса `PrestaShop` и предоставляет методы для работы с клиентами PrestaShop.

**Методы**:

- `__init__`:

**Описание**: Инициализирует объект `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не возвращает ничего.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.


```
```python
# Пример использования
# (не включен в документацию, но важен для понимания)
# prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
# prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
# ...
```


**Примечание**:  В примере использования класса, приведенном в документации класса, предполагается, что `API_DOMAIN` и `API_KEY` определены где-то вне данного файла.  Для удобства и полноты документации было бы полезно добавить примеры (возможно, в формате кода) использования `credentials`.

**Примечание**: Документация к методам `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop`, и `get_customer_details_PrestaShop` отсутствует.  Для полной документации необходимо добавить описания этих методов с указанием параметров, возвращаемых значений и возможных исключений.