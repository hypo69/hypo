# Модуль `__morlevi__.py`

## Обзор

Модуль `__morlevi__.py` предназначен для работы с поставщиком Morlevi. Он содержит функции для авторизации, сбора информации о товарах и получения списка товаров из категорий. Модуль использует библиотеки `pathlib`, `requests`, `pandas`, `selenium` для взаимодействия с веб-сайтом поставщика.

## Подробней

Этот модуль является частью системы автоматизации сбора данных о товарах с сайтов поставщиков для дальнейшей загрузки в PrestaShop. Он включает в себя функции для логина на сайте поставщика, извлечения данных о товарах (таких как ID, SKU, название, описание, цены, изображения и т.д.) и получения списка товаров из категорий с учетом пагинации.

## Классы

### `Product`

**Описание**: Класс, представляющий товар.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Product`.

**Параметры**:
- `supplier`: Объект поставщика.

**Примеры**
```python
from src.suppliers.Product import Product
from src.suppliers.ivory import __morlevi__

# Пример создания объекта Product
# Сначала необходимо создать объект supplier, который будет использоваться для инициализации Product
# Здесь предполагается, что supplier уже определен и инициализирован где-то выше по коду
# product = Product(supplier=supplier)
```

## Функции

### `login`

```python
def login(supplier):
    """
    Args:
        supplier:

    Returns:
        bool:

    Raises:
        Exception:
    """
    ...
```

**Описание**: Функция для авторизации на сайте поставщика Morlevi.

**Параметры**:
- `supplier`: Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, иначе `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при попытке авторизации или закрытии модальных окон.

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова функции login
# __morlevi__.login(supplier)
```

### `_login`

```python
def _login(_s):
    """
    Args:
        _s:

    Returns:
        bool:

    Raises:
        Exception:
    """
    ...
```

**Описание**: Внутренняя функция, выполняющая фактический процесс авторизации на сайте Morlevi.

**Параметры**:
- `_s`: Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, иначе `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при вводе данных или нажатии кнопок.

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова внутренней функции _login
# __morlevi__._login(supplier)
```

### `grab_product_page`

```python
def grab_product_page(s):
    """
    Args:
        s:

    Returns:
        Product:

    Raises:
        Exception:
    """
    ...
```

**Описание**: Функция для сбора информации о товаре со страницы товара на сайте поставщика.

**Параметры**:
- `s`: Объект поставщика, содержащий информацию о драйвере, локаторах и настройках.

**Возвращает**:
- `Product`: Объект `Product`, содержащий собранную информацию о товаре.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных со страницы товара.

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова функции grab_product_page
# __morlevi__.grab_product_page(supplier)
```

### `list_products_in_category_from_pagination`

```python
def list_products_in_category_from_pagination(supplier):
    """
    Args:
        supplier:

    Returns:
        list:

    Raises:
        Exception:
    """
    ...
```

**Описание**: Функция для получения списка ссылок на товары из категории с учетом пагинации.

**Параметры**:
- `supplier`: Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list`: Список ссылок на товары в категории.

**Вызывает исключения**:
- `Exception`: В случае ошибки при навигации по страницам пагинации или извлечении ссылок на товары.

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова функции list_products_in_category_from_pagination
# __morlevi__.list_products_in_category_from_pagination(supplier)
```

### `get_list_products_in_category`

```python
def get_list_products_in_category(s, scenario, presath):
    """
    s:Supplier
    scenario:JSON
    presath:PrestaShopWebServiceDict
    """
    ...
```

**Описание**: Функция для получения списка товаров в категории.

**Параметры**:
- `s`: Объект поставщика.
- `scenario`: JSON-сценарий.
- `presath`: Словарь веб-сервиса PrestaShop.

**Возвращает**:
- `None`:

**Вызывает исключения**:
- `Exception`:

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова функции list_products_in_category_from_pagination
# __morlevi__.list_products_in_category_from_pagination(supplier, scenario, presath)
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    """
    Args:
        s:
        scenario_file:
        brand:

    Returns:
        None:

    Raises:
        Exception:
    """
    ...
```

**Описание**: Функция для получения списка категорий с сайта.

**Параметры**:
- `s`:
- `scenario_file`:
- `brand`:

**Возвращает**:
- `None`:

**Вызывает исключения**:
- `Exception`:

**Примеры**:
```python
from src.suppliers.ivory import __morlevi__
# Пример вызова функции list_products_in_category_from_pagination
# __morlevi__.get_list_categories_from_site(supplier, scenario_file, brand)