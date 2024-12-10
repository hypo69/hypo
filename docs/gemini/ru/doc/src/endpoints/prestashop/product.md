# Модуль hypotez/src/endpoints/prestashop/product.py

## Обзор

Этот модуль предоставляет класс `PrestaProduct` для работы с товарами в системе управления интернет-магазином PrestaShop через API.  Класс наследуется от класса `PrestaShop` для общего управления API. Он содержит методы для проверки наличия товара, расширенного поиска и получения информации о товаре по ID.


## Классы

### `PrestaProduct`

**Описание**: Класс `PrestaProduct` предназначен для работы с товарами в PrestaShop через API. Он предоставляет методы для проверки наличия товара, расширенного поиска и получения данных о товаре.

**Методы**:

- `check(product_reference: str)`: Проверка наличия товара в базе данных по `product_reference` (SKU, MKT). Возвращает словарь с информацией о товаре, если товар найден, иначе `False`.
- `search(filter: str, value: str)`: Расширенный поиск в базе данных по заданным фильтрам.
- `get(id_product: int)`: Возвращает информацию о товаре по его ID.


**Инициализация**:

### `__init__(self, credentials: Optional[dict | SimpleNamespace] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None, *args, **kwards)`

**Описание**: Метод инициализации класса `PrestaProduct`. Он принимает параметры для подключения к API PrestaShop.

**Параметры**:

- `credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Возвращает `None`.

**Исключения**:
- `ValueError`: Бросается, если не указаны оба параметра `api_domain` и `api_key`.


## Функции

(В файле нет функций, только класс)


```