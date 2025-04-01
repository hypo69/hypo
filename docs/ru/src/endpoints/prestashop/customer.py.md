# Модуль для работы с клиентами PrestaShop

## Обзор

Модуль `customer.py` предоставляет класс `PrestaCustomer`, предназначенный для взаимодействия с API PrestaShop для управления информацией о клиентах. Он позволяет добавлять, удалять, обновлять и получать информацию о клиентах в магазине PrestaShop.

## Подробнее

Этот модуль обеспечивает удобный интерфейс для работы с клиентами PrestaShop, используя API PrestaShop. Он наследует функциональность из класса `PrestaShop` и предоставляет дополнительные методы для управления клиентами. Расположение модуля в структуре проекта указывает на его роль как части подсистемы, отвечающей за взаимодействие с PrestaShop.

## Классы

### `PrestaCustomer`

**Описание**: Класс `PrestaCustomer` предназначен для работы с клиентами в PrestaShop. Он наследует функциональность подключения к API PrestaShop от класса `PrestaShop` и предоставляет методы для создания, удаления, обновления и получения информации о клиентах.

**Наследует**:

- `PrestaShop`: Класс, предоставляющий базовые методы для взаимодействия с API PrestaShop.

**Атрибуты**:

- Отсутствуют, класс использует атрибуты родительского класса `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PrestaCustomer`, проверяет наличие ключа API и домена, вызывает конструктор родительского класса `PrestaShop`.

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
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:

- None

**Вызывает исключения**:

- `ValueError`: Если не предоставлены `api_domain` или `api_key`.

**Как работает функция**:

1. **Проверка наличия `credentials`**: Функция проверяет, был ли передан аргумент `credentials`. Если да, то пытается извлечь значения `api_domain` и `api_key` из этого аргумента, используя метод `.get()`. Это позволяет передавать параметры API в виде словаря или объекта `SimpleNamespace`.

2. **Проверка наличия `api_domain` и `api_key`**: Функция проверяет, были ли переданы `api_domain` и `api_key` либо как отдельные аргументы, либо внутри аргумента `credentials`. Если хотя бы один из этих параметров отсутствует, вызывается исключение `ValueError`.

3. **Инициализация родительского класса**: Если все необходимые параметры присутствуют, вызывается конструктор родительского класса `PrestaShop` с переданными значениями `api_domain`, `api_key` и остальными аргументами `*args` и `**kwards`. Это необходимо для настройки соединения с API PrestaShop.

**Примеры**:

```python
# Инициализация с использованием отдельных параметров
prestacustomer = PrestaCustomer(api_domain='example.com', api_key='12345')

# Инициализация с использованием объекта SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='12345')
prestacustomer = PrestaCustomer(credentials=credentials)

# Инициализация с использованием словаря
credentials = {'api_domain': 'example.com', 'api_key': '12345'}
prestacustomer = PrestaCustomer(credentials=credentials)