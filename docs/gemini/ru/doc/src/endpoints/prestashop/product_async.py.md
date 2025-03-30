# Модуль `product_async`

## Обзор

Модуль `product_async` предназначен для взаимодействия с API PrestaShop для управления продуктами, включая добавление новых продуктов и обработку связанных данных, таких как категории и изображения. Модуль использует асинхронный подход для обеспечения эффективной работы с API.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за автоматизацию процессов, связанных с продуктами в PrestaShop. Он включает в себя классы и функции для работы с API PrestaShop, категориями продуктов и полями продуктов. Асинхронный подход позволяет эффективно обрабатывать запросы к API и выполнять операции параллельно, что особенно важно при работе с большим объемом данных.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для выполнения операций с продуктами в PrestaShop. Он наследуется от класса `PrestaShopAsync` и предоставляет методы для добавления новых продуктов, получения данных о продуктах и обработки связанных данных, таких как категории и изображения.

**Методы**:
- `__init__`: Инициализирует объект `PrestaProductAsync`.
- `add_new_product_async`: Асинхронно добавляет новый продукт в PrestaShop.

#### `__init__`

```python
def __init__(*args, **kwargs):
    """
    Initializes a Product object.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    ...
```

**Описание**: Инициализирует объект `PrestaProductAsync`, вызывая конструктор родительского класса `PrestaShopAsync` и инициализируя объект `PrestaCategoryAsync` для работы с категориями продуктов.

**Параметры**:
- `*args`: Произвольный список позиционных аргументов.
- `**kwargs`: Произвольный словарь именованных аргументов.

**Примеры**:
```python
product = PrestaProductAsync(api_url='https://your-prestashop-api.com', api_key='your_api_key')
```

#### `add_new_product_async`

```python
async def add_new_product_async(f: ProductFields) -> ProductFields | None:
    """
    Add a new product to PrestaShop.

    Args:
        f (ProductFields): An instance of the ProductFields data class containing the product information.

    Returns:
        ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
    """
    ...
```

**Описание**: Асинхронно добавляет новый продукт в PrestaShop, используя информацию, предоставленную в объекте `ProductFields`.

**Параметры**:
- `f` (ProductFields): Объект `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product` в случае успешного добавления продукта, иначе `None`.

**Примеры**:
```python
product_fields = ProductFields(
    lang_index=1,
    name='Test Product Async',
    price=19.99,
    description='This is an asynchronous test product.',
    id_category_default=3
)

new_product = await product.add_new_product_async(product_fields)
if new_product:
    print(f'New product id = {new_product.id_product}')
else:
    print('Error adding new product')
```

## Функции

### `main`

```python
async def main():
    ...
```

**Описание**: Асинхронная функция `main` предназначена для демонстрации использования класса `PrestaProductAsync` и его методов.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Примеры**:
```python
asyncio.run(main())