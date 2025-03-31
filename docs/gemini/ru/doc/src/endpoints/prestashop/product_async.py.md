# Модуль `src.endpoints.prestashop.product_async`

## Обзор

Модуль `src.endpoints.prestashop.product_async` предназначен для взаимодействия с API PrestaShop для управления продуктами. Он предоставляет функциональность для добавления новых продуктов, получения информации о продуктах и выполнения других операций, связанных с продуктами, в асинхронном режиме.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с PrestaShop для автоматизации управления продуктами. Он использует асинхронные запросы для повышения производительности и эффективности. Расположение файла в структуре проекта указывает на его роль как одного из endpoints для взаимодействия с PrestaShop.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для манипуляций с продуктами в PrestaShop. Он наследует функциональность от класса `PrestaShopAsync` и расширяет её методами для работы с продуктами.

**Как работает класс**:
1.  Инициализируется с использованием `PrestaShopAsync`.
2.  Предоставляет метод `add_new_product_async` для добавления новых продуктов в PrestaShop.
3.  Использует `PrestaCategoryAsync` для получения списка родительских категорий продукта.

```python
class PrestaProductAsync(PrestaShopAsync):
    """Manipulations with the product.
    Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """
```

**Методы**:

*   `__init__(self, *args, **kwargs)`:
    Инициализирует объект `PrestaProductAsync`.
*   `add_new_product_async(self, f: ProductFields) -> ProductFields | None`:
    Добавляет новый продукт в PrestaShop.

#### `__init__`

```python
 def __init__(self, *args, **kwargs):
        """
        Initializes a Product object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
```

**Назначение**: Инициализирует объект класса `PrestaProductAsync`.

**Как работает функция**:
1.  Вызывает конструктор родительского класса `PrestaShopAsync` для инициализации общих параметров.
2.  Создает экземпляр класса `PrestaCategoryAsync` для работы с категориями продуктов.

**Параметры**:

*   `*args`: Произвольный список позиционных аргументов.
*   `**kwargs`: Произвольный словарь именованных аргументов.

**Возвращает**:

*   `None`

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
```

**Назначение**: Асинхронно добавляет новый продукт в PrestaShop.

**Как работает функция**:

Функция `add_new_product_async` асинхронно добавляет новый продукт в PrestaShop, используя API PrestaShop.

Внутри функции происхоят следующие действия и преобразования:

A. Получение списка родительских категорий продукта:
   |
   -- B. Преобразование данных продукта в словарь:
      |
      C. Создание продукта в PrestaShop через API:
      |
      D. Проверка успешности создания продукта:
         |
         -- E. Загрузка изображения продукта:
            |
            F. Возврат результата в зависимости от успешности операций

A. `f.additional_categories = await self.presta_category_async.get_parent_categories_list(f.id_category_default)` - Получает список родительских категорий продукта на основе `id_category_default`.

B. `presta_product_dict:dict = f.to_dict()` - Преобразует объект `ProductFields` в словарь для отправки в API PrestaShop.

C. `new_f:ProductFields = await self.create('products', presta_product_dict)` - Создает продукт в PrestaShop, используя метод `create` класса `PrestaShopAsync`.

D. `if not new_f:` - Проверяет, был ли продукт успешно создан. Если нет, логирует ошибку и возвращает `None`.

E. `if await self.create_binary(f'images/products/{new_f.id_product}', f.local_image_path, new_f.id_product):` - Загружает изображение продукта, используя метод `create_binary`.

F. В зависимости от успешности загрузки изображения, возвращает `True` или `None`.

**Параметры**:

*   `f` (`ProductFields`): Объект `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

*   `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

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

**Назначение**: Функция `main` является точкой входа для демонстрации работы с классом `PrestaProductAsync`.

**Как работает функция**:

1.  Создает экземпляр класса `ProductAsync`.
2.  Создает экземпляр класса `ProductFields` с тестовыми данными продукта.
3.  Получает родительские категории продукта.
4.  Добавляет новый продукт с использованием метода `add_new_product`.
5.  Выводит информацию о результате добавления продукта.

**Параметры**:

*   `None`

**Возвращает**:

*   `None`