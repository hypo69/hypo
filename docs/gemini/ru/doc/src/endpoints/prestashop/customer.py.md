# Модуль `customer.py`

## Обзор

Модуль `customer.py` предназначен для работы с клиентами в PrestaShop. Он содержит класс `PrestaCustomer`, который наследуется от класса `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

## Подробней

Этот модуль является частью подсистемы интеграции с PrestaShop и предназначен для управления данными клиентов. Он использует API PrestaShop для выполнения операций с клиентами, такими как создание, удаление, обновление и получение информации о клиентах. Класс `PrestaCustomer` предоставляет удобный интерфейс для работы с API PrestaShop, абстрагируя детали реализации. Расположен в `src/endpoints/prestashop/customer.py`, что указывает на его роль как одной из точек входа для взаимодействия с PrestaShop.

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.

**Методы**:
- `__init__`: Инициализация клиента PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Примеры**
```python
prestacustomer = PrestaCustomer(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
prestacustomer.delete_customer_PrestaShop(3)
prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
print(prestacustomer.get_customer_details_PrestaShop(5))
```

## Функции

### `__init__`

```python
def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """Инициализация клиента PrestaShop.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.
        """
```

**Описание**: Инициализирует экземпляр класса `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.

**Примеры**:

```python
# Пример 1: Инициализация с использованием отдельных параметров api_domain и api_key
customer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')

# Пример 2: Инициализация с использованием словаря credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
customer = PrestaCustomer(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
customer = PrestaCustomer(credentials=credentials)
```
```python