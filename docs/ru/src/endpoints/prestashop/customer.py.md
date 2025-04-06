# Модуль для работы с клиентами PrestaShop

## Обзор

Модуль `customer.py` предназначен для взаимодействия с API PrestaShop для управления информацией о клиентах. Он содержит класс `PrestaCustomer`, который предоставляет методы для добавления, удаления, обновления и получения информации о клиентах в магазине PrestaShop.

## Подробней

Этот модуль облегчает интеграцию с PrestaShop API, позволяя автоматизировать процессы управления клиентами, такие как создание учетных записей, обновление данных и удаление устаревших профилей. Он использует модуль `PrestaShop` из этого же пакета `src.endpoints.prestashop.api`, для работы с API PrestaShop.  Также применяются модули `src.logger.logger` для ведения логов и `src.utils.jjson` для загрузки JSON-данных.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop. Он наследует функциональность от класса `PrestaShop` и предоставляет методы для выполнения операций CRUD (Create, Read, Update, Delete) над данными клиентов через API PrestaShop.

**Принцип работы**:
1.  **Инициализация**: При создании экземпляра класса `PrestaCustomer` происходит инициализация с использованием домена API и ключа API, необходимыми для аутентификации при взаимодействии с PrestaShop API.
2.  **Методы CRUD**: Класс содержит методы для добавления (`add_customer_PrestaShop`), удаления (`delete_customer_PrestaShop`), обновления (`update_customer_PrestaShop`) и получения информации (`get_customer_details_PrestaShop`) о клиентах.

**Наследует**:
*   `PrestaShop`: Класс `PrestaCustomer` наследует от класса `PrestaShop`, что позволяет ему использовать общие методы и свойства для взаимодействия с API PrestaShop.

**Атрибуты**:
*   Отсутствуют явно объявленные атрибуты, но используются атрибуты, унаследованные от класса `PrestaShop`, такие как `api_domain` и `api_key`.

**Методы**:
*   `__init__`: Инициализирует экземпляр класса `PrestaCustomer` с заданными учетными данными и выполняет инициализацию родительского класса `PrestaShop`.

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

**Назначение**: Инициализация экземпляра класса `PrestaCustomer`.

**Параметры**:
*   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
*   `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
*   `api_key` (Optional[str], optional): Ключ API для доступа к PrestaShop. По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**: None

**Вызывает исключения**:
*   `ValueError`: Если не предоставлены `api_domain` и `api_key` ни через `credentials`, ни как отдельные аргументы.

**Как работает функция**:

1.  Извлекает `api_domain` и `api_key` из `credentials`, если они предоставлены.
2.  Проверяет, что `api_domain` и `api_key` установлены, и вызывает исключение `ValueError`, если это не так.
3.  Вызывает конструктор родительского класса `PrestaShop` с переданными `api_domain`, `api_key` и другими аргументами.

```
Credentials -> Извлечь api_domain и api_key
    |
    No Credentials -> api_domain & api_key arguments
    |
    Check api_domain & api_key
    |
    api_domain & api_key -> super().__init__(api_domain, api_key, *args, **kwards)
    |
    Not api_domain & api_key -> ValueError
```

**Примеры**:

```python
# Пример 1: Инициализация с использованием отдельных параметров
prestacustomer = PrestaCustomer(api_domain='example.com', api_key='12345')

# Пример 2: Инициализация с использованием словаря credentials
credentials = {'api_domain': 'example.com', 'api_key': '12345'}
prestacustomer = PrestaCustomer(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='12345')
prestacustomer = PrestaCustomer(credentials=credentials)