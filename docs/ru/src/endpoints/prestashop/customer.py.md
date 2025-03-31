# Модуль src.endpoints.prestashop.customer

## Обзор

Модуль `src.endpoints.prestashop.customer` предназначен для работы с клиентами в PrestaShop. Он предоставляет класс `PrestaCustomer`, который позволяет добавлять, удалять, обновлять и получать информацию о клиентах через API PrestaShop.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с платформой PrestaShop для управления информацией о клиентах. Он использует API PrestaShop для выполнения операций, таких как добавление новых клиентов, удаление существующих, обновление информации о клиентах и получение подробных данных о конкретных клиентах. Модуль предназначен для упрощения взаимодействия с PrestaShop API и предоставляет удобный интерфейс для работы с клиентами.

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.

**Как работает класс**:
Класс `PrestaCustomer` наследуется от класса `PrestaShop` и предоставляет методы для выполнения операций с клиентами в PrestaShop. При инициализации класса требуется указать домен API и ключ API. Класс использует эти учетные данные для аутентификации и авторизации при взаимодействии с PrestaShop API. Он предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCustomer`.

#### `__init__`

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

**Как работает функция**:
Функция `__init__` является конструктором класса `PrestaCustomer`. Она принимает параметры для инициализации клиента PrestaShop, такие как домен API и ключ API. Если переданы учетные данные в виде словаря или объекта `SimpleNamespace`, они используются для получения домена API и ключа API. Если домен API и ключ API не переданы или не найдены в учетных данных, вызывается исключение `ValueError`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в родительский класс.
- `**kwards`: Произвольные именованные аргументы, передаваемые в родительский класс.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.

**Примеры**:

```python
prestacustomer = PrestaCustomer(api_domain='https://yourdomain.com/api', api_key='YOUR_API_KEY')
prestacustomer = PrestaCustomer(credentials={'api_domain': 'https://yourdomain.com/api', 'api_key': 'YOUR_API_KEY'})
```
```