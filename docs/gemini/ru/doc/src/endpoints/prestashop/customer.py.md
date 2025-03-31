# Модуль `src.endpoints.prestashop.customer`

## Обзор

Модуль `src.endpoints.prestashop.customer` предназначен для работы с клиентами в PrestaShop. Он содержит класс `PrestaCustomer`, который предоставляет методы для добавления, удаления, обновления и получения информации о клиентах PrestaShop через API.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с PrestaShop для управления данными клиентов. Он использует модуль `src.logger` для логирования и обработки ошибок, а также модуль `src.utils.jjson` для работы с JSON.

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.

**Как работает класс**:
Класс `PrestaCustomer` наследуется от класса `PrestaShop` и предоставляет методы для выполнения различных операций с клиентами PrestaShop, таких как добавление, удаление, обновление и получение информации о клиентах.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaCustomer`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Примеры**:

```python
prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
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
    ...
```

**Как работает функция**:

Функция `__init__` является конструктором класса `PrestaCustomer`. Она инициализирует экземпляр класса, принимая параметры учетных данных (`credentials`), домен API (`api_domain`) и ключ API (`api_key`). Если параметры учетных данных переданы в виде словаря или объекта `SimpleNamespace`, функция извлекает значения `api_domain` и `api_key` из них. Если `api_domain` или `api_key` не указаны, функция вызывает исключение `ValueError`. Затем вызывается конструктор родительского класса `PrestaShop` для инициализации общих параметров.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:

- `ValueError`: Если не указаны `api_domain` или `api_key`.

**Примеры**:

```python
# Пример инициализации с использованием api_domain и api_key
prestacustomer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')

# Пример инициализации с использованием словаря credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
prestacustomer = PrestaCustomer(credentials=credentials)

# Пример инициализации с использованием SimpleNamespace credentials
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
prestacustomer = PrestaCustomer(credentials=credentials)