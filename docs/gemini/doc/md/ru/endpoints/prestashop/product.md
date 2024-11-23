```markdown
# Модуль `hypotez/src/endpoints/prestashop/product.py`

## Обзор

Модуль `product.py` предоставляет инструменты для работы с товарами в API PrestaShop.  Он использует класс `PrestaProduct`, наследующий от `PrestaShop`, для выполнения операций по проверке, поиску и получению информации о товарах.


## Оглавление

- [Классы](#классы)
    - [PrestaProduct](#prestaproduct)
- [Функции](#функции)
    


## Классы

### `PrestaProduct`

**Описание**: Класс `PrestaProduct` представляет собой сущность товара из модуля PrestaShop. Он предоставляет методы для взаимодействия с API PrestaShop для работы с товарами. Наследуется от класса `PrestaShop`.

**Методы**:

- `check(product_reference: str)`: Проверка наличия товара в базе данных по product_reference (SKU, MKT). Возвращает словарь товара, если товар найден, иначе `False`.
- `search(filter: str, value: str)`: Расширенный поиск в базе данных по фильтрам.
- `get(id_product)`: Возвращает информацию о товаре по ID.


#### `__init__(self, credentials: Optional[dict | SimpleNamespace] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None, *args, **kwards)`

**Описание**: Инициализирует экземпляр класса `PrestaProduct`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Если не заданы `api_domain` и `api_key`.  (или если не заданы необходимые параметры через `credentials`).


## Функции


```
```
