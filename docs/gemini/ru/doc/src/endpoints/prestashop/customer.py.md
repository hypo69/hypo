# Модуль `customer.py`

## Обзор

Модуль `customer.py` предназначен для работы с клиентами в PrestaShop. Он предоставляет класс `PrestaCustomer`, который позволяет добавлять, удалять, обновлять и получать информацию о клиентах через API PrestaShop.

## Подробней

Этот модуль предоставляет удобный интерфейс для взаимодействия с API PrestaShop, упрощая выполнение операций, связанных с управлением клиентами. Он использует модуль `src.logger.logger` для логирования действий и ошибок, а также модуль `src.utils.jjson` для обработки JSON-данных. Расположен в структуре проекта в `src/endpoints/prestashop/customer.py`, что указывает на его роль как части подсистемы взаимодействия с PrestaShop.

## Классы

### `PrestaCustomer`

**Описание**: Класс для работы с клиентами в PrestaShop.

**Методы**:
- `__init__`: Инициализация клиента PrestaShop.
- `add_customer_PrestaShop`: Добавляет нового клиента в PrestaShop.
- `delete_customer_PrestaShop`: Удаляет клиента из PrestaShop.
- `update_customer_PrestaShop`: Обновляет информацию о клиенте в PrestaShop.
- `get_customer_details_PrestaShop`: Получает подробную информацию о клиенте из PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Примеры**
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
```

**Описание**: Инициализирует экземпляр класса `PrestaCustomer`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены и не найдены в `credentials`.

**Примеры**:
```python
prestacustomer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')
```

```python
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
prestacustomer = PrestaCustomer(credentials=credentials)
```
```python
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
prestacustomer = PrestaCustomer(credentials=credentials)
```