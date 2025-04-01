# Модуль `product_async.py`

## Обзор

Модуль `product_async.py` предназначен для управления продуктами в PrestaShop с использованием асинхронных операций. Он включает в себя функциональность добавления новых продуктов, взаимодействия с API PrestaShop и категориями продуктов.

## Подробней

Этот модуль является частью системы для взаимодействия с PrestaShop API. Он использует асинхронные вызовы для более эффективной работы с данными, особенно при выполнении сетевых запросов. Он содержит класс `PrestaProductAsync`, который позволяет манипулировать продуктами, загружать данные о продуктах и добавлять новые продукты через API PrestaShop.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для управления продуктами в PrestaShop. Он позволяет добавлять новые продукты и взаимодействовать с API PrestaShop для выполнения различных операций с продуктами.

**Принцип работы**:

1.  Класс инициализируется с использованием асинхронных параметров подключения к PrestaShop.
2.  Он использует класс `PrestaCategoryAsync` для работы с категориями продуктов.
3.  Метод `add_new_product_async` позволяет добавлять новые продукты, включая информацию о категориях и изображениях.

**Наследует**:

-   `PrestaShopAsync`: Класс, предоставляющий базовую функциональность для взаимодействия с PrestaShop API.

**Методы**:

-   `__init__(*args, **kwargs)`: Инициализирует объект класса `PrestaProductAsync`.
-   `add_new_product_async(self, f: ProductFields) -> ProductFields | None`: Асинхронно добавляет новый продукт в PrestaShop.

### `__init__`

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

**Назначение**: Инициализирует объект `PrestaProductAsync`, вызывая конструктор родительского класса `PrestaShopAsync` и создавая экземпляр класса `PrestaCategoryAsync`.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `PrestaShopAsync` для инициализации общих параметров.
2.  Создает экземпляр класса `PrestaCategoryAsync` для работы с категориями продуктов.

**Примеры**:

```python
product = PrestaProductAsync(url='your_prestashop_url', api_key='your_api_key')
```

### `add_new_product_async`

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

**Назначение**: Асинхронно добавляет новый продукт в PrestaShop с использованием данных, предоставленных в объекте `ProductFields`.

**Параметры**:

-   `f` (ProductFields): Объект класса `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

-   `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе возвращает `None`.

**Как работает функция**:

1.  **Получение дополнительных категорий**:
    - Функция `get_parent_categories_list` используется для получения списка родительских категорий на основе `id_category_default`. Результат сохраняется в атрибуте `additional_categories` объекта `f` типа `ProductFields`.

2.  **Преобразование данных продукта**:
    - Объект `ProductFields` преобразуется в словарь `presta_product_dict` с использованием метода `to_dict()`.

3.  **Создание продукта в PrestaShop**:
    - Асинхронно создает новый продукт в PrestaShop, используя метод `create` с параметрами `'products'` и `presta_product_dict`. Результат сохраняется в `new_f` типа `ProductFields`.

4.  **Обработка ошибки создания продукта**:
    - Проверяется, удалось ли создать продукт. Если `new_f` равен `None`, в лог записывается сообщение об ошибке, и функция завершается.

5.  **Создание бинарного изображения продукта**:
    - Пытается создать бинарное изображение продукта, используя метод `create_binary` с параметрами пути к изображению и ID продукта.

6.  **Возврат результата**:
    - Если изображение успешно создано, функция возвращает `True`. В противном случае в лог записывается сообщение об ошибке, и функция завершается.

**Примеры**:

```python
async def main():
    product = PrestaProductAsync()
    product_fields = ProductFields(
        lang_index=1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
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
    # Example usage
    product = ProductAsync()
    product_fields = ProductFields(
        lang_index = 1,
        name=\'Test Product Async\',\n        price=19.99,\n        description=\'This is an asynchronous test product.\',\n    )
    
    parent_categories = await Product.get_parent_categories(id_category=3)
    print(f\'Parent categories: {parent_categories}\')

    new_product = await product.add_new_product(product_fields)
    if new_product:
        print(f\'New product id = {new_product.id_product}\')
    else:
        print(f\'Error add new product\')

    await product.fetch_data_async()
```

**Назначение**: Функция `main` является точкой входа для демонстрации работы с классом `PrestaProductAsync`.

**Как работает функция**:

1.  Создает экземпляр класса `PrestaProductAsync`.
2.  Создает экземпляр класса `ProductFields` с тестовыми данными продукта.
3.  Вызывает метод `add_new_product` для добавления нового продукта.
4.  Выводит результат операции в консоль.
5.  Вызывает метод `fetch_data_async` для получения данных.

**Примеры**:

```python
if __name__ == '__main__':
    asyncio.run(main())