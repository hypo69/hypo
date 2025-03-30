# Модуль `src.endpoints.prestashop.product`

## Обзор

Модуль предназначен для взаимодействия с PrestaShop API для управления продуктами. Он включает классы и функции для получения схемы продукта, добавления нового продукта, а также для выполнения других операций, связанных с продуктами в PrestaShop.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает взаимодействие между веб-сайтом, продуктами и PrestaShop. Он определяет поведение продукта в проекте, используя API PrestaShop для выполнения различных операций, таких как добавление новых продуктов и получение информации о существующих продуктах. Модуль использует конфигурацию, определенную в классе `Config`, для подключения к API PrestaShop.

## Оглавление
- [Классы](#Классы)
  - [`Config`](#Config)
  - [`PrestaProduct`](#PrestaProduct)
- [Функции](#Функции)
  - [`example_add_new_product`](#example_add_new_product)
  - [`example_get_product`](#example_get_product)

## Классы

### `Config`

**Описание**: Класс, содержащий конфигурацию для подключения к API PrestaShop.

**Параметры**:
- `USE_ENV` (bool): Флаг, указывающий, использовать ли переменные окружения для конфигурации. По умолчанию `False`.
- `MODE` (str): Режим работы (`dev`, `dev8` или другой). По умолчанию `'dev'`.
- `POST_FORMAT` (str): Формат данных для POST-запросов (`XML`). По умолчанию `'XML'`.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Примеры**:

```python
config = Config()
print(config.API_DOMAIN)
print(config.API_KEY)
```

### `PrestaProduct`

**Описание**: Класс для работы с продуктами в PrestaShop. Позволяет получать и добавлять продукты через API PrestaShop.

**Методы**:
- `__init__`: Инициализирует объект `PrestaProduct`.
- `get_product_schema`: Возвращает схему продукта.
- `get_parent_category`: Получает родительскую категорию.
- `_add_parent_categories`: Добавляет родительские категории.
- `get_product`: Получает информацию о продукте.
- `add_new_product`: Добавляет новый продукт.

**Параметры**:
- `API_KEY` (str): Ключ API PrestaShop.
- `API_DOMAIN` (str): Домен API PrestaShop.

**Примеры**:

```python
API_KEY = Config.API_KEY
API_DOMAIN = Config.API_DOMAIN
product = PrestaProduct(API_KEY, API_DOMAIN)
```

## Функции

### `example_add_new_product`

```python
def example_add_new_product():
    """ Пример для добавления товара в Prestashop """
```

**Описание**: Пример добавления нового продукта в PrestaShop.

**Примеры**:

```python
example_add_new_product()
```

### `example_get_product`

```python
def example_get_product(id_product:int, **kwards):
    """"""
```

**Описание**: Пример получения информации о продукте из PrestaShop.

**Параметры**:
- `id_product` (int): ID продукта.

**Примеры**:

```python
example_get_product(id_product=2191)