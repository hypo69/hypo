# Модуль `customer.py`

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для взаимодействия с клиентами в PrestaShop. Он позволяет добавлять, удалять, обновлять и получать информацию о клиентах через API PrestaShop.

## Оглавление

- [Классы](#классы)
  - [`PrestaCustomer`](#class-prestacustomer)
    - [`__init__`](#__init__)
    
## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop. Позволяет выполнять операции добавления, удаления, обновления и получения информации о клиентах.

**Пример использования:**

```python
prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
prestacustomer.delete_customer_PrestaShop(3)
prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
print(prestacustomer.get_customer_details_PrestaShop(5))
```
#### `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key`.