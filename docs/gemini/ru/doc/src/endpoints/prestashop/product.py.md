# Модуль `product.py`

## Обзор

Модуль `product.py` предназначен для взаимодействия с продуктами в PrestaShop. Он включает в себя классы и функции для получения информации о продуктах, добавления новых продуктов и управления их категориями.

## Содержание

- [Классы](#классы)
  - [`PrestaProductAsync`](#class-prestaproductasync)
- [Функции](#функции)
  - [`get_parent_categories`](#get_parent_categories)
  - [`add_new_product`](#add_new_product)
  - [`main`](#main)

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предоставляет методы для манипуляций с продуктами, включая получение данных с веб-сайта и взаимодействие с PrestaShop API.

**Наследует**: `PrestaShopAsync`

**Методы**:
- [`__init__`](#__init__)
- [`get_parent_categories`](#get_parent_categories)
- [`add_new_product`](#add_new_product)

#### `__init__`

**Описание**: Инициализирует объект `PrestaProductAsync`.

**Параметры**:
- `*args`: Произвольное количество позиционных аргументов.
- `**kwargs`: Произвольное количество именованных аргументов.

#### `get_parent_categories`

**Описание**: Получает родительские категории для заданной категории. Дублирует функциональность метода `get_parents` из класса `Category`.

**Параметры**:
- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int, optional): Глубина категории. По умолчанию 0.

**Возвращает**:
- `list`: Список родительских категорий.

**Вызывает исключения**:
- `TypeError`: Если `id_category` не является целым числом.

#### `add_new_product`

**Описание**: Добавляет новый продукт в PrestaShop.

**Параметры**:
- `f` (`ProductFields`): Экземпляр `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт успешно добавлен. Возвращает `None` в случае ошибки.

## Функции

### `get_parent_categories`

**Описание**: Получает родительские категории для заданной категории. Дублирует функциональность метода `get_parents` из класса `Category`.

**Параметры**:
- `id_category` (int): ID категории, для которой нужно получить родительские категории.
- `dept` (int, optional): Глубина категории. По умолчанию 0.

**Возвращает**:
- `list`: Список родительских категорий.

**Вызывает исключения**:
- `TypeError`: Если `id_category` не является целым числом.

### `add_new_product`

**Описание**: Добавляет новый продукт в PrestaShop.

**Параметры**:
- `f` (`ProductFields`): Экземпляр `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт успешно добавлен. Возвращает `None` в случае ошибки.

### `main`

**Описание**: Основная функция для демонстрации работы с модулем.

**Параметры**:
   - Нет

**Возвращает**:
   - Нет

**Пример использования**:
   ```python
    product = Product()
    product_fields = ProductFields(
        lang_index = 1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
    )
    
    parent_categories = await Product.get_parent_categories(id_category=3)
    print(f'Parent categories: {parent_categories}')


    new_product = await product.add_new_product(product_fields)
    if new_product:
        print(f'New product id = {new_product.id_product}')
    else:
        print(f'Error add new product')

    await product.fetch_data_async()
   ```