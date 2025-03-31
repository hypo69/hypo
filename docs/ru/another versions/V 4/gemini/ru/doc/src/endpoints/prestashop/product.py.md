# Модуль `product`

## Обзор

Модуль `product` предназначен для взаимодействия с PrestaShop API для управления продуктами. Он включает в себя классы и функции для получения схемы продукта, добавления новых продуктов, а также вспомогательные методы для работы с категориями продуктов.

## Подробней

Модуль предоставляет класс `PrestaProduct`, который наследуется от `PrestaShop` и реализует методы для работы с продуктами. Он позволяет получать и изменять информацию о продуктах в PrestaShop, а также добавлять новые продукты с использованием API.
Модуль содержит класс :class:`PrestaProduct`, который используется для взаимодействия с API PrestaShop и выполнения задач, связанных с управлением продуктами.

## Содержание

- [Классы](#Классы)
  - [`Config`](#Config)
  - [`PrestaProduct`](#PrestaProduct)
- [Функции](#Функции)
  - [`example_add_new_product`](#example_add_new_product)
  - [`example_get_product`](#example_get_product)

## Классы

### `Config`

**Описание**: Класс `Config` предназначен для хранения конфигурационных параметров, необходимых для подключения к API PrestaShop.

**Параметры**:
- `USE_ENV` (bool): Указывает, следует ли использовать переменные окружения для получения параметров API. По умолчанию `False`.
- `MODE` (str): Режим работы (например, `dev`, `dev8`). В зависимости от режима выбираются параметры API. По умолчанию `dev`.
- `POST_FORMAT` (str): Формат отправки данных (например, `XML`). По умолчанию `XML`.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Примеры**:

```python
config = Config()
print(config.API_DOMAIN)
print(config.API_KEY)
```

### `PrestaProduct`

**Описание**: Класс `PrestaProduct` предназначен для взаимодействия с PrestaShop API для управления продуктами.

**Методы**:
- `__init__`: Инициализирует объект `PrestaProduct`.
- `get_product_schema`: Получает схему ресурса продукта из PrestaShop.
- `get_parent_category`: Рекурсивно извлекает родительские категории из PrestaShop для заданной категории.
- `_add_parent_categories`: Вычисляет и добавляет все родительские категории для списка идентификаторов категорий к объекту `ProductFields`.
- `get_product`: Получает информацию о продукте из PrestaShop.
- `add_new_product`: Добавляет новый продукт в PrestaShop.

**Параметры**:
- `API_KEY` (str): Ключ API PrestaShop.
- `API_DOMAIN` (str): Домен API PrestaShop.

**Примеры**:

```python
p = PrestaProduct(API_KEY=Config.API_KEY, API_DOMAIN=Config.API_DOMAIN)
product = p.get_product(id_product=2191)
print(product)
```

## Функции

### `example_add_new_product`

```python
def example_add_new_product():
    """ Пример для добавления товара в Prestashop """
```

**Описание**: Функция `example_add_new_product` предоставляет пример добавления нового продукта в PrestaShop.

**Примеры**:

```python
example_add_new_product()
```

### `example_get_product`

```python
def example_get_product(id_product:int, **kwards):
    """"""
```

**Описание**: Функция `example_get_product` предоставляет пример получения информации о продукте из PrestaShop.

**Параметры**:
- `id_product` (int): Идентификатор продукта.
- `**kwards`: Дополнительные параметры запроса.

**Примеры**:

```python
example_get_product(id_product=2191)