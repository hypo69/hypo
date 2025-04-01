# Модуль `product_async`

## Обзор

Модуль `product_async` предназначен для управления продуктами в PrestaShop. Он обеспечивает взаимодействие между веб-сайтом, информацией о продуктах и API PrestaShop. В частности, модуль позволяет асинхронно добавлять новые продукты в PrestaShop, используя API.

## Подробней

Этот модуль предоставляет класс `PrestaProductAsync`, который наследуется от `PrestaShopAsync` и расширяет его функциональность для работы с продуктами. Он использует другие модули, такие как `PrestaCategoryAsync` для управления категориями продуктов, и `ProductFields` для представления данных о продукте. Модуль предназначен для асинхронного выполнения операций, что позволяет эффективно управлять продуктами в PrestaShop.

## Классы

### `PrestaProductAsync`

**Описание**: Класс для асинхронного управления продуктами в PrestaShop.

**Как работает класс**:
Класс `PrestaProductAsync` предназначен для манипуляций с продуктами в PrestaShop. Он инициализируется с использованием асинхронного API PrestaShop и предоставляет методы для добавления новых продуктов. Класс использует другие классы, такие как `PrestaCategoryAsync` для получения информации о категориях продукта, и `ProductFields` для представления данных о продукте.

**Методы**:
- `__init__`: Инициализирует объект `PrestaProductAsync`.
- `add_new_product_async`: Асинхронно добавляет новый продукт в PrestaShop.

#### `__init__`

```python
def __init__(self, *args, **kwargs):
    """
    Initializes a Product object.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    PrestaShopAsync.__init__(self, *args, **kwargs)
    self.presta_category_async = PrestaCategoryAsync(*args, **kwargs)
```

**Описание**: Инициализирует объект `PrestaProductAsync`.

**Как работает функция**:
Метод инициализации класса `PrestaProductAsync`. Он вызывает конструктор родительского класса `PrestaShopAsync` и создает экземпляр класса `PrestaCategoryAsync` для работы с категориями продуктов.

**Параметры**:
- `*args`: Переменное количество позиционных аргументов.
- `**kwargs`: Переменное количество именованных аргументов.

**Примеры**:
```python
product = PrestaProductAsync(api_url='https://your-prestashop.com/api', api_key='YOUR_API_KEY')
```

#### `add_new_product_async`

```python
async def add_new_product_async(self, f: ProductFields) -> ProductFields | None:
    """
    Add a new product to PrestaShop.

    Args:
        f (ProductFields): An instance of the ProductFields data class containing the product information.

    Returns:
        ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
    """

    f.additional_categories = await self.presta_category_async.get_parent_categories_list(f.id_category_default)
    
    presta_product_dict:dict = f.to_dict()
    
    new_f:ProductFields = await self.create('products', presta_product_dict)

    if not new_f:
        logger.error(f"Товар не был добавлен в базу данных Presyashop")
        ...
        return

    if await self.create_binary(f'images/products/{new_f.id_product}', f.local_image_path, new_f.id_product):
        return True

    else:
        logger.error(f"Не подналось изображение")
        ...
        return
    ...
```

**Описание**: Асинхронно добавляет новый продукт в PrestaShop.

**Как работает функция**:
Метод `add_new_product_async` добавляет новый продукт в PrestaShop. Сначала он получает список родительских категорий для продукта, используя `presta_category_async.get_parent_categories_list`. Затем он преобразует данные продукта в словарь и вызывает метод `create` для создания продукта в PrestaShop. Если продукт успешно создан, метод пытается загрузить изображение продукта, используя метод `create_binary`. В случае успеха возвращается `True`, иначе логируется ошибка и возвращается `None`.

**Параметры**:
- `f` (ProductFields): Объект `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

**Примеры**:
```python
product_fields = ProductFields(
    lang_index=1,
    name='Test Product Async',
    price=19.99,
    description='This is an asynchronous test product.',
)

product = PrestaProductAsync(api_url='https://your-prestashop.com/api', api_key='YOUR_API_KEY')
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
    # Example usage
    product = ProductAsync()
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

**Описание**: Пример использования асинхронных функций для работы с продуктами.

**Как работает функция**:
Функция `main` является примером использования асинхронных функций для работы с продуктами. Она создает экземпляр класса `ProductAsync`, заполняет объект `ProductFields` данными о продукте и пытается добавить новый продукт, используя метод `add_new_product`.

**Примеры**:
```python
asyncio.run(main())
```
```python
if __name__ == '__main__':
    asyncio.run(main())
```
```python
    product_fields = ProductFields(
        lang_index = 1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
    )
```
```python
    parent_categories = await Product.get_parent_categories(id_category=3)
    print(f'Parent categories: {parent_categories}')
```
```python
   new_product = await product.add_new_product(product_fields)
    if new_product:
        print(f'New product id = {new_product.id_product}')
    else:
        print(f'Error add new product')
```
```python
    await product.fetch_data_async()