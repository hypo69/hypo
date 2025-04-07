# Модуль для работы с клиентами PrestaShop

## Обзор

Модуль `customer.py` предназначен для работы с клиентами в PrestaShop. Он предоставляет класс `PrestaCustomer`, который наследует базовый класс `PrestaShop` и реализует методы для добавления, удаления, обновления и получения информации о клиентах через API PrestaShop.

## Подробнее

Модуль содержит класс `PrestaCustomer`, который используется для взаимодействия с API PrestaShop для управления данными о клиентах. Класс предоставляет удобные методы для выполнения различных операций, таких как добавление нового клиента, удаление существующего, обновление информации о клиенте и получение детальной информации о конкретном клиенте. Для работы с API требуется указать домен API и ключ API.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop.

**Наследует**:
- `PrestaShop`: Класс наследует функциональность для взаимодействия с API PrestaShop.

**Атрибуты**:
- Отсутствуют, поскольку используются атрибуты родительского класса `PrestaShop`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCustomer`.
- `add_customer_PrestaShop`: Добавляет нового клиента в PrestaShop.
- `delete_customer_PrestaShop`: Удаляет клиента из PrestaShop.
- `update_customer_PrestaShop`: Обновляет информацию о клиенте в PrestaShop.
- `get_customer_details_PrestaShop`: Получает детальную информацию о клиенте из PrestaShop.

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
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- Ничего.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.

**Как работает функция**:

1. **Проверка наличия `credentials`**: Функция проверяет, был ли передан аргумент `credentials`.
2. **Извлечение параметров из `credentials`**: Если `credentials` передан, функция пытается извлечь значения `api_domain` и `api_key` из `credentials`.
3. **Проверка наличия `api_domain` и `api_key`**: Функция проверяет, были ли переданы `api_domain` и `api_key` либо через `credentials`, либо напрямую.
4. **Вызов конструктора родительского класса**: Если все необходимые параметры присутствуют, вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.
5. **Генерация исключения `ValueError`**: Если `api_domain` или `api_key` не были переданы, генерируется исключение `ValueError`.

```
Проверка наличия credentials --> Извлечение api_domain и api_key из credentials --> Проверка наличия api_domain и api_key --> Вызов конструктора родительского класса PrestaShop
    ^                                                                                                                                                   |
    |_____________________________________________________________________________________________________________________________________________________|
```

**Примеры**:

```python
# Пример 1: Инициализация с передачей api_domain и api_key напрямую
prestacustomer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')

# Пример 2: Инициализация с передачей credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
prestacustomer = PrestaCustomer(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
prestacustomer = PrestaCustomer(credentials=credentials)
```

## Функции

В данном модуле функции отсутствуют.