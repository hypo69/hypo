# Модуль `products.py`

## Обзор

Модуль `products.py` содержит функции для обработки и парсинга данных о продуктах, полученных от AliExpress API. Основная цель модуля - предобработка данных продуктов для дальнейшего использования.

## Оглавление

1. [Функции](#Функции)
   - [`parse_product`](#parse_product)
   - [`parse_products`](#parse_products)

## Функции

### `parse_product`

**Описание**: Функция принимает на вход данные о продукте и преобразует URL маленьких изображений продукта из объекта в строку.

**Параметры**:
- `product` (Any): Объект, содержащий информацию о продукте, включая URL маленьких изображений.

**Возвращает**:
- `Any`: Объект продукта с преобразованными URL маленьких изображений.

```python
def parse_product(product):
    """
    Args:
        product (Any): Объект, содержащий информацию о продукте.

    Returns:
        Any: Объект продукта с преобразованными URL маленьких изображений.
    """
    product.product_small_image_urls = product.product_small_image_urls.string
    return product
```

### `parse_products`

**Описание**: Функция принимает список данных о продуктах, итерируется по списку, применяя функцию `parse_product` к каждому элементу.

**Параметры**:
- `products` (List[Any]): Список объектов, содержащих информацию о продуктах.

**Возвращает**:
- `List[Any]`: Список объектов продуктов с преобразованными URL маленьких изображений.

```python
def parse_products(products):
    """
    Args:
        products (List[Any]): Список объектов, содержащих информацию о продуктах.

    Returns:
        List[Any]: Список объектов продуктов с преобразованными URL маленьких изображений.
    """
    new_products = []

    for product in products:
        new_products.append(parse_product(product))

    return new_products
```