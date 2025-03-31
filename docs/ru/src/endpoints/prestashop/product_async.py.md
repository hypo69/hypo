# Модуль: src.endpoints.prestashop.product_async

## Обзор

Модуль `product_async.py` предназначен для асинхронного взаимодействия с PrestaShop API для управления продуктами. Он предоставляет функциональность для добавления новых продуктов, получения родительских категорий и выполнения других операций, связанных с продуктами в PrestaShop.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за асинхронное взаимодействие с PrestaShop API для управления продуктами. Он использует другие модули, такие как `PrestaShopAsync`, `PrestaCategoryAsync` и `ProductFields`, для выполнения своих задач. Модуль позволяет добавлять новые продукты, получать родительские категории и выполнять другие операции, связанные с продуктами в PrestaShop.

## Классы

### `PrestaProductAsync`

**Описание**: Класс `PrestaProductAsync` предназначен для манипуляций с продуктами в PrestaShop. Он наследуется от класса `PrestaShopAsync` и предоставляет методы для добавления новых продуктов и выполнения других операций, связанных с продуктами.

**Как работает класс**:
1.  Инициализируется с использованием аргументов и ключевых слов, переданных в конструктор.
2.  Использует `PrestaCategoryAsync` для получения списка родительских категорий.
3.  Преобразует объект `ProductFields` в словарь для отправки в PrestaShop API.
4.  Создает новый продукт с использованием метода `create` класса `PrestaShopAsync`.
5.  Загружает изображение продукта, используя метод `create_binary` класса `PrestaShopAsync`.

**Методы**:

*   `__init__`: Инициализирует объект `PrestaProductAsync`.
*   `add_new_product_async`: Асинхронно добавляет новый продукт в PrestaShop.

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

**Назначение**: Инициализирует объект `PrestaProductAsync`.

**Как работает функция**:
1.  Вызывает конструктор родительского класса `PrestaShopAsync` для инициализации общих параметров.
2.  Инициализирует атрибут `presta_category_async` экземпляром класса `PrestaCategoryAsync`.

**Параметры**:

*   `*args`: Произвольный список аргументов.
*   `**kwargs`: Произвольный словарь именованных аргументов.

**Возвращает**: Ничего.

**Вызывает исключения**: Отсутствуют.

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

Внутри функции происходят следующие действия и преобразования:

A.  Получение списка родительских категорий с использованием `presta_category_async.get_parent_categories_list(f.id_category_default)`.
|
B.  Преобразование объекта `ProductFields` в словарь `presta_product_dict` с использованием `f.to_dict()`.
|
C.  Создание продукта в PrestaShop с использованием `self.create('products', presta_product_dict)`.
|
D.  Проверка, был ли продукт успешно добавлен в базу данных PrestaShop. Если нет, то логируется ошибка и функция возвращает `None`.
|
E.  Загрузка изображения продукта с использованием `self.create_binary(f'images/products/{new_f.id_product}', f.local_image_path, new_f.id_product)`.
|
F.  Проверка, было ли изображение успешно загружено. Если да, то функция возвращает `True`. Если нет, то логируется ошибка и функция возвращает `None`.

**Параметры**:

*   `f` (`ProductFields`): Объект класса `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

*   `ProductFields | None`: Возвращает объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

**Вызывает исключения**: Отсутствуют.

## Функции

### `main`

```python
async def main():
    """
    Example usage
    """
```

**Назначение**: Пример использования класса `PrestaProductAsync`.

**Как работает функция**:

Внутри функции происходят следующие действия и преобразования:

A.  Создание экземпляра класса `ProductAsync`.
|
B.  Создание экземпляра класса `ProductFields` с тестовыми данными.
|
C.  Получение родительских категорий с использованием `Product.get_parent_categories(id_category=3)`.
|
D.  Добавление нового продукта с использованием `product.add_new_product(product_fields)`.
|
E.  Проверка, был ли продукт успешно добавлен. Если да, то выводится идентификатор нового продукта. Если нет, то выводится сообщение об ошибке.
|
F.  Вызов `product.fetch_data_async()`.

**Параметры**: Отсутствуют.

**Возвращает**: Ничего.

**Вызывает исключения**: Отсутствуют.