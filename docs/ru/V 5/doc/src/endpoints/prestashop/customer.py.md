# Модуль для работы с клиентами в PrestaShop

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer` для взаимодействия с API PrestaShop, позволяя выполнять операции, связанные с клиентами, такие как добавление, удаление, обновление и получение информации о клиентах.

## Подробней

Этот модуль предназначен для упрощения работы с клиентами в PrestaShop путем предоставления удобного интерфейса для выполнения операций через API PrestaShop. Он использует класс `PrestaShop` из модуля `api.py` для установления соединения и выполнения запросов к API. Расположение файла в структуре проекта указывает на его роль как части endpoints для PrestaShop.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop. Он предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

**Как работает класс**:
Класс `PrestaCustomer` наследуется от класса `PrestaShop` и использует его для взаимодействия с API PrestaShop. При инициализации класса требуется передать учетные данные API (домен и ключ). Класс содержит методы для выполнения различных операций с клиентами, таких как добавление, удаление, обновление и получение информации о клиентах.

**Методы**:

- `__init__`: Инициализация клиента PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
- `api_domain` (Optional[str], optional): Домен API. Defaults to None.
- `api_key` (Optional[str], optional): Ключ API. Defaults to None.

**Примеры**
   ```python
        prestacustomer = PrestaCustomer(API_DOMAIN='https://yourdomain.com/api', API_KEY='YOUR_API_KEY')
        prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        prestacustomer.delete_customer_PrestaShop(3)
        prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
        print(prestacustomer.get_customer_details_PrestaShop(5))
   ```

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

**Описание**: Метод инициализации класса `PrestaCustomer`.

**Как работает функция**:
Метод `__init__` инициализирует класс `PrestaCustomer`. Он принимает параметры `credentials`, `api_domain` и `api_key` для аутентификации в API PrestaShop. Если передан параметр `credentials`, он должен содержать `api_domain` и `api_key`. Если `api_domain` и `api_key` не переданы ни в `credentials`, ни отдельно, вызывается исключение `ValueError`. Затем вызывается конструктор родительского класса `PrestaShop` с переданными учетными данными.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Вызывает исключения**:

- `ValueError`: Если не переданы `api_domain` и `api_key`.

**Примеры**:

```python
prestacustomer = PrestaCustomer(api_domain='https://yourdomain.com/api', api_key='YOUR_API_KEY')
# или
credentials = {'api_domain': 'https://yourdomain.com/api', 'api_key': 'YOUR_API_KEY'}
prestacustomer = PrestaCustomer(credentials=credentials)
```