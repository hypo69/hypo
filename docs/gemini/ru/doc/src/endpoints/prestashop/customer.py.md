# Модуль `customer.py`

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для работы с клиентами в PrestaShop. Он позволяет добавлять, удалять, обновлять и получать информацию о клиентах через API PrestaShop.

## Оглавление

- [Класс `PrestaCustomer`](#класс-prestacustomer)
    - [Метод `__init__`](#метод-__init__)
    - [Метод `add_customer_PrestaShop`](#метод-add_customer_prestashop)
    - [Метод `delete_customer_PrestaShop`](#метод-delete_customer_prestashop)
    - [Метод `update_customer_PrestaShop`](#метод-update_customer_prestashop)
    - [Метод `get_customer_details_PrestaShop`](#метод-get_customer_details_prestashop)

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.

**Пример использования:**
```python
prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
prestacustomer.delete_customer_PrestaShop(3)
prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
print(prestacustomer.get_customer_details_PrestaShop(5))
```

#### Метод `__init__`

**Описание**: Инициализация клиента PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены.

#### Метод `add_customer_PrestaShop`

**Описание**: Добавляет нового клиента в PrestaShop.

**Параметры**:
- `name` (str): Имя клиента.
- `email` (str): Электронная почта клиента.
- `options` (Optional[dict], optional): Дополнительные опции для создания клиента. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь с данными о созданном клиенте.
- `None`: В случае ошибки.

**Вызывает исключения**:
- `PrestaShopException`: При возникновении ошибки в PrestaShop.

#### Метод `delete_customer_PrestaShop`

**Описание**: Удаляет клиента из PrestaShop по ID.

**Параметры**:
- `customer_id` (int): ID клиента для удаления.

**Возвращает**:
- `bool`: `True` в случае успешного удаления, `False` в противном случае.

**Вызывает исключения**:
- `PrestaShopException`: При возникновении ошибки в PrestaShop.

#### Метод `update_customer_PrestaShop`

**Описание**: Обновляет данные существующего клиента в PrestaShop.

**Параметры**:
- `customer_id` (int): ID клиента для обновления.
- `data` (dict): Словарь с данными для обновления клиента.

**Возвращает**:
- `dict`: Словарь с данными об обновленном клиенте.
- `None`: В случае ошибки.

**Вызывает исключения**:
- `PrestaShopException`: При возникновении ошибки в PrestaShop.

#### Метод `get_customer_details_PrestaShop`

**Описание**: Получает детальную информацию о клиенте по ID.

**Параметры**:
- `customer_id` (int): ID клиента для получения информации.

**Возвращает**:
- `dict`: Словарь с данными о клиенте.
- `None`: В случае ошибки.

**Вызывает исключения**:
- `PrestaShopException`: При возникновении ошибки в PrestaShop.