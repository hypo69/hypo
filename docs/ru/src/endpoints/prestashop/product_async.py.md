# Модуль `src.endpoints.prestashop.product_async`

## Обзор

Модуль предназначен для организации взаимодействия между веб-сайтом, информацией о продукте и PrestaShop.
Он определяет поведение продукта в проекте, включая добавление новых продуктов в PrestaShop через API.

## Подробней

Этот модуль предоставляет класс `PrestaProductAsync`, который позволяет манипулировать продуктами в PrestaShop.
Он использует асинхронные запросы для взаимодействия с API PrestaShop и включает функциональность для добавления новых продуктов,
а также загрузки изображений продуктов.

## Классы

### `PrestaProductAsync`

**Описание**: Класс для манипуляций с продуктами в PrestaShop. Инициализирует объект продукта,
получает данные со страницы продукта и взаимодействует с API PrestaShop.

**Принцип работы**:
1.  Инициализация класса `PrestaProductAsync` наследует функциональность от `PrestaShopAsync`, предоставляя возможность работы с API PrestaShop.
2.  Метод `add_new_product_async` позволяет добавлять новые продукты в PrestaShop, используя данные из объекта `ProductFields`.
3.  Вспомогательный класс `PrestaCategoryAsync` используется для получения списка родительских категорий продукта.

**Методы**:

*   `__init__(self, *args, **kwargs)`: Инициализирует объект `PrestaProductAsync` и вызывает конструктор родительского класса `PrestaShopAsync`, а также инициализирует `PrestaCategoryAsync`.
*   `add_new_product_async(self, f: ProductFields) -> ProductFields | None`: Асинхронно добавляет новый продукт в PrestaShop.

### `__init__(self, *args, **kwargs)`

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

**Назначение**: Инициализирует объект `PrestaProductAsync`.

**Параметры**:

*   `*args`: Список позиционных аргументов переменной длины.
*   `**kwargs`: Словарь именованных аргументов переменной длины.

**Как работает функция**:

1.  Вызывает метод `__init__` родительского класса `PrestaShopAsync` для инициализации базовых параметров.
2.  Создает экземпляр класса `PrestaCategoryAsync` для работы с категориями PrestaShop.

### `add_new_product_async(self, f: ProductFields) -> ProductFields | None`

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

**Назначение**: Асинхронно добавляет новый продукт в PrestaShop.

**Параметры**:

*   `f` (`ProductFields`): Экземпляр класса `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

*   `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

**Как работает функция**:

1.  Получает список родительских категорий, используя метод `get_parent_categories_list` класса `PrestaCategoryAsync`.
2.  Преобразует объект `ProductFields` в словарь.
3.  Создает новый продукт в PrestaShop, используя метод `create`.
4.  Если продукт не был создан, логирует ошибку и возвращает `None`.
5.  Загружает изображение продукта, используя метод `create_binary`.
6.  Если изображение не было загружено, логирует ошибку и возвращает `None`.

```text
Получение родительских категорий
    │
    └──> Преобразование ProductFields в словарь
         │
         └──> Создание продукта в PrestaShop
              │
              ├──> Успех: Загрузка изображения продукта
              │    │
              │    └──> Возврат True
              │
              └──> Ошибка: Логирование ошибки
                   │
                   └──> Возврат None
```

## Функции

### `main()`

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

**Назначение**: Пример использования асинхронных методов для работы с продуктами.

**Как работает функция**:

1.  Создает экземпляр класса `ProductAsync`.
2.  Создает экземпляр класса `ProductFields` с тестовыми данными.
3.  Получает родительские категории продукта (пример).
4.  Пытается добавить новый продукт, используя метод `add_new_product`.
5.  Выводит информацию о результате добавления продукта.
6.  Вызывает метод `fetch_data_async` (назначение не указано в предоставленном коде).