# Модуль `product.py`

## Обзор

Модуль `product.py` представляет собой класс `PrestaProduct`, который наследуется от класса `PrestaShop` и предназначен для взаимодействия с API PrestaShop для управления товарами. Он предоставляет методы для проверки наличия товара, поиска и получения информации о товарах по их идентификаторам.

## Содержание

- [Классы](#классы)
  - [`PrestaProduct`](#prestaproduct)
- [Функции](#функции)

## Классы

### `PrestaProduct`

**Описание**: Класс товара из модуля PrestaShop. Непосредственно выполняет все операции через API.

**Методы**:
- `check(product_reference: str)`: Проверка наличия товара в БД по `product_reference` (SKU, MKT). Вернет словарь товара, если товар есть, иначе `False`.
- `search(filter: str, value: str)`: Расширенный поиск в БД по фильтрам.
- `get(id_product)`: Возвращает информацию о товаре по ID.
- `__init__(credentials: Optional[dict | SimpleNamespace] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None, *args, **kwards)`: Инициализация товара PrestaShop.

#### `__init__`
**Описание**: Инициализация экземпляра класса `PrestaProduct`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
- `*args`: Произвольное количество позиционных аргументов.
- `**kwards`: Произвольное количество именованных аргументов.

**Возвращает**:
    - `None`: Метод ничего не возвращает.
**Вызывает исключения**:
    - `ValueError`: Если не переданы `api_domain` или `api_key` и не найдены в `credentials`.