# Модуль `hypotez/src/endpoints/prestashop/product.py`

## Обзор

Модуль `product.py` предоставляет класс `PrestaProduct` для работы с товарами в системе PrestaShop через API. Он расширяет базовый класс `PrestaShop`, предоставляя методы для проверки наличия товаров, расширенного поиска и получения информации о товаре по ID.

## Классы

### `PrestaProduct`

**Описание**: Класс `PrestaProduct` представляет собой класс товара из модуля PrestaShop. Он взаимодействует с API PrestaShop для выполнения операций с товарами.

**Методы**:

- `check(product_reference: str)`
- `search(filter: str, value: str)`
- `get(id_product)`

#### `check(product_reference: str)`

**Описание**: Проверяет наличие товара в базе данных по указанному `product_reference` (SKU, MKT).

**Параметры**:

- `product_reference` (str): Ссылка на товар (SKU, MKT).

**Возвращает**:

- dict: Словарь, содержащий информацию о товаре, если товар найден.
- False: Если товар не найден.

#### `search(filter: str, value: str)`

**Описание**: Выполняет расширенный поиск в базе данных по указанным `filter` и `value`.

**Параметры**:

- `filter` (str): Фильтр поиска.
- `value` (str): Значение для фильтра.

**Возвращает**:

- list: Список результатов поиска.

#### `get(id_product)`

**Описание**: Возвращает информацию о товаре по его `id_product`.

**Параметры**:

- `id_product` (int): ID товара.

**Возвращает**:

- dict: Словарь, содержащий информацию о товаре.

### `__init__(self, credentials: Optional[dict | SimpleNamespace] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None, *args, **kwards)`

**Описание**: Инициализирует класс `PrestaProduct`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`, `**kwards`: Дополнительные аргументы и ключевые слова.


**Вызывает исключения**:

- `ValueError`: Если `api_domain` или `api_key` не заданы.


## Модули

- `header`
- `src.logger`
- `src.utils.printer`
- `.api` (PrestaShop)


## Константы

- `MODE`:  `'dev'`