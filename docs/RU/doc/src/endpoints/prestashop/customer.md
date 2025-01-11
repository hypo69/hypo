# Модуль `hypotez/src/endpoints/prestashop/customer.py`

## Обзор

Данный модуль предоставляет класс `PrestaCustomer` для взаимодействия с клиентами в системе PrestaShop. Он наследуется от класса `PrestaShop` и расширяет функциональность для работы с клиентами.

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.  Позволяет добавлять, удалять, обновлять и получать информацию о клиентах.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  None

**Вызывает исключения**:
- `ValueError`: Если не заданы значения `api_domain` и `api_key`.


```python
# Пример использования класса PrestaCustomer
# prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
# prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
# prestacustomer.delete_customer_PrestaShop(3)
# prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
# print(prestacustomer.get_customer_details_PrestaShop(5))
```

**Примечание**:  Методы `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop` и `get_customer_details_PrestaShop` предполагаются как часть класса `PrestaCustomer`, но их реализации в данном примере не представлены.  Эти методы должны быть реализованы для полноценного функционирования класса.


## Функции

(В данном файле нет других функций, кроме `__init__`)


## Модули

(Список импортированных модулей)

- `sys`
- `os`
- `attr`
- `pathlib`
- `typing`
- `types`
- `header`
- `gs`
- `logger`
- `jjson`
- `PrestaShop`
- `PrestaShopException`


```