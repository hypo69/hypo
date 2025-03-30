# Модуль `src.endpoints.prestashop.product_async`

## Обзор

Модуль `src.endpoints.prestashop.product_async` предназначен для взаимодействия с PrestaShop API с целью управления продуктами. Он включает в себя функциональность для добавления новых продуктов и работы с категориями продуктов.

## Подробней

Этот модуль является частью системы, которая автоматизирует взаимодействие между веб-сайтом, информацией о продуктах и PrestaShop. Он позволяет асинхронно управлять продуктами, используя API PrestaShop, и предназначен для упрощения процесса добавления и обновления информации о продуктах.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для асинхронного управления продуктами в PrestaShop. Он позволяет добавлять новые продукты и взаимодействовать с API PrestaShop для выполнения различных операций.

**Методы**:
- `__init__`: Инициализирует объект класса `PrestaProductAsync`.
- `add_new_product_async`: Асинхронно добавляет новый продукт в PrestaShop.

**Параметры**:
- `*args`: Переменное количество позиционных аргументов.
- `**kwargs`: Произвольное количество именованных аргументов.

### `PrestaProductAsync.__init__`

```python
    def __init__(self, *args, **kwargs):
        """
        Initializes a Product object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        ...
```

**Описание**: Инициализирует объект `PrestaProductAsync`, вызывая конструктор базового класса `PrestaShopAsync` и инициализируя `PrestaCategoryAsync`.

**Параметры**:
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

### `PrestaProductAsync.add_new_product_async`

```python
    async def add_new_product_async(self, f: ProductFields) -> ProductFields | None:
        """
        Add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """
        ...
```

**Описание**: Асинхронно добавляет новый продукт в PrestaShop, используя API.

**Параметры**:
- `f` (ProductFields): Объект `ProductFields`, содержащий информацию о продукте.

**Возвращает**:
- `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт успешно добавлен, иначе `None`.

## Функции

### `main`

```python
async def main():
    """
    
    """
    ...
```

**Описание**: Пример использования асинхронных методов для работы с продуктами.

**Примеры**:
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