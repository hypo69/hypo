# Модуль `__morlevi__.py`

## Обзор

Модуль `__morlevi__.py` предназначен для работы с поставщиком Morlevi. Он содержит функции для авторизации на сайте поставщика, сбора информации о товарах и получения списка товаров в категории. Модуль использует библиотеки `pathlib`, `requests`, `pandas` и `selenium` для взаимодействия с веб-сайтом поставщика.

## Подробней

Этот модуль является частью системы для автоматизации сбора и обработки данных о товарах от различных поставщиков. Он предоставляет функциональность для входа в систему поставщика, навигации по сайту и извлечения необходимой информации о товарах, такой как идентификаторы, описания, цены и изображения. Полученные данные используются для дальнейшей обработки и интеграции с другими системами, такими как PrestaShop.

## Функции

### `login`

```python
def login(supplier):
    """
    Args:
        supplier: Объект поставщика.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `None`.

    Raises:
        Exception: Если не удается залогиниться.

    """
```

**Описание**: Осуществляет вход на сайт поставщика Morlevi.

**Как работает функция**: Функция принимает объект поставщика в качестве аргумента. Она пытается войти на сайт, используя предоставленные учетные данные. Если вход не удался, функция пытается закрыть модальные окна и повторить попытку входа.

**Параметры**:
- `supplier`: Объект поставщика, содержащий информацию о драйвере, локаторах и настройках.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно.
- `None`: Если не удалось выполнить вход после нескольких попыток.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при попытке входа или закрытия модальных окон.

**Примеры**:
```python
# Пример использования функции login
# from src.suppliers.morlevi import __morlevi__
# from src.driver import Driver
# supplier = Driver()
# supplier.driver = ...  # инициализация драйвера
# if __morlevi__.login(supplier):
#     print("Вход выполнен успешно")
# else:
#     print("Не удалось выполнить вход")
```

### `_login`

```python
def _login(_s):
    """
    Args:
        _s: Объект поставщика.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `None`.

    Raises:
        Exception: Если не удается залогиниться.

    """
```

**Описание**: Внутренняя функция для осуществления входа на сайт Morlevi.

**Как работает функция**: Функция принимает объект поставщика в качестве аргумента. Она выполняет фактический вход на сайт, используя локаторы для полей ввода и кнопки входа.

**Параметры**:
- `_s`: Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно.
- `None`: Если не удалось выполнить вход.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при попытке входа.

**Примеры**:
```python
# Пример использования функции _login
# from src.suppliers.morlevi import __morlevi__
# from src.driver import Driver
# supplier = Driver()
# supplier.driver = ...  # инициализация драйвера
# if __morlevi__._login(supplier):
#     print("Вход выполнен успешно")
# else:
#     print("Не удалось выполнить вход")
```

### `grab_product_page`

```python
def grab_product_page(s):
    """
    Args:
        s: Объект поставщика.

    Returns:
        Product: Объект товара с заполненными данными.

    Raises:
        Exception: Если не удается получить цену товара.

    """
```

**Описание**: Собирает информацию о товаре со страницы товара на сайте поставщика.

**Как работает функция**: Функция принимает объект поставщика в качестве аргумента. Она создает объект `Product` и заполняет его поля, извлекая данные со страницы товара с использованием локаторов. Функция также обрабатывает модальные окна, которые могут появляться на странице.

**Параметры**:
- `s`: Объект поставщика, содержащий информацию о драйвере, локаторах и настройках.

**Возвращает**:
- `Product`: Объект товара с заполненными данными.

**Вызывает исключения**:
- `Exception`: Если не удается получить цену товара.

**Примеры**:
```python
# Пример использования функции grab_product_page
# from src.suppliers.morlevi import __morlevi__
# from src.driver import Driver
# supplier = Driver()
# supplier.driver = ...  # инициализация драйвера
# product = __morlevi__.grab_product_page(supplier)
# if product:
#     print(f"Товар: {product.fields['title']}")
# else:
#     print("Не удалось получить информацию о товаре")
```

### `list_products_in_category_from_pagination`

```python
def list_products_in_category_from_pagination(supplier):
    """
    Args:
        supplier: Объект поставщика.

    Returns:
        list: Список ссылок на товары в категории.

    """
```

**Описание**: Получает список ссылок на товары в категории, переходя по страницам пагинации.

**Как работает функция**: Функция принимает объект поставщика в качестве аргумента. Она извлекает ссылки на товары со страницы категории и переходит на следующую страницу, пока не достигнет конца пагинации.

**Параметры**:
- `supplier`: Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list`: Список ссылок на товары в категории.

**Примеры**:
```python
# Пример использования функции list_products_in_category_from_pagination
# from src.suppliers.morlevi import __morlevi__
# from src.driver import Driver
# supplier = Driver()
# supplier.driver = ...  # инициализация драйвера
# product_list = __morlevi__.list_products_in_category_from_pagination(supplier)
# if product_list:
#     print(f"Найдено {len(product_list)} товаров в категории")
# else:
#     print("Не удалось получить список товаров в категории")
```

### `get_list_products_in_category`

```python
def get_list_products_in_category(s, scenario, presath):
    """
    Args:
        s: Supplier
        scenario: JSON
        presath: PrestaShopWebServiceDict
    """
```

**Описание**:  Получает список товаров в категории.

**Как работает функция**:  Функция вызывает `list_products_in_category_from_pagination` для получения списка товаров в категории.

**Параметры**:
- `s`: Supplier
- `scenario`: JSON
- `presath`: PrestaShopWebServiceDict

**Примеры**:
```python
# from src.suppliers.morlevi import __morlevi__
# from src.driver import Driver
# supplier = Driver()
# scenario = ... # JSON
# presath = ... # PrestaShopWebServiceDict
# supplier.driver = ...  # инициализация драйвера
# product_list = __morlevi__.get_list_products_in_category(supplier, scenario, presath)
# if product_list:
#     print(f"Найдено {len(product_list)} товаров в категории")
# else:
#     print("Не удалось получить список товаров в категории")
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    """
    Args:
        s:
        scenario_file:
        brand (str, optional):  Defaults to ''.
    """
```

**Описание**:  Получает список категорий с сайта.

**Как работает функция**:  ...

**Параметры**:
- `s`:
- `scenario_file`:
- `brand` (str, optional):  Defaults to ''.