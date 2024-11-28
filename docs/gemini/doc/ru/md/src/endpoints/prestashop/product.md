# Модуль hypotez/src/endpoints/prestashop/product.py

## Обзор

Этот модуль предоставляет класс `PrestaProduct` для работы с товарами в системе PrestaShop через API. Он предоставляет методы для проверки наличия товара, расширенного поиска и получения информации о товаре по ID.

## Классы

### `PrestaProduct`

**Описание**: Класс `PrestaProduct` наследуется от класса `PrestaShop` и предоставляет методы для работы с продуктами в PrestaShop API.

**Методы**:

- `check(product_reference: str)`: Проверка наличия товара в базе данных по `product_reference` (SKU, MKT). Возвращает словарь с информацией о товаре, если товар найден, иначе `False`.
- `search(filter: str, value: str)`: Расширенный поиск в базе данных по заданным фильтрам.
- `get(id_product)`: Возвращает информацию о товаре по его ID.


### `PrestaProduct.__init__`

**Описание**: Конструктор класса `PrestaProduct`. Инициализирует объект, устанавливая необходимые параметры для взаимодействия с API PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Если не заданы `api_domain` и `api_key`.


```
```python
def check(product_reference: str) -> dict | False:
    """
    Args:
        product_reference (str): Ссылка на товар.

    Returns:
        dict | False: Информация о товаре или False, если товар не найден.
    """
    pass

def search(filter: str, value: str) -> dict | None:
    """
    Args:
        filter (str): Фильтр поиска.
        value (str): Значение фильтра.

    Returns:
        dict | None: Результат поиска или None, если поиск не выполнен.
    """
    pass

def get(id_product: int) -> dict | None:
    """
    Args:
        id_product (int): Идентификатор товара.

    Returns:
        dict | None: Информация о товаре или None, если товар не найден.
    """
    pass
```