# Модуль `product_async.py`

## Обзор

Модуль `product_async.py` предназначен для асинхронного взаимодействия между веб-сайтом, продуктом и PrestaShop. Он определяет поведение продукта в проекте, позволяя добавлять и управлять продуктами в PrestaShop через API. Модуль использует асинхронные запросы для повышения производительности и эффективности.

## Подробней

Модуль содержит класс `PrestaProductAsync`, который наследует `PrestaShopAsync` и реализует методы для добавления новых продуктов в PrestaShop. Он использует другие модули, такие как `PrestaCategoryAsync` для работы с категориями продуктов и `ProductFields` для представления данных о продукте.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для выполнения манипуляций с продуктами в PrestaShop. Он инициализирует взаимодействие с API PrestaShop и предоставляет методы для добавления новых продуктов.

**Принцип работы**:
1.  При инициализации класса создается экземпляр класса `PrestaCategoryAsync`, который используется для получения информации о родительских категориях продукта.
2.  Метод `add_new_product_async` используется для добавления нового продукта в PrestaShop. Он принимает объект `ProductFields`, содержащий информацию о продукте, и использует API PrestaShop для создания нового продукта.

**Методы**:

*   `__init__(self, *args, **kwargs)`: Инициализирует объект `PrestaProductAsync`.
*   `add_new_product_async(self, f: ProductFields) -> ProductFields | None`: Асинхронно добавляет новый продукт в PrestaShop.

### `PrestaProductAsync.__init__`

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

**Параметры**:

*   `*args`: Список позиционных аргументов переменной длины.
*   `**kwargs`: Словарь именованных аргументов переменной длины.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `PrestaShopAsync` для инициализации общих параметров.
2.  Создает экземпляр класса `PrestaCategoryAsync`, который используется для работы с категориями продуктов.

**Примеры**:

```python
product = PrestaProductAsync()
```

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

**Назначение**: Асинхронно добавляет новый продукт в PrestaShop, используя API.

**Параметры**:

*   `f` (`ProductFields`): Объект класса `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

*   `ProductFields | None`: Объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

**Как работает функция**:

1.  Получает список родительских категорий продукта с использованием метода `get_parent_categories_list` класса `PrestaCategoryAsync`.
2.  Преобразует объект `ProductFields` в словарь.
3.  Вызывает метод `create` для создания нового продукта в PrestaShop.
4.  Если продукт не был создан, регистрирует ошибку и возвращает `None`.
5.  Загружает изображение продукта с использованием метода `create_binary`.
6.  Если загрузка изображения прошла успешно, возвращает `True`, иначе регистрирует ошибку и возвращает `None`.

```
Получение родительских категорий
    A: Получение родительских категорий продукта (f.id_category_default) с использованием presta_category_async.get_parent_categories_list
    |
    Преобразование в словарь
    B: Преобразование объекта ProductFields в словарь (presta_product_dict)
    |
    Создание продукта через API
    C: Вызов метода create('products', presta_product_dict) для создания продукта в PrestaShop
    |
    Проверка успешности создания
    D: Проверка, был ли продукт успешно создан (if not new_f)
    |
    Загрузка изображения продукта
    E: Вызов метода create_binary для загрузки изображения продукта
    |
    Проверка успешности загрузки изображения
    F: Проверка, было ли изображение успешно загружено
```

**Примеры**:

```python
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
    print('Error add new product')
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

**Назначение**: Пример использования класса `PrestaProductAsync` и его методов.

**Как работает функция**:

1.  Создает экземпляр класса `ProductAsync`.
2.  Создает экземпляр класса `ProductFields` с данными о продукте.
3.  Получает список родительских категорий продукта (в данном примере код не будет работать, так как он обращается к несуществующему методу `Product.get_parent_categories`).
4.  Пытается добавить новый продукт с использованием метода `add_new_product` (в данном примере код не будет работать, так как такого метода в классе `PrestaProductAsync` нет).
5.  Вызывает метод `fetch_data_async` (в данном примере код не будет работать, так как такого метода в классе `PrestaProductAsync` нет).

**Примеры**:

```python
if __name__ == '__main__':
    asyncio.run(main())